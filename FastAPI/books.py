from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"titulo": "titulo1", "autor": "autor1", "categoria": "Arqueologia"},
    {"titulo": "titulo2", "autor": "autor2", "categoria": "Historia"},
    {"titulo": "titulo3", "autor": "autor1", "categoria": "Arqueologia"},
    {"titulo": "titulo4", "autor": "autor3", "categoria": "Historia"},
    {"titulo": "titulo5", "autor": "autor3", "categoria": "Arqueologia"}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

# Parametros de ruta
@app.get("/books/{title_book}") # recibe el parametro y lo agrega la ruta
async def read_books(title_book: str): # funcion que recibe un parametro
    for book in BOOKS:
        if book.get("titulo").casefold() ==  title_book.casefold():
            return book # retorna el parametro

# Parametros de consulta
# Podemos usar List Comprehesion
'''
Devuelve una lista con cada book que encuentres dentro de BOOKS, 
pero solo if (si) la categoría coincide".
'''
@app.get("/books/")
async def read_category_by_query(categoria: str):
    return [book for book in BOOKS if book.get('categoria').casefold() == categoria.casefold() ]
'''   
Manera mas larga de hacerlo
    for book in BOOKS:
        if book.get('categoria').casefold() == categoria.casefold():
            books_to_return.append(book)
    return books_to_return
'''

# Parametro de ruta y de consulta
@app.get("/books/{author}/")
async def read_author_category_by_query(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('autor').casefold() == author.casefold() and book.get('categoria').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book = Body() ):
    BOOKS.append(new_book)

