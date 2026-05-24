from fastapi import FastAPI #Importamos
from pydantic import BaseModel, Field #Importamos BaseModel de pyndatic y campo(Field)
from typing import Optional

app = FastAPI() #instanciamos

class Book: #Clase de book
    id: int
    title: str
    author: str
    description: str
    rating: int

    #Constructor
    def __init__(self, id, title, author, description, rating):
        self.id = id 
        self.title = title 
        self. author = author 
        self.description = description 
        self.rating = rating

# Creamos una clase heredando BaseModel
class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3) # Con Field, agregamos validacion
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

BOOKS = [ # Lista de libros
    Book(1, "Clean Code", "Joshua", "Codigo limpio", 5),
    Book(2, "Data Modeling con Power BI", "Marco Russo", "Modelado avanzado y DAX", 5),
    Book(3, "Arqueología del Perú", "Luis Lumbreras", "Estudio de cerámica y contextos", 5),
    Book(4, "Python para Análisis de Datos", "Wes McKinney", "Fundamentos de Pandas y Numpy", 4),
    Book(5, "Industria Lítica", "George Odell", "Análisis de cuarzo y obsidiana", 4),
    Book(6, "SQL Avanzado", "Itzik Ben-Gan", "Consultas complejas y bases de datos", 5)
] 

@app.get("/books") #Endpoint
async def read_all_books():
    return BOOKS #retorna la lista de libros


@app.post("/create_book") # Crear libro
async def create_book(book_request : BookRequest): #Recibe un llibro
    #Convertimos el libro en dic y con ** desempaquetamos para pasar al constructor
    new_book = Book(**book_request.model_dump()) 
    BOOKS.append(find_id(new_book)) #Agregamos el libro a la lista

def find_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book