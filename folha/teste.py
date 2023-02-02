import os
import shutil

def move_files_adto(source_dir, destination_dir, search_string):
    for filename in os.listdir(source_dir):
        if search_string in filename.split("-")[1]:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"

move_files_adto(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA", "RecibodePagamento")

move_files_adto(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA", "ExtratoMensal")

move_files_adto(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA", "RelatóriodeLíquidos")
