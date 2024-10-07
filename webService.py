import cherrypy
import pandas as pd
import Tokenization
import FaceRecognition
import Wordvec
import KeywordFilter
import os
#import SentenceBuilder

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')
nltk.download('omw-1.4')

import cherrypy_cors

#cherrypy.config.update({'server.socket_port': 5000})

tokens = Tokenization.Tokenization()
faces = FaceRecognition.FaceRecognition()
wordvec = Wordvec.Wordvec()
#sb = SentenceBuilder.SentenceBuilder()

#try:
#    os.mkdir("Data")
#except OSError as error:
#    print(error)

class MyWebService(object):
	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in()
	def tokenize(self):
		"""Handle HTTP requests against ``/tokenize`` URI."""
		if cherrypy.request.method == 'OPTIONS':
		#	# This is a request that browser sends in CORS prior to
		#	# sending a real request.

		#	# Set up extra headers for a pre-flight OPTIONS request.
			return cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])

		data = cherrypy.request.json
		#print(data)
		df = pd.DataFrame(data)
		output = tokens.run(df)
		return output.to_json()

	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in()
	def recognize(self):
		"""Handle HTTP requests against ``/tokenize`` URI."""
		if cherrypy.request.method == 'OPTIONS':
		#	# This is a request that browser sends in CORS prior to
		#	# sending a real request.

		#	# Set up extra headers for a pre-flight OPTIONS request.
			return cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])

		data = cherrypy.request.json
		df = pd.DataFrame(data)
		output = faces.run(df)
		return output.to_json()

	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in()
	def savePerson(self):
		"""Handle HTTP requests against ``/tokenize`` URI."""
		if cherrypy.request.method == 'OPTIONS':
		#	# This is a request that browser sends in CORS prior to
		#	# sending a real request.

		#	# Set up extra headers for a pre-flight OPTIONS request.
			return cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])

		data = cherrypy.request.json
		df = pd.DataFrame(data)
		output = faces.runNewPerson(df)
		return output.to_json()

	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in()
	def similarWords(self):
		"""Handle HTTP requests against ``/tokenize`` URI."""
		if cherrypy.request.method == 'OPTIONS':
		#	# This is a request that browser sends in CORS prior to
		#	# sending a real request.

		#	# Set up extra headers for a pre-flight OPTIONS request.
			return cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])

		data = cherrypy.request.json
		#print(data)
		df = pd.DataFrame(data)
		output = wordvec.run(df)
		return output.to_json()

	#@cherrypy.expose
	#@cherrypy.tools.json_out()
	#@cherrypy.tools.json_in()
	#def sentenceBuilder(self):
	#    data = cherrypy.request.json
	#    #print(data)
	#    df = pd.DataFrame(data)
	#    output = sb.run(df)
	#    #return output.to_json()
	#    return output

if __name__ == '__main__':
	#keyword stuff first
	#keywordstuff = KeywordFilter.KeywordFilter("../../UnityProjects/Arthur/")
	#keywordstuff.updateHistoric()
	cherrypy_cors.install()
	config = {'tools.sessions.timeout': 60, 'server.socket_host': '0.0.0.0', 'server.socket_port': int(os.environ.get('PORT', 5000)), 'cors.expose.on': True} #, 'cors.expose.on': True
	cherrypy.config.update(config)
	#change to final link after
	#cherrypy.response.headers["Access-Control-Allow-Origin"] = "https://secret-spire-67273.herokuapp.com"
	#cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"
	#cherrypy.response.headers["Access-Control-Allow-Headers"] = "Origin, Content-Type, Accept, X-Requested-With, X-Access-Token, X-Application-Name, X-Request-Sent-Time"
	#cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
	cherrypy.quickstart(MyWebService())

#running: 
#curl -d "{\"text\" : [\"i am not feeling good\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/tokenize
#curl -d "{\"image\" : [\"camImage.png\"], \"direc\" : [\"Data\"], \"th\" : [0.5], \"mode\" : [\"n\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/recognize
#curl -d "{\"typeTransaction\" : [\"createNode\"], \"node\" : [\"Knob\"], \"typeNode\" : [\"Person\"], \"label\" : [\"age:31,ocupation:'teacher'\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/neo4jTransaction
#curl -d "{\"text\" : [\"potato-father-shirt\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/similarWords 
#curl -d "{\"text\" : [\"Knob*loves*pizza\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/sentenceBuilder