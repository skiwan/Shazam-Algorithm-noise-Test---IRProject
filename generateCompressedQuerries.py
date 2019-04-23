import subprocess
import os
import random
querryPath = "querries/"
querryLen = [5,10,15]
goalPath = querryPath+"compression"
compressionrate = [0.9,0.7,0.5,0.3]
for ql in querryLen:
    print("Strated with QL: " + str(ql))
    # Create subfolder if not existend
    fullgoalpath = goalPath + str(ql) + '/'
    if not os.path.exists(fullgoalpath):
        os.makedirs(fullgoalpath)
    files = os.listdir(querryPath+str(ql)+'/')
    # for every file in temp
    for c in compressionrate:
        print("Starting compression for",c)
        sf = str(c)
        sf = sf.replace('.','_')
        compresspath = fullgoalpath+sf+'/'
        if not os.path.exists(compresspath):
            os.makedirs(compresspath)
        for f in files:            
            # prepare output name
            outf = compresspath + f
            # get bitrate of file
            command = ['ffprobe' ,'-v','error','-show_entries','format=bit_rate','-of','default=noprint_wrappers=1' ,querryPath+str(ql)+'/'+f]
            ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out =(ffmpeg_P.communicate()[0])
            out = out.replace('bit_rate=','')
            bitrate=int(out)
            print(bitrate)
            newbitrate = int(bitrate * c)
            print(newbitrate)
            # get duration inseconds of current song
            command = ['ffmpeg' ,'-i' ,querryPath+str(ql)+'/'+f ,'-ab' ,str(newbitrate) ,outf]
            print(command)
            ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out =(ffmpeg_P.communicate()[0])
