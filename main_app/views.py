from django.shortcuts import render


# Create your views here.


def jinja2_demo(request):
    return render(request, 'jinja2_demo.html', {'tmpValue': [1, 2, 3, 4, 5]})
