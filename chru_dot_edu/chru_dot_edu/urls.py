from django.conf.urls import include, url
from django.contrib import admin
from . import views 

#admin.autodiscover()

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^people/$',views.people, name='people'),
    url(r'^faculty/$',views.faculty_list, name='faculty_list'),
    url(r'^staff/$',views.staff, name='staff'),
    url(r'^trainees/$',views.trainees, name='trainees'),
    #url(r'^collaborators/$',views.collaborators, name='collaborators'),
    url(r'^faculty/(?P<faculty>\w+)/$',views.faculty, name='faculty'),
    url(r'^education/$',views.education, name='education'),
    url(r'^education/archives$',views.education_archives, name='education_archives'),    
    url(r'^research/$',views.research, name='research'),
    url(r'^research/archives$',views.research_archives, name='research_archives'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^support/$',views.support, name='support'),

    # util for web services
    #url(r'^pubmed/$',views.pubmed_list'),
    #url(r'^pubmed/(?P<pubId>\w+)/$',views.pubmed', name='pubmed-stub' ),

    #url(r'^admin/', include(admin.site.urls)),
]

"""
if settings.DEBUG:
    urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
] + urlpatterns
"""