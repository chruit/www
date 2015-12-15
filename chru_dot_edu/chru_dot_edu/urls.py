from django.conf.urls import patterns, include, url
from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','chru_dot_edu.views.index'),
    url(r'^people/$','chru_dot_edu.views.people'),
    url(r'^faculty/$','chru_dot_edu.views.faculty_list'),
    url(r'^staff/$','chru_dot_edu.views.staff'),
    url(r'^trainees/$','chru_dot_edu.views.trainees'),
    url(r'^collaborators/$','chru_dot_edu.views.collaborators'),
    url(r'^faculty/(?P<faculty>\w+)/$','chru_dot_edu.views.faculty'),
    url(r'^education/$','chru_dot_edu.views.education'),
    url(r'^education/archives$','chru_dot_edu.views.education_archives'),    
    url(r'^research/$','chru_dot_edu.views.research'),
    url(r'^research/archives$','chru_dot_edu.views.research_archives'),
    url(r'^contact/$','chru_dot_edu.views.contact'),
    url(r'^support/$','chru_dot_edu.views.support'),

    # util for web services
    #url(r'^pubmed/$','chru_dot_edu.views.pubmed_list'),
    #url(r'^pubmed/(?P<pubId>\w+)/$','chru_dot_edu.views.pubmed', name='pubmed-stub' ),

    #url(r'^admin/', include(admin.site.urls)),
)
"""
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
"""
