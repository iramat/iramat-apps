---
title: "iiif-loader"
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

Ce webservice est accessible ici: <https://iramat-apps.cnrs.fr/iiif-loader/> 

Le webservice `iiif-loader` permet de mettre des images en IIIF. Il ingère des images statiques (.JPG, .TIFF, etc.) et génère automatiquement leur _manifest_ et _viewer_ IIIF[^1]. Les métadonnées des images sont lues à la volée lors de leur importet restituées dans leur _manifest_ et _viewer_ IIIF[^2]. Les images, leur _manifest_ et _viewer_ IIIF sont stockées dans différents `dossiers-projets`[^3]. 


[^1]: API présentation 
[^2]: voir la documentation sur les [métadonnées des images](https://iramat.github.io/iramat-apps/iiif/doc/metadata)
[^3]: voir la documentation sur la [structuration des données](https://iramat.github.io/iramat-apps/docs/structure/structuration/)