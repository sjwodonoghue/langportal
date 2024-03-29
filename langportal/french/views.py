from django.shortcuts import render
from django.template import Context, loader
from models import dictionary
from random import randint
from django.db.models import Max, Min
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


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
    testwords = request.POST.keys()
    context = Context({
        'testwords': testwords
    })
    #return render(request, 'french/checkanswers.html', context)
    return HttpResponseRedirect(reverse('french/checkanswers.html'))



