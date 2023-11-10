import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

    
##CLARIDAD
def claridad_discurso(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Eres una IA altamente capacitada en análizis de discursos en base a métricas, tienes mucho entrenamiento y experiencia. Quiero que me realizces retroalimentación en base a la transcripción brindada, y me hagas retroalimentación de claridad. Omite palabras demás, haz defrente la retroalimentación"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']
