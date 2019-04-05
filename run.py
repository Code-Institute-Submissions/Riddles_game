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
        
        

# add user's answer to file with wrong answers
def add_user_answers(username, answer, correct_answer):
    write_to_file("data/user_answers.json", "{0} - {1}    ( Correct - {2} )\n".format(
                                    username, answer, correct_answer))


          
#  Function to get/read answers from the file (last five)
def get_user_answers():
    wrong_answers = []
    with open("data/user_answers.json", "r+") as wrong_answer:
        wrong_answers = wrong_answer.readlines()
    return wrong_answers[-5:]


# Function to add online users and points to user's ranking board
def add_online_users(username, user_points):
    user_points = user_points
    online_users = get_online_users()
    with open('data/online_users.txt', 'a') as ranking:
        if not (username, user_points) in online_users:
            ranking.write('\n{} : {}'.format(str(username), str(user_points)))


#  Function to get online user from the file
def get_online_users():
    online_users=[]
    with open("data/online_users.txt") as online_users:
        online_users = online_users.readlines()
    return online_users[-5:]
        
        

if __name__ == '__main__':app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)