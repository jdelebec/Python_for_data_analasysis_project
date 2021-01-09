# Python_for_data_analasysis_project
Jean-louis Delebecque - Simon Hervé

Attention: pour pouvoir lancer notre projet vous devez avoir une certaine version de scikit-learn (0.22.1) ! (pip install scikit-learn==0.22.1) 

Afin d'utiliser notre application, allez dans le dossier final_project dans votre terminal, puis entrez la commande python app.py (application flask). Ensuite ouvrez un browser et entrez l'adresse qui s'affiche dans votre terminal.
Une fois dans l'application, entrez les valeurs des variables de votre molécule. Faites bien attention au nom des variables, car notre modèle prend en compte que 23 variales. Ensuite cliquez sur le bouton Entrer. Vous aurez la réponse sur votre molécule.

Attention la réponse est oui ou non et elle est toute à la fin de la page.

Voici un jeux de données (première ligne du dataset) : 3.919,0,0,	0,0,31.4,0,0,3.106,2.550,9.002,0,1.201,0,	1.932,	4.489,	0,	0,	2.949,	0,	7.253,	0,	0
Pour ces valeurs le modèle doit donner comme réponse oui.

En conclusion nous avons entrainer un modèle (basé sur l'algorithme SVM) qui determine ou non si une molécule est biodégradable. 

Pour plus d'informations techniques (accuracy et choix du modèle) veuillez regarder le rapport.pdf dans le dossier final_project.
