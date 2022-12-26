from Kaldi_transcript import *
from Output import *
from Separateur import *

separateur = Separateur()
transcripter = Kaldi_transcript()
output = Output()

document_a_traiter = str(sys.argv[1])
print(document_a_traiter)


#audio_tab = separateur.split_sb(document_a_traiter)
#nb_personnes_entendues = separateur.export_np(audio_tab)
nb_personnes_entendues = 2
for i in range(nb_personnes_entendues):
    separateur.split_silence("personne{0}.wav".format(i),"p{0}".format(i))

output.to_JSON(transcripter,"p0","p1","Personne0","Personne1",str(sys.argv[2]))