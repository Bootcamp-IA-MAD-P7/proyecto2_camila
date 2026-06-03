# Trae la herramienta FastAPI para poder crear una API
from fastapi import FastAPI, HTTPException

# Trae BaseModel para definir cómo deben ser los datos 
from pydantic import BaseModel

# Crear la aplicación FastAPI
app = FastAPI()

# Esto es una base de datos temporal. Una lista vacía donde vamos a guardar los productos que creemos
products = []

# Define como deben ser los datos de un producto usando Pydantic
class Product(BaseModel):
    nombre: str
    tipo: str
    precio: float

# Endpoint para la ruta raíz, que devuelve un mensaje de bienvenida
@app.get("/")
def home():
    return {"message": "Hola Mundo!"}

# Endpoint para obtener la lista de productos. Devuelve una lista de productos predefinidos
@app.get("/products")
def get_products():
    
    # Devuelve la lista de productos 
    return products

# Endpoint para obtener un producto por su ID. 
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
        
    raise HTTPException(status_code=404, detail="Producto no encontrado")
    
# Endpoint para crear un nuevo producto
@app.post("/products")
def create_product(product: Product):
        new_product =  {
            "id": len(products) + 1,
            # dato que enviaste desde /docs
            "nombre": product.nombre,
            "tipo": product.tipo,
            "precio": product.precio
        }
        
        # Guardar en lista  
        products.append(new_product)
        
        # Devolver el nuevo producto creado
        return new_product

# Endpoint para actualizar un producto existente
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for p in products:
        if p["id"] == product_id:
            p["nombre"] = product.nombre
            p["tipo"] = product.tipo
            p["precio"] = product.precio
            return p
        
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# Endpoint para eliminar un producto por su ID
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return {"message": "Producto eliminado"}
        
    raise HTTPException(status_code=404, detail="Producto no encontrado")