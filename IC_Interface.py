import re  

# 🔹 **Diccionario de palabras clave** (completar con tus términos)
KEYWORDS = {
    "Keyword1", "keyword2", "Keyword3", "Keyword4", "Keyword5", "Keyword6", "Keyword7", "Keyword8",
    "Keyword9", "Keyword10", "Keyword11", "Keyword12", "Keyword13"
}

def clean_text(text):
    """Limpia texto eliminando caracteres especiales y formato no deseado."""
    if not text:
        return ""
    text = text.replace("\n", " ").replace("\r", " ")  # Elimina saltos de línea
    text = re.sub(r'\*+', '', text)  # Elimina *, **, ***
    text = re.sub(r'\s+', ' ', text).strip()  # Remueve espacios extra
    return text

def extract_keywords(text):
    """Extrae palabras clave que están en el diccionario."""
    words = text.split()
    return [word for word in words if word in KEYWORDS]

def convert_document_to_instructions(document):
    """Convierte los pasos de un documento escrito en lenguaje natural al formato instructions."""
    instructions = []
    
    for step in document["custom_steps_separated"]:
        content = clean_text(step.get("content", ""))
        expected = clean_text(step.get("expected", ""))

        # Extrae palabras clave
        stage_keywords = extract_keywords(content)
        action_keywords = extract_keywords(expected)

        if stage_keywords and action_keywords:
            instruction_line = f"{stage_keywords[0]}:{', '.join(action_keywords)}"
            instructions.append(instruction_line)

    return '|\n'.join(instructions)

# 🔹 **Ejemplo de uso con datos simulados de un documento**
document = {
    "custom_steps_separated": [
        {
            "content": "**Keyword1**\n- Keyword9",
            "expected": "**Keyword7**\n- Keyword5 Keyword58 Keyword89, Keyword1"
        },
        {
            "content": "**Keyword2**\n- Keyword6",
            "expected": "Keyword3"
        }
    ]
}

instructions = convert_document_to_instructions(document)
print(instructions)
