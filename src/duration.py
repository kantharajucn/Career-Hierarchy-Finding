########################################
#version 1.0
#Date: 04/11/2016
#Author: Kantharaju C N
#######################################
from parseJson import durations,uniqueJobs
import json

def findDuration():
    usualDuration = {}
    for job in uniqueJobs.keys():
        if job in durations.keys():
            usualDuration[job] = (durations.get(job)/uniqueJobs.get(job))
    
    '''writing usual durations of each job '''
    duration = open('../output/averageDuration.json',"w")
    for key,val in usualDuration.items():
        pair = '{'+key+':'+str(val)+'}'
        duration.write(json.dumps(pair.encode('utf-8')) + "\n")   
    duration.close() 
        
    


