# 客服聊天机器人

这是一个基于FastAPI和大语言模型的客服聊天机器人，能够回答用户的问题。

## 功能

- 基于阿里云百炼-通义千问大模型
- 实时聊天界面
- 简洁美观的前端设计

## 本地运行

1. 安装依赖
   ```
   pip install -r requirements.txt
   ```

2. 设置环境变量
   ```
   # Windows PowerShell
   $env:DASHSCOPE_API_KEY="sk-你的阿里云百炼APIKey"
   
   # macOS / Linux
   export DASHSCOPE_API_KEY="sk-你的阿里云百炼APIKey"
   ```

3. 启动服务器
   ```
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

4. 访问聊天界面
   ```
   http://localhost:8000/static/index.html
   ```

## 部署到Railway

1. 登录Railway账号
2. 创建新的项目
3. 连接GitHub仓库
4. 配置环境变量
   - DASHSCOPE_API_KEY: 你的阿里云百炼API Key
5. 部署项目
6. 通过Railway提供的公网地址访问

## 技术栈

- 后端: FastAPI, Uvicorn
- 前端: HTML, CSS, JavaScript
- 大模型: 阿里云百炼-通义千问