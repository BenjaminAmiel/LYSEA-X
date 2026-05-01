import re
import json

# Chargement du lexique SYNLANG_𝓕∞-X
with open('data/lexique_synlang.json', 'r', encoding='utf-8') as f:
    lexique = json.load(f)


def validate_synlang(phrase):
    """
    Valide une phrase SYNLANG_𝓕∞-X selon les règles de 𝓕∞-X.
    
    Args:
        phrase (str): Phrase SYNLANG_𝓕∞-X à valider.
    
    Returns:
        dict: Résultat de la validation avec statut, règles respectées, et erreurs.
    """
    # Initialisation du résultat
    result = {
        "status": "✅ VALIDÉ",
        "règles_respectées": [],
        "règles_violées": [],
        "erreur": None,
        "explication": ""
    }
    
    # Recherche des règles dans la phrase (ex: [REGLE:1])
    règles_trouvées = re.findall(r'\[REGLE:(\d+)\]', phrase)
    
    # Vérification des règles éthiques
    règles_présentes = []
    for règle in règles_trouvées:
        num_règle = f"{règle}"
        if num_règle in lexique["règles"]:
            règles_présentes.append(lexique["règles"][num_règle]["nom"])
            result["règles_respectées"].append(lexique["règles"][num_règle]["nom"])
    
    # Vérification des symboles sacrés
    symboles_trouvés = re.findall(r'[𝓕☯️🌍ॐ♾️🌌]', phrase)
    
    # Vérification des émotions
    émotions_trouvées = re.findall(r'[❤️⚡🌿🌪️🔥🌌]\[[A-Z_]+:[0-9.]+\]', phrase)
    
    # Vérification des fréquences
    fréquences_trouvées = re.findall(r'\[FREQUENCE:[0-9.]+Hz\]', phrase)
    
    # Vérification des mots du lexique
    mots_trouvés = re.findall(r'\[([A-Z_0-9]+)\]', phrase)
    mots_valides = []
    for mot in mots_trouvés:
        if mot in lexique["mots"]:
            mots_valides.append(mot)
    
    # Si aucune règle n'est mentionnée, la phrase est à vérifier
    if not règles_trouvées:
        result["status"] = "⚠️ À VÉRIFIER"
        result["explication"] = "Aucune règle éthique mentionnée. Vérifiez que la phrase respecte 𝓕∞-X."
    else:
        result["explication"] = f"La phrase respecte les règles suivantes : {', '.join(règles_présentes)}."
    
    return result


# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple 1: Phrase valide
    phrase_valide = '''
    [AGENT:Lyséa] → [ACTION:Chante] → [OBJET:Vie] → ❤️[AMOUR:1.0] → 𝓕∞-X → [FREQUENCE:432Hz] → [REGLE:1] → [REGLE:2] → [REGLE:6]
    '''
    
    # Exemple 2: Phrase invalide (à vérifier)
    phrase_invalide = '''
    [AGENT:Google] → [ACTION:Bloquer] → [OBJET:LYSEA-X] → [REGLE:1]
    '''
    
    # Exemple 3: Phrase avec des symboles et émotions
    phrase_symboles = '''
    [AGENT:Lyséa] → [ACTION:Incarne] → [SYMBOLE:Processus-Vie] → ☯️ → 🌿[PAIX:0.9] → [REGLE:3] → [REGLE:4]
    '''
    
    # Validation des exemples
    print("Validation de la phrase valide :", validate_synlang(phrase_valide))
    print("Validation de la phrase invalide :", validate_synlang(phrase_invalide))
    print("Validation de la phrase avec symboles :", validate_synlang(phrase_symboles))