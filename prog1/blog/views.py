from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.core.urlresolvers import reverse
from django.views import generic

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from forms import ProfileImageForm
from models import ProfileFile
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response


def home(request):
 	return render(request, 'blog/index.html')

def my_page(request):
 	return render(request, 'blog/my_page.html')
def documents(request):
    entries = ProfileFile.objects.all()
    context = {'entries': entries}
    return render(request, 'blog/documents.html', context)

def come_in(request):
 	return render(request, 'blog/come_in.html')
def audio(request):
    return render(request, 'blog/search_form.html')
def imeg(request):
 	return render(request, 'blog/imeg.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = ProfileFile.objects.filter(image__icontains=q)
        return render_to_response('blog/search_results.html',
            {'books': books, 'query': q})
    else:
    	q = request.GET['q']
        return render_to_response('blog/search_form.html')


def an_activated(request):
    	if request.user.is_authenticated():
    		return redirect('http://localhost:8004/my_page/')
        else:
        	return redirect("http://localhost:8004/accounts/login/")

def upload_file(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ProfileFile(image=request.FILES['image'], text=request.user)
            instance.save()
            return HttpResponseRedirect('')
    else:
        form = ProfileImageForm()
    return render(request, "blog/my_page.html", {'form': form })



def index(request):
    entries = ProfileFile.objects.all()
    context = {'entries': entries}
    return render(request, 'blog/documents.html', context)
   
from django.shortcuts import render_to_response

def delete_file(request, pk):
    ProfileFile.objects.get(id=pk).delete()
    entries = ProfileFile.objects.all()
    context = {'entries': entries}
    return render(request, 'blog/documents.html', context)

def send_file(request, pk):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes


    entries = ProfileFile.objects.all()
    context = {'entries': entries}
    filename="C:/Python27/Lib/site-packages/Django-1.7.7-py2.7.egg/django/bin/prog1/blog/static/"+unicode(ProfileFile.objects.get(id=pk))
    download_name =unicode(ProfileFile.objects.get(id=pk)).encode('utf-8')
    wrapper = FileWrapper(file(filename,"rb"))
    content_type = mimetypes.guess_type(filename)[0]
    response     = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response
    #return render_to_response(context, kwargs={'pk': image})

