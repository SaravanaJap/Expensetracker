from django.shortcuts import render,redirect
from  .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime
# Create your views here.


def index(request):
    user = request.user
    print(user)
    if user.id is  None:
        return redirect('login')
    else:
        if request.method == "POST":
            expense_form  = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense  =expense_form.save(commit=False)
                expense.user = request.user
                expense.save()
        expenses = Expense.objects.filter(user = request.user)    
        total_income = expenses.filter(transaction_type = 'income').aggregate(Sum('cost'))
        total_expense = expenses.filter(transaction_type = 'expense').aggregate(Sum('cost'))
        total_expenses = (total_income['cost__sum'] - total_expense['cost__sum'] )
        print(total_expenses)

        #Logic to calculate 365 days expenses
        last_year = datetime.date.today() - datetime.timedelta(days=365)
        data = Expense.objects.filter(user = request.user , date__gt=last_year)
        yearly_sum = data.aggregate(Sum('cost'))
        
        #Logic to calculate 30 days expenses
        last_month = datetime.date.today() - datetime.timedelta(days=30)
        data = Expense.objects.filter(transaction_type = 'expense'  , date__gt=last_month)
        monthly_sum = data.aggregate(Sum('cost'))
        
        #Logic to calculate 7 days expenses
        last_week = datetime.date.today() - datetime.timedelta(days=7)
        data = Expense.objects.filter(date__gt=last_week)
        weekly_sum = data.aggregate(Sum('cost'))

        daily_sums = Expense.objects.filter(user = request.user,transaction_type = 'expense' ).values('date').order_by('date').annotate(sum=Sum('cost'))
        
        categorical_sums = Expense.objects.filter(user = request.user,transaction_type = 'expense' ).values('category').order_by('category').annotate(sum=Sum('cost'))

        
        expenseform = ExpenseForm()
        return render(request,'myapp/index.html',{'expenseform':expenseform,'expenses':expenses,'total_expenses':total_expenses,'yearly_sum':yearly_sum,'weekly_sum':weekly_sum,'monthly_sum':monthly_sum,'daily_sums':daily_sums,'categorical_sums':categorical_sums})

    
def edit(request,id):
    expense_detail = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense_detail)
    if request.method == "POST":
        edited_expense = ExpenseForm(request.POST,instance=expense_detail)
        if edited_expense.is_valid():
            edited_expense.save()
            return redirect('index')
    return render(request,'myapp/edit.html',{'expense_form':expense_form})


def delete(request,id):
    if request.method == 'POST' and 'delete' in request.POST:
        expense = Expense.objects.get(id = id)
        expense.delete()
    return redirect('index')