import os
import shutil

def move_files_folha(source_dir, destinations):
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break

source_dir = "C:\\DOCUMENTOS ROTINA"
destinations = [("ProgramaçãodeFérias", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"), 
                ("ExtratoMensal", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"),
                ("RecibodePagamento", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"),
                ("RelatóriodeLíquidos", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos")]

move_files_folha(source_dir, destinations)