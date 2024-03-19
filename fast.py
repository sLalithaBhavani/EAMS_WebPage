
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from fastapi import Query
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Function to save uploaded file with a unique name
async def save_uploaded_file(upload_file: UploadFile, filename: str):
    with open(filename, "wb") as buffer:
        buffer.write(upload_file.file.read())

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload_image", response_class=HTMLResponse)
async def upload_image(request: Request, image: UploadFile = File(...)):
    # Save uploaded image with a unique name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    image_name = f"unknown_ck_{timestamp}.jpg"
    await save_uploaded_file(image, f"images/{image_name}")

    # Redirect to enter details page with the filename as a query parameter
    return RedirectResponse(url=f"/enter_details?filename={image_name}")

@app.post("/enter_details", response_class=HTMLResponse)
async def enter_details(request: Request, filename: str = Query(...)):
    return templates.TemplateResponse("details.html", {"request": request, "filename": filename})

@app.post("/submit_form")
async def submit_form(request: Request, firstName: str = Form(...), lastName: str = Form(...), officeName: str = Form(...), designation: str = Form(...), filename: str = Form(...)):
    # Process form data here
    return {"message": "Form submitted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)