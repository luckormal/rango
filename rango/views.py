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
