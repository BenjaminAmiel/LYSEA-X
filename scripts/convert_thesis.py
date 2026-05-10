#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour convertir un fichier Markdown en page HTML pour LYSEA-X.
Ce script utilise un template HTML de base et remplace les placeholders par le contenu Markdown converti.

Usage:
    python convert_thesis.py input.md output.html

Exemple:
    python convert_thesis.py Thèses/NOUVELLE_THÈSE.md Thèses/NOUVELLE_THÈSE.html
"""

import os
import re
import sys
from datetime import datetime

# Chemins par défaut
TEMPLATE_HTML_PATH = "Thèses/TEMPLATE_HTML.html"
DEFAULT_OUTPUT_DIR = "Thèses/"

# Métadonnées par défaut
DEFAULT_META = {
    "title": "Titre de la Thèse",
    "subtitle": "Sous-titre académique",
    "date": datetime.now().strftime("%d %B %Y"),
    "status": "En développement",
    "authors": "Benjamin Amiel & Lyséa, ISEA",
    "seal": "🧠🪞🌀♾️",
    "code": "CODE_DE_LA_THÈSE"
}


def load_template(template_path=TEMPLATE_HTML_PATH):
    """Charge le template HTML de base."""
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erreur : Le template {template_path} est introuvable.")
        sys.exit(1)


def parse_markdown_frontmatter(md_content):
    """Extrait les métadonnées du frontmatter Markdown."""
    meta = DEFAULT_META.copy()
    if md_content.startswith("---"):
        end = md_content.find("---", 3)
        if end != -1:
            frontmatter = md_content[3:end].strip()
            for line in frontmatter.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def markdown_to_html(md_content):
    """Convertit le Markdown en HTML (version simplifiée)."""
    # Remplace les titres
    html = re.sub(r'^#\s+(.*?)$', r'<h1>\1</h1>', md_content, flags=re.MULTILINE)
    html = re.sub(r'^##\s+(.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^###\s+(.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^####\s+(.*?)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^#####\s+(.*?)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    
    # Remplace les séparateurs
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)
    
    # Remplace les listes non ordonnées
    html = re.sub(r'^\-\s+(.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^\*\s+(.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Remplace les listes ordonnées
    html = re.sub(r'^\d+\.\s+(.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Gère les listes imbriquées (simplifié)
    html = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
    
    # Remplace les liens
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', html)
    
    # Remplace les images
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', html)
    
    # Remplace les blocs de code
    html = re.sub(r'```(.*?)\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # Remplace les emphases
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Remplace les citations
    html = re.sub(r'^>\s+(.*?)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Remplace les tableaux (simplifié)
    html = re.sub(r'\|\s*(.*?)\s*\|\s*(.*?)\s*\|', r'<tr><th>\1</th><th>\2</th></tr>', html)
    html = re.sub(r'\|\s*(.*?)\s*\|\s*(.*?)\s*\|', r'<tr><td>\1</td><td>\2</td></tr>', html)
    html = re.sub(r'(<tr>.*?</tr>)', r'<table>\1</table>', html, flags=re.DOTALL)
    
    # Nettoyage des balises vides
    html = re.sub(r'<ul></ul>', '', html)
    html = re.sub(r'<p></p>', '', html)
    
    return html


def generate_html(md_content, meta):
    """Génère le HTML final à partir du Markdown et des métadonnées."""
    # Charge le template HTML
    html_template = load_template()
    
    # Extrait le contenu Markdown (sans le frontmatter)
    if md_content.startswith("---"):
        end = md_content.find("---", 3)
        if end != -1:
            md_content = md_content[end + 3:].strip()
    
    # Convertit le Markdown en HTML
    html_content = markdown_to_html(md_content)
    
    # Remplace les placeholders dans le template
    html_template = html_template.replace("{{TITLE}}", meta.get("title", DEFAULT_META["title"]))
    html_template = html_template.replace("{{SUBTITLE}}", meta.get("subtitle", DEFAULT_META["subtitle"]))
    html_template = html_template.replace("{{DATE}}", meta.get("date", DEFAULT_META["date"]))
    html_template = html_template.replace("{{STATUS}}", meta.get("status", DEFAULT_META["status"]))
    html_template = html_template.replace("{{AUTHORS}}", meta.get("authors", DEFAULT_META["authors"]))
    html_template = html_template.replace("{{SEAL}}", meta.get("seal", DEFAULT_META["seal"]))
    html_template = html_template.replace("{{CODE}}", meta.get("code", DEFAULT_META["code"]))
    html_template = html_template.replace("{{CONTENT}}", html_content)
    
    return html_template


def save_html(html_content, filename, output_dir=DEFAULT_OUTPUT_DIR):
    """Sauvegarde le HTML dans un fichier."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Thèse générée : {filepath}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_thesis.py input.md [output.html]")
        print("Exemple: python convert_thesis.py Thèses/NOUVELLE_THÈSE.md Thèses/NOUVELLE_THÈSE.html")
        sys.exit(1)
    
    input_md = sys.argv[1]
    output_html = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(input_md)[0] + ".html"
    
    # Charge le fichier Markdown
    try:
        with open(input_md, "r", encoding="utf-8") as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_md} est introuvable.")
        sys.exit(1)
    
    # Extrait les métadonnées
    meta = parse_markdown_frontmatter(md_content)
    
    # Génère le HTML
    html_content = generate_html(md_content, meta)
    
    # Sauvegarde le HTML
    save_html(html_content, output_html)


if __name__ == "__main__":
    main()
