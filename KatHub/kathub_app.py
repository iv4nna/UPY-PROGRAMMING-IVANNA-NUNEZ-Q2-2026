import os
import logging
from datetime import datetime
import requests

# CONFIGURACIÓN DE AUDIT LOGGING
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=os.path.join("logs", "app.log"),
    level=logging.INFO,
    format="%(asctime)s — [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# CONFIGURACIÓN DE FIREBASE
FIREBASE_BASE_URL = "https://kathub-7a49d-default-rtdb.firebaseio.com/"

def modo_autor():
    print("\n--- MODO AUTOR: CREAR ENCUESTA ---")
    author_name = input("Nombre del Autor: ")
    survey_title = input("Título de la Encuesta: ")
    print("Ingresa las preguntas separadas por '|' (Ej: Q1? | Q2?)")
    survey_questions = input("Preguntas: ")
    
    # características del repositorio
    end_date = input("Fecha de cierre de la encuesta (AAAA-MM-DD): ")
    privacy = input("¿Hacer el repositorio de respuestas público al cerrar? (PUBLIC/PRIVATE): ").strip().upper()

    # Estructura de la encuesta para la nube
    survey_data = {
        "title": survey_title,
        "author": author_name,
        "questions": survey_questions,
        "end_date": end_date,
        "privacy": privacy
    }

    print("Subiendo encuesta a KatHub...")
    try:
        url = f"{FIREBASE_BASE_URL}surveys/{survey_title}.json"
        response = requests.put(url, json=survey_data)
        if response.status_code == 200:
            print(f"¡Encuesta '{survey_title}' publicada con éxito!")
            logging.info(f"Encuesta creada por {author_name}: '{survey_title}' (Cierre: {end_date}, Estado: {privacy})")
        else:
            print("Error al publicar en la nube.")
            logging.error(f"Error modo autor: Status {response.status_code}")
    except Exception as e:
        print(f"Error de conexión: {e}")
        logging.error(f"Excepción en modo autor: {e}")

def modo_estudiante():
    print("\n--- MODO ESTUDIANTE: RESPONDER ENCUESTA ---")
    
    try:
        response = requests.get(f"{FIREBASE_BASE_URL}surveys.json")
        surveys = response.json()
        
        if not surveys:
            print("No hay encuestas disponibles en este momento.")
            return
            
        print("\nEncuestas activas en KatHub:")
        lista_encuestas = list(surveys.keys())
        for i, title in enumerate(lista_encuestas, 1):
            print(f"[{i}] '{title}' por {surveys[title]['author']} (Cierra el: {surveys[title].get('end_date', 'N/A')})")
            
        opcion = int(input("\nSelecciona el número de la encuesta a responder: ")) - 1
        selected_title = lista_encuestas[opcion]
        survey = surveys[selected_title]
        
    except Exception as e:
        print(f"Error al conectar con el catálogo: {e}")
        logging.error(f"Error al obtener encuestas: {e}")
        return

    print("\n--------------------------------------------------")
    print(f"Encuesta: {survey['title']} | Preguntas: {survey['questions']}")
    print("--------------------------------------------------")
    
    respondent_id = input("Ingresa tu ID Institucional (Anónimo): ")
    print("Ingresa tus respuestas separadas por '|' en el mismo orden:")
    answers_summary = input("Respuestas: ")
    
    confirm = input("\n¿Deseas enviar tus respuestas al hub público? (YES/NO): ").strip().upper()
    
    if confirm == "YES":
        new_entry = f"Account ID: {respondent_id} | Answers: {answers_summary}"
        try:
            resp_url = f"{FIREBASE_BASE_URL}responses/{selected_title}.json"
            current_resp = requests.get(resp_url).json() or ""
            
            updated_log = new_entry if current_resp == "" else f"{current_resp}\n{new_entry}"
            
            put_response = requests.put(resp_url, json=updated_log)
            if put_response.status_code == 200:
                print("¡Respuestas guardadas en la nube de forma segura!")
                logging.info(f"Respuestas guardadas para '{selected_title}' por ID: {respondent_id}")
            else:
                logging.error(f"Error al subir respuestas: Status {put_response.status_code}")
        except Exception as e:
            print(f"Error al enviar respuestas: {e}")
    else:
        print("Envío cancelado.")

def ver_repositorio_publico():
    print("\n--- REPOSITORIO PÚBLICO DE DATOS RECABADOS ---")
    try:
        # Traer encuestas y respuestas simultáneamente
        surveys = requests.get(f"{FIREBASE_BASE_URL}surveys.json").json()
        responses = requests.get(f"{FIREBASE_BASE_URL}responses.json").json()
        
        if not surveys or not responses:
            print("No hay registros de datos públicos disponibles todavía.")
            return

        lista_encuestas = list(surveys.keys())
        print("\nSelecciona un dataset del repositorio para visualizar:")
        for i, title in enumerate(lista_encuestas, 1):
            privacidad = surveys[title].get('privacy', 'PRIVATE')
            print(f"[{i}] '{title}' — Estado: {privacidad}")

        opcion = int(input("\nNúmero de dataset a consultar: ")) - 1
        selected_title = lista_encuestas[opcion]
        
        # Validación de privacidad
        if surveys[selected_title].get('privacy') == 'PUBLIC':
            print(f"\n=== DATASET PÚBLICO RECABADO PARA: {selected_title} ===")
            print(f"Preguntas originales: {surveys[selected_title]['questions']}")
            print("--------------------------------------------------")
            print(responses.get(selected_title, "No hay respuestas aún registradas para esta encuesta."))
            print("--------------------------------------------------")
            logging.info(f"Visualización pública exitosa para el dataset: '{selected_title}'")
        else:
            print("\n[ACCESO DENEGADO]: Este repositorio ha sido configurado como PRIVADO por su autor.")
            logging.warning(f"Intento de acceso no autorizado a repositorio privado: '{selected_title}'")
            
    except Exception as e:
        print(f"Error al acceder al repositorio: {e}")

def main():
    logging.info("KatHub program started successfully.")
    while True:
        print("\n=========================================")
        print("    BIENVENIDO A KATHUB DATA INTERFACE   ")
        print("=========================================")
        print("[1] Modo Autor (Crear y publicar encuesta)")
        print("[2] Modo Estudiante (Responder encuesta)")
        print("[3] Ver Repositorio de Datos Públicos")
        print("[4] Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            modo_autor()
        elif opcion == "2":
            modo_estudiante()
        elif opcion == "3":
            ver_repositorio_publico()
        elif opcion == "4":
            print("\n¡Gracias por usar KatHub! Conexión cerrada.")
            logging.info("Program execution finished normally. Connection closed.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()