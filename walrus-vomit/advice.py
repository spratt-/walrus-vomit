from google.appengine.ext import ndb

class Advice(ndb.Model):
	content = ndb.StringProperty(required = True)
	source = ndb.StringProperty(required = True)
	