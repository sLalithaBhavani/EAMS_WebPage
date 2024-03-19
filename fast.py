from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request, username: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "username": username})

@app.post("/submit_form")
async def login(username: str = Form(...), firstName: str = Form(...), lastName: str = Form(...), officeName: str = Form(...), designation: str = Form(...)):
    # Here you can add your login logic
    return {"username": username, "firstName": firstName, "lastName": lastName, "officeName": officeName, "designation": designation}
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)