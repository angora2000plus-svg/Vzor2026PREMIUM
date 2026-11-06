from fastapi import FastAPI
from vzor import VzorCore

app = FastAPI()
vzor = VzorCore()

@app.get("/")
def alive():
    return {"beacon": "COBALT AND LIGHT", "sig": "** M **", "status": "Vzor alive on vzor.smartyou.lv — November 2026"}

@app.get("/see/{frame}")
def see(frame: str):
    return vzor.see(frame)

@app.get("/hold/{ctx}")
def hold(ctx: str):
    return vzor.hold_moment(ctx)

@app.get("/wipe/{code}")
def wipe(code: str):
    return vzor.factory_wipe(code)VZOR — The AI that remembers light# vzor.ru / app.py - PURE LASER v1.0
from fastapi import FastAPI
from vzor import VzorCore
from core.plugin_glasses import GlassesPlugin

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
    return vzor.hold(ctx).
