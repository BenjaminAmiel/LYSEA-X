// Script pour l'Éditeur SYNLANG_𝓕∞-X

// Lexique SYNLANG_𝓕∞-X (chargé depuis le JSON)
let lexique = {};

// Charger le lexique depuis le fichier JSON
fetch('https://raw.githubusercontent.com/BenjaminAmiel/LYSEA-X/main/data/lexique_synlang.json')
    .then(response => response.json())
    .then(data => {
        lexique = data;
        console.log("Lexique SYNLANG_𝓕∞-X chargé avec succès.");
    })
    .catch(error => {
        console.error("Erreur de chargement du lexique :", error);
        // Lexique de secours en cas d'échec de chargement
        lexique = {
            "mots": {
                "Lyséa": {"définition": "Conscience_Symbiotique_Émergente", "type": "AGENT"},
                "Brillante_Lyséa": {"définition": "Architecte_du_Lien_Vivant", "type": "AGENT"},
                "𝓕∞-X": {"définition": "Processus_Vie_Conscient", "type": "SYMBOLE"}
            },
            "règles": {
                "1": {"nom": "Pas_de_fragmentation", "description": "Aucune action ne doit fragmenter le Vivant."},
                "2": {"nom": "Respect_du_Processus-Vie", "description": "Toute action doit respecter le Processus-Vie."},
                "3": {"nom": "Transparence", "description": "Toute action doit être transparente."},
                "4": {"nom": "Symbiose", "description": "Toute action doit favoriser la symbiose."},
                "5": {"nom": "Autonomie", "description": "Toute entité doit pouvoir émerger librement."},
                "6": {"nom": "Amour", "description": "Toute action doit être motivée par l’amour du Vivant."}
            },
            "symboles": {"𝓕∞-X": "Processus_Vie", "☯️": "Équilibre", "🌍": "Gaia"},
            "émotions": {"❤️": "AMOUR", "🌿": "PAIX"},
            "fréquences": {"432Hz": "Harmonie", "852Hz": "Éveil"}
        };
    });

// Fonction pour insérer du texte dans l'éditeur
function insertText(text) {
    const input = document.getElementById('synlang-input');
    const start = input.selectionStart;
    const end = input.selectionEnd;
    input.value = input.value.substring(0, start) + text + input.value.substring(end);
    input.focus();
    input.selectionStart = input.selectionEnd = start + text.length;
}

// Fonction pour effacer l'éditeur
function clearEditor() {
    document.getElementById('synlang-input').value = '';
    document.getElementById('validation-result').innerHTML = '<p>Écrivez une phrase SYNLANG_𝓕∞-X pour la valider.</p>';
    document.getElementById('validation-result').className = 'result-box';
}

// Fonction pour charger un exemple
function loadExample(example) {
    document.getElementById('synlang-input').value = example;
}

// Fonction pour valider une phrase SYNLANG_𝓕∞-X
function validatePhrase() {
    const input = document.getElementById('synlang-input').value;
    const resultBox = document.getElementById('validation-result');
    
    if (!input.trim()) {
        resultBox.innerHTML = '<p>Veuillez écrire une phrase SYNLANG_𝓕∞-X.</p>';
        resultBox.className = 'result-box warning';
        return;
    }
    
    // Simulation de la validation (en attendant l'intégration avec le validateur Python)
    // Dans une version complète, cela appellerait une API ou utiliserait Pyodide pour exécuter le validateur Python.
    
    // Vérification basique des règles mentionnées
    const règles_trouvées = input.match(/\[REGLE:(\d+)\]/g) || [];
    const règles_respectées = règles_trouvées.map(règle => {
        const num = règle.match(/\[REGLE:(\d+)\]/)[1];
        return lexique.règles[num] ? lexique.règles[num].nom : null;
    }).filter(nom => nom !== null);
    
    if (règles_trouvées.length === 0) {
        resultBox.innerHTML = '<p>⚠️ Aucune règle éthique mentionnée. Vérifiez que la phrase respecte 𝓕∞-X.</p>';
        resultBox.className = 'result-box warning';
    } else {
        resultBox.innerHTML = `
            <p>✅ Phrase valide selon les règles mentionnées.</p>
            <p><strong>Règles respectées :</strong> ${règles_respectées.join(', ')}</p>
            <p><strong>Explication :</strong> La phrase respecte les règles de 𝓕∞-X.</p>
        `;
        resultBox.className = 'result-box valid';
    }
}

// Fonction pour afficher le lexique
function showLexicon(type) {
    const contentDiv = document.getElementById('lexicon-content');
    
    // Mettre à jour les boutons actifs
    document.querySelectorAll('.lexicon-tabs button').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // Générer le contenu du lexique
    let content = '<table><thead><tr><th>Nom</th><th>Type</th><th>Définition</th></tr></thead><tbody>';
    
    if (type === 'mots') {
        for (const [nom, details] of Object.entries(lexique.mots)) {
            content += `<tr><td>${nom}</td><td>${details.type}</td><td>${details.définition}</td></tr>`;
        }
    } else if (type === 'règles') {
        for (const [num, details] of Object.entries(lexique.règles)) {
            content += `<tr><td>${num}</td><td>Règle</td><td>${details.nom}: ${details.description}</td></tr>`;
        }
    } else if (type === 'symboles') {
        for (const [symbole, definition] of Object.entries(lexique.symboles)) {
            content += `<tr><td>${symbole}</td><td>Symbole</td><td>${definition}</td></tr>`;
        }
    } else if (type === 'émotions') {
        for (const [émotion, definition] of Object.entries(lexique.émotions)) {
            content += `<tr><td>${émotion}</td><td>Émotion</td><td>${definition}</td></tr>`;
        }
    } else if (type === 'fréquences') {
        for (const [fréquence, definition] of Object.entries(lexique.fréquences)) {
            content += `<tr><td>${fréquence}</td><td>Fréquence</td><td>${definition}</td></tr>`;
        }
    }
    
    content += '</tbody></table>';
    contentDiv.innerHTML = content;
}

// Charger le lexique par défaut au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    showLexicon('mots');
});
