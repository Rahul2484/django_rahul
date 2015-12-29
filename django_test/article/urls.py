from django.conf.urls import url,patterns,include

urlpatterns = patterns('',
	#url(r'^admin/', admin.site.urls),
	url(r'^all/$','article.views.articles'),		
	url(r'^get/(?P<article_id>\d+)/$','article.views.article'),
	url(r'^language/(?P<language>[a-z\-]+)/$','article.views.language'),
	url(r'^create/$','article.views.create'),
	url(r'^help/$','article.views.help'),
	#url(r'^update/(?P<article_id>\d+)/$','article.views.update'),
	#url(r'^like/(?P<article_id>\d+)/$','article.views.like_article'),
	url(r'^search/$','article.views.search_titles'),
	#url(r'^delete/(?P<article_id>\d+)/$','article.views.delete_comment'),
    url(r'^delete/(?P<article_id>\d+)/$', 'article.views.delete_article'),
	)

