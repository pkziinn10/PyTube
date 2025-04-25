import argparse
import yt_dlp

def download_video(url: str, output_path: str = "."):
    ydl_opts = {
        'outtmpl': f"{output_path}/%(title)s.%(ext)s",
        'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download video from yt-dlp")
    parser.add_argument("url", help="Video URL")
    parser.add_argument(
        "--path", "-p",
        default=".",
        help="Directory where the video will be saved"
    )
    args = parser.parse_args()
    download_video(args.url, args.path)
