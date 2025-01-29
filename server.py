from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from kumc import KUMCClient

app = FastAPI()

kumc_client = KUMCClient()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    await kumc_client.sign_in()
    resp = await kumc_client.get_health_check_result(hpCd="AA", strtYmd=20241101, fnshYmd=20250129)
    return templates.TemplateResponse(request=request, name="index.html", context={"results": resp['lemonRsltDetlOutDVOList']})
