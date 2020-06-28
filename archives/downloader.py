from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=5jKZ9KGtee0")
print("Title: " + str(yt.title))

length = yt.length
if length < 60:
    print(str(length%60) + " seconds")
else:
    if length%60 < 10:
        print(str(length//60) + ":" + "0" + str(length%60))
    else:
        print(str(length//60) + ":" + str(length%60))
