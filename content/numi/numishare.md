---
title: "Numishare"
description: "My IIIF collection"
summary: "Lorem Ipsum"
layout: docs
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

## Numishare

_Numishare_ est un système _open source_ de gestion de collections numismatiques (<a href="https://github.com/ewg118/numishare/" target="_blank">code source</a>, <a href="https://github.com/ewg118/numishare/wiki" target="_blank">wiki</a>), développé et maintenu par l'_American Numismatic Society_ (ANS) et plus particulièrement <a href="https://github.com/ewg118" target="_blank">Ethan Gruber</a>. Conçu pour le Web sémantique, _Numishare_ repose principalement sur les technologies suivantes :

- l'utilisation du XML[^3], tant pour pour le stockage des notices numismatiques au format NUDS[^1] que pour la configuration de l'application ;
- Les fichiers XSLT[^2] pour un flux d'échange : XML (notices numismatiques + configuration) ↔ HTML(expérience utilisateur)
- les technologies d'interrogation et d'échange de données XML, notamment XQuery et les API REST ;
- l'adoption du standard NUDS ainsi que du thésaurus et de l'ontologie <a href="https://nomisma.org/" target="_blank">Nomisma</a> ;
- la publication native de données au moyen de points d'accès SPARQL et d'API REST.

_Numishare_ est aujourd'hui largement adopté par la communauté de la recherche en numismatique antique et médiévale (voir la <a href="https://numismatics.org/resources/" target="_blank">liste des projets utilisant _Numishare_</a>). 

### À l'IRAMAT

Utilisée dans le(s) projet(s):

* <img src="https://raw.githubusercontent.com/iramat/almacir/master/img/logo.png" style="height: 30px;vertical-align: middle;"><a href="https://iramat.github.io/almacir/ " target="_blank"> ALMACIR</a>

### Demo

Une version de démonstration est accessible ici: <https://iramat-apps.cnrs.fr/numishare/demo/>

<center>

<img src="https://raw.githubusercontent.com/iramat/iramat-dev/main/img/bdd-numishare-demo.png" style="width:700px;vertical-align:middle">

</center>

[^3]: _Extensible Markup Language_, la principale extension du HTML
[^1]: _NUmismatic Description Standard_ ou _Numismatic Database Standard_: c'est l'ensemble de noms de champs suggérés pour l'enregistrement d'informations numismatiques dans une BDD.
[^2]: _Extensible Styles Language Transform_, pour transformer des fichiers XML en HTML, HTML table, PDF, etc. 