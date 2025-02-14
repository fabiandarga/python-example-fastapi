from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_index():
    return { "message": "Hello from Index" }

@app.get('/server/{server_name}')
def get_stats(server_name: str, quick_check: Union[str, None] = None):
    # ping server
    return { "message": f"Server '{server_name}' is active", "q": quick_check}
