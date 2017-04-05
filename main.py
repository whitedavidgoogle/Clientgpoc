import textindex
from google.cloud import datastore

def search(lu):
	index = textindex.Index()
	#index.print_lookup(lu) 
def dslist(lu):	
	list = textindex.Index()
	print "textindex Class constructor"
	list.lookuplist(lu)
	print "call lookuplist function"

lu=raw_input('Enter Word,separate multiples with a comma: ')
search(lu)
print '---now the just the files---'
dslist(lu)