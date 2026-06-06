# Trae BaseModel para definir cómo deben ser los datos 
from pydantic import BaseModel

# Define como deben ser los datos de un producto usando Pydantic
class Product(BaseModel):
    nombre: str
    tipo: str
    precio: float

