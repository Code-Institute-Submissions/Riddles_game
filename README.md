
# PROJECT NAME:

- Riddle-me-this quessing game

- this game is a mile stone project for Practical Python module.

- This is the game where user is asked to answer for 15 questions to get points.

- If users answers correctly they are redirected to next riddle and get point.

- If users answers wrong, they are redirected to next riddle with no points

- After The game user can compare his/her's results with other users results in the user's ranking board.

- The game is very good for entertainment 


# UX

LINK TO PROJECT MOCKUP : https://app.moqups.com/zsQrNCKgod/view

# USER'S STORIES :

# As a student I want to find correct answers so that I train my creativity and challenge with others
- after submit answer, user can see message if the answer was correct or not. 
  Also see correct answer in the bracket beside wrong answer in WRONG USER'S ANSWERS board
- all wrong answers are stored and displayed on the "" WRONG ANSWERS" board


# As a gamer I want to get the best results so that I enjoy more and be the best player
- It is possible for multiple players to play at the same time so players can compete with each other.
- After finish game users and their final results are displayed on "USER'S RANKING BOARD" so users can compare their results to each other


# FEATURES  

- Players are asked to quess answer to a pictorial or text-based riddle.
 
- The player is presented with text that contains the riddle.
 
- Answers submitt - Players types answers into a textarea and submit them using a form.
 
- Scoring - If users answers correctly they are redirected to next riddle and get point.

- If users answers incorrectly, they are redirected to next riddle with no points and textarea is cleared. 
  Their wrong answer is stored and displayed on "WRONG ANSWERS" board. correct answer is displayed beside it.
 
- Log in functionality - User submit his/her name by the form and is logged in to the game.

- Multiplayer possibility - Multiple players can play in the game in the same time form their own browser.

- Flash messges- Displayed after user answers each question let user know if the answer was correct or not.

- After answer all 15 questions, user is redirected to game over page where total scores and user's ranking board are displayed.

- Button "CLICK TO PLAY AGAIN" (game over page) -  which redirect users to log in page so user can play game again.

- User's ranking board -  displays last 5 users and their points played recently so users can compare their results to others

- Wrong answers board - displays last 5 user's wrong answers so user can see his/her mistakes and aslo correct answer in the brackets



# TESTING :

Application was tested manually by pretending to be a user and play the game:

- Enter name and using form to log in to the game and test if form requests are sent correctly and user is redirected to game page
    Also if username is passed to the game page(displayed as a player).

- Submit correct answer to test if the point is adding, next riddle is shown, success flash message is shown.

- Submit incorrect answer to test if the next riddle is shown, point's are not added, error flash message is shown 
    and also if the user's wrong answer is displayed in WRONG ANSWER'S board (correct answer in bracket's)

- submit an empty form to test if info flash message is shown and there are no changes in points and riddles redirection.
    Also nothing should be added to WRONG ANSWER boar.

- Tests if after last question, user is added to ranking board, submitt form is disapear and "go to ranking" buttom is displayed

- click "go to ranking" buttom to test if it lead user to game over page.

- click "click to play again" buttom to test if it lead to log in page (index.html)


- Application was also tested by using google developers tools to check it responsiveness for particular screen width,
to check if there are active user's session or if there are errors 

- Project responsiveness was tested by google developer tools where it was resising to particular device size(for example iphones,samsung )
It was tested also by changing size of browser window and by opening application on diferent types of devices(Iphone 5s, Iphone XR, Huawei).
I chose Desktop first approach because percentage of users using website will be using PC's.
Application looks good on all screen sizes but works best on the large and medium screen size. On small sizes pages  
Application was tested after each functionality was added to it.


# TECHNOLOGIES USED:

- Python - To create backend and add functionalities to project.

- HTML - To create basic structure of the project LINK ( https://www.w3schools.com/html/ ) 

- CSS - To add styles to the project. Also some part of responsiveness was done by css styles by adding media queries.

- Bootstrap framework to create responsive layout and add some design and components by add helpfull classes. LINK: https://getbootstrap.com/ 

- Flask framework to create backend and add functionalities to the project. Flask helps backend and front en work together as a whole LINK: http://flask.pocoo.org/



# DEPLOYMENT

 The project was deployed on Heroku platform under link : https://riddles-game-app.herokuapp.com/
 COMMANDS USED TO DEPLOY PROJECT TO Heroku:
- git init (create empty repository)
- git add ( to add files)
- git commit -m'' (to commit changes and add message)
- heroku login (To log in to heroku platform)
- heroku ps:scale web=1 (to run app on heroku)
- git push heroku master ( to push local repository to heroku)



# CREDITS

Used as aa example:  https://github.com/ckz8780/ci-pp-milestone-riddlemethis

Used as a guide for user sessions:
https://www.youtube.com/watch?v=T1ZVyY1LWOg

Used as a guide for flash messages:
http://flask.pocoo.org/docs/1.0/patterns/flashing/


# Acknowledgements
  I received inspiration for this project from my mentor Theo Despoudis 

# Background image taken from:
  www.images.pexels.com  (https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940)

