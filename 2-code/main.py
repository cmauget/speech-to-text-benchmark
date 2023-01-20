
from Sphinx_transcript import *
from Brain_transcript import * 
from BrainW_transcript import *
from Whisper_transcript import *
from Kaldi_transcript import *
from Output import *
from Separateur import *

output = Output()
separateur = Separateur()
choice = input("1 - Sphinx \n2 - Brain \n3 - BrainW \n4 - Whisper \n5 - Kaldi \nEnter model to use : ")

match choice:
    case "1":
        transcripter = Sphinx_transcript()
    case "2":
        transcripter = Brain_transcript()
    case "3":
        transcripter = BrainW_transcript()
    case "4":
        transcripter = Whisper_transcript()
    case "5":
        transcripter = Kaldi_transcript()
    case _:
        print("Invalid syntax, defaulting to BrainW")
        transcripter = BrainW_transcript()



document_a_traiter = str(sys.argv[1])
chemin_relatif_entree="../1-input/"
chemin_relatif_sortie = "../3-output/"
print(document_a_traiter)


audio_tab = separateur.split_sb(chemin_relatif_entree+document_a_traiter)
nb_personnes_entendues = separateur.export_np(audio_tab,chemin_relatif_entree)
#nb_personnes_entendues = 2
for i in range(nb_personnes_entendues):
    separateur.split_silence(chemin_relatif_entree+"personne{0}.wav".format(i),chemin_relatif_entree+"p{0}".format(i))

output.to_JSON(transcripter,chemin_relatif_entree+"p0",chemin_relatif_entree+"p1","Personne0","Personne1",chemin_relatif_sortie+str(sys.argv[2]))
