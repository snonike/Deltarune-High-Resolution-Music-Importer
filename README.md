# Deltarune HiRes Music Importer
Converts a downloaded deltarune chapter 1-4 ost into game ready files then replaces the existing audio files in deltarune with them.

First download and install ffmpeg 
[https://github.com/icedterminal/ffmpeg-installer](https://github.com/icedterminal/ffmpeg-installer/releases/download/7.0.0.20240429/FFmpeg_Full.msi)


If you have downloaded deltarune into the default location on your C: drive as well as the soundtrack; there is no need to change the config you can just run the .exe file immediately.

If not, type your DELTARUNE directory into the config.txt file. It can be found by going to steam, right clicking on the icon in library and browsing local files the files on the filesystem.


![Steam Local Files](/Images/steamlocalfiles.png)


The file path can be found by clicking on the top bar like so

![filepath](/Images/filepath.png)


Now type in the directory of the OST Soundtrack that you have downloaded using the same method.

![Config Screenshot](/Images/config.png)

After those steps have been taken all you have to do is run the .exe file and it will take care of the rest.

## EXTRA
If you want to convert the mp3 files instead for whatever reason, just change the filetype in the config from .flac to .mp3 but first, make sure all of the soundtrack is in the same
directory before running the .exe.

If there is any failures, it means that the file is not present or you did not input the correct directories; so just check the directories provided in the default config they should
both end in DELTARUNE unless you moved the files somewhere else.
