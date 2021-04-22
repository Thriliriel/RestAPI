from neo4j import GraphDatabase
import pandas as pd

class Neo4J:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run(self, text):   
        #print(text)
        hasNode = hasTypeNode = hasLabel = hasMatch = hasNode2 = hasRelat = False

        #for item in text:
        #    if "node" in item:
        #        hasNode = True
        #    elif "typeNode" in item:
        #        hasTypeNode = True
        #    elif "label" in item:
        #        hasLabel = True
        #    elif "match" in item:
        #        hasMatch = True
        #    elif "node2" in item:
        #        hasNode2 = True
        #    elif "relationship" in item:
        #        hasRelat = True

        result = "false"
        if text["typeTransaction"][0] == "createNode":
            result = self.transaction(typeTransaction = text["typeTransaction"][0], node = text["node"][0], typeNode = text["typeNode"][0], label = text["label"][0])
        elif text["typeTransaction"][0] == "matchNode":
            result = self.transaction(typeTransaction = text["typeTransaction"][0], match = text["match"][0])
        elif text["typeTransaction"][0] == "updateNode":
            result = self.transaction(typeTransaction = text["typeTransaction"][0], node = text["node"][0], nodeKey = text["nodeKey"][0], nodeValue = text["nodeValue"][0])
        elif text["typeTransaction"][0] == "deleteNode":
            result = self.transaction(typeTransaction = text["typeTransaction"][0], node = text["node"][0])
        elif text["typeTransaction"][0] == "addRelationship":
            result = self.transaction(typeTransaction = text["typeTransaction"][0], node = text["node"][0], node2 = text["node2"][0], relationship = text["relationship"][0])

        #print(result)

        #if result == "false":
        #    return pd.DataFrame([result])
        #else: 
        return pd.DataFrame([result])

    def transaction(self, typeTransaction, node = None, typeNode = None, label = None, match = None, node2 = None, relationship = None, nodeKey = None, nodeValue = None):
        with self.driver.session() as session:
            #print(typeTransaction)
            if typeTransaction == 'createNode':
                returnValues = session.write_transaction(self.createNode, node, typeNode, label)
                return returnValues
                #print(returnValues)
            elif typeTransaction == "matchNode":
                returnValues = session.write_transaction(self.matchNodes, match)
                #print(returnValues)
                return returnValues
            elif typeTransaction == "updateNode":
                returnValues = session.write_transaction(self.updateNode, node, nodeKey, nodeValue)
                #print(returnValues)
                return returnValues
            elif typeTransaction == "deleteNode":
                returnValues = session.write_transaction(self.deleteNodes, node)
                #print(returnValues)
                return returnValues
            elif typeTransaction == "addRelationship":
                returnValues = session.write_transaction(self.addRelationship, node, node2, relationship)
                #print(returnValues)
                return returnValues

    @staticmethod
    def createNode(tx, node, typeNode, label):
        #print(node, typeNode, label)
        #MERGE will create if not exists
        if label == "":
            result = tx.run("MERGE ("+node+":"+typeNode+" {name:'"+node+"'}) return "+node)
        else:
            result = tx.run("MERGE ("+node+":"+typeNode+" {name:'"+node+"',"+label+"}) return "+node)
        #print(result.value()[0].id)
        #return {"id": result.value()[0].id}
        return result.value()[0].id

    @staticmethod
    def matchNodes(tx, match):
        result = tx.run(match)
        return result.data()

    @staticmethod
    def updateNode(tx, node, nodeKey, nodeValue):
        qry = "match (a {name:'"+str(node)+"'}) set a."+str(nodeKey)+" = '"+str(nodeValue)+"'"
        #return qry
        #print(qry)
        result = tx.run(qry)
        return result.value()

    @staticmethod
    def deleteNodes(tx, node):
        #delete relationships first
        result = tx.run("match (a {name:'"+node+"'}) match (a)-[b]->() delete b")
        result = tx.run("match (a {name:'"+node+"'}) delete a")
        return result.value()

    #add relationship between 2 nodes
    @staticmethod
    def addRelationship(tx, node, node2, relationship):
        #result = tx.run("match (a {name:'"+node+"'}),(b {name:'"+node2+"'}) create (a)-[:"+relationship+"]->(b)")
        result = tx.run("match (a),(b) where id(a)="+str(node)+" AND id(b)="+str(node2)+" merge (a)-[:"+relationship+"]->(b)")
        return result.value()


#if __name__ == "__main__":
    #greeter = NeoWebService("bolt://localhost:7687", "neo4j", "sh4d0w")
    #greeter.transaction("createNode", "Knob", "Person", "age:31,ocupation:'teacher'")
    #greeter.transaction("createNode", "Arthur", "Person", "age:1,ocupation:'Bot'")
    #greeter.transaction("addRelationship", node = "Knob", node2 = "Arthur", relationship = "KNOWS")
    #greeter.transaction("matchNode", match = "match (a:Person {name:'Knob'}) return a")
    #greeter.transaction("deleteNode", node = "Knob")
    #greeter.close()