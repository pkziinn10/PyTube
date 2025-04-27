import yt_dlp

class VideoDownloader:
    def __init__(self, output_path: str = "."):
        self.output_path = output_path
        self.ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }
            ],
            'outtmpl': f"{self.output_path}/%(title)s.%(ext)s",
            'ffmpeg_location': 'ffmpeg',
        }

    def download(self, url: str):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])
