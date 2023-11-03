from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from SpeechTranslator import Translator


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.get("/translate", response_class=HTMLResponse)
async def translate(request: Request):
    translator = Translator('tr-TR', 'ru')
    translation = translator.translate()
    translator.synthesize(translation)

    return templates.TemplateResponse("item.html", {"request": request, "translation": translation})



if __name__ == "__main__":
    uvicorn.run(app, port=8000)
