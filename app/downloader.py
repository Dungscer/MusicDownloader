from yt_dlp import YoutubeDL

# base package imports
import os
import re
import subprocess
from abc import ABC, abstractmethod
from typing import Optional

base_output = "./download"
base_resoulution = "1080p"

class IDownloader(ABC):
    @abstractmethod
    def download(self, url:str,output:Optional[str] = base_output):
        pass

class YoutubeDownloader(IDownloader):
    def __init__(self):
        self.resolution = base_resoulution

    def download(self,url:str,output:Optional[str] = base_output):
        os.makedirs(output, exist_ok=True)
        print(f"- The url is {url}")
        settings = {
            'format': 'bestaudio/best',
            'outtmpl':  os.path.join(base_output, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(settings) as ydl:
            print(f"🎵 Download started")
            ydl.download([url])
            print("✅ Downloaded")
        
        

def GetDownloader(url:str) -> IDownloader:
    print("- Get downloader")
    if "http" in url or "https" in url:
        # the added item is url
        print("- Test url with regex")
       
        if re.search(".{7,8}www.youtube.{1,}", url) or re.search(".{8}youtu.be.{1,}", url):
            print("- Give back youtube downloader")
            return YoutubeDownloader()

        elif re.search(".{8}music.youtube.{1,}", url):
            return

        elif re.search(".{8}soundcloud.{1,}", url):
            return

        raise Exception("Link is not downloadable with this package")
    print("- Added string is not url")
    # the added item is the name of the song


    return

def download(url:str, output:str=base_output):
    try:
        downloader = GetDownloader(url)
        downloader.download(url,output)
        pass
    except Exception as e:
        print("-----------------------")
        print(f"Error during the {url}")
        print(e) 



download("https://youtu.be/xjLDkbq1U8A?si=rYdJMpMdqUEGdJkc")