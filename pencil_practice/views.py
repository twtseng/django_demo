from django.shortcuts import render

# Create your views here.
def default_view(request):
    return render(request, 'pencil_practice.html')