# 📝 Guide d'édition du site - Pour Stéphanie

Bienvenue ! Ce guide vous explique comment modifier facilement le contenu de votre site.

## 🗂️ Organisation des fichiers

```
📁 Votre site
├── 📄 index.md                 → Page d'accueil
├── 📄 cv.md                    → Votre CV
├── 📁 _expositions/            → Vos expositions
│   ├── huisclos.md
│   ├── paradise.md
│   └── ...
├── 📁 _residences/             → Vos résidences
│   ├── maroc.md
│   ├── inde.md
│   └── ...
└── 📁 _photos/                 → Vos séries photo
    ├── confinement.md
    └── ...
```

## ✏️ Comment modifier un fichier

### 1. Ouvrir le fichier

- Utilisez un éditeur de texte simple comme **TextEdit** (Mac) ou **Notepad** (Windows)
- Ou mieux : téléchargez [**Typora**](https://typora.io) (éditeur Markdown gratuit et visuel)

### 2. Structure d'un fichier

Chaque fichier commence par un **en-tête** entre `---` :

```markdown
---
layout: project
title: Titre de votre projet
subtitle: Résidence
main_image: /images/maroc_main.avif
---

Ici commence votre texte...
```

⚠️ **NE PAS TOUCHER** aux lignes entre les `---` (sauf les titres)

### 3. Écrire du texte

Après le deuxième `---`, écrivez simplement votre texte comme dans Word :

```markdown
Ceci est un paragraphe normal.

Ceci est un autre paragraphe (une ligne vide entre les deux).
```

## 🎨 Mise en forme simple

### Titres

```markdown
## Grand titre
### Titre moyen
#### Petit titre
```

### Gras et italique

```markdown
**Ce texte est en gras**
*Ce texte est en italique*
```

### Listes

```markdown
- Premier élément
- Deuxième élément
- Troisième élément
```

### Liens

```markdown
[Texte cliquable](https://www.example.com)
```

### Images

```liquid
{% include image.html path="/images/inde_1.avif" alt="Deux personnes allument des lampes à huile" %}
```

## 📷 Ajouter des images

1. Placez une version AVIF ou WebP dans `images/`, avec un nom simple et une largeur maximale de 1 600 px.
2. Renseignez sa largeur et sa hauteur réelles dans `_data/images.yml`. Si plusieurs tailles existent, ajoutez leurs chemins et largeurs dans `srcset`.
3. Utilisez l’include ci-dessus dans le texte avec une description adaptée à la langue. Pour l’image principale d’un projet, indiquez le chemin dans `main_image` et le texte alternatif dans `main_image_alt`.
4. Dans `image.path`, indiquez la version JPG destinée au partage et renseignez ses propres dimensions dans `image.width` et `image.height`.
5. Lancez `python3 _scripts/og_images.py` : il prépare la vignette de partage (1200 × 630) utilisée par Facebook, Instagram et les messageries. Sans elle, l’image JPG est partagée telle quelle.
6. Pour une exposition, si le lieu indiqué dans `schema.events` (champ `location`) est nouveau, ajoutez sa commune et son pays dans `_data/lieux.yml`.

Voici l’entrée de l’image utilisée dans l’exemple.

```yaml
/images/inde_1.avif:
  width: 568
  height: 382
```

## 📄 Exemples pratiques

### Modifier un projet existant

**Fichier : `_residences/maroc.md`**

```markdown
---
layout: project
title: Maroc
subtitle: Résidence
main_image: /images/maroc_main.avif
---

Voici le texte de ma résidence au Maroc...

Je peux ajouter des paragraphes facilement.

### Un sous-titre

Et continuer à écrire.

![Une belle photo](images/maroc_main.avif)
```

### Ajouter un nouveau projet

1. **Copiez** un fichier existant (par exemple `maroc.md`)
2. **Renommez-le** : `tunisie.md`
3. **Modifiez** le contenu :

```markdown
---
layout: project
title: Tunisie
subtitle: Résidence 2026
main_image: images/tunisie.jpg
---

Description de ma résidence en Tunisie...
```

4. **Sauvegardez** le fichier dans le bon dossier (`_residences/`)

## 🚀 Publier les modifications

Une fois vos modifications faites :

1. **Sauvegardez** vos fichiers
2. **Demandez** à quelqu'un de pousser les changements sur GitHub
3. Le site se met à jour automatiquement ! ✨

## 💡 Conseils

- ✅ **Gardez les choses simples** : pas besoin de HTML
- ✅ **Une ligne vide** = nouveau paragraphe
- ✅ **Sauvegardez souvent**
- ❌ **Ne touchez pas** aux lignes entre `---`
- ❌ **N'utilisez pas** les caractères spéciaux `* # < >` au début d'une ligne

## 🆘 Aide rapide

| Je veux...              | J'écris...                          |
| ----------------------- | ----------------------------------- |
| Un titre                | `## Mon titre`                      |
| Du texte en gras        | `**mon texte**`                     |
| Une liste               | `- Point 1`<br>`- Point 2`          |
| Un lien                 | `[clic ici](https://...)`           |
| Une image               | `![description](images/inde_1.avif)`  |
| Un nouveau paragraphe   | (une ligne vide)                    |

## 📞 Questions ?

En cas de doute, demandez de l'aide ! Le plus important est de ne pas avoir peur de modifier les fichiers - on peut toujours revenir en arrière. 😊

---

**Bonne édition ! 🎨**
