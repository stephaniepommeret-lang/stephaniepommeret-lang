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
main_image: images/maroc_main.jpg
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

```markdown
![Description de l'image](images/inde_1.jpg)
```

## 📷 Ajouter des images

1. **Placez votre image** dans le dossier `images/`
2. **Nommez-la simplement** : `maroc_1.jpg` (pas d'espaces, pas d'accents)
3. **Ajoutez-la dans votre texte** :

```markdown
![Mon atelier au Maroc](images/maroc_1.jpg)
```

## 📄 Exemples pratiques

### Modifier un projet existant

**Fichier : `_residences/maroc.md`**

```markdown
---
layout: project
title: Maroc
subtitle: Résidence
main_image: images/maroc_main.jpg
---

Voici le texte de ma résidence au Maroc...

Je peux ajouter des paragraphes facilement.

### Un sous-titre

Et continuer à écrire.

![Une belle photo](images/maroc_1.jpg)
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
| Une image               | `![description](images/inde_1.jpg)`  |
| Un nouveau paragraphe   | (une ligne vide)                    |

## 📞 Questions ?

En cas de doute, demandez de l'aide ! Le plus important est de ne pas avoir peur de modifier les fichiers - on peut toujours revenir en arrière. 😊

---

**Bonne édition ! 🎨**
