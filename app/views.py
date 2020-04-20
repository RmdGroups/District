from django.shortcuts import render
def index(request):
    return render(request,"index.html")


def html(request):
    return render(request,"Html.html")