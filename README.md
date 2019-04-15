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