# rti-loader<no value>

Ce webservice est accessible ici: <https://iramat-apps.cnrs.fr/rti-loader/> 

Le webservice `rti-loader` permet de mettre en ligne des fichiers RTI. Il prend en entrée des fichiers RTI optimisés pour le web (`plane_0.jpg`, `plane_1.jpg`, `plane_2.jpg`, etc. et `info.json`[^1]

- Les [métadonnées des images](https://iramat.github.io/iramat-apps/lod/metadata/images/) sont à rentrer dans l'image `plane_0.jpg` (image photographique standard).
- Les images avec leur visualiseur RTI seront stockées sur le serveur de l'IRAMAT (voir [structuration des images](https://iramat.github.io/iramat-apps/docs/structure/structuration/#images))

[^1]: En l'état, ce webservice prend en entrée les fichiers issus du système [HASOR](https://hasorimaging.com/): `plane_0.jpg`, `plane_1.jpg`, `plane_2.jpg`, , `plane_3.jpg` et `info.json`.