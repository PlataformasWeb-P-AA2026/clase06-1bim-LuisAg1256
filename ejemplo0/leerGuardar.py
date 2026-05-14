import csv
import os
from base_datos import conn

def importar_datos_desde_csv(nombre_archivo):
    # 1. Obtener la ruta absoluta para evitar errores de "File Not Found"
    # Esto busca la carpeta 'data' al lado de este script
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_script, 'data', nombre_archivo)
    
    cursor = conn.cursor()

    try:
        print(f"Intentando abrir: {ruta_archivo}")
        
        # 2. Abrir el archivo
        with open(ruta_archivo, encoding='utf-8') as archivo_csv:
            # Sniffer detecta automáticamente si usas coma o punto y coma
            contenido = archivo_csv.read(2048)
            archivo_csv.seek(0)
            dialecto = csv.Sniffer().sniff(contenido)
            
            lector_csv = csv.DictReader(archivo_csv, dialect=dialecto)
            
            print("Cargando datos en la base de datos...")
            contador = 0

            for fila in lector_csv:
                # Extraer datos (asegúrate que los nombres coincidan con el encabezado del CSV)
                nombre = fila['nombre']
                apellido = fila['apellido']
                cedula = fila['cedula']
                edad = int(fila['edad'])

                # 3. Sentencia SQL (Usando el formato de tus archivos previos)
                cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
                VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

                cursor.execute(cadena_sql)
                contador += 1
            
            # 4. Guardar cambios permanentemente
            conn.commit()
            print(f"¡Éxito! Se importaron {contador} registros correctamente.")

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{nombre_archivo}' en la carpeta '{directorio_script}/data/'")
    except KeyError as e:
        print(f"ERROR: No se encontró la columna {e} en el CSV. Revisa los encabezados.")
    except Exception as e:
        print(f"ERROR inesperado: {e}")
        conn.rollback()
    finally:
        cursor.close()

if __name__ == "__main__":
    # Nombre del archivo dentro de la carpeta 'data'
    importar_datos_desde_csv("info.csv")