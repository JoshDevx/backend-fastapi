from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"titulo": "Cerámica Prehispánica del Norte", "autor": "Julio C. Tello", "categoria": "Arqueología"},
    {"titulo": "Industria Lítica y Obsidianas", "autor": "Luis Guillermo Lumbreras", "categoria": "Historia"},
    {"titulo": "Documentación de Conchales", "autor": "Ruth Shady", "categoria": "Investigación"},
    {"titulo": "Minerales y Cuarzos Andinos", "autor": "Federico Kauffmann Doig", "categoria": "Geología"},
    {"titulo": "Rutas Preincas en los Cerros", "autor": "Maria Rostworowski", "categoria": "Arqueología"}
]

@app.get("/books")
async def first_api():
    return BOOKS