# Instagram Reels Scraper API
A fast, stealthy REST API built with FastAPI and Playwright (or undetected-chromedriver), which scrapes public Instagram Reels for a given username and returns structured JSON data.

🚀 Features
⚡ Fast scraping of 20–30 Instagram Reels in under 10 seconds

🔒 Stealthy scraping using headless Chromium or undetected-chromedriver

JSON output with:
Unique Reel ID

Reel URL
Video URL (.mp4)
Thumbnail URL
Caption text
Posted date (UTC)
Views, likes, comments (if accessible)


Robust error handling:

404 for private or non-existent accounts
500 for internal errors or CAPTCHA/login walls


🛠️ Tech Stack
FastAPI
Playwright or undetected-chromedriver
Python 3.7+



Endpoint:
GET http://localhost:8000/scrape?username=cristiano

