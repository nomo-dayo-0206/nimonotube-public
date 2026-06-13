import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse

app = FastAPI()
TIMEOUT_CONFIG = httpx.Timeout(10.0, read=30.0)


@app.get("/")
async def read_index():
    return FileResponse("index.html")


@app.get("/api/search")
async def proxy_search(q: str = Query(...)):
    url = f"https://nimonotube.sitaci.com/api/search?q={q}"
    async with httpx.AsyncClient(timeout=TIMEOUT_CONFIG) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code)
        except httpx.RequestError:
            raise HTTPException(status_code=503)


@app.get("/api/stream/{video_id}")
async def proxy_stream(video_id: str, quality: str = Query("360p")):
    url = f"https://nimonotube.sitaci.com/api/stream/{video_id}?quality={quality}"
    async with httpx.AsyncClient(timeout=TIMEOUT_CONFIG) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code)
        except httpx.RequestError:
            raise HTTPException(status_code=503)
