import openai
import os


openai.api_key = os.getenv('OPENAI_API_KEY')



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
                "content": "Dime las palabras clave de la transcripción, sé preciso, sólo las palabras clave o key words"
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
                "content": "Eres una IA altamente capacitada y entrenada en análisis de discurso, haz una retroalimentación sobre la métrica de 'COHERENCIA' dime si el discurso es coherente y por qué. Evita palabras de más, sé preciso, ve defrente con al respuesta"
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
                "content": "Eres una IA altamente capacitada y entrenada en análisis de discurso, haz una retroalimentación sobre la métrica de 'CLARIDAD' dime si el discurso es claro y por qué. Evita palabras de más, sé preciso, ve defrente con al respuesta"
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
                "content": "Eres una IA altamente capacitada y entrenada en análisis de discurso, haz una retroalimentación sobre la métrica de 'MULETILLAS' dime si hay o no muletillas, en casi si dime cuantas muletillas tiene el discurso y cuáles son. Evita palabras de más, sé preciso, ve defrente con al respuesta"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#SUGERENCIA
def sugerencia_discurso():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "En base a las métricas anteriores, coherencia, claridad y muletillas y en base tus respuestas, dame sugerencias para mejorar en esos aspectos"
            },
            {
                "role": "user",
                "content": ""
            }
        ]
    )
    return response['choices'][0]['message']['content']