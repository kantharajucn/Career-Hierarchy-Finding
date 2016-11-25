########################################
#version 1.0
#Date: 04/11/2016
#Author: Kantharaju C N
#######################################
import json
import re
from dateutil.parser import parse
import datetime as dt
from collections import defaultdict
from collections import Counter
count = 1
objectNumber = 1
myDict = defaultdict(list)
durations = {}
uniqueJobs = Counter()
with open('../input/career.sample.json') as json_data:
    for eachline in json_data:
        parseline = re.split('},',eachline[1:-2])
        for eachObject in reversed(parseline):
            myList = []
            if not eachObject.endswith("}"):
                eachObject = eachObject.encode("ascii", errors="ignore")
                eachObject = json.loads(eachObject.strip() +"}")
                if(eachObject['start'] == ''):
                    continue
                try:
                    start = parse(eachObject['start'])
                except ValueError:
                    continue
                if(eachObject['end'] == 'Present'):
                    end = dt.datetime.now()
                elif(eachObject['end'] == ''):
                    continue
                else:
                    try:
                        end = parse(eachObject['end'])
                    except ValueError:
                        continue
                duration = (end.year - start.year)*12 + end.month - start.month
                myDict[count].append(eachObject['job'].lower())
                durations[eachObject['job'].lower()] = durations.get(eachObject['job'].lower(),0) + duration
                uniqueJobs[eachObject['job'].lower()] += 1
                objectNumber += 1
        count += 1

parseFile = open('../output/dict.json',"w")
for i,value in zip(range(0,len(myDict)),myDict.values()):
    parseFile.write(json.dumps(value) + "\n")

parseFile.close()
