import datetime
from google.appengine.ext import db
from google.appengine.ext import users

class ddstatus(db.Model):
	fn = db.StringPropert(required=True)
	status = db.Boolean(required=True)
	
