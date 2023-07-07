from django.shortcuts import render


def Home_info(request):
    return render(request,'Home.html')