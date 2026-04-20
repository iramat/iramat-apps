# Pile logicielle<no value>

Les applications de l'Iramat (Iramat-apps) décrites sur ce site web sont hebergées sur une machine virtuelle (_Virtual Machine_, VM)

## GitHub

Ce site web (Hugo), ainsi que des données de référence, les presentations Quarto, les discussions, etc. sont hébergées sur le GitHub de l'IRAMAT: <https://github.com/iramat>

## VM

Instance Ubuntu 22.04 LTS hébergée au Mésocentre de l'Université Paris-Saclay

### Bases de données

#### CHIPS

La VM héberge une système de gestion de base de données (SGBD) PostgreSQL/Postgis. Ce SGBD héberge la base de données (BDD) CHIPS, présentée dans le [site web dédié](https://iramat.github.io/chips/)

#### Instance Numishare

La VM héberge une instance Numishare (voir [documentation](https://iramat.github.io/iramat-dev/talks/2026-almacir-preparatory-meeting/pres/#/numishare))

##### Modèle conceptuel de données

Le Modèle conceptuel de données (MCD) de l'instance Numishare est le suivant:

```mermaid
flowchart TB
    Browser["🌐 Web Browser<br/>(User / Admin / API)"]
	subgraph Numishare stack
    	Tomcat["🧱 Apache Tomcat 9<br/>Port 8080"]
    	Orbeon["📄 Orbeon Forms CE<br/>Context: /orbeon"]
    	Numishare["🪙 Numishare App<br/>/orbeon/numishare"]
   		Exist["🗄️ eXist-db<br/>Port 8888<br/>NUDS / RDF / Config"]
    	Solr["🔍 Apache Solr<br/>Port 8983<br/>Core: numishare"]
    	Cantaloupe["🖼️ Cantaloupe IIIF<br/>Base: /iiif/2/"]
    	Images["💾 Image Storage<br/>/home/ubuntu/data/numishare/images"]
	end

    Browser -->|HTTP/S| Tomcat
    Tomcat --> Orbeon
    Orbeon --> Numishare
    Numishare --> Exist
    Numishare --> Solr
    Numishare --> Cantaloupe
    Cantaloupe --> Images
```

### IIIF

La VM héberge un serveur d'image Cantaloupe et un _viewer_ Mirador (CDN). Des _webservices_ sont installés pour faciliter la transformation des images à l'isostandard IIIF... [lien](https://iramat.github.io/iramat-apps/iiif/)

### GeoServer

La VM héberge un seveur de cartes GeoServer... [lien](https://iramat.github.io/iramat-apps/geoserver/)

## Zenodo

L'IRAMAT dispose d'une communauté Zenodo pour le dépôt des jeux de données, données de références, et de _pre prints_: <https://zenodo.org/communities/iramat>