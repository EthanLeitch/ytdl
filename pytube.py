from pytube import YouTube
import os

video = YouTube("https://www.youtube.com/watch?v=wDgQdr8ZkTw").streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
ytvideo.download("Downloads/")
