# Pile logicielle<no value>

Les applications informatiques de l'Iramat (<https://iramat-apps.cnrs.fr/>) décrites sur ce site web sont hebergées sur un [serveur web](#serveur). L'utilisation de [GitHub](#github) permet de développer un écosystème _user-friendly_ autour des données et l'entrepôt [Zenodo](#zenodo) de publier des dépôts de données facilement citables et réutilisables


## Serveur

Le serveur web[^1] est une instance Ubuntu 22.04 LTS hébergée au [Mésocentre](https://mesocentre.universite-paris-saclay.fr/) de l'Université Paris-Saclay, tutelle secondaire du LAPA-IRAMAT.

### Bases de données

Le serveur web héberge différentes Base de données (BDD) :

- un système de gestion de base de données (SGBD) PostgreSQL/Postgis v17.5.

  - **CHIPS** pour le stockage et le partage de données chimiques <br><p style="text-align: right;"><a href="https://iramat.github.io/chips/"><img src="https://raw.githubusercontent.com/iramat/iramat-dev/main/img/logo-chips-round.png" style="height: 30px;vertical-align: middle;"> Visitez le site web dédié</a></p>

- un SGBD Numishare v1.2.

  - **ALMACIR** pour l'étude des monnayages de l'Islam médiéval en Occident <br><p style="text-align: right;"><a href="https://iramat.github.io/almacir/"><img src="https://raw.githubusercontent.com/iramat/almacir/master/img/logo.png" style="height: 30px;vertical-align: middle;"> Visitez le site web dédié</a></p>

### Imagerie

Des _webservices_ Flask (v3.1.1) sont installés pour faciliter la transformation de l'imagerie scientifique (ex : Microscopie optique, MEB-EDS, Raman) en IIIF et pour exposer des images RTI sur un autre visualiseur interactif.

#### IIIF

Le serveur web héberge un serveur d'image Cantaloupe et un _viewer_ Mirador (CDN). 

#### RTI

Le serveur web héberge un visualiseur OpenLIME.

### GeoServer

Le serveur web héberge un GeoServer pour l'information spatiale

{{< callout context="note" title="<https://iramat.github.io/iramat-apps/geoserver/>" icon="outline/info-circle" >}}
{{< /callout >}}

## GitHub

Le site web, ainsi que des données de référence, les présentations Quarto, les discussions, etc. sont hébergées sur le GitHub de l'IRAMAT.

{{< callout context="note" title="<https://github.com/iramat>" icon="outline/info-circle" >}}
{{< /callout >}}

### Site web

Les données de ce site web, développé en Hugo, sont hébergées ici: <https://github.com/iramat/iramat-apps/tree/hugo-files/content>.

## Zenodo

L'IRAMAT dispose d'une communauté Zenodo pour le dépôt des jeux de données, données de références, et de _pre prints_.

{{< callout context="note" title="<https://zenodo.org/communities/iramat>" icon="outline/info-circle" >}}
{{< /callout >}}

[^1]: synonymes: _server_, _Virtual Machine_, VM, machine virtuelle