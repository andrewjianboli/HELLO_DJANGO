# from django.shortcuts import render

# Create your views here.

import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse ("hello Django!")

def hello_there(request, name):

    print(request.build_absolute_uri()) # optional

    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
    
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")
    #
    # filter the name argument to letters only using regular expressons. URL arugements 
    # can contain arbitrary text, so we restrict to safe characters only.
    #
    # match_object = re.match("[a-zA-Z]+", name)
    #
    # if match_object:
    #    clean_name = match_object.group(0)
    # else:
    #    clean_name = "Friend"
    #
    # content = "Hello there, " + clean_name + "! It's " + formatted_now
    #
    # return HttpResponse(content)

