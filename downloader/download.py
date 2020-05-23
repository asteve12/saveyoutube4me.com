from pytube import YouTube
import os.path
url=input("Enter the Youtube Url:")
homedir = os.path.expanduser("~")
dirs=homedir +'/Downloads'
download = YouTube(url).streams.first().download(dirs)
if(download):
    print("Download Completed Check Your Downloads Directory")