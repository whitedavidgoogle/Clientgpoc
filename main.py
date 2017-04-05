#import datastoremodel
import textindex
from google.cloud import datastore
n=4
def random_with_N_digits(n):
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
	
#	print "for lookp to put dict in DS"

lu=raw_input('Enter Word,separate multiples with a comma: ')
#search(lu)
dslist(lu)
