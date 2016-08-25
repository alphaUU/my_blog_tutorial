from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    # url(r'^test/$', 'article.views.test'),
    url(r'^$', 'article.views.home', name='home'),
    url(r'^archives/$', 'article.views.archives', name='archives'),
    url(r'^aboutme/$', 'article.views.about_me', name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name='search_tag'),
    url(r'^search/$','article.views.blog_search',name='search'),

)
