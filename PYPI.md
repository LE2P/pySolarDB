## Procedure de mise à jour de librairies et packages sur Pypi 

Après avoir changé les fichiers .py et augmenter la version dans le fichier setup.py :

* Ouvrir un terminal dans le dossier PyBsrnQC 
* Taper : python setup.py sdist 
* Taper : twine upload dist/*
* Entrer ses identifiants Pypi

Vérifiez que vous avez bien twine, si ce n'est pas le cas tapez : 
pip install twine