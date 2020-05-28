from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=5jKZ9KGtee0")
print("Title: " + str(yt.title))
print(str(yt.length) + " seconds long")
