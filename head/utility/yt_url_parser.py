import re
from urllib.parse import urlparse, parse_qs

class yt_parser():
    def __init__(self,url):
        self.url = url

    def get_youtube_id(self):
        """
        Extracts the YouTube video ID from a URL.
        Handles regular, shortened, and embed URLs.
        """
        # Try URL parsing first (to catch query string & embed links)
        parsed = urlparse(self.url)

        # Example: https://www.youtube.com/watch?v=b-K4oDRk04M
        if parsed.hostname in {'www.youtube.com', 'youtube.com'}:
            qs = parse_qs(parsed.query)
            if 'v' in qs:
                return qs['v'][0]

            # Also handle /embed/VIDEOID
            path_parts = parsed.path.split('/')
            if 'embed' in path_parts:
                return path_parts[-1]

        # Example: https://youtu.be/b-K4oDRk04M
        if parsed.hostname in {'youtu.be'}:
            return parsed.path.lstrip('/')

        # Fallback to regex to capture different formats
        regex = (
            r'(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|v/|shorts/))'
            r'([^?&/"\']{11})'
        )
        match = re.search(regex, self.url)
        if match:
            return match.group(1)

        return None

if __name__ == "__main__":
    test_urls = [
        "https://www.youtube.com/watch?v=b-K4oDRk04M",
        "https://youtu.be/b-K4oDRk04M",
        "https://www.youtube.com/embed/b-K4oDRk04M",
        "https://youtube.com/shorts/b-K4oDRk04M",
        "https://www.youtube.com/watch?v=mdWe9HbA-P0",
        "invalid_url",
        "https://www.youtube.com/shorts/9JcC8re07a4"
    ]
    for url in test_urls:
        vid = yt_parser(url).get_youtube_id()
        print(f"URL: {url}\nExtracted video_id: {vid}\n")
        print(datatype(vid))
