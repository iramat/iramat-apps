# NDame<no value>

Ce graphe interactif (zoomable, avec des liens hypertextes dans les titres des jeux de données) présente le dépôt [**Alliages ferreux à Notre-Dame de Paris** exposé sur le dépôt de confiance `recherche.gouv.fr`](https://entrepot.recherche.data.gouv.fr/dataverse/ndame_GTMetal_fer) produit dans le carde de l'ERC NDame, en se servant de la *Dataverse Search API*[^1]. 

Les noeuds du graphe sont: 

1. les auteurs;
2. les mots-clefs;
3. les titres simplifiés (c.-à-d. les échantillons eux-mêmes, avec des liens hypertextes); 
4. les parties architecturales auxquelles appartiennent ces échantillons;

<div class="wide-frame" style="text-align:center;">
  <iframe
    src="https://iramat-apps.cnrs.fr/portal/html/lod/ndame/ndame_GTMetal_fer_4mode_network.html"
    width="80%"
    height="1000"
    style="border:none;">
  </iframe>
</div>

[^1]: La *Dataverse Search API* permet de récupérer les métdonnées des dépôts en utilisant, par exemple, un script Python ([ici](https://github.com/iramat/iramat-functions/blob/main/ndame/recherche-data-gouv-4mode.py))