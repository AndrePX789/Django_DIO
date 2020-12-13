from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
    soma = num1 + num2
    return HttpResponse('<h1>A Resposta da Soma é {}</h1>'.format(soma))

def sub(request, num1, num2):
    sub = num1 - num2
    return HttpResponse('<h1>A Resposta da Subtração é {}</h1>'.format(sub))

def mult(request, num1, num2):
    mult = num1 * num2
    return HttpResponse('<h1>A Resposta da Multiplicação é {}</h1>'.format(mult))

def div(request, num1, num2):
    div = num1 / num2
    return HttpResponse('<h1>A Resposta da Divisão é {}</h1>'.format(div))