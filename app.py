# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:25:56 2021

@author: Kalp Dalal
"""

# Importing the necessary Libraries
from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request,jsonify
#from scrapperImage.ScrapperImage import ScrapperImage
#from businesslayer.BusinessLayerUtil import BusinessLayer
import os


# import request
app = Flask(__name__) # initialising the flask app with the name 'app'

#response = 'Welcome!'


@app.route('/')  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages',methods=['Get','POST'])
@cross_origin()
def displayImages():
    list_images=os.listdir('static')
    print(list_images)
    
    try:
        if(len(list_images)>0):
            return render_template('showImage.html',user_images=list_images)
        else:
            return "Images are not present"
    except Exception as e:
        print("No images found",e)
        return "Please try with a different search keyword"
    

    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000) # port to run on local machine
   #app.run(debug=True) # to run on cloud