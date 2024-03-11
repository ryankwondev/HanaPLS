from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from jose import jwt
from pydantic import BaseModel

from app.config import settings
from app.database import mongo
from app.login import get_personal_code

app = FastAPI(title="HanaPLS API")
templates = Jinja2Templates(directory="app/pages")


@app.get("/")
def index():
    with open("app/pages/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


class IntranetLoginData(BaseModel):
    login_id: str
    login_pw: str


@app.post("/intranet_login")
def intranet_login(data: IntranetLoginData, response: Response):
    code = get_personal_code(data.login_id, data.login_pw)
    if code == "DOCTY" or " " in code:
        response.status_code = 404
        return {"message": "로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요."}
    else:
        return {"code": jwt.encode({"code": int(code)}, settings.SECRET_KEY, algorithm="HS256")}


# @app.get("/inquiry")
# def inquiry(code: int):
#     with open("app/pages/inquiry.html", "r", encoding="utf-8") as f:
#         return HTMLResponse(f.read())


@app.get("/inquiry")
async def inquiry_page(token: str, request: Request):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"error": "토큰이 만료되었습니다."}
    except jwt.JWTError:
        return {"error": "토큰이 유효하지 않습니다."}

    return [i for i in mongo["20240312"].find({"code": int(payload["code"])}, {"_id": 0})]
