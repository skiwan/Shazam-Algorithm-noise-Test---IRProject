# -*- coding: cp1252 -*-
# imports
import subprocess
import os
import random
import audfprint
import re
"""
Calculates the basis accuracy on the non modified queries
"""

# query length array
querryLen = [5,10,15]
#querryLen = [5]
# name of the matching file
qpath = 'matches.txt'

# for all lines in matches count matching lines and matches
for ql in querryLen:
    print("CalcGroundtruth for: " + str(ql))
    c = 0
    l = 0
    fileName = 'q' + str(ql) + qpath
    print("Calculate for file: " + fileName)

    with open(fileName) as f:
        allLines = f.readlines()
    for line in allLines:
        if('Matched' in line):
            line = line.lower()
            line = line.replace('ä','')
            line = line.replace('ö','')
            line =  line.replace('ü','')
            line =  line.replace('ß','')
            line =  line.replace('é','')
            l += 1
            cline = line.replace('Matched ','')
            cline = cline.replace('sec','')
            cline = cline.replace('raw hashes as ','')
            cline = cline.replace('common hashes at rank ', '')
            # query question
            qq = re.search(r"(querries)[\–,\',\w,\/,\s,\d,\[,\],\-,\(,\),\.,\&]+(\.mp3|\.m4a|\.wma|\.wav)(?! at)",cline).group(0)
            qq = qq.replace('querries/'+str(ql)+'/'+str(ql)+'query_','')
            # query answer
            qa = re.search(r"(\.\.)[\–,\',\w,\/,\s,\d,\[,\],\-,\(,\),\.,\&]+(\.mp3|\.m4a|\.wma|\.wav)",cline).group(0)
            qa = qa.replace('../temp/','')
            if(qa == qq):
                c += 1
            else:
                print('\nMISMATCH')
                print(cline)
                print(qq)
                print(qa)
    print(ql,c,'/',l,float(c)/l)
            
