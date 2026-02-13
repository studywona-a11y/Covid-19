from django.http import HttpResponse

def hello(request):

    return HttpResponse("helle,world")
