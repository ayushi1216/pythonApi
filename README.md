# Instagram Reels Scraper API
A fast, stealthy REST API built with FastAPI and Playwright (or undetected-chromedriver), which scrapes public Instagram Reels for a given username and returns structured JSON data.

🚀 Features
⚡ Fast scraping of 20–30 Instagram Reels in under 10 seconds

🔒 Stealthy scraping using headless Chromium or undetected-chromedriver

📦 JSON output with:

Unique Reel ID

Reel URL
Video URL (.mp4)
Thumbnail URL
Caption text
Posted date (UTC)
Views, likes, comments (if accessible)


🔁 Robust error handling:

404 for private or non-existent accounts
500 for internal errors or CAPTCHA/login walls


🛠️ Tech Stack
FastAPI
Playwright or undetected-chromedriver
Python 3.7+



Endpoint:

GET http://localhost:8000/scrape?username=cristiano
Sample Response:
{
  "username": "cristiano",
  "reels": [
    {
      "id": "123456789",
      "reel_url": "https://www.instagram.com/reel/Cx12345/",
      "video_url": "https://instagram.fxyz1-1.fna.fbcdn.net/....mp4",
      "thumbnail_url": "https://instagram.fxyz1-1.fna.fbcdn.net/....jpg",
      "caption": "Game day ready ⚽",
      "posted_at": "2024-06-01T18:00:00",
      "views": 1234567,
      "likes": 98765,
      "comments": 1234
    }
  ]
}


⚠️ Limitations & Notes

Instagram frequently updates its layout and anti-bot measures. This scraper might need maintenance over time.

This API works only with public accounts and may fail on:
Private profiles
