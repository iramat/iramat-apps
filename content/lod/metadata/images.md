---
title: "Métadonnées des images"
date: 2026-02-17T13:03:14+01:00
description: "Documentation du webservice"
draft: false
params:
  seo:
    title: "" # custom title (optional)
    description: "" # custom description (recommended)
    canonical: "" # custom canonical URL (optional)
    robots: "" # custom robot tags (optional)
---

Utiles autant pour le IIIF que pour le RTI.

## Liste des métadonnées

La liste des métadonnées XMP et des métadonnées IPTC étendues à l'XMP[^1] lues par le webservice [`iiif-loader`](http://localhost:1313/iiif/webservices/iiif-loader/), et bientôt par le webservice `rti-loader`, est présentée dans le tableau ci-dessous. 

Pour le moment, seuls les champs notés **IN** = O sont lus lors de l'import[^2]:

{{< tsvtable2 "data/metadata.tsv" >}}

<center>

voir [code source](https://github.com/iramat/iramat-apps/blob/hugo-files/static/data/metadata.tsv) du tableau

</center>

## Édition des métadonnées

Création et édition des métadonnées. 

### Exemple de création de métadonnées

Dans l'exemple ci-dessous, l'édition des métadonnées de l'image est faite dans le logiciel [XnView](https://www.xnview.com/en/):

##### onglet `Description`

- Document title
- Author
- Description
- Copyright Notice

<img width="700" alt="Image" src="https://github.com/user-attachments/assets/c46a21be-014c-47f3-99ed-d0f53343b556" />

#### onglet `Origin`

- Source

<img width="700" alt="Image" src="https://github.com/user-attachments/assets/af3309da-861d-45be-af6c-7cd5b6173c4c" />

[^1]: `Iptc4xmpExt`
[^2]: La liste complète des métadonnées, et plus spécifiquement des métadonnées des images, fait l'objet d'une [Discussion](https://github.com/orgs/iramat/discussions/51) au sein de l'IRAMAT