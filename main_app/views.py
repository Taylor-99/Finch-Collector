from django.shortcuts import render

finches = []

# Create your views here.
def home(request):
  return render(request, 'home.html')

