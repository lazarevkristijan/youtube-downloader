from pytube import YouTube
import os

urls = ["https://www.youtube.com/watch?v=Z8FarCnm1mE"]

save_path = 'C:\\Users\\lazar\\Desktop\\Songs'

for url in urls:
    yt = YouTube(url)

    stream = yt.streams.filter(only_audio=True).first()

    downloaded_file = stream.download(output_path=save_path)

    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)

    print(f"Downloaded MP3: {new_file}")