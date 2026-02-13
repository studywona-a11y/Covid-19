import csv
import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.



def home(request):

    return HttpResponse("home/home.html")

def index(request):
    return render(request, "home/index.html")
def map(request):
    return  render(request,"home/map.html")
def movie(request):
    return  render(request,"home/movie.html")
# def pie(request):
#     return  render(request,"home/pie.html")
# def rank(request):
#     return  render(request,"home/rank.html")
def pie(request):
    pwd = os.path.dirname(__file__)
    with open(pwd+'/china_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)

        today_confirm1 = {}
        today_confirm2 = []
        today_confirm_name = []
        today_confirm_value = []
        for item in reader:
            args = tuple(item)
            today_confirm1.update({args[2]: args[3]})
        for key, value in today_confirm1.items():
            if (value != '0'):
                # today_confirm2.append({key: value})
                today_confirm2.append({'name': key,'value':value})
    return render(request,'home/pie.html',{'today_confirm2':today_confirm2})
def	rank(request):
    pwd = os.path.dirname(__file__)
    with open(pwd+'/china_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        time=[]
        province_name = []
        province_confirm = []
        for item in reader:
            args = tuple(item)
            # print(args)
            time.append(args[1])
            province_name.append(args[2])
            province_confirm.append(args[9])
            # time.sort()
            # atime=time[0]
        print(province_name)
        print(province_confirm)

    return render(request,'home/rank.html', {'province_name':province_name,'province_confirm':province_confirm,})
def	map(request):
    pwd = os.path.dirname(__file__)
    with open(pwd+'/china_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        time=[]
        province_name = []
        province_totalnowConfirm = []
        for item in reader:
            args = tuple(item)
            # print(args)
            time.append(args[1])
            province_name.append(args[2])
            province_totalnowConfirm.append(args[15])
            # time.sort()
            # atime=time[0]
        print(province_name)
        print(province_totalnowConfirm)

    return render(request,'home/map.html', {'province_name':province_name,'province_totalnowConfirm':province_totalnowConfirm,})