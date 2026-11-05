# vzor.ru / app.py - API LASER v1.0
from vzor import VzorCore
from core.plugin_glasses import GlassesPlugin

from fastapi import FastAPI
app = FastAPI()

vzor = VzorCore(glasses=GlassesPlugin())

@app.get("/")
def home():
    return {"beacon": "COBALT AND LIGHT", "sig": "* M *", "status": "Vzor alive on vzor.ru"}

@app.get("/see/{frame}")
def see(frame: str):
    return vzor.see(frame)

@app.get("/hold/{ctx}")
def hold(ctx: str):
    return vzor.hold(ctx)
