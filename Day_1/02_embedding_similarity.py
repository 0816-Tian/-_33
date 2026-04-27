import os
import numpy as np
from openai import OpenAI


QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_EMBEDDING_MODEL = "text-embedding-v4"


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)
    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )


api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise RuntimeError("没有读取到环境变量 DASHSCOPE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url=QWEN_BASE_URL,
)

# 要嵌入的文本
texts = [
    "我喜欢自然语言处理，尤其是大语言模型。",
    "大模型可以完成文本生成、摘要和问答任务。",
    "今天学校食堂的红烧肉很好吃。",
    "语义向量可以用来计算两个句子的相似度。",
]

# 获取每个文本的向量
embeddings = []
for text in texts:
    response = client.embeddings.create(
        model=QWEN_EMBEDDING_MODEL,
        input=text
    )
    embeddings.append(response.data[0].embedding)

# 计算两两之间的相似度
print("两两之间的相似度：")
for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        similarity = cosine_similarity(embeddings[i], embeddings[j])
        print(f"{texts[i]} 与 {texts[j]} 的相似度: {similarity:.4f}")

# 查找与"语义向量有哪些作用"最相似的句子
query = "语义向量有哪些作用"
query_response = client.embeddings.create(
    model=QWEN_EMBEDDING_MODEL,
    input=query
)
query_embedding = query_response.data[0].embedding

print(f"\n与\"{query}\"最相似的句子：")
similarities = []
for i, text in enumerate(texts):
    similarity = cosine_similarity(query_embedding, embeddings[i])
    similarities.append((text, similarity))
    print(f"{text}: {similarity:.4f}")

# 找出最相似的句子
most_similar = max(similarities, key=lambda x: x[1])
print(f"\n最相似的句子是：{most_similar[0]}，相似度: {most_similar[1]:.4f}")