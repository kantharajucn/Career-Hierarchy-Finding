########################################
#version 1.0
#Date: 07/11/2016
#Author: Kantharaju C N
#Name: main.py
#Description: Call all other functionalities to find the hierarchy of jobs and usual duration
#######################################

import duration
import jobHierarchies

'''Calling functions'''    
level = input('Enter the level from which job Hierarchy needs to be find\n')
print ('Finding the Job Hierarchy for level %d....\n'%(level))
if level == '' or type(level) == str:
    print("Level should be integer value")
jobHierarchies.findHierarchy(level)
print('Job Hierarchy has written to ../output/probability.json')
print("Calculating the average durations of each job")
duration.findDuration()
print('Probabilities are written to ../output/verageDuration.json')
