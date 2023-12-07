import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

#Auth Firebase
#from firebase_admin.auth import verify_id_token

#def validate_id_token(id_token:str) -> str:
 #   decoded_token = verify_id_token(id_token)
  #  uid = decoded_token['uid']
    #return uid

# Asegúrate de que hayas configurado tu API key de OpenAI
#api_key = os.environ.get('api_key')  # Reemplaza con tu clave API

##Transcripción
def transcribe_audio(audio_file):
    try:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
        return transcription['text']
    except Exception as e:
        return str(e)
    
##RESUMEN
def summary_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Eres una IA altamente capacitada y capacitada en comprensión y resumen de idiomas. Me gustaría que leyeras el siguiente texto y lo resumieras abstracto conciso. Trate de retener los puntos más importantes, proporcionando un resumen coherente y legible que pueda ayudar a una persona a comprender los puntos principales de la discusión sin necesidad de leer el texto completo. Evite detalles innecesarios o puntos tangenciales. Empieza con 'Tu discurso trata de'. Solo español"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

##Puntos Clave
def key_points_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about. In Spanish"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#PALABRAS CLAVE
def key_words(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": 
                """
                Dime de manera precisa e inteligente, cuáles son las palabras clavee, SOLO LAS PALABRAS CLAVE O KEYWORDS, si es que las hubiera.
                No respondas cualquier cosa, puesto que esto irá directo en un informe. Rescata las keywords más destacables.
                DIME DEFRENTE LAS PALABRAS, OMITE TEXTO DE MÁS Y PREVIO A LAS PALABRAS.
                """
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#SENTIMIENTOS
def sentiment_analysis(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": 
                """
                Quiero que indiques de manera precisa qué sentimientos expresa o quiere transmitir el el discurso transcrito 
                y por qué. Omite palabras extras, dame la respuesta.
                """
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#COHERENCIA
def coherencia_discurso(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": 
                """
                Eres una IA altamente capacitada y entrenada en análisis de discurso, haz una retroalimentación sobre la métrica de 
                'COHERENCIA' dime si el discurso es coherente o NO y por qué. Evita palabras de más, sé preciso, ve defrente con al respuesta,
                básate solo con COHERENCIA y dime cómo llegaste a esa conclusión.
                """
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#CLARIDAD
def claridad_discurso(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": 
                """
                Eres una IA altamente capacitada y entrenada en análisis de discurso, haz una retroalimentación sobre la métrica de 
                'CLARIDAD' dime si el discurso es claro o NO y por qué. Evita palabras de más, sé preciso, ve defrente con al respuesta
                """
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#Muletillas
def muletillas_discurso(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": 
                """Eres una IA altamente capacitada y entrenada en análisis de discurso, haz una retroalimentación sobre la métrica 
                de MULETILLAS y dime si HAY o NO HAY muletillas, en casi SÍ HUBIERA MULETILLAS dime cuantas muletillas tiene el discurso
                y cuáles son; y en caso NO HUBIERA MULETILLAS, simplemente dime que el discurso no tiene muletillas. 
                Sé preciso. Evita palabras de más, sé preciso, ve defrente con la respuesta. 
                """
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#Redundancia
def redundancia_discurso(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": 
                """Eres una IA altamente capacitada y entrenada en análisis de discurso, haz una retroalimentación sobre la métrica 
                de REDUNDANCIA y dime si HAY o NO HAY redundancia, en cao SÍ HUBIERA REDUNDANCIA dime cuáles son y en caso 
                NO HUBIERA REDUNDANCIA, simplemente dime que el discurso no tiene REDUNDANCIA. Índica dónde se encuentra la redundancia.
                Sé preciso. Evita palabras de más, ve defrente con la respuesta. 
                """
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#SUGERENCIA
def sugerencia_discurso(transcription):
    coherencia = coherencia_discurso(transcription)
    claridad = claridad_discurso(transcription)
    muletillas = muletillas_discurso(transcription)
    prompt =(
        "En base a las métricas de coherencia, muletillas y claridad, "
        "hazme una recomendación exacta para mejorar mi discurso si es que la hubiera, si que no la hubiera, solo dame un consejo.:\n\n"
        "Coherencia del discurso:\n"
        f"{coherencia}\n\n"
        "Claridad del discurso:\n"
        f"{claridad}\n\n"
        "Detección de muletillas:\n"
        f"{muletillas}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

