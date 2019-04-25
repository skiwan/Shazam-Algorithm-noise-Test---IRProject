import subprocess
import os
import random
import re
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
                outf = dbpath + 'prep_'+ f
                outff = dbpath + f
        
                # get mean db of file
                command = ['ffmpeg', '-i', querryPath+str(ql)+'/'+f, '-af', 'volumedetect','-f','null','NUL']
                ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out =(ffmpeg_P.communicate())
                meanA = re.search('(mean_volume: -)[\d,\.]+ dB',out[1])
                meanA = meanA.group(0)
                meanA = meanA.replace('mean_volume: ','')
                meanA = meanA.replace(' dB','')
                meanA = float(meanA)
                goaldB = -28.0
                difference = goaldB -  meanA -db
                # generate querry with target db
                command = ['ffmpeg','-i',querryPath+str(ql)+'/'+f, '-filter:a', 'volume='+str(difference)+'dB:precision=double', outf]
                ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out =(ffmpeg_P.communicate()[0])
                # add normalized noise file
                filePathOfNormalized = 'noiseQuerries/noiseN/'+ns+str(ql)+'N.wav'
                command = ['ffmpeg', '-i', outf, '-i' ,filePathOfNormalized, '-filter_complex', 'amerge', '-ac', '2', '-c:a' , 'libmp3lame', '-q:a','4', outff]
                ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out =(ffmpeg_P.communicate()[0])
            garbageFiles = os.listdir(dbpath)
            for f in garbageFiles:
                if('prep_' in f):
                    os.remove(dbpath+f)
    
