# Python_Kivi_MP3

### Résumé

Python_Kivi_MP3 est un programme qui recueille un fichier audio via une interface graphique, le traduit en texte, génère des clés de cryptage, encrypte le texte et met le texte crypté dans un fichier texte. L'ensemble des informations de texte, de cryptage et de décryptage se font directement via l'interface graphique

### Installation préalable

Nous partons du principe que Python est installer sur votre odinateur est fonctionnel.
En utilisant le temrminal installer les biblithèques suivant via la commande :

```
pip install nomDeLaLibrairie
ou
python -m pip install nomDeLaLibrairie
```

Librairie a installer :

- cryptography
- pydub
- base64
- tkinter
- speech_recognition

### Utilisation

- Ouvrez votre terminal, déplacez vous jusqu'a la racine du dossier les fichier sont installés via la commande :
```
cd cheminDuDossier
```
- Demarrer le programme via votre terminal en entrant la commande suivante : 

```
python .\app.py
```

- L'interface graphique vas s'ouvrir, cliquer alors sur le bouttons "Parcourir" et charger le fichier Rue_Maurice_Carraz_2.waw situé a la racine du projet

- Cliquez sur le bouton "Crypter" pour crypter le message et l'afficher dans votre console lorsqu'il est crytpé ; cliquez sur le bouton décrypter pour l'afficher votre console lorsqu'il est décripter.

### Erreur de fonctionnement

Le fichier peut être crypté mais ne s'affiche pas en décriptage car la valeur d'variable global n'arrive pas a être affecté et créer une erreur

La convertion du fichier MP3 en Wav n'est pas fonctionnel mais le code est le suivant :

```
from os import path
from pydub import AudioSegment

# files                                                                         
src = "nomDuFichier.mp3"
dst = "nomDuFichier.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
```