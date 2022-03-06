from io import BytesIO
import zipfile
import pytube

def generate_zip(files):
    mem_zip = BytesIO()
    with zipfile.ZipFile(mem_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in files:
            zf.writestr(file[0].replace('/','-'), file[1]) # filename and data

    return mem_zip.getvalue()

def getVideoAsBufferMP3(url):
    video = pytube.YouTube(url)
    buffer = BytesIO()
    video.streams.get_audio_only().stream_to_buffer(buffer)
    video_data = buffer.getvalue()
    buffer.close()
    return (f"{video.title}.mp3", video_data)

def getVideoAsBufferMP4(url):
    video = pytube.YouTube(url)
    buffer = BytesIO()
    try:
        video.streams.get_by_resolution("720p").stream_to_buffer(buffer)
    except:
        video.streams.first().stream_to_buffer(buffer)
    video_data = buffer.getvalue()
    buffer.close()
    return (f"{video.title}.mp4", video_data)