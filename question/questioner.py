import os
import shutil

def move_files_relatorios(source_dir, destination_dir, search_string, adiantamento=False):
    def __move_files_relatorios(source_dir, destination_dir, search_string):
        for filename in os.listdir(source_dir):
            if search_string in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

    source_dir = "C:\\DOCUMENTOS ROTINA"

    if adiantamento:
        search_strings = ["else:RecibodePagamento", "else:ExtratoMensal", "RelatóriodeLíquidos"]
        destination_dirs = [
            "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA",
            "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA",
            "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA",
        ]
    else:
        search_strings = ["ProgramaçãodeFérias", "RecibodePagamento", "ExtratoMensal", "RelatóriodeLíquidos"]
        destination_dirs = [
            "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias",
            "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites",
            "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos",
            "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos",
        ]

    for search_string, destination_dir in zip(search_strings, destination_dirs):
        __move_files_relatorios(source_dir, destination_dir, search_string)
