# Métadonnées des images<no value>

Les métadonnées (_metadata_) des images sont autant utiles autant pour le IIIF que pour le RTI.

## Liste des métadonnées

La liste des métadonnées XMP et des métadonnées IPTC étendues à l'XMP[^1] lues par les webservices [`iiif-loader`](https://iramat.github.io/iramat-apps/iiif/webservices/iiif-loader/) ([IIIF](https://iramat.github.io/iramat-apps/iiif/)) et [`rti-loader`](https://iramat.github.io/iramat-apps/rti/webservices/rti-loader/) ([RTI](https://iramat.github.io/iramat-apps/rti/)), est présentée dans le tableau ci-dessous.

Pour le moment[^2], seuls les champs notés **IN** = O sont lus lors de l'import:

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