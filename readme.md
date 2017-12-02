# This is an introductory course to Python covering the following notions

## How to start?

* starting both the presentation and the notebook server:

  From the root directory, run `./launchme.sh` from the command line (under Ubuntu a terminal can be started using <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>T</kbd>).

* starting only the presentation:

  from the reveal.js directory, run `grunt serve` from the command line (or `npm start` if you plan to make changes)

* starting the notebook server

  from the notebook directory, run `jupyter notebook`

## What do we cover?

1. Introduction au langage python

	* Notion de variables dynamiques, initialisation, portée d’une  
variable, affectation, opérateurs

	* Chaînes de caractères, conversion de type, les booléens.

	* Listes : affectation et copie, les dictionnaires.

	* Structures de contrôle : branchements, boucles, itérateurs et générateurs.

	* Fonctions et librairies classiques. Arguments d’une fonction.  
Passage de paramètres par nom.

	* Passage d’une fonction comme paramètre, fonctions lambda.

	* Les modules math et random.

	* Entrées / sorties sur fichiers ASCII et binaires. Formatage des sorties.

2. La programmation objet

	* Intérêt, concept de classe, apport de l’approche objet

	* Constructeur, destructeurs, méthodes magiques

	* Surcharge d’opérateurs

	* Gestion des exceptions.

## What did we use

* persistent Ubuntu USB keys were prepared with [mkusb](https://help.ubuntu.com/community/mkusb/persistent)

* versioning of the presentation and the notebooks was made possible through git and github

* the presentation is based on the [reveal.js](https://github.com/hakimel/reveal.js/) html/javascript presentation module

* python has been served by [Anaconda inc.](https://www.anaconda.com) through a [miniconda](https://conda.io/miniconda.html) installation with the packages numpy, scipy, matplotlib, seaborn, bokeh, pandas, jupyter

## Setting up your environment

If you'd like to have a similar installation on another computer

* using conda and its packages, install [miniconda](https://conda.io/miniconda.html), then from a terminal

	```shell
	conda install numpy scipy matplotlib seaborn bokeh pandas jupyter ipywidgets
	jupyter nbextension enable --py --sys-prefix widgetsnbextension
	```

* setting up [reveal.js](https://github.com/hakimel/reveal.js/) on a `deb`-based linux:

  * install `git` through apt

  * install the packages `nodejs`, `nodejs-legacy` through `apt`

  * `git clone https://github.com/hakimel/reveal.js.git`

  * `cd` into the `reveal.js` directory and run `npm install` from the command line
