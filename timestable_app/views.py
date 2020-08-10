from django.shortcuts import render

# Create your views here.
def default_view(request):
    return render(request, 'super_times_table.html') 