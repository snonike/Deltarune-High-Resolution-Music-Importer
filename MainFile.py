import pandas as pd 
import os
import subprocess
import sys
from os.path import dirname as up



def Converter(musicFileNames,deltaruneDirectory,ostDirectory):

      #Format the Time for both the ost length and InGameLength from the csv into seconds
    ostLength = int(musicFileNames["OSTLength"][count][0:1])*60 + int(musicFileNames["OSTLength"][count][2:3])
    inGameLength = int(musicFileNames["InGameLength"][count][0:1])*60 + int(musicFileNames["InGameLength"][count][2:3])
    #Check if the Output length is equal or below the input length there is only one such case in the game rn but just in case a full function will be written
    if(ostLength==inGameLength):
        inputFilePath = ostDirectory[1:len(ostDirectory)-1]+'\\'+musicFileNames["OSTFileName"][count]
        outputFilePath = deltaruneDirectory[1:len(deltaruneDirectory)-1]+"\\mus"+'\\'+musicFileNames["GameFileName"][count]
        command = [
        'ffmpeg',
        '-i', inputFilePath+'.flac',
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
        outputFilePath = deltaruneDirectory[1:len(deltaruneDirectory)-1]+"\\mus"+'\\'+musicFileNames["GameFileName"][count]
        command = [
        'ffmpeg',
        '-ss', '0',
        '-i', inputFilePath+'.flac',
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
        #Format time from sheet

        inputFilePath = ostDirectory[1:len(ostDirectory)-1]+'\\'+musicFileNames["OSTFileName"][count]
        outputFilePath = deltaruneDirectory[1:len(deltaruneDirectory)-1]+"\\mus"+'\\'+musicFileNames["GameFileName"][count]
        command = [
        'ffmpeg',
        '-ss', '0',
        '-i', inputFilePath+'.flac',
        '-t', str(inGameLength),
        '-map', '0:a',
        '-c:a', 'libvorbis',
        '-q:a', '10',
        '-vn',
        '-af', "apad=pad_dur="+str(inGameLength-ostLength),
        '-y',
        outputFilePath+'.ogg'
        
        ]

        subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

      
 


 

  
    print(musicFileNames["OSTFileName"][count]+ " converted and moved")

#Trims a song down from the front using a start point
def TrimmedConverter(musicFileNames,deltaruneDirectory,ostDirectory):

    #Format the Time for both the ost length and InGameLength from the csv into seconds
    startPoint = int(musicFileNames["StartPoint"][count][0:1])*60 + int(musicFileNames["StartPoint"][count][2:3])
    endPoint = int(musicFileNames["EndPoint"][count][0:1])*60 + int(musicFileNames["EndPoint"][count][2:3])

    inputFilePath = ostDirectory[1:len(ostDirectory)-1]+'\\'+musicFileNames["OSTFileName"][count]
    outputFilePath = deltaruneDirectory[1:len(deltaruneDirectory)-1]+'\\mus'+'\\'+musicFileNames["GameFileName"][count]
    command = [
    'ffmpeg',
    '-ss', str(startPoint),
    '-i', inputFilePath+'.flac',
    '-t', str(endPoint),
    '-map', '0:a',
    '-c:a', 'libvorbis',
    '-q:a', '10',
    '-vn',
    '-y',
    outputFilePath+'.ogg'
    
    ]

    subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

      
 


 

  
    print(musicFileNames["OSTFileName"][count]+ " converted and moved")




#workingPath = 

configFile = open("Config.txt")
musicFileNames = pd.read_csv("MusicFileNames.csv")
musicFileNamesSpecialFiles = pd.read_csv("MusicFileNamesSpecialFiles.csv")
musicFileNamesTrimmedSongs = pd.read_csv("MusicFileNamesTrimmedSongs.csv")
musicFileNamesLength = len(musicFileNames)
musicFileNamesSpecialFilesLength = len(musicFileNamesSpecialFiles)
musicFileNamesTrimmedSongsLength = len(musicFileNamesTrimmedSongs)
deltaruneDirectory = configFile.readline()
deltaruneDirectory = deltaruneDirectory[deltaruneDirectory.find('"'):deltaruneDirectory.find('"',deltaruneDirectory.find('"')+1)+1]
ostDirectory = configFile.readline()
ostDirectory = ostDirectory[ostDirectory.find('"'):ostDirectory.find('"',ostDirectory.find('"')+1)+1]
# print(deltaruneDirectory)
# print(ostDirectory)


#Convert all OST FLAC Files to OGG and overwrite the files in the deltarune/mus folder
count = 0
while(count<musicFileNamesLength):
    Converter(musicFileNames,deltaruneDirectory,ostDirectory)

    count+=1

count = 0
while(count<musicFileNamesSpecialFilesLength):
    #Format the Time for both the ost length and InGameLength from the csv into seconds
    Converter(musicFileNamesSpecialFiles,deltaruneDirectory,ostDirectory)
    count+=1

count = 0
while(count<musicFileNamesTrimmedSongsLength):
    TrimmedConverter(musicFileNamesTrimmedSongs,deltaruneDirectory,ostDirectory)
    count+=1


print("Completed Successfully")
input("Press enter to exit....")
   