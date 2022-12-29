from Kaldi_transcript import *
from Output import *
from Separateur import *

separateur = Separateur()
transcripter = Kaldi_transcript()
output = Output()

document_a_traiter = str(sys.argv[1])
chemin_relatif_entree="./1-input/"
chemin_relatif_sortie = "./3-output/"
print(document_a_traiter)


audio_tab = separateur.split_sb(document_a_traiter)
nb_personnes_entendues = separateur.export_np(audio_tab)
#nb_personnes_entendues = 2
for i in range(nb_personnes_entendues):
    separateur.split_silence("personne{0}.wav".format(i),chemin_relatif_entree+"p{0}".format(i))

output.to_JSON(transcripter,chemin_relatif_entree+"p0",chemin_relatif_entree+"p1","Personne0","Personne1",str(sys.argv[2]))
