from django.shortcuts import render
from .models import Food,Consume
from django.shortcuts import redirect
# Create your views here.

def index(request):
    food = Food.objects.all()
    if request.method == 'POST':
        food_consumed  =  request.POST.get('food_consumed')
        consume = Food.objects.get(name = food_consumed)
        user = request.user
        consume = Consume(user = user,food_consumed = consume)
        consume.save()
        consumed_food = Consume.objects.filter(user = request.user)
    else:
        if request.user.is_authenticated:
            consumed_food = Consume.objects.filter(user = request.user)
        else:
            consumed_food = None 
    
    return render(request,'myapp/index.html',{'foods':food,'consumed_food':consumed_food})


def delete_consume(request,id):
    consume = Consume.objects.get(id = id)
    if request.method == "POST":
        consume.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')