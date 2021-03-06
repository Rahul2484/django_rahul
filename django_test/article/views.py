from django.shortcuts import render_to_response,get_object_or_404
from article.models import Article
from django.http import HttpResponse
from article.forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.conf import settings
from django.contrib import messages

def articles(request):
	
	language = 'en-gb'
	session_language = 'en-gb'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']
		
	args = {}
	args.update(csrf(request))

	args['articles'] = Article.objects.all()
	args['language'] = language
	args['session_language'] = session_language

	return render_to_response('articles.html',args)

def article(request,article_id=1):
	return render_to_response('article.html',
							 {'article':Article.objects.get(id=article_id)})

def language(request,language='en-gb'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang',language)
	response.session['lang'] = language
	return response


def create(request):
	if request.POST:
		form = ArticleForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/articles/all')

	else:
		form = ArticleForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create_article.html',args)

def help(request):
	return render_to_response('about.html')

def delete_article(request, article_id):
    c = Article.objects.get(id=article_id)
    
    #article_id = c.article.id
    
    c.delete()

    #print("Comment was deleted")
    return HttpResponseRedirect("/articles/all")



def search_titles(request):
	if request.method =="POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''	

	articles = Article.objects.filter(tags__contains = search_text)

	return render_to_response('ajax_search.html',{'articles' :articles})
