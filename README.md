# Transcription (speech to text) d’échanges téléphoniques adressés au support IT d’une entreprise

Ce projet donne des ressources pour transcrire des conversations téléphoniqe ainsi que des outils pour évaluer leurs performances.

## Organisation
Notre code s'articule autour de trois modules :

* La couche d'entrée
* La couche de traduction
* La couche de sortie

<a href="url"><img src="https://github.com/cmauget/speech-to-text-benchmark/blob/main/utils/diag.png" height="383" width="325" ></a>

  
  
## Setup
Nous utilisons de nombreuses bibliothèques python ainsi que des modèles tel que :
* [Speechrabin](https://speechbrain.github.io/)
* [Sphinx](https://github.com/bambocher/pocketsphinx-python)
* [Vosk](https://alphacephei.com/vosk/)
* [Whisper](https://github.com/openai/whisper)  
  
Pour faciliter l'installation nous avons créé un environnement [conda](https://docs.conda.io/en/latest/) avec toute les dépendances. Vous pouvez trouver le fichier de configuration dans utils/environment.yaml.  

---------------------------------------
Vous pouvez changer le nom de l'environnement (wikit par défaut) en changeant le nom écrit à la première ligne. Il faudra par la suite modifié le wikit par le nom choisit.

Vous devez au sein de environment.yaml changer la dernière ligne :

    prefix: !modify !this ~/anaconda3/envs/wikit

Par le chemin d'installation de conda, ex :

    prefix: /home/user/anaconda3/envs/wikit
    
Il ne reste plus qu'a installer l'environnement avec la commande : 

    conda env create -f environment.yml  
    
 
---------------------------------------

    
Il faudra de plus télécharger les modèles necessaire pour faire tourner le code. Ils sont disponible dans ce [Drive](https://drive.google.com/drive/folders/1J2lzr-wJGA_9SSn_876XJvbMTBzvRhkX?usp=share_link)  

Il faudra alors unzip le fichier telecharger et le placer dans le repositories comme ci-dessous:
```
📂 speech-to-text-benchmark/ # this is root
├── 📂 1-input/
├── 📂 2-data/
├── 📂 3-outputs/
├── 📂 models/
├── 📂 utils/
│...
```
Il faut par la suite copier le fichier _utils/fr-FR_ au sein du dosssier :  

    ~/anaconda3/envs/wikit/lib/python3.10/site-packages/speech_recognition/pocketsphinx-data/ 
     
Pour utiliser Whisper il faut également installer ffmpeg (sous Ubuntu) :

    sudo apt update && sudo apt install ffmpeg
    
    
*Remarque : bien que nous ayons fait le maximum pour garantir un setup facile, il peut être necessaire d'installer d'autres dépendances. Nous vous invitons a regarder les erreurs d'executuion si jamais*

## Fonctionnement  

Il faut déposer le fichier .wav à transcrire dans le dossier 1-input/ :  

```
📂 speech-to-text-benchmark/ 
├── 📂 1-input/
|       ├── 📜 audio.wav
|       |...
├── 📂 2-data/
│...
```
Si toutes les dépendances sont correctements installées il suffit alors de lancer les commandes suivantes. 

    cd 2-code  
    
puis 

    python3 main.py <nom-du-fichier.wav> <nom-du-fichier-de-sortie.json>

Le fichier de sortie sera alors dans le dossier 3-outpout/

```
📂 speech-to-text-benchmark/ # this is root
|...
├── 📂 3-output/
|       ├── 📜 sortie.json
|       |...
│...
```
