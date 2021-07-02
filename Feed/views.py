from django.shortcuts import render

# Create your views here.
def Feed(request):
    return render(request, 'feed/home.html')

def About(request):
    return render(request, 'feed/about.html')