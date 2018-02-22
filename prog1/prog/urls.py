from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView
from django.conf import settings
#rom blog.views import ProfileImageIndexView
#rom blog.views import ProfileImageView
#from blog.views import ProfileDetailView
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    #url(r'^accounts/', include('registration.urls')),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media'}),
    url(r'^$', 'blog.views.home', name='home'),
    #url(r'^documents/', 'blog.views.documents', name='documents'),
    #url(r'^audio/$', 'blog.views.audio', name='audio'),
    #url(r'^search-form/$', 'blog.views.search_form'),
    url(r'^search/$', 'blog.views.search'),
    url(r'^audio/(?P<pk>\d+)/$', 'blog.views.send_file', name='audio'),
    url(r'^del/(?P<pk>\d+)/$', 'blog.views.delete_file', name='audio'),
    url(r'^imeg/', 'blog.views.imeg', name='imeg'),
    #url(r'^my_page/', 'blog.views.my_page', name='my_page'),
    url(r'^$', 'registration.views.reg', name='reg'),
    url(r'^$', 'registration.views.login', name='login'),
    
    (r'^accounts/', include('registration.urls')),
        # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url('accounts/', include('registration.backends.default.urls')),
    #url(r'^$', ProfileImageIndexView.as_view(), name='home'),

    url(r'^my_page/', 'blog.views.upload_file', name='profile_image_upload'),
    url(r'^accounts/profile/', 'blog.views.an_activated', name=''),
    url(
        r'^uploaded/(?P<pk>\d+)/$', 'blog.views.send_file',
        name='profile_image'),
    url(r'^documents/', 'blog.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),

    (r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)