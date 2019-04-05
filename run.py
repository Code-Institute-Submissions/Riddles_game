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
    write_to_file("data/user_answers.txt", "{0} - {1}    ( Correct - {2} )\n".format(
                                    username, answer, correct_answer))


          
#  Function to get/read answers from the file (last five)
def get_user_answers():
    wrong_answers = []
    with open("data/user_answers.txt", "r+") as wrong_answer:
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
        


   
# Route to log in user
# from login page user is redirected to game page (game function) after submitting "login" button, 
@app.route('/', methods=["GET", "POST"])
@app.route('/log_in/', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('game'))
    return render_template("index.html")



# Route to the game page
@app.route("/game", methods=["GET", "POST"])
def game():
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    
    # Set variables  to default values 
    username = session.get('username')
    session['user_points'] = 0
    user_points = session.get('user_points')
    question_nr = 1
    riddles_json = 0
    

    if request.method == "POST":
        session['answer'] = request.form["user-answer"].lower()
        session['user_points'] = int(request.form["user_points"])
        user_points = session.get('user_points')
        riddles_json = int(request.form["riddles_track"])
        question_nr =int(request.form["question_nr"])
        answer = session.get('answer').lower()
        correct_answer = data[riddles_json]["answer"]
        last_question = data[riddles_json]["description"] == "GAME OVER!"  
        
        
        # Check if submitted answer is the same as correct answer
        # If the answer is correct, go to next riddle, change question nr and add point, message about correct answer
        # After last question online users and point's are added to the user's ranking.
        # If the answer is wrong user doesn't get point and go for next riddle, users get message about wrong answer
        
        
        
        if  data[riddles_json]["answer"].lower() == answer:
            question_nr +=1
            riddles_json +=1
            user_points +=1
            flash('WELL DONE !  CORRECT ANSWER !', 'success')
        elif answer == '':
            flash('PLEASE TYPE YOUR ANSWER !', 'info')
        elif data[riddles_json]["answer"] != answer:
            add_user_answers(username, answer.upper(), correct_answer.upper())
            question_nr += 1
            riddles_json +=1
            flash('SORRY !  WRONG ANSWER !', 'error')
        


        if riddles_json > 14:
            add_online_users(username, user_points)
            
    
    wrong_answers=get_user_answers()
    online_users = get_online_users()
    last_question = data[riddles_json]["description"] == "GAME  OVER !"
    
    
    return render_template("game_page.html",  riddle_data=data, riddles=riddles_json,
        question_nr=question_nr, user = username, online_users = online_users, user_points = user_points,
        wrong_answers=wrong_answers, last_question = last_question
         )

# Route to game over page 
@app.route('/game_over', methods=["GET", "POST"])
def game_over():
    username = session.get('username')
    user_points = session.get('user_points')
    online_users = get_online_users()
    return render_template("game_over.html",  user = username, user_points = user_points, online_users = online_users)
       

if __name__ == '__main__':app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)