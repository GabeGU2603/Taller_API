import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

    
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