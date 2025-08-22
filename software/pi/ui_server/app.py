# FastAPI UI/API server (skeleton)
# Requirements (install):
#   fastapi uvicorn jinja2 pydantic
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

def create_app():
    app = FastAPI(title="DIY Dillon 1050 Autodrive API")

    @app.get("/", response_class=HTMLResponse)
    def home():
        return """<html><body><h1>DIY Dillon 1050 Autodrive</h1>
        <ul>
            <li><a href='/status'>Status</a></li>
            <li><a href='/logs'>Logs</a></li>
        </ul></body></html>"""

    @app.get("/status")
    def status():
        return {"ok": True, "message": "API alive"}

    @app.get("/logs")
    def logs():
        return {"errors": [], "maintenance": [], "production": []}

    return app

def run_dev(app):
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
