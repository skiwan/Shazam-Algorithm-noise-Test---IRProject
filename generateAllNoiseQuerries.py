import subprocess
import os
import random
querryPath = "querries/"
querryLen = [5,10,15]
noisesamples = ['noise','noisyenv','speech']
dbValues = [-15,-10,-5,0,5,10,15]
for ql in querryLen:
    for ns in noisesamples:
        goalPath = querryPath+ns
    print("Strated with QL: " + str(ql))

    # Create subfolder if not existend
    fullgoalpath = goalPath + str(ql) + '/'

    # Generate noise querry folder
    if not os.path.exists(fullgoalpath):
        os.makedirs(fullgoalpath)

    # get all files from querry path
    files = os.listdir(querryPath+str(ql)+'/')

    # for every file in temp
    # add the noise file so that the n/s ratio is equal to db
    for db in dbValues:
        print("Starting noise for",db,ns,ql)
        sf = str(db)
        sf = sf.replace('.','_')
        dbpath = fullgoalpath+sf+'/'
        # Create querry folder for noise
        if not os.path.exists(dbpath):
            os.makedirs(dbpath)
        # for file
        for f in files:            
            # prepare output name
            outf = dbpath + f

            # get mean db of file

            # generate querry with target db
            # add normalized noise file

            """
            """
            
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
