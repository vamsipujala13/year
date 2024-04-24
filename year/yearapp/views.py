from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("<h1><big>Hello</big></h1>")
    return render(request,"home.html")


def year(request):
    year = int(request.POST.get('year'))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = f"Yes {year} is a leap year."
    else:
        is_leap = f"No {year} is not a leap year."

    return render(request, "home.html", {"is_leap": is_leap})

def marriage(request):
    age = int(request.POST.get('age'))
    gender= request.POST['ddlgender']
    if age>=18:
        eligibility_status="You are eligible for marriage"

    else:
        eligibility_status ="Your not eligible for marriage"

    data = {"gender": gender, "eligibility_status": eligibility_status}
    return render(request, "home.html",data)