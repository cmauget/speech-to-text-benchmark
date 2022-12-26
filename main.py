from Kaldi_transcript import *
from Output import *
from Separateur import *

separateur = Separateur()
transcripter = Kaldi_transcript()
output = Output()

document_a_traiter = sys.argv[1]
print(document_a_traiter)

nom_fichier_personne_0 = "personne0.wav"
nom_fichier_personne_1 = "personne1.wav"

audio_tab = separateur.split_sb(document_a_traiter)
nb_personnes_entendues = separateur.export_np(audio_tab)

for i in range(nb_personnes_entendues):
    separateur.split_silence("personne{0}.wav".format(i),"p{0}".format(i))

output.to_JSON(transcripter,"p0","p1","Personne0","Personne1",sys.argv[2])