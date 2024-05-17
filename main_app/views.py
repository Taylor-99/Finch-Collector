from django.shortcuts import render
# Import the Finch Model
from .models import Finch


finches = [
   {'species': 'American Goldfinch', 'description': 'A vibrant symbol of summer, sports bright yellow plumage with black wings and a distinct black cap.', 'size': 4.5, 'habitat': "Open Woodlands"},
   {'species': 'Black Rosy-Finch', 'description': 'A striking alpine bird, boasts a glossy black plumage with contrasting pinkish tones on its wings and belly.', 'size': 6, 'habitat': "Tundra"},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})