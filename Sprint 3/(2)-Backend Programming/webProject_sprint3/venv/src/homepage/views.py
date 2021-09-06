from django.shortcuts import render

# A function that renders the "index" or "greetings" page
def homepage_view(request, *args, **kwargs):
    return render(request, "index.html", {})