#! /usr/bin/python
# Mark Christiansen 2/26/14
import xmltodict, json
from Bio import Entrez
from datetime import date
import sys, getopt

def dumpXML( articleID ):
    Entrez.email = "chruit@uw.edu"
    handle = Entrez.efetch(db="pubmed", id=articleID, retmode="xml")
    xml = handle.read()
    print xml

def getPubmedInfo( articleID ):

    month = {}
    month['Jan'] = 1
    month['Feb'] = 2
    month['Mar'] = 3
    month['Apr'] = 4
    month['May'] = 5
    month['Jun'] = 6
    month['Jul'] = 7
    month['Aug'] = 8
    month['Sep'] = 9
    month['Oct'] = 10
    month['Nov'] = 11
    month['Dec'] = 12

    Entrez.email = "chruit@uw.edu"
    handle = Entrez.efetch(db="pubmed", id=articleID, retmode="xml")
    xml = handle.read()
    #print xml
    o = xmltodict.parse(xml)
    print json.dumps(o)

    
    #print o.keys()
    pmarticles = o['PubmedArticleSet']
    #print pmarticles.keys()
    pmarticle = pmarticles['PubmedArticle']
    #print pmarticle.keys()
    
    # pubmed data contains mostly revision info.  
    # we do not want this for now
    #pubmeddata = pmarticle['PubmedData']
    #print pubmeddata.keys()
    
    # the critical information is included in MedlineCitation
    medlinecitation = pmarticle['MedlineCitation']
    #print medlinecitation.keys()
    #print "article"

    article = medlinecitation['Article']
    journal = article['Journal']
    journal_issue = journal['JournalIssue']
    #print journal_issue
    isoabbreviation = journal['ISOAbbreviation']
    #print isoabbreviation 

    journal_pubdate = journal_issue['PubDate']
    #print str(journal_pubdate) + "; "

    # doesn't exist for some records
    try:
        journal_volume = journal_issue['Volume']
    except:
        print "No Volume number "
        journal_volume = None

    # doesn't exist for some records
    try:
        journal_issue_val = journal_issue['Issue']
    except:
        print "No Issue number "
        journal_issue_val = None


    # doesn't exist for some records
    #pagination = article['Pagination']['MedlinePgn']

    # PUBMED has terribly incomplete data.  
    try:
        month = month[journal_pubdate['Month']]
    except KeyError:
        print "No Month"
        month = 1
    
    try:
        day = int(journal_pubdate['Day'])
    except KeyError:
        print "No Day:"
        day = int(1)

    #print "month " + str(month)

    journal_date_val = date(int(journal_pubdate['Year']),month,day)
    journal_title = journal['Title']

    article_title = article['ArticleTitle']
    
    pagination = article['Pagination']
    #print pagination

    # construct a string of our author list
    author_list = article['AuthorList']
    authors = author_list['Author']
    nauthors = len(authors)
    #print nauthors
    count = 0
    author_val = ''
    for author in authors:
        #print author
        temp_author = ''
        #print author.keys()
        for key in author.keys():
            #print key
            if key == 'LastName':
                #print 'last'
                temp_author = author[key]
            elif key == 'Initials':
                #print 'inits'
                temp_author = author[key] + ' ' + temp_author
            elif key == 'CollectiveName':
                #print 'collective'
                temp_author = author[key]
                #     print author['Initials'] + ' ' + author['LastName']
                #     author_val+= author['Initials'] + ' ' + author['LastName']

                #     author_val+= author['CollectiveName'] 
        author_val += temp_author
        
        if count < nauthors-1:
             author_val+= ', '
        count+=1

    #print 'journal title is ' + journal_title
    ##print 'journal volume is ' + journal_volume
    ##print 'journal issue is ' + journal_issue_val
    #print 'journal pub date is ' + str(journal_date_val)
    #print 'article title is ' + article_title
    #print 'author list is ' + author_val

    # generate this in the template for now
    #link = '<a href="http://www.ncbi.nlm.nih.gov/pubmed/' + articleID + '">' + 'PMID:' + articleID + '</a>'

    stub =  author_val + '. ' + article_title + ' '  #+ link

    # append journal info
    if journal_volume is not None:    
        stub = stub + str(journal_volume) + ": "

    if journal_issue_val is not None:
        stub = stub + journal_issue_val + "."

    stub = stub + journal_title + ' ' + str(journal_date_val) + '. '

    return stub
    

def main(argv):
    pubmedID = ''
    try:
      
      opts, args = getopt.getopt(argv,"d:h:p:",["pubmed="])
    except getopt.GetoptError:
      print 'pubmedUtil.py -p <pubmedID>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'pubmedUtil.py -d <pubmedIID>  # dumps pubmed XML '
         print 'pubmedUtil.py -p <pubmedIID>  # will parse pubmed entry'
         sys.exit()

      elif opt in ("-d"):
         pubmedId = arg
         dumpXML(pubmedId)

      elif opt in ("-p", "--pubmed"):
         pubmedID = arg
         print getPubmedInfo(pubmedID)

if __name__ == "__main__":
   main(sys.argv[1:])