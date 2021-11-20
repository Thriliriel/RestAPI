import cherrypy
import pandas as pd
import Tokenization
import FaceRecognition
import Wordvec
import KeywordFilter
import os

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')

#cherrypy.config.update({'server.socket_port': 5000})

tokens = Tokenization.Tokenization()
faces = FaceRecognition.FaceRecognition()
wordvec = Wordvec.Wordvec()

class MyWebService(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def tokenize(self):
        data = cherrypy.request.json
        #print(data)
        df = pd.DataFrame(data)
        output = tokens.run(df)
        return output.to_json()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def recognize(self):
        data = cherrypy.request.json
        df = pd.DataFrame(data)
        output = faces.run(df)
        return output.to_json()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def savePerson(self):
        data = cherrypy.request.json
        df = pd.DataFrame(data)
        output = faces.runNewPerson(df)
        return output.to_json()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def similarWords(self):
        data = cherrypy.request.json
        #print(data)
        df = pd.DataFrame(data)
        output = wordvec.run(df)
        return output.to_json()

if __name__ == '__main__':
    #keyword stuff first
    #keywordstuff = KeywordFilter.KeywordFilter("../../UnityProjects/Arthur/")
    #keywordstuff.updateHistoric()

    config = {'server.socket_host': '0.0.0.0', 'server.socket_port': int(os.environ.get('PORT', 5000))}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())

#running: 
#curl -d "{\"text\" : [\"i am not feeling good\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/tokenize
#curl -d "{\"image\" : [\"camImage.png\"], \"direc\" : [\"Data\"], \"th\" : [0.5], \"mode\" : [\"n\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/recognize
#curl -d "{\"typeTransaction\" : [\"createNode\"], \"node\" : [\"Knob\"], \"typeNode\" : [\"Person\"], \"label\" : [\"age:31,ocupation:'teacher'\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/neo4jTransaction
#curl -d "{\"text\" : [\"potato-father-shirt\"]}" -H "Content-Type: application/json" -X POST http://localhost:8080/similarWords 