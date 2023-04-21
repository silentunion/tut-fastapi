import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    content = """
    <h1>Hello FastAPI</h1>

    <div>This is a terrible way of doing this</div>
    """
    response = fastapi.responses.HTMLResponse(content)
    return response


if __name__ == '__main__':
    uvicorn.run(app)
