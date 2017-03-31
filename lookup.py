import textindex
from google.cloud import datastore

def search(lu):

	index = textindex.Index()
#	index.print_lookup(lu) 
def dslist(lu):	
	list = textindex.Index()
	print "called lookuplist"
	list.lookuplist(lu)
	print "passed input"
	client = datastore.Client()
	print "connected DS"
	entry = client.put(list.lookuplist(lu))
#	print "write list"
'''
class Discharge(ndb.model):
	honorable = ndb.BooleanProperty()
	fn = ndb.StringProperty()

def dstore(lookuplist):
	datastore_client = datastore.Client
	kind = 'discharge'
	
	dc_key = datastore+cloent.key(kind)
	dc = datastore.Entity( 
'''
lu=raw_input('Enter Word,separate multiples with a comma: ')
search(lu)
dslist(lu)
