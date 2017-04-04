#import datastoremodel
import textindex
from google.cloud import datastore

def random_with_N_digits(4):
	from random import randint
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
def search(lu):

	index = textindex.Index()
#	index.print_lookup(lu) 
def dslist(lu):	
	list = textindex.Index()
	print "textindex Class constructor"
	list.lookuplist(lu)
	print "call lookuplist function"
	client = datastore.Client()
	print "created Client class constructor"
	
	print "for lookp to put dict in DS"

class Datastoremodel(db.Model):
	db.fn=StringProperty()
	
	entry = list.lookuplist(lu)
		print "call dictionary"
		for i in entry:
			entry.put(i)
key = Datastoremodel(key_name=random_with_N_digits)





lu=raw_input('Enter Word,separate multiples with a comma: ')
#search(lu)
dslist(lu)