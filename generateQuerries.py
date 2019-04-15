import subprocess
import os
import random
files = os.listdir("temp/")
fileLengths = []
querryLen = int(input("How long (in seconds) shall the result querry be?"))

# Create subfolder if not existend
if not os.path.exists('querries/'+str(querryLen)):
    os.makedirs('querries/'+str(querryLen))

# for every file in temp
for f in files:
    # prepare output name
    outf = 'querries/'+str(querryLen)+'query_'+f

    # get duration inseconds of current song
    command = ['ffprobe' ,'-v' ,'quiet' ,'-print_format' ,'compact=print_section=0:nokey=1:escape=csv' ,'-show_entries' ,'format=duration', 'temp/'+f]
    ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out =(ffmpeg_P.communicate()[0])
    out = out.replace("\r\n","")
    print(out)
    duration = int(float(out))

    # get random start time for querry
    start = random.randint(5,duration-10)
    end = start + querryLen
    
    command = ['ffmpeg','-i','temp/'+f, '-ss', str(start), '-t', str(end), outf]
    ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output = ffmpeg_P.communicate()

