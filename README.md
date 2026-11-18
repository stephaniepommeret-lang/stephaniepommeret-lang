# Site de Stéphanie Pommeret

Site web de Stéphanie Pommeret - Plasticienne / Poétesse / Photographe

## 🚀 Jekyll

Ce site utilise Jekyll, un générateur de sites statiques compatible avec GitHub Pages.

### Installation locale

Ruby 3.1 ou plus récent (le déploiement utilise Ruby 3.4).

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
├── _sass/site.scss      # Feuille de style (intégrée dans chaque page au build)
├── _data/               # Dimensions des images, diplômes, lieux d'exposition
├── _scripts/            # Contrôle du site généré, vignettes de partage
├── assets/              # Polices, scripts, Swiper
│   ├── fonts/
│   ├── js/
│   └── swiper/
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
Le workflow construit le site puis vérifie les ressources générées :

```bash
JEKYLL_ENV=production bundle exec jekyll build
python3 _scripts/verify_assets.py _site
```

Sécurité : la page déclare une Content-Security-Policy (dans `_layouts/default.html`).
Tout est servi par le site ; une page qui intègre un contenu tiers doit le déclarer
dans son front matter (`embeds: [instagram]`). Pour vérifier les dépendances :
`gem install bundler-audit && bundle-audit check --update`.

## 📝 Scripts utiles

- `_scripts/verify_assets.py` : vérifie que toutes les ressources locales du site généré existent
- `_scripts/og_images.py` : génère les vignettes de partage 1200 × 630 (`images/og/`)
- `optimize_images.py` : Optimise les images (WebP, compression)

## 🌐 URL

Site web : https://www.stephaniepommeret.com
