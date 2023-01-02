# Transcription (speech to text) d’échanges téléphoniques adressés au support IT d’une entreprise

Ce projet donne des ressources pour transcrire des conversations téléphoniqe ainsi que des outils pour évaluer leurs performances.

## Organisation
Notre code s'articule autour de trois modules :

* La couche d'entrée
* La couche de traduction
* La couche de sortie

## Setup
Nous utilisons de nombreuses bibliothèques python ainsi que des modèles tel que :
* [Speechrabin](https://speechbrain.github.io/)
* [Sphinx](https://cmusphinx.github.io/)
* [Vosk](https://alphacephei.com/vosk/)
* [Whisper](https://github.com/openai/whisper)  
  
Pour faciliter l'installation nous avons créé un environnement [conda](https://docs.conda.io/en/latest/) avec toute les dépendaces. Vous pouvez trouver le fichier de configuration dans utils/sb.yaml.  

    conda env create -f sb.yml  
    
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
