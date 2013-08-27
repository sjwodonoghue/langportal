from django.shortcuts import render
from django.template import Context, loader
from models import dictionary
from random import randint
from django.db.models import Max, Min
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('french/login.html', c)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('french/loggedin')
    else:
        return HttpResponseRedirect('invalid_login.html')
    
def loggedin(request):
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
        return render_to_response('invalid_login.html')
   

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')




def index(request):
    
    #    Get min id and max id and then get a random number between them.
    #    Retrieve from the dictionary model the entry for that ID.
    #    Send the retrieved information to the template.
    
    minval = dictionary.objects.all().aggregate(Min('id'))
    maxval = dictionary.objects.all().aggregate(Max('id'))
    idval = randint(minval['id__min'],maxval['id__max'])
    
    word_details = dictionary.objects.get(id=idval)
    french = word_details.french.encode(encoding='UTF-8',errors='strict')

    context = Context({
        'word_details': word_details, 'french':french
    })

    return render(request, 'french/index.html', context)




def wordtest(request):

    #    Get min id and max id and then get a random number between them.
    #    Retrieve from the dictionary model the entry for that ID.
    #    Send the retrieved information to the template.

    minval = dictionary.objects.all().aggregate(Min('id'))
    maxval = dictionary.objects.all().aggregate(Max('id'))
    idval = randint(minval['id__min'],maxval['id__max'])
    
    word_details = dictionary.objects.get(id=idval)
    #print test_words
    context = Context({'word_details': word_details})
    return render(request, 'french/wordtest.html', context)


def checkanswers(request):
    #    get POST data
    #    get the key values of the POST querydict object, these are also the words we are asking the user to translate
    vals = []
    testwords = sorted(request.POST.keys())
    user_answer = request.POST[testwords[0]]
    id = testwords[0]
    
    word = dictionary.objects.filter(pk=id)[0]
    french = word.french
    response = ''
    if french == user_answer:
        response = 'correct'
        extra = ''
    else:
        response = 'incorrect'
        extra = "The correct answer is: " + french 
    
    vals.append(testwords)
    vals.append(user_answer)
    vals.append(id)
    vals.append(french)
    vals.append(response)
    context = Context({
        'response': response, 'extra':extra  
    })
    return render(request, 'french/checkanswers.html', context)
    #return HttpResponseRedirect(reverse('checkanswers.html'))



