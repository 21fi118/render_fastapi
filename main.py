from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加
from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "takoyaki🐙"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}
    
@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>21fi118's HTML</title>
        </head>
        <body>
            <h1>Hello! There is 21fi118's HTML!</h1>
            <h2>I want to go Thailand 🇹🇭</h2>
            <h2>I need money...</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def new_naming(present):
    return {"response": f"サーバです。いつもお世話になっています！ {present}こちらこそありがとう。お返しは花束です💐"}