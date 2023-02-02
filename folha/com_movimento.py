import os
import shutil

def move_files(source_dir, destination_dir, search_string):
    for filename in os.listdir(source_dir):
        if search_string in filename.split("-")[1]:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"

move_files(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias", "ProgramaçãodeFérias")

move_files(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites", "RecibodePagamento")

move_files(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos", "ExtratoMensal")

move_files(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos", "RelatóriodeLíquidos")
