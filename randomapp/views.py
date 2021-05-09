from django.shortcuts import render
import random 

def home(request):
    return render(request, 'randomapp/home.html')

def result(request):
    list = ('강연우', '김서영', '김소은', '김유진', '노은성', '문다연', '박경나', '박혜준', '안현주', '오예림', '이민정', '이연수', '장한빛', '김정운', '조원아', '황서경')
    partner = random.sample(list, 2)

    return render(request, 'randomapp/result.html', {'partner':partner})
# Create your views here.
