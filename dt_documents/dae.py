import os
import shutil

def move_files_dae(source_dir, destinations):
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break

source_dir = "C:\\DOCUMENTOS ROTINA"
destinations = [("DAE", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\DAE")]

move_files_dae(source_dir, destinations)
