import textindex
from google.cloud import datastore

def search(lu):
	index = textindex.Index()
	#index.print_lookup(lu) 
def dslist(lu):	
	index = textindex.Index()
	print "index textindex Class constructor"
	index.lookuplist(lu)
	print "call lookuplist function"
lu=raw_input('Enter Word,separate multiples with a comma: ')
search(lu)
#print '---now the just the files---'
dsin = dslist(lu)
ds = textindex.Dstore()
ds.add_aafes(dsin)
print 'write to datastore'
