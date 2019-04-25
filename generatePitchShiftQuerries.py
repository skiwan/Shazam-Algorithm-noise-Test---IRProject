import subprocess
import os
import random
querryPath = "querries/"
querryLen = [5,10,15]
goalPath = querryPath+"pitchAdjust"
pitch = [30000,20000,10000]
for ql in querryLen:
    print("Strated with QL: " + str(ql))
    # Create subfolder if not existend
    fullgoalpath = goalPath + str(ql) + '/'
    if not os.path.exists(fullgoalpath):
        os.makedirs(fullgoalpath)
    files = os.listdir(querryPath+str(ql)+'/')
    # for every file in temp
    for p in pitch:
        print("Starting pitchshift for",p)
        sf = str(p)
        sf = sf.replace('.','_')
        pitchpath = fullgoalpath+sf+'/'
        if not os.path.exists(pitchpath):
            os.makedirs(pitchpath)
        for f in files:
            # prepare output name
            outf = pitchpath + f
            
            # get duration inseconds of current song
            command = ['ffmpeg' ,'-i' ,querryPath+str(ql)+'/'+f ,'-af' ,'aresample='+str(p),outf]
            ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out =(ffmpeg_P.communicate()[0])
