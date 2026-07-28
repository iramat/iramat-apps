---
title: "Documentation RTI"
description: "My RTI collection"
summary: ""
date: 2023-09-07T16:12:03+02:00
lastmod: 2023-09-07T16:12:03+02:00
draft: false
weight: 999
layout: docs
toc: true
params:
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

# Documentation RTI

RTI (_Reflectance Transformation Imaging_) est une technique d’imagerie numérique qui permet de capturer et d’analyser les détails de surface d’objets en 2.5D. La RTI utilise les propriétés de réflectance de toutes surfaces pour améliorer la perception de sa forme. La lumière à angle faible et multidirectionnelle crée des détails de texture et met en valeur les irrégularités planes[^2]. Elle est largement utilisée en archéologie[^1].

## Fonctionnalités clés

Ces solutions sont développées, ou utilisées, par l'IRAMAT.

<table>
  <tr>
    <td><b>Capture</b></td>
    <td><b>Visualisation</b></td>
  </tr>
  <tr>
    <td>Utilise une série de photos sous différents éclairages pour générer une image interactive</td>
    <td>Permet d’ajuster virtuellement la lumière pour étudier les textures et les détails de surface </td>
  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;">{{< simple-img src="img/RTI_v1_animation_20260415_72pp_0-15s_50perc.gif" alt="Hazor" width="400" >}} <br> Acquisition avec le système <a href="https://hasorimaging.com/">HASOR</a></td>
    <td style="text-align: center; vertical-align: middle;">  <iframe
    src="https://iramat-apps.cnrs.fr/portal/openlime/dist/examples/rti-viewer/rti-viewer.html"
    width="100%"
    height="540"
    style="border:none;">
  </iframe><br> Visualisation avec le visualiseur web <em>open source</em> <a href="https://github.com/cnr-isti-vclab/openlime/tree/main">OpenLIME</a></td>
  </tr>
</table>

## Développement

Le visualisateur web [OpenLIME](https://github.com/cnr-isti-vclab/openlime/tree/main) offre de nombreuses fonctionnalités qui font l’objet d’une [Discussion](https://github.com/orgs/iramat/discussions/52) au sein de l’IRAMAT.

[^1]: Exemples de cas d’usage: analyse d’inscriptions ou de gravures, tracéologie (_use-wear analysis_), etc.
[^2]: M'Darhri, A. A., Baillet, V., Bourineau, B., Calantropio, A., Carpentiero, G., Chayani, M., de Luca, L., Dudek, I., Dutailly, B., Gautier, H., & al. (2019). _Share-Publish-Store-Preserve. Methodologies, Tools and Challenges for 3D Use in Social Sciences and Humanities_. in "Share—Publish—Store—Preserve. Methodologies, Tools and Challenges for 3D Use in Social Sciences and Humanities".
