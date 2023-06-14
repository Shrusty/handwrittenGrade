from PIL import Image, ImageTk
import requests
import json
import base64
import os 
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def gen_text():
    api_key = "INSERT API KEY"
    url = "https://vision.googleapis.com/v1/images:annotate?key=" + api_key
    # Load image data from file into memory
    answer={}
    global subject
    for name in os.listdir('./'+subject):
        count=int(name[0])
        key=count
        if key in answer.keys():
            pass
        else:
            answer[key]=''
        with open('./'+subject+'/'+name, 'rb') as image_file:
            image_content = image_file.read()
        image_content_base64 = base64.b64encode(image_content).decode('utf-8')
        request_json = {
          "requests": [
            {
              "image": {
                "content": image_content_base64
              },
              "features": [
                {
                  "type": "DOCUMENT_TEXT_DETECTION"
                }
              ]
            }
          ]
        }



def preprocess(text):
    
    text = text.lower()

    
    text = text.replace('\n', '')

    
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])

    
    tokens = word_tokenize(text)

    
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

def extract_matching_words(word_list, combined_word):
    matching_words = []
    for word in word_list:
        if word in combined_word:
            matching_words.append(word)
    return matching_words,1
def calc_simi(answer):
    global subject
    with open('iot.txt', 'r') as file:
        file_contents = file.read()