from django.shortcuts import render

# Create your views here.

# function to return home.html template
def welcome(request):
    return render(request, 'recipes/recipes_home.html')
