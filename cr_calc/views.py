from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .calc import helper

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Калькулятор", 'url_name': 'calc'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    return render(request, 'cr_calc/about.html', {'menu': menu, 'title': 'О сайте'})

def about(request):
    return render(request, 'cr_calc/about.html', {'menu': menu, 'title': 'О сайте'})


def calculate(request):
    if request.method == 'POST':
        form = CalcPostForm(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                value = helper.calc(form.cleaned_data)
                print(value)
                form = CalcPostForm()
                if value['Approve'] == 'Кредит не одобрен':
                    result = value['Approve']
                    approve = f'Результат: {result}'
                    return render(request, 'cr_calc/calc.html', {
                                                                'form': form, 
                                                                'menu': menu, 
                                                                'title': 'Кредитный калькулятор',
                                                                'approve': approve
                                                            })
                else:
                    result = value['Approve']
                    approve = f'Результат: {result}'
                    summa=value['Approved_amount']
                    amount_value = f'Одобренная сумма: {summa} млн. рублей'
                    rate = round(value['Rate'], 2)
                    approve_rate = f'Процент ставки по кредиту: {rate}%'
                    summa=value['Annual']
                    annual_payment = f'Ежегодный платеж: {summa} млн. рублей'
                    return render(request, 'cr_calc/calc.html', {
                                                                'form': form, 
                                                                'menu': menu, 
                                                                'title': 'Кредитный калькулятор',
                                                                'approve': approve,
                                                                'amount': amount_value,
                                                                'approve_rate': approve_rate,
                                                                'annual_payment': annual_payment
                                                            })
                # return redirect('home')
            except Exception:
                form.add_error(None, 'Ошибка расчета')

    else:
        form = CalcPostForm()
    return render(request, 'cr_calc/calc.html', {'form': form, 'menu': menu, 'title': 'Кредитный калькулятор'})

def login(request):
    return redirect('home')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
