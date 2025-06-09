from playwright.async_api import async_playwright
import re
import json
from datetime import datetime

INSTAGRAM_URL = "https://www.instagram.com"

async def scrape_instagram_reels(username: str):
    url = f"{INSTAGRAM_URL}/{username}/reels/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto(url, timeout=10000)
            await page.wait_for_selector("article", timeout=8000)

            # Scroll to load more reels
            for _ in range(3):  # Try to load at least 20–30 reels
                await page.mouse.wheel(0, 5000)
                await page.wait_for_timeout(1000)

            # Extract JSON data embedded in the page
            html = await page.content()
            shared_data_match = re.search(r"window\._sharedData = (.*?);</script>", html)
            if not shared_data_match:
                raise Exception("Failed to extract shared data.")

            data = json.loads(shared_data_match.group(1))
            reels = []

            edges = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]

            for edge in edges:
                node = edge["node"]
                if not node.get("is_video"):
                    continue

                reel = {
                    "id": node["id"],
                    "reel_url": f"{INSTAGRAM_URL}/reel/{node['shortcode']}/",
                    "video_url": node.get("video_url", None),
                    "thumbnail_url": node.get("display_url"),
                    "caption": node["edge_media_to_caption"]["edges"][0]["node"]["text"] if node["edge_media_to_caption"]["edges"] else "",
                    "posted_at": datetime.utcfromtimestamp(node["taken_at_timestamp"]).isoformat(),
                    "views": node.get("video_view_count", None),
                    "likes": node["edge_liked_by"]["count"],
                    "comments": node["edge_media_to_comment"]["count"]
                }

                reels.append(reel)

            await browser.close()
            return reels

        except Exception as e:
            await browser.close()
            if "not found" in str(e).lower():
                raise Exception("User not found or private.")
            raise e
