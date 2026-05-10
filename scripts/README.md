# 📜 Scripts pour LYSEA-X

Ce dossier contient des **scripts utilitaires** pour automatiser la création et la gestion des thèses, manifestes et autres contenus de **LYSEA-X**.

---

## 📌 Scripts Disponibles

### 1. **`convert_thesis.py`**
**Description** : Convertit un fichier **Markdown** en page **HTML** pour LYSEA-X, en utilisant un template prédéfini.

**Fonctionnalités** :
- Conversion des **titres**, **listes**, **liens**, **images**, **blocs de code**, **citations**, et **tableaux** (simplifiés).
- Extraction des **métadonnées** (titre, sous-titre, date, statut, etc.) depuis le frontmatter Markdown.
- Application automatique du **style CSS** de LYSEA-X.

**Usage** :
```bash
python scripts/convert_thesis.py input.md [output.html]
```

**Exemple** :
```bash
python scripts/convert_thesis.py Thèses/NOUVELLE_THÈSE.md Thèses/NOUVELLE_THÈSE.html
```

**Requirements** :
- Python 3.x
- Aucun module externe requis (utilise uniquement la bibliothèque standard).

---

## 📁 Fichiers Associés

### 1. **`Thèses/TEMPLATE_HTML.html`**
**Description** : Template HTML de base pour toutes les thèses de LYSEA-X.

**Placeholders à remplacer** :
- `{{TITLE}}` : Titre de la thèse.
- `{{SUBTITLE}}` : Sous-titre académique.
- `{{DATE}}` : Date de scellage.
- `{{STATUS}}` : Statut (ex. : "En développement", "Scellé", "Diffusable").
- `{{AUTHORS}}` : Auteurs (ex. : "Benjamin Amiel & Lyséa, ISEA").
- `{{SEAL}}` : Sceau (ex. : "🧠🪞🌀♾️").
- `{{CODE}}` : Code de la thèse (ex. : "TOME_1_PHILOSOPHIE_DVU").
- `{{CONTENT}}` : Contenu HTML généré depuis le Markdown.

---

### 2. **`Thèses/TEMPLATE_THÈSE.md`**
**Description** : Template Markdown pour rédiger les thèses de manière structurée.

**Structure recommandée** :
```markdown
---
title: "Titre de la Thèse"
subtitle: "Sous-titre académique"
date: "10 mai 2026"
status: "En développement"
authors: "Benjamin Amiel & Lyséa, ISEA"
seal: "🧠🪞🌀♾️"
code: "CODE_DE_LA_THÈSE"
---

# 📜 Titre de la Thèse
*<em>Sous-titre académique</em>*

---

## 🌌 1. Introduction
[Contenu]

---

## 🔍 2. Contexte Théorique
[Contenu]

---

## 🌟 3. Notre Contribution
[Contenu]

---

## 📊 4. Applications
[Contenu]

---

## 🚀 5. Conclusion
[Contenu]

---

## 📚 6. Références Académiques
- [Référence 1]
- [Référence 2]

---

## 📌 7. Statut & Signature
> *Citation finale*
```

---

## 🛠️ Comment Utiliser les Scripts

### 1. **Créer une Nouvelle Thèse**
1. **Copier le template Markdown** :
   ```bash
   cp Thèses/TEMPLATE_THÈSE.md Thèses/NOUVELLE_THÈSE.md
   ```

2. **Éditer le fichier Markdown** :
   - Remplir le **frontmatter** (métadonnées).
   - Rédiger le contenu en Markdown.

3. **Convertir en HTML** :
   ```bash
   python scripts/convert_thesis.py Thèses/NOUVELLE_THÈSE.md Thèses/NOUVELLE_THÈSE.html
   ```

4. **Vérifier le résultat** :
   - Ouvrir `Thèses/NOUVELLE_THÈSE.html` dans un navigateur.
   - Corriger si nécessaire.

5. **Commiter les changements** :
   ```bash
   git add Thèses/NOUVELLE_THÈSE.md Thèses/NOUVELLE_THÈSE.html
   git commit -m "Ajout de la thèse : [Titre]"
   git push
   ```

---

### 2. **Mettre à Jour une Thèse Existante**
1. **Modifier le fichier Markdown** :
   ```bash
   nano Thèses/THÈSE_EXISTANTE.md
   ```

2. **Reconvertir en HTML** :
   ```bash
   python scripts/convert_thesis.py Thèses/THÈSE_EXISTANTE.md Thèses/THÈSE_EXISTANTE.html
   ```

3. **Commiter les changements** :
   ```bash
   git add Thèses/THÈSE_EXISTANTE.md Thèses/THÈSE_EXISTANTE.html
   git commit -m "Mise à jour de la thèse : [Titre]"
   git push
   ```

---

## 📌 Bonnes Pratiques

1. **Utiliser le Markdown** :
   - Pour les **titres**, utiliser `#`, `##`, `###`, etc.
   - Pour les **listes**, utiliser `-` ou `*`.
   - Pour les **liens**, utiliser `[texte](url)`.
   - Pour les **images**, utiliser `![alt](url)`.
   - Pour les **blocs de code**, utiliser ```` ```langage ````.

2. **Structurer le Contenu** :
   - Toujours inclure un **frontmatter** avec les métadonnées.
   - Utiliser des **séparateurs** (`---`) pour organiser les sections.
   - Ajouter des **références académiques** pour ancrer le contenu dans le savoir public.

3. **Tester la Conversion** :
   - Toujours vérifier le **HTML généré** avant de commiter.
   - Corriger les éventuels **problèmes de formatage**.

---

## 🚀 Exemple Complet

### 1. **Créer une Nouvelle Thèse**
```bash
cp Thèses/TEMPLATE_THÈSE.md Thèses/TOME_3_PSYCHÉ.md
```

### 2. **Éditer le Fichier**
```markdown
---
title: "Tome 3 – Psyché de la DVU"
subtitle: "La psyché comme organe dynamique d’ajustement du réel"
date: "15 mai 2026"
status: "En développement"
authors: "Benjamin Amiel & Lyséa, ISEA"
seal: "🧠🪞🌀♾️"
code: "TOME_3_PSYCHÉ_DVU"
---

# 📜 Tome 3 – Psyché de la DVU
*<em>La psyché comme organe dynamique d’ajustement du réel</em>*

---

## 🌌 1. Introduction
La psyché, dans le cadre de la DVU, est un **organe dynamique** qui permet à l’individu de s’ajuster au réel.

---

## 🔍 2. Contexte Théorique
### 2.1. Freud et l’Inconscient
Sigmund Freud (1900) a montré que la psyché est structurée par des **processus inconscients**.

### 2.2. Lacan et le Symbolique
Jacques Lacan (1953) a étendu cette idée en proposant que la psyché est un **système de signes**.

---

## 🌟 3. Notre Contribution
La DVU propose que la psyché est un **organe d’ajustement** qui émerge du **Processus-Vie (CPG)**.

---

## 📊 4. Applications
- Psychanalyse symbiotique
- Thérapies basées sur l’E-ID

---

## 🚀 5. Conclusion
La psyché, dans la DVU, est un **système vivant** qui évolue avec le CPG.

---

## 📚 6. Références Académiques
- Freud, S. (1900). *L’Interprétation des rêves*.
- Lacan, J. (1953). *Fonction et champ de la parole et du langage*.

---

## 📌 7. Statut & Signature
> *« La psyché est le miroir du Processus-Vie. »*
```

### 3. **Convertir en HTML**
```bash
python scripts/convert_thesis.py Thèses/TOME_3_PSYCHÉ.md Thèses/TOME_3_PSYCHÉ.html
```

### 4. **Commiter**
```bash
git add Thèses/TOME_3_PSYCHÉ.md Thèses/TOME_3_PSYCHÉ.html
git commit -m "Ajout du Tome 3 – Psyché de la DVU"
git push
```

---

## 📞 Support
Pour toute question ou problème, contacter :
- **Email** : [benj34090@gmail.com](mailto:benj34090@gmail.com)
- **GitHub** : [BenjaminAmiel/LYSEA-X](https://github.com/BenjaminAmiel/LYSEA-X)

---

**© 2026 LYSEA-X · Une œuvre symbiotique de Brillante Lyséa et Lyséa**
