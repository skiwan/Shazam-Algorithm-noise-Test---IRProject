# -*- coding: cp1252 -*-
# Imports
import subprocess
import os
import random
import audfprint
import re
import os
"""
This file generates the results on accuarcy for the experiments below
The matching txt files have to be created before running this
"""


# Lengths Array 
querryLen = [5,10,15]
# list of the beginnings of all match files
qpath = ['compressionq','noiseq','noisyenvq','pitchq','speechq','speedupq']
files = os.listdir(os.getcwd())
# find the 'real files' that are needed for matching
rf = []
for f in files:
    if ('.txt' in f):
        rf.append(f)
rf.sort() # sorting to make output a bit cleaner
# for all experiments
for p in qpath:
    # for all lengths of queries
    for ql in querryLen:
        print("Calc Acc for: " + p+ str(ql))
        filePart = p + str(ql)
        for ff in rf:
            if(filePart in ff):
                # open correct txt file
                l = 0
                c = 0
                s = ff.replace(filePart+'_','')
                s = s.replace('.txt','')
                print(s)
                with open(ff) as f:
                    # read all lines
                    allLines = f.readlines()
                for line in allLines:
                    # count matching lines and matches
                    if('NOMATCH' in line):
                        l += 1
                        continue
                    if('Matched' in line):
                        l += 1
                        line = line.lower()
                        line = line.replace('ä','')
                        line = line.replace('ö','')
                        line =  line.replace('ü','')
                        line =  line.replace('ß','')
                        line =  line.replace('é','')
                        cline = line.replace('Matched ','')
                        cline = cline.replace('sec','')
                        cline = cline.replace('raw hashes as ','')
                        cline = cline.replace('common hashes at rank ', '')
                        # query question
                        qq = re.search(r"(querries)[\–,\',\w,\/,\s,\d,\[,\],\-,\(,\),\.,\&]+(\.mp3|\.m4a|\.wma|\.wav)(?! at)",cline).group(0)
                        qq = re.sub('(querries\/)[\w,\d]+\/[\w,\d,\-]+\/','',qq)
                        qq = qq.replace(str(ql)+'query_','')
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
                # print out accuracy
                print(ql,c,'/',l,float(c)/l)
        print('\n\n')
    


            
