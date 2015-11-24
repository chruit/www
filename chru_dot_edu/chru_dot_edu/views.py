from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404

from chru_pubs.models import *
from chru_pubs.forms import *
from chru_pubs import pubmedUtil

def index(request):
    return render(request, 'front.html', {})

def people(request):
    # investigators
    p_list = Person.objects.filter(employment_type=INVESTIGATOR).exclude(uwnetid='nsotoo').exclude(uwnetid='psaty').order_by('order')
    half_size = len(p_list)/2 + len(p_list)%2
    p_list2 = p_list[half_size:]
    p_list = p_list[:half_size]
    # staff
    e_list = Person.objects.filter(employment_type=STAFF).order_by('order')
    # trainees
    s_list = Person.objects.filter(employment_type=STUDENT).order_by('order')
    return render(request, 'people.html', {'p_list':p_list,'p_list2':p_list2,'e_list':e_list,'s_list':s_list})


def staff(request):
    p_list = Person.objects.filter(employment_type=STAFF).order_by('order')
    return render(request, 'staff.html', {'p_list':p_list})

def collaborators(request):
    p_list = Person.objects.filter(employment_type=AFFILIATE)
    return render(request, 'collaborators.html', {'p_list':p_list})

def trainees(request):
    s_list = Person.objects.filter(employment_type=STUDENT).order_by('order')
    return render(request, 'trainees.html', {'s_list':s_list})

def faculty_list(request):
    p_list = Person.objects.filter(employment_type=INVESTIGATOR).exclude(uwnetid='dsisk').exclude(uwnetid='psaty').order_by('order')
    half_size = len(p_list)/2 + len(p_list)%2
    p_list2 = p_list[half_size:]
    p_list = p_list[:half_size]
    return render(request, 'faculty_list.html', {'p_list':p_list,'p_list2':p_list2})

def faculty(request,faculty):
    print faculty
    try:
        faculty_member = get_object_or_404(Person, uwnetid=faculty)
        faculty_publications = get_list_or_404(Publication, authors__uwnetid=faculty)
        publications = faculty_publications
        # paginator = Paginator(faculty_publications, 10)

        # page = request.GET.get('page')
        # try: 
        #     publications = paginator.page(page)
        # except PageNotAnInteger:
        #     publications = paginator.page(1)
        # except EmptyPage:
        #     publications = paginator.page(paginator.num_pages)

    except:
        # is it possible to also redirect here?
        return faculty_list(request)

    return render(request, 'faculty.html', {'faculty_member':faculty_member,'publications':publications})

def pubmed_list(request):
    #print "list all faculty at this page"
    p_list = Publication.objects.all()
    return render(request, 'pub_list.html', {'p_list':p_list})

def pubmed(request,pubId):

    # retrieve from web services 
    pub = pubmedUtil.getPubmedInfo( pubId )
    return render(request, 'pub.html', {'pubId':pubId,'pub':pub})    

def education(request):
    return render(request, 'education.html')

def education_archives(request):
    return render(request, 'education_archives.html')

def research(request):
    return render(request, 'research.html')

def research_archives(request):
    return render(request, 'research_archives.html')

def chs(request):
    return render(request, 'chs.html')

def ghc(request):
    return render(request, 'ghc.html')    

def charge(request):
    return render(request, 'charge.html')    

def hvh(request):
    return render(request, 'hvh.html')

def cabs(request):
    return render(request, 'cabs.html')        

def contact(request):
    return render(request, 'contact.html')       

def support(request):
    return render(request, 'support.html')   

def contribute(request):
    if request.method == 'GET':
        form = ContactForm()

    elif request.method == 'POST': # If the form has been submitted...
        print "contribute post"

        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules 
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            print name + message + sender
            # Process the data in form.cleaned_data
            # ...

            return HttpResponseRedirect('/thanks/') # Redirect after POST

        else:
            return HttpResponseRedirect('/thanks/') # Redirect after POST


    else:
        print "contribute get?  " + request.method
    
    return render(request, 'contribute.html', {'form': form,})

def thanks(request):
    return render(request, 'thanks.html')
