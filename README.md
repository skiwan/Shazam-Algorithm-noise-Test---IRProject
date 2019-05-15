# Shazam-Algorithm-noise-Test---IRProject
Testing the shazam algorithm on its noise resistence.

First clone the repo

Then make sure Ffmpeg is installed on your computer

https://ffmpeg.org/

# How to use this repo

## Add Music to database

First we need to add music to our database to have something to test on
Create a folder called "temp" on the same level as audfprint.
Next put the music files you want to index into that folder.

Now navigate with a shell into the audfprint folder (cd audfprint/)

execute the following command with python2 in your shell

```shell
python audfprint.py add -dbase fulldbase.pklz ../temp/Ü
```

this will add your music to the database completly indexed
(Note the songs you index should not exceed a playtime of 6 minutes per song)

## Create search queries

now we need to create our querie files that will be used to seearch against the database. In this example queries with the length of 5sec, 10 sec and 15sec will be created.

go back into the root folder and execute the "generateQuerries.py" file with python 2

This will create our base queries.

Now lets match those base queries. For that execute the following commands in you shell
```shell
sh matchq5.sh > q5matches.txt
sh matchq10.sh > q10.matches.txt
sh matchq15.sh > q15.matches.txt
```

Now we want to calculate the ground truth accuracy of those base queries.

Execute the python file calculateGroundtruth.py
This will print the accuary for all query types

## Generate Noise queries

Now we need to generate all the noise queries of different kinds to test our algorithm. For that we need to execute the following python files.

generateAllNoiseQuerries.py
-> This will generate queries with added white noise, speech noise and ambience noise

generateCompressedQuerries.py
-> This will generate queries with compressed bitrate

generatePitchShiftQuerries.py
-> This will generate queries with shifted pitch

generateSpedUpQuerries.py
-> This will generate queries which have different speeds

## Generate matching files for queries.

Now we need to generate the matches for the different queires. For that we need to execute a multitude of different shell scripts.

all of them follow the same naming
matchq*noisetype**querylength*_*noiseparameter*

execute them in the following manner

sh *shfile* > *noisetype*q_*noiseparameter*.txt

So for example

sh matchqcompression5_5.sh > compression15_5.txt

after you executed all the batch files and thus created all the matching files (txt files) you can finally compute the accuracy

## Calculate accuracy

execute calculateAccAll.py via python2 and pipe the output into a txt file. For example

python calculateAccAll.py > results.txt

Now you are done.
You can find all the accuracy values in the result.txt files to find out how well the audfprint (shazam) algorithm works with different noise types.










Execute the file

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
