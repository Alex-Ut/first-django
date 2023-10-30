from django.http import HttpResponse

def hello_page(request):
    return HttpResponse("<h1>Homework =Alex Ut= (1-MGV-2) </h1>"
                        "<p> Hello, World! </p>")
