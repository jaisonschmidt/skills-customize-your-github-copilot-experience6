from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float

# Banco de dados em memória
itens: Dict[int, Item] = {}

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API FastAPI!"}

@app.post("/items/")
def create_item(item: Item):
    item_id = len(itens) + 1
    itens[item_id] = item
    return {"id": item_id, **item.dict()}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in itens:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"id": item_id, **itens[item_id].dict()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in itens:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    itens[item_id] = item
    return {"id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in itens:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del itens[item_id]
    return {"mensagem": "Item removido com sucesso"}
