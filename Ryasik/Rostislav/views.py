from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    data = {"header": '7 927 041 57 09', "message": "Telegram: @rryasik"}
    return render(request, "contacts.html", context=data)

def forms(request):
    return render(request, "forms.html")
