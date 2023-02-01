import os
import shutil

def mover_ferias():
    source_dir = "C:\\DOCUMENTOS ROTINA"
    destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"

    for filename in os.listdir(source_dir):
        if "ProgramaçãodeFérias" in filename.split("-")[1]:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

mover_ferias()
