import pandas as pd
import ffmpeg
import subprocess

configFile = open("Config.txt")
musicFileNames = pd.read_csv("MusicFileNames.csv")
musicFileNamesLength = len(musicFileNames)
print(musicFileNamesLength)
deltaruneDirectory = configFile.readline()
deltaruneDirectory = deltaruneDirectory[deltaruneDirectory.find('"'):deltaruneDirectory.find('"',deltaruneDirectory.find('"')+1)+1]
ostDirectory = configFile.readline()
ostDirectory = ostDirectory[ostDirectory.find('"'):ostDirectory.find('"',ostDirectory.find('"')+1)+1]
print(deltaruneDirectory)
print(ostDirectory)


#Convert all OST MP3 Files to OGG and store in the temp directory
count = 0
while(count<musicFileNamesLength):
    inputFilePath = ostDirectory[1:len(ostDirectory)-1]+'\\'+musicFileNames["OSTFileName"][count]
    outputFilePath = deltaruneDirectory[1:len(deltaruneDirectory)-1]+'\\'+musicFileNames["GameFileName"][count]
    command = [
        'ffmpeg',
        '-i', inputFilePath,
        '-map', '0:a',
        '-c:a', 'libvorbis',
        '-q:a', '10',
        '-vn',
        '-y',
        outputFilePath
        
    ]
    
    subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)


    count+=1
   