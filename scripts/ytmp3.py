from pytube import YouTube
import os
import urllib.request
  
def convert_youtube_url(url):
    try:
        # url input from user
        yt = YouTube(str(url))

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
        
        # config destination
        destination = os.path.abspath(os.path.join(os.path.dirname(__file__), '../mp3files'))
        
        # download the file
        out_file = video.download(output_path=destination)
     
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")

    except urllib.error.HTTPError as e:
        print("Error: The YouTube video is unavailable or has been removed.")


input_url = input()
convert_youtube_url(input_url)


