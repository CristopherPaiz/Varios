#pip install anthropic

import anthropic

# Inicializar la lista de mensajes
conversation = []

client = anthropic.Anthropic(
    api_key="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",
)

while True:
    # Obtener el mensaje del usuario
    user_message = input("===================================================\n\nTú: ")

    # Agregar el mensaje del usuario al historial de la conversación
    conversation.append({"role": "user", "content": user_message})

    # Enviar el historial de la conversación a Claude AI
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        messages=conversation
    )

    # Agregar la respuesta de Claude AI al historial de la conversación
    conversation.append({"role": "assistant", "content": response.content[0].text})

    # Imprimir la respuesta de Claude AI
    print("===================================================\nClaude: \n" + response.content[0].text +"\n")

    # Verificar si el usuario desea salir de la conversación
    if user_message.lower() == "salir":
        break