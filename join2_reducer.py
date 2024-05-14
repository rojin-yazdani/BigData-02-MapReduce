#!/usr/bin/env python3
import sys

ABC_dict={}
kvs=[]
 
for line in sys.stdin:
    line = line.strip()
    key_value = line.split('\t')
    kvs.append(key_value)
    
    if key_value[0]=="ABC":
        if key_value[1] not in ABC_dict:
            ABC_dict.update({key_value[1]:0})
 
for key_value in kvs:
    if key_value[0] in ABC_dict:
        ABC_dict[key_value[0]]+=int(key_value[1])

for key, value in ABC_dict.items() :
    print( '%s %s' % (key, value))  
