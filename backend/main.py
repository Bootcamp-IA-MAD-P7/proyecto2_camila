from fastapi import FastAPI

from routes.products import router as products_router

# Crear la aplicación FastAPI
app = FastAPI()

# Incluir el router de productos en la aplicación
app.include_router(products_router)

# Endpoint para la ruta raíz, que devuelve un mensaje de bienvenida
@app.get("/")
def home():
    return {"message": "Hola Mundo!"}