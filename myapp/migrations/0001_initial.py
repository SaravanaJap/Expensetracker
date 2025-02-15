# Generated by Django 5.1.1 on 2024-12-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
