# Site de Stéphanie Pommeret

Site web de Stéphanie Pommeret - Plasticienne / Poétesse / Photographe

## 🚀 Jekyll

Ce site utilise Jekyll, un générateur de sites statiques compatible avec GitHub Pages.

### Installation locale

```bash
# Installer les dépendances
bundle install

# Lancer le serveur de développement
bundle exec jekyll serve

# Ouvrir http://localhost:4000
```

### Structure du site

```
.
├── _config.yml          # Configuration Jekyll
├── _layouts/            # Templates HTML
│   ├── default.html     # Layout de base
│   ├── page.html        # Layout pour les pages
│   └── project.html     # Layout pour les projets
├── _includes/           # Composants réutilisables
│   ├── header.html
│   ├── navigation.html
│   └── footer.html
├── _expositions/        # Collection des expositions
├── _residences/         # Collection des résidences
├── _photos/             # Collection des séries photo
├── assets/              # Fichiers statiques (CSS, JS)
│   ├── css/
│   └── js/
├── images/              # Images du site
├── index.md             # Page d'accueil
└── cv.md                # Page CV
```

### Modifier le contenu

Les pages sont maintenant en **Markdown** (.md) pour faciliter les modifications :

- **Pages principales** : `index.md`, `cv.md`
- **Expositions** : dans le dossier `_expositions/`
- **Résidences** : dans le dossier `_residences/`
- **Séries photo** : dans le dossier `_photos/`

#### Format des fichiers Markdown

Chaque fichier commence par un "front matter" YAML :

```yaml
---
layout: project
title: Titre du projet
subtitle: Sous-titre
main_image: images/projet.jpg
---

Contenu en Markdown...
```

### Déploiement

Le site est automatiquement déployé sur GitHub Pages à chaque push sur la branche `main`.

## 📝 Scripts utiles

- `find_duplicate_images.py` : Détecte les images en doublon
- `cleanup_duplicates.py` : Nettoie les doublons automatiquement
- `optimize_images.py` : Optimise les images (WebP, compression)
- `convert_html_to_md.py` : Convertit les HTML en Markdown

## 🌐 URL

Site web : https://www.stephaniepommeret.com
