#from google.appengine.ext import ndb
def search(lu):
	import textindex
	from google.cloud import datastore

	index = textindex.Index()
#	index.print_lookup(lu) 
	
	list = textindex.Index()
	print "called lookuplist"
	list.lookuplist(lu)
	print "passed input"
'''	client = datastore.Client()
	print "connected DS"
	var = ar(HONORABLE=True, fn=list[0])
#	list.put()
#	print "write list"


class Discharge(ndb.model):
	honorable = ndb.BooleanProperty()
	fn = ndb.StringProperty()

d = Discharge()
def get_entity(honorable):
	honorable_key = honorable.get()
'''
lu=raw_input('Enter Word,separate multiples with a comma: ')
search(lu)

#for i in result
#print index


#def dbwrite():
	#python mysql connection

