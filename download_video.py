import argparse
import yt_dlp

def download_video(url: str, output_path: str = "."):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # força a preferência por vídeo MP4 e áudio M4A
        'merge_output_format': 'mp4',  # Se precisar juntar, será em MP4
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # converte para mp4 se o download não for mp4 direto
            }
        ],
        'outtmpl': f"{output_path}/%(title)s.%(ext)s",  # nome do arquivo de saída
        'ffmpeg_location': 'ffmpeg',  # garante que use o ffmpeg (assume que está no PATH)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a video via yt-dlp as a single MP4 file"
    )
    parser.add_argument("url", help="URL of the video to download")
    parser.add_argument(
        "--path", "-p",
        default=".",
        help="Directory where the video will be saved (default: current directory)"
    )
    args = parser.parse_args()
    download_video(args.url, args.path)
