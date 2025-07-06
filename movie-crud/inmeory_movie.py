movies = [
    {"id": 1, "title": "Shotgun Wedding", "year": 2022},
    {"id": 2, "title": "Unwelcome", "year": 2023},
    {"id": 3, "title": "Avatar: The Way of Water", "year": 2022},
]


@app.get("/")
async def root():
    return {"hello": "word"}


@app.get("/movies")
async def get_movies():
    return movies


@app.get("/movie/{id}")
async def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    else:
        return {"err": "moive not found"}


@app.delete("/movie/{id}")
async def remove_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"err": "moive deleted"}
    else:
        return {"err": "moive not found"}


@app.post("/movie/")
async def create_movie(movie: dict):
    movies.append(movie)
    return {"msg": "moive has added"}


@app.put("/movie/")
async def update_movie(id: int, new_movie: dict):
    for movie in movies:
        if movie["id"] == id:
            movie["id"] = new_movie["id"]
            movie["title"] = new_movie["title"]
            movie["year"] = new_movie["year"]

            return {"msg": "moive updated"}
    else:
        return {"err": "moive not found"}


# uvicorn main:app --reload
