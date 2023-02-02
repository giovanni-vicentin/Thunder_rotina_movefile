import os
import shutil

def move_files_impostos(source_dir, destinations):
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword == "IRRF":
                index = 1
            else: 
                index = 2
            if keyword in filename.split("-")[index]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break

source_dir = "C:\\DOCUMENTOS ROTINA"
destinations = [("GRF", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS"),
                ("Guia", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS"),
                ("IRRF", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\IRRF")]

move_files_impostos(source_dir, destinations)