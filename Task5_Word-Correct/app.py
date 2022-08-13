from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from spellchecker import spell_checker
import requests

def word_tokenize(text : str) :
  r = requests.post('http://nlp1.exp.superai.me:10100/seg' , json = {
        "payload" : text
  })
  result = r.json()['segged']
  return result

origins = ['*']
app = FastAPI()
app.add_middleware(CORSMiddleware,
                  allow_origins = origins,
                  allow_credentials=True,
                  allow_methods=['*'],
                  allow_headers=['*']
)
spell_check = spell_checker('config.json')

class spellInput(BaseModel) :
  payload : str
 
@app.post("/spell_chk")
async def spell_check_return(data : spellInput) :
    input_data = data.payload
    input_data = word_tokenize(input_data)
    outputs = spell_check.predict(input_data)
    return {"ret" : list(outputs)}
