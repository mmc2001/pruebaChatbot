import fitz #PRUEBA

# 1. Cargar la bbdd con langchain
from langchain.sql_database import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///pruebascti.db")

# 1.2 Cursor para ejecutar queries (Prueba)
cursor = db.cursor()

# 1.3 Leer Pdfs y extraer el texto (Prueba)
pdf_data = []
for row in cursor.execute("Select id, pdf_path From pdfs"):
    with fitz.open(row[1]) as doc:
        pdf_data.append({"id": row[0], "text": "\n\n".join(page.getText() for page in doc)})

# 1.4 Cerrar conexión (Prueba)
db.close()

# 2. Importar las APIs
import a_env_vars
import os
os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY

# 3. Crear el LLM
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo')

# 4. Crear la cadena
from langchain import SQLDatabaseChain
cadena = SQLDatabaseChain(llm = llm, database = db, verbose=False)

# 5. Formato personalizado de respuesta
formato = """
Dada una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
"""

# 6. Función para hacer la consulta

def consulta(input_usuario):
    consulta = formato.format(question = input_usuario)
    resultado = cadena.run(consulta)
    return(resultado)