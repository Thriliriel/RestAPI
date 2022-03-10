#from keytotext import pipeline
##import pandas as pd

#class SentenceBuilder:  
#    nlp = None

#    def __init__(self): 
#        #self.nlp = pipeline("k2t-base")  #loading the pre-trained model
#        self.nlp = pipeline("mrm8488/t5-base-finetuned-common_gen")  #loading the pre-trained model

#    def run(self, text):        
        
#        #wait a bit
#        #time.sleep(0.2)
#        #textFile = sys.argv[1]
#        #print(text)

#        text = text["text"][0]
#        writeResult = ""

#        if text == "":
#            print("false")
#            return False
#        else:
#            #get all tokens from the text
#            #using * to mark it
#            tokens = text.split('*')
#            #params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":3, "early_stopping":True}    #decoding params
#            #writeResult = self.nlp(tokens, **params)  #keywords
#            writeResult = self.nlp(tokens)  #keywords
        
#        return writeResult
#        #return pd.DataFrame(writeResult)
#        #return pd.DataFrame(clean_tokens)
#        #return pd.DataFrame([sentiResult])



##To quote keytotext please use this citation

##@misc{bhatia, 
##      title={keytotext},
##      url={https://github.com/gagan3012/keytotext}, 
##      journal={GitHub}, 
##      author={Bhatia, Gagan}
##}
