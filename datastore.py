from google.cloud import datastore
#def dsinput():
client = datastore.Client()#namespace=ocr)
x=client.get(1)
print x


#def dsoutput():
