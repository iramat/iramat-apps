---
title: "NDame"
description: "My NDame collection"
summary: "Lorem Ipsum"
date: 2023-09-07T16:12:03+02:00
lastmod: 2023-09-07T16:12:03+02:00
draft: false
weight: 999
toc: false
params:
  fullwidth: true
  seo:
    title: "" # custom title (optional)
    description: "" # custom description (recommended)
    canonical: "" # custom canonical URL (optional)
    robots: "" # custom robot tags (optional)
  section:
    title: "Documentation"
    iconName: "book"
    startUrl: "/docs/guides/example-guide/"
---

Ce graphe interactif (zoomable, avec des liens hypertextes dans les titres des jeux de données) présente le dépôt [**Alliages ferreux à Notre-Dame de Paris** exposé sur le dépôt de confiance `recherche.gouv.fr`](https://entrepot.recherche.data.gouv.fr/dataverse/ndame_GTMetal_fer) produit dans le carde de l'ERC NDame, en se servant de la *Dataverse Search API*[^1]. 

Les noeuds du graphe sont: 

1. les auteurs;
2. les mots-clefs;
3. les titres simplifiés (c.-à-d. les échantillons eux-mêmes, avec des liens hypertextes); 
4. les parties architecturales auxquelles appartiennent ces échantillons;

<!-- <p align="center"> -->
<div class="wide-frame">
  <iframe
    src="https://iramat-apps.cnrs.fr/portal/html/lod/ndame/ndame_GTMetal_fer_4mode_network.html"
    width="100%"
    height="1000"
    style="border:none;">
  </iframe>
</div>
<!-- </p> -->

[^1]: La *Dataverse Search API* permet de récupérer les métdonnées des dépôts en utilisant, par exemple, un script Python ([ici](https://github.com/iramat/iramat-functions/blob/main/ndame/recherche-data-gouv-4mode.py))