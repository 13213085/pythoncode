# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:13:38 2017

@author: 29907
"""

#random_quiz_generator.py - Creat quizes with questions and answers
#in random order and the answers

import random

#The quiz data.Keys are states and values are their capitals
state_capital={'Albama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
               'Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver',
               'Connecticut':'Harford','Delaware':'Dover','Florida':'Tallahassee',
               'Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illibois':
               'Springfield','Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':
               'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':
               'Augusta','Maryland':'Annapolis','Massachusetts':'Boston','Michigan':
               'Lansing','Minnesota':'Saint Paul','Mississippi':'Jackson','Missouri':
               'Jefferson City','Montana':'Helena','Nebraska':'Lincoln','Nevada':
               'Carson City','New Hampshire':'Concord','New Jersey':'Trenton','New Mexico'
               :'Santa Fe','New York':'Albany','North Carolina':'Raleigh',
               'North Dakota':'Bismarck','Ohio':'Columblus','Oklahoma':'Oklahoma City',
               'Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence',
               'South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':
               'Nashville','Texas':'Austin','Utah':'Salt Lake City','Vermont':
               'Montopellier','Vriginia':'Richmod','Washington':'Olympia','West Virginia':
               'Charleston','Wisconsin':'Madison','Wyoming':'Cheyenne'}
state_list=list(state_capital.keys())

#Generate quiz file.
for quiz_num in range(35):
    #Create quiz and answer file.
    quiz_file=open('No%d_quiz.txt'%(quiz_num+1),'w')
    answer_file=open('No%d_answer.txt'%(quiz_num+1),'w')
    
    #Print file header
    quiz_file.write('Name:\n')
    quiz_file.write('Student Number:\n')
    quiz_file.write((' '*10)+'State Capital Quize %s'%(quiz_num+1)+'\n')
    answer_file.write((''*10)+'Answer %s'%(quiz_num+1)+'\n')

    #Generate answer       
    answer_list=[]
    for i in range(50):
        answer=random.choice(['A','B','C','D'])
        answer_list.append(answer)
        answer_file.write('%s.'%(i+1)+answer+'\n')          
    
    #Generate quiz
    random.shuffle(state_list)
    for i in range(50):
        capital_list=list(state_capital.values())
        quiz_file.write('%s.'%(i+1)+'The captital of '+state_list[i]+' is ____.\n')
        capitals=capital_list
        capitals.remove(state_capital[state_list[i]])
        for answer_num in ['A','B','C','D']:
            if answer_num==answer_list[i]:
                quiz_file.write(answer_num+' .'+state_capital[state_list[i]]+'\n')
            else:
                quiz_file.write(answer_num+' .'+random.choice(capital_list)+'\n')
      
    quiz_file.close()
    answer_file.close()
               
                   
                   
                   
                   
                 
    
              
            
               