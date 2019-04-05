import os
import json
from flask import Flask, render_template,flash,Response, request, redirect,url_for,session


app = Flask(__name__)
app.secret_key = os.urandom(26)

data = []    
wrong_answers=[]



# Handle the process of writing data to a file
def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)
        
        
        
        

if __name__ == '__main__':app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)