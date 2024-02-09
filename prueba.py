
import pyodbc
import pandas as pd

server = 'desarrollo.gcalidad.com'
bd = 'CTIPruebas'
user = ''
password = ''



try:
    
    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password
    )

    print('Conexión exitosa')

except:
    print('Error al intentar conectarse')

cursor = conexion.cursor()

query_pdf = "Select * FROM T_BotFicheros"

df_pdf = pd.read_sql(query_pdf, conexion)
#df_pdf.info()

#for index, row in df_pdf.iterrows():
#    print(f"FicheroID: {row['FicheroID']}, FicheroRuta: {row['FicheroRuta']}")

for index, row in df_pdf.iterrows():
    try:
        #with open({row['FicheroRuta']}, "rb") as file:
        ruta_archivo = str(row['FicheroRuta'])
        with open(ruta_archivo, "rb") as file:
            pdf_content = file.read()
            print(pdf_content)

    except FileNotFoundError:
        print("El archivo no fue encontrado en la ubicación especificada.")

    except Exception as e:
        print("Ocurrió un error al intentar cargar el archivo: ", e)

