import pandas as pd 
import os
import ffmpeg
import subprocess
import sys

#workingPath = 
os.chdir(sys.path[0])

configFile = open("Config.txt")
musicFileNames = pd.read_csv("MusicFileNames.csv")
musicFileNamesSpecialFiles = pd.read_csv("MusicFileNamesSpecialFiles.csv")
musicFileNamesTrimmedSongs = pd.read_csv("MusicFileNamesTrimmedSongs.csv")
musicFileNamesLength = len(musicFileNames)
print(musicFileNamesLength)
deltaruneDirectory = configFile.readline()
deltaruneDirectory = deltaruneDirectory[deltaruneDirectory.find('"'):deltaruneDirectory.find('"',deltaruneDirectory.find('"')+1)+1]
ostDirectory = configFile.readline()
ostDirectory = ostDirectory[ostDirectory.find('"'):ostDirectory.find('"',ostDirectory.find('"')+1)+1]
print(deltaruneDirectory)
print(ostDirectory)


#Convert all OST MP3 Files to OGG and overwrite the files in the deltarune/mus folder
count = 0
while(count<musicFileNamesLength):
    #Format the Time for both the ost length and InGameLength from the csv into seconds
    ostLength = int(musicFileNames["OSTLength"][count][0:1])*60 + int(musicFileNames["OSTLength"][count][2:3])
    inGameLength = int(musicFileNames["InGameLength"][count][0:1])*60 + int(musicFileNames["InGameLength"][count][2:3])
    #Check if the Output length is equal or below the input length there is only one such case in the game rn but just in case a full function will be written
    if(ostLength==inGameLength):
        inputFilePath = ostDirectory[1:len(ostDirectory)-1]+'\\'+musicFileNames["OSTFileName"][count]
        outputFilePath = deltaruneDirectory[1:len(deltaruneDirectory)-1]+'\\'+musicFileNames["GameFileName"][count]
        command = [
        'ffmpeg',
        '-i', inputFilePath+'.mp3',
        '-map', '0:a',
        '-c:a', 'libvorbis',
        '-q:a', '10',
        '-vn',
        '-y',
        outputFilePath+'.ogg'
        
        ]

        subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    

    #Check if the Output length is below the input length
    elif(ostLength > inGameLength):
        #Format time from sheet

        inputFilePath = ostDirectory[1:len(ostDirectory)-1]+'\\'+musicFileNames["OSTFileName"][count]
        outputFilePath = deltaruneDirectory[1:len(deltaruneDirectory)-1]+'\\'+musicFileNames["GameFileName"][count]
        command = [
        'ffmpeg',
        '-ss', '0',
        '-i', inputFilePath+'.mp3',
        '-t', str(ostLength),
        '-map', '0:a',
        '-c:a', 'libvorbis',
        '-q:a', '10',
        '-vn',
        '-y',
        outputFilePath+'.ogg'
        
        ]

        subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)




    #Since it's neither it's the special exception and however many seconds of silence will be added to the end of the track
    else:

        #PlaceHolder
        i = 0
 


 

  
    print(musicFileNames["OSTFileName"][count]+ " converted and moved")
    count+=1

print("Completed Successfully")
   