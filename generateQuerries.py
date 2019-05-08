import subprocess
import os
import random
"""
Generate the ground Queries
"""


files = os.listdir("temp/")
print('Toalfiles: ' + str(len(files)))
fileLengths = []
querryLen = [5,10,15]
# choose 50% of the orignal songs randomly
files = random.sample(files,len(files)//2)
print('Selected Files: ' + str(len(files)))

for ql in querryLen:
    print("Strated with QL: " + str(ql))
    # Create subfolder if not existend
    if not os.path.exists('querries/'+str(ql)):
        os.makedirs('querries/'+str(ql))
    c = 0
    # for every file in temp
    for f in files:
        # prepare output name
        outf = 'querries/'+str(ql)+'/'+str(ql)+'query_'+f

        # get duration inseconds of current song
        command = ['ffprobe' ,'-v' ,'quiet' ,'-print_format' ,'compact=print_section=0:nokey=1:escape=csv' ,'-show_entries' ,'format=duration', 'temp/'+f]
        ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out =(ffmpeg_P.communicate()[0])
        out = out.replace("\r\n","")
        duration = int(float(out))
        # if the song is at least 50 seconds crop a peace out of the middle
        if(duration > 50):
            c+=1
            # get random start time for querry
            start = random.randint(20,(duration-duration//3))
            
            command = ['ffmpeg','-i','temp/'+f, '-ss', str(start), '-t', str(ql), outf]
            
            ffmpeg_P = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            output = ffmpeg_P.communicate()
        print(c)

