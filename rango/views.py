from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construck a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same {{ boldmessage}} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parametere is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

    #return HttpResponse("Rango says hay there partner! <br> \
    #<a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <br> \
    <a href='/rango/'>Index</a>")

def luc(request):
    context_cities = {'cities': [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]}
    return render(request, 'rango/luc.html', context=context_cities )