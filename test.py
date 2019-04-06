
from flask import Flask, render_template,flash,Response, request, redirect,url_for,session
from test_framework import *
from run import *
import json

data = []
with open("data/riddles.json", "r") as json_data:
    data = json.load(json_data)
    

question_nr = 1
riddles_json = 0
correct_answer = data[riddles_json]["answer"]


#---------- TESTED FUNCTIONS ---- #

# ---------AUTOMATED TESTS -------#

# Test
test_are_equal('test' ,'test')


# test that question nr is not the same as riddles index  
test_not_equal(question_nr , riddles_json)


# test that correct answer is not in the wrong answers collection
test_is_not_in(wrong_answers, correct_answer)

print('TEST PASSED')

