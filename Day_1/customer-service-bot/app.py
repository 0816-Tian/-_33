import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse
from openai import OpenAI
from rag_system import get_rag_system

app = FastAPI()

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 配置大模型API
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_CHAT_MODEL = "deepseek-v4-flash"

api_key = os.getenv("DEEPSEEK_API_KEY", "sk-71937bb4666244f1ba9bc34cea213374")
# 注意：在实际使用时，请将上面的默认值替换为真实的API Key

client = OpenAI(
    api_key=api_key,
    base_url=DEEPSEEK_BASE_URL,
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    
    try:
        # 使用RAG系统生成回答
        rag_system = get_rag_system()
        answer = rag_system.generate_answer(message)
        return JSONResponse({"answer": answer})
    except Exception as e:
        # 捕获所有异常，确保返回有效的JSON响应
        return JSONResponse({"answer": f"抱歉，调用RAG系统时出现错误：{str(e)}"})

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")