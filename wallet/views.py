from django.http import HttpResponse


# Create your views here.
def hello(request):
    print(request)
    return HttpResponse('<h1>Cohort 13</h1>')
