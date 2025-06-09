from fastapi import FastAPI, HTTPException, Query
from scraper import scrape_instagram_reels
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/scrape")
async def scrape(username: str = Query(..., min_length=1)):
    try:
        print('Hello ayushi in try')
        reels_data = await scrape_instagram_reels(username)
        if not reels_data:
            raise HTTPException(status_code=404, detail="No reels found or user is private/non-existent.")
        return JSONResponse(content={"username": username, "reels": reels_data})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
