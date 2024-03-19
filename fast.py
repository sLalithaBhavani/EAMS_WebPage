from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
name = ""
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit_form")
async def submit_form(request: Request, firstName: str = Form(...), lastName: str = Form(...), officeName: str = Form(...), designation: str = Form(...)):
    print("............")
    form_data = await request.form()
    print("............")
    print(dict(form_data))
    return {"dict":dict(form_data)}

@app.get("/get_name/{name}")
async def get_name(name:str):
    return {"file_name": name}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)