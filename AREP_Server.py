#!/usr/bin/env python
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes


import os

# Establecer la clave de API en el entorno
os.environ["OPENAI_API_KEY"] = "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"


# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatOpenAI()

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser

# 5. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 6. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)