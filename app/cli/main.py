import argparse
from app.services.download_video import VideoDownloader

def main():
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

    downloader = VideoDownloader(output_path=args.path)
    downloader.download(args.url)

if __name__ == "__main__":
    main()
