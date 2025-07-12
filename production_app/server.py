#this is another method to run the app
# call the server.py file directly e.g `python3 server.py`
# or use uvicorn command to run the app
# e.g `uvicorn app:app --reload`
# or use uv command to run the app in development mode (auto-discovery)
# e.g `uv run fastapi dev`
# or use uv command to run the app in production mode
# e.g `uv run fastapi prod`
import uvicorn
if __name__ == "__main__":
    #uvicorn.run("app.main:app", reload=True)
    # customize the host and port for production use listen to all interfaces
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
    