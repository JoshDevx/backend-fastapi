from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"titulo": "titulo1", "autor": "Julio C. Tello", "categoria": "Arqueología"},
    {"titulo": "titulo2", "autor": "Luis Guillermo Lumbreras", "categoria": "Historia"},
    {"titulo": "titulo3", "autor": "Ruth Shady", "categoria": "Investigación"},
    {"titulo": "titulo4", "autor": "Federico Kauffmann Doig", "categoria": "Geología"},
    {"titulo": "titulo5", "autor": "Maria Rostworowski", "categoria": "Arqueología"}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

# Parametros dinamicos
@app.get("/books/{title_book}") # recibe el parametro y lo agrega la ruta
async def read_books(title_book: str): # funcion que recibe un parametro
    for book in BOOKS:
        if book.get("titulo").casefold() ==  title_book.casefold():
            return book # retorna el parametro