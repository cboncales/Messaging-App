from django.shortcuts import render

# Create your views here.
def home_view(request):
    title = "Welcome to Tabily"
    return render(request, "a_posts/home.html" , {"title": title})