########################################
#version 1.0
#Date: 04/11/2016
#Author: Kantharaju C N
#######################################
from parseJson import myDict
from collections import Counter
from _collections import defaultdict
import json
import decimal

def findHierarchy(level):
    tempCounter_1 = Counter();
    tempCounter_2 = Counter();
    tempHierarchy = defaultdict(list)
    probability = {}
    for values in myDict.values():
        lenngth = len(values) - 1
        if lenngth <= level:
            continue
        else:
            tempCounter_1[values[level]] += 1
    
    for key in tempCounter_1.keys():
        for value in myDict.values():
            length = len(value) - 1
            if length <= level:
                continue
            else:
                if key == value[level]:
                    tempHierarchy[key].append(value[level+1])
                    mykey = key +"->"+ value[level+1]
                    tempCounter_2[mykey] += 1
    '''Calculating Probability'''
    probfile = open('../output/probability.json',"w")
    for key,vallist in tempHierarchy.items():
        for val in vallist:
            keyval = key+"->"+val
            if key in tempCounter_1.keys() and keyval in tempCounter_2.keys():
                probability[keyval] = round(decimal.Decimal(tempCounter_2[keyval])/decimal.Decimal(tempCounter_1[key]),2)
            
    for key,val in probability.items():
        pair = '{'+key+':'+str(val)+'}'
        probfile.write(json.dumps(pair.encode('utf-8')) + "\n")  
    probfile.close()
 


            
        
    