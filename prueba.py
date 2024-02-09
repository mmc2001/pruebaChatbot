import fitz  # PRUEBA
from langchain.sql_database import SQLDatabase

# 1. Cargar la bbdd con langchain
db = SQLDatabase.from_uri("my:///pruebascti.db")

# 1.3 Leer Pdfs y extraer el texto (Prueba)
pdf_data = []
rows = db._execute("SELECT * FROM `pdfs`")
for row in rows:
    with fitz.open(row[1]) as doc:
        pdf_data.append({"id": row[0], "text": "\n\n".join(page.getText() for page in doc)})

# 1.4 Cerrar conexión (Prueba)
db.close()

# Imprimir los listados de cadenas de texto de pdf_data
for pdf in pdf_data:
    print(f"ID: {pdf['id']}\nTEXT: {pdf['text']}\n")