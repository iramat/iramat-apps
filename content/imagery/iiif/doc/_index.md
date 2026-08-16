---
title: "Documentation IIIF"
description: "My IIIF collection"
summary: ""
date: 2023-09-07T16:12:03+02:00
lastmod: 2023-09-07T16:12:03+02:00
draft: false
weight: 999
toc: true
layout: docs
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

# Documentation IIIF

Le IIIF (_International Image Interoperability Framework_) est un standard ouvert largement intéropérable pour la publication d’images, et l'annotation de régions d'images, haute résolution (HR) sur le web. Il permet une visualisation interactive et collaborative d’images[^1].

## Fonctionnalités clés

Ces solutions sont utilisées par l'IRAMAT: zoom profond[^2], métadonnées[^4] et annotations[^3]. Les images IIIF peuvent aussi être réunies en séquences et collections ([exemples](../examples/)).

<table>
  <tr>
    <td><b>Zoom profond</b></td>
    <td><b>Métadonnées</b></td>
  </tr>
  <tr>
    <td>Visualisation avec un zoom profond et navigation fluide dans des images haute résolution.</td>
    <td>Les métadonnées des images (auteurs, licence, etc.) sont enregistrées dans le <em>manifest</em> JSON</td>
  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <iframe
        src="https://iramat-apps.cnrs.fr/view/_test/barre531ober-deepzoom_landing_ex.html"
        width="100%"
        height="540"
        style="border:none;">
      </iframe>
      <br> Zoom profond dans une métallographie d'une <em>currency-bar</em> (barre de fer) gauloise après attaque Öberhoffer.
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <iframe
        src="https://iramat-apps.cnrs.fr/view/numismatic/1986.416_landing_attribution.html"
        width="100%"
        height="540"
        style="border:none;">
      </iframe>
      <br> Métadonnées d'attibution d'un <em>dirham</em> conservé à la Bibliothèque Nationale de France (BnF).
    </td>
  </tr>
  <tr>
    <td><b>Annotations</b></td>
    <td><b>XXXX</b></td>
  </tr>
  <tr>
    <td>Annotation de régions de l'image qui peuvent être partagées indépendamment sans perte du contexte (l'image entière)</td>
    <td></td>
  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;"> 
          <iframe
            src="https://iramat-apps.cnrs.fr/view/acies/seax_sample_process.html"
            width="100%"
            height="540"
            style="border:none;">
          </iframe>
         <br> Annotations IIIF sur une scramasaxe du 6<sup>e</sup> s. CE, trouvée dans une inhumation (Alsace, France)
    </td>
    <td></td>
  </tr>
</table>

[^1]: Exemples de cas d’usage: collections culturelles et scientifiques éparpillées, caractérisation de métallographies, etc.
[^2]: source: <https://iramat-apps.cnrs.fr/view/_test/barre531ober-deepzoom_landing_ex.html>
[^3]: source: <https://iramat-apps.cnrs.fr/view/acies/seax_sample_process.html>
[^4]: source: <https://iramat-apps.cnrs.fr/view/numismatic/1986.416_landing_attribution.html>



## Documentation externe

### Introduction au IIIF

<body>
  <table>
    <tr>
      <th>auteur</th>
      <th>document</th>
    </tr>
    <tr>
      <td>Biblissima</td>
      <td><a href="https://projet.biblissima.fr/sites/default/files/atelier_iiif_dhnord_robineau_20201118.pdf" target="_blank">Adopter et utiliser les standards IIIF pour vos corpus d'images numériques</a></td>
    </tr>
    <tr>
      <td>INHA</td>
      <td><a href="https://devisu.inha.fr/docannexe/file/274/medici2024_atelieriiif_01.07_compressed_1.pdf" target="_blank">L’utilisation du protocole IIIF dans un cadre éditorial</a></td>
    </tr>
    <tr>
      <td>BnF</td>
      <td><a href="https://docs.google.com/presentation/d/1-v_tSVFFh2zpFf6oZ32ERe2vWMPOo8xH/edit?slide=id.p1#slide=id.p1" target="_blank">IIIF@BnF Bilan, perspectives</a></td>
    </tr>
  </table>
</body>