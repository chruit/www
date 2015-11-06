from django.db import models

INVESTIGATOR = 0
STAFF = 1
AFFILIATE = 2
STUDENT = 3

EMPLOYEE_TYPE = (
    (INVESTIGATOR,'Investigator'),
    (STAFF,'Staff'),
    (AFFILIATE,'Affiliate'),
    (STUDENT,'Student'),
)

class Person(models.Model):

    full_name = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    #picture = models.ImageField
    uwnetid = models.CharField(max_length=12)
    education = models.CharField(max_length=600, blank=True)
    interests = models.CharField(max_length=600, blank=True)
    honors = models.CharField(max_length=700, blank=True)
    employment_type = models.IntegerField(default=INVESTIGATOR, choices=EMPLOYEE_TYPE)
    order = models.IntegerField()
    # according to django docs, many to many mappings should only be in one object
    #pubs = models.ManyToManyField(Publications, verbose_name="publications")
    #def __unicode__(self):
    #    return u'%s %s' % (self.full_name)

    def __unicode__(self):
        return u'%s ' % (self.full_name)

    def __str__(self):
        return str(self.full_name)

class Study(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)

    def __str__(self):
        return str(self.title)

class Publication(models.Model):
    pubmedid = models.IntegerField(primary_key=True)
    pubmedcentralid = models.IntegerField(blank=True)
    opusid = models.IntegerField(blank=True)
    title = models.CharField(max_length=200, blank=True)
    journal = models.CharField(max_length=100,blank=True)
    url = models.CharField(max_length=100,blank=True)
    pubdate = models.DateField()
    stub = models.CharField(max_length=1100)
    authors = models.ManyToManyField(Person, verbose_name="manuscript authors",blank=True)
    studies = models.ManyToManyField(Study, verbose_name="manuscript studies",blank=True)

    def __str__(self):
        return str(self.pubmedid)

    class Meta:
        # use - for descending order
        ordering = ['-pubdate']