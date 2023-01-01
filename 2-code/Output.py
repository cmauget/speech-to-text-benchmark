import json
import os
import sys
from Kaldi_transcript import *
class Output :
    def to_JSON(this,transcripter,dossier_personne_1,dossier_personne_2,nom_1,nom_2,nom_json):

        files = os.listdir(dossier_personne_1)
        l={}
        l[nom_1]={}
        l[nom_2]={}
        for file in files :
            name = file.split(".")[0]
            l[nom_1][name]=transcripter.transcript(dossier_personne_1+"/"+file)

        files = os.listdir(dossier_personne_2)
        for file in files :
            name = file.split(".")[0]
            l[nom_2][name]=transcripter.transcript(dossier_personne_2+"/"+file)

        # Serializing json
        json_object = json.dumps(l, indent=4)
        # Writing to sample.json
        with open(nom_json, "w") as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    o = Output()
    transcripter = Kaldi_transcript() # type: ignore
    o.to_JSON(transcripter,"../1-input/p0","../1-input/p1","Personne0","Personne1","nom")