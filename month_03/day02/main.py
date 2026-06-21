from fastapi import FastAPI

app = FastAPI()

# 模拟前端发起的搜索请求，例如：/api/v1/search?keyword=fastapi&limit=5
@app.get("/api/v1/search")
async def search_items(keyword: str, limit: int = 10):
    return {
        "status": "success",
        "search_keyword": keyword,
        "return_count": limit
    }