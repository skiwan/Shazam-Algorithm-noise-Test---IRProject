import subprocess
import os
import random
querryPath = "querries/"
querryLen = [5,10,15]
goalPath = querryPath+"speedUp"
speedUp = [0.5,0.75,1.25,1.5]
for ql in querryLen:
    print("Strated with QL: " + str(ql))
    # Create subfolder if not existend
    fullgoalpath = goalPath + str(ql) + '/'
    if not os.path.exists(fullgoalpath):
        os.makedirs(fullgoalpath)
    files = os.listdir(querryPath+str(ql)+'/')
    # for every file in temp
    for s in speedUp:
        print("Starting Speeup for",s)
        sf = str(s)
        sf = sf.replace('.','_')
        speedpath = fullgoalpath+sf+'/'
        if not os.path.exists(speedpath):
            os.makedirs(speedpath)
        for f in files:
            # prepare output name
            outf = speedpath + f
            
            # get duration inseconds of current song
            command = ['ffmpeg' ,'-i' ,querryPath+str(ql)+'/'+f ,'-filter:v' ,'setpts='+str(s)+'*PTS' ,outf]
            ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out =(ffmpeg_P.communicate()[0])
