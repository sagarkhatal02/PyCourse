
from django.http import HttpResponse
from django.shortcuts import render


#def about(request):
#    return HttpResponse("Hello about")    

def index(request):
    #params={'Name':'Sagar','Place':'Pune'}
    #return render(request,'index.html',params)
    return render(request,'index.html')

#def removepunc(request):
#    restxt=request.GET.get('text','default')
#    return HttpResponse("remove punc <a href='/'>"+restxt+"</a>")

def analyzer(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    punctu='''!()-[]{}:;'"\,<>/?@#$%^^&*-'''
    analyzed=""
    if removepunc=='on':
        for c in djtext:
            if c not in punctu:
                analyzed=analyzed+c
    else:
        analyzed=djtext
        
    params={'purpose':'remove pu2nc','analyzed_text':analyzed}
    punctu=""
    return render(request,'analyze.html',params)

    #return HttpResponse("remove punc <a href='/'>"+removepunc+"</a>")

#def capfirst(request):
#    return HttpResponse("capitilized first")
    
#def newlineremove(request):
#    return HttpResponse("new line remove")

#def spaceremove(request):
#    return HttpResponse("space remove")

#def charcount(request):
#    return HttpResponse("character count")