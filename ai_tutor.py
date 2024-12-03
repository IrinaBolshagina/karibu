from huggingface_hub import InferenceClient


def make_prompt(question, answer):
    return f"""Évalue ma réponse.
    Question : "{question}"
    Ma réponse : "{answer}"
    Évalue cette réponse en suivant exactement ce format :

    **Compréhension**
    [Analyse si la réponse correspond à la question posée]

    **Vocabulaire**
    [Analyse du vocabulaire utilisé]
    
    **Grammaire**
    [Corrections nécessaires OU "Le texte est correct. Félicitations !"]
    
    **Appréciation générale**
    [Bref commentaire encourageant]
    
    Importante: Évalue uniquement le texte fourni, sans le réécrire ni en générer un nouveau.
    """

def correct_text(question, answer, hf_token):
    client = InferenceClient(model="meta-llama/Meta-Llama-3-70B-Instruct", token=hf_token)
    output = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Tu es un enseignant qui évalue ma réponse."},
        {"role": "user", "content": make_prompt(question, answer)},
    ],
    max_tokens=1024,)
    return output['choices'][0]['message']['content']
