from fastapi import FastAPI,Path,Query

app = FastAPI()

@app.get("/")
def read():
    return {"msg" : "我正在学习Fastapi..." }

@app.get("/user/{id}")
async def get_book(id: int):
    return {"id": id, "title": f"这是第{id}本书"}

@app.get("/news/id/{news_id}")
async def get_news_id(news_id: int = Path(gt=0, lt=101)):
    return{"id":f"新闻分类id是{news_id}"}

@app.get("/news/name/{news_name}")
async def get_news_name(news_name: str = Path(min_length=0, max_length=10)):
    return{"newsname": f"新闻分类名称是{news_name}"}

@app.get("/book")
#需求:图书分类，默认值为"Python开发"，长度限制5~255

async def read_book(
    category: str = Query(
        "python开发",
        min_length=5,
        max_length=255,
        description="图书分类名称"
    ),
    #需求:价格，限制大小范围50~100
    price: int = Query(
        ge=50,
        le=100,
        description="图书价格范围"
    )
):
    return{
        "category" : category,
        "price" : price,
        "massage" : "查询成功"
    }