# Shazam-Algorithm-noise-Test---IRProject
Testing the shazam algorithm on its noise resistence.

First clone the repo

Then make sure Ffmpeg is installed on your computer

https://ffmpeg.org/


Now short how tos for different tasks

## add music to the database
create a folder called temp on the same level as audfprint
put your music files into that folder (temp is in git ignore so it wont be tracked)
navigate with your shell into the audfprint folder

execute the following command with python2

```python
python audfprint.py add -dbase fulldbase.pklz ../temp/*
```

this will add your music to the database completly indexex
(Note the songs you index should not ecxeed a playtime of 6 minutes per song)


## create an x second snippet from an audio file with ffmpeg
in your command shell execute
ffmpeg -i "name of songfile" -ss "startsecond" -t "endsecond" "outputfilename"
for example
ffmpeg -i temp/Up_All_Night.mp3 -ss 100 -t 115 querries/Up_All_Night_query15.mp3

## turn all your songs in temp into querries of length x
start the python file generateQuerries
give a number of seconds of querry length (e.g. 5 ; 10 ; 15)
-> For now I have created my querries with the lenght of 15 seconds

## **NOTE** Add all generated querries to the git so we have them, but dont save the temp folder to git


# Roadmap
Roadmap:

- Read the Article and get a basic understanding of the algorithm used (we dont need to implement this ourself but they will ask questions during th presentation) **done**
- Get the Code of https://github.com/dpwe/audfprint working locally on your own computer (note you need to install ffmpeg first on your pc, if you have problems with that contact me, ive been using it on my windows for a while now)
-Gather data and out it into a goole drive (max of 500 songs from our own librarys in mp3 format) **done**
- use 50% of recordings to create snippes of them fro querries and create baseline acc of the algorithm (we could discuss oin the 50 % and use less if you guys want but thats what ming and me came up with) **done**
- Condcut the following noise test
	+ add white noise
	+ add speech sample
	+ add noisi environment sample
	+ pitch shifting
	+ fasten querry
	+ slow querry
	+ compress querry

all those experiments that add noise need to be tested on singla/noise ratio form -15db to +15db

- Write the Report (max 10 pages) till 15th of may (Deadline is 17th)
- Create a Poster for the presentation (8-12 DinA4 pages) till 15th of may (presentation on 15th)
- Create Demo for Presentation
