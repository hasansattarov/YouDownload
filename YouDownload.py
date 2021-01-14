import pytube

#Add the URL of the video you wish to download in the text file named "videos"
#Separate each URL line by line
#Once you have added all the videos you wish to download, run the program
#Create a folder named "Videos" without the quotes and make sure it is in the same directory as the two files YouDownload.py and videos.txt
#The files you wish to download will appear inside the folder named "Videos"


def get_all_videos(file):
    vidInfo = open (file, "r")
    vidList = []
    videos = vidInfo.readlines()
    for video in videos:
        video = video.strip()
        vidList.append(video)
    return vidList


fileName = "videos.txt"
vidList = get_all_videos(fileName)
numVideos = len(vidList)

for j, i in enumerate(vidList):
    video = pytube.YouTube(i)
    stream = video.streams.get_highest_resolution()
    print("Downloading video " + str(j+1) + " of " + str(numVideos))

    try:
        stream.download("Videos/")
        print(f"Finished downloading video {j+1}")
    except:
        print("Error downloading")

print("You downloaded all the videos in your queue")


