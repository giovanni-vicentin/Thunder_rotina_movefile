import os
import shutil

def move_files_relatorios(source_dir, destination_dir, search_string, adiantamento=False):
    def __move_files_relatorios(source_dir, destination_dir, search_string):
        for filename in os.listdir(source_dir):
            if search_string in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

    if adiantamento==True:
        search_strings = ["else:RecibodePagamento", "else:ExtratoMensal", "RelatóriodeLíquidos"]
        destination_dirs = [
            os.path.join(destination_dir, "HoleritesA"),
            os.path.join(destination_dir, "ExtratosA"),
            os.path.join(destination_dir, "LiquidosA"),
        ]
    else:
        search_strings = ["ProgramaçãodeFérias", "RecibodePagamento", "ExtratoMensal", "RelatóriodeLíquidos"]
        destination_dirs = [
            os.path.join(destination_dir, "Ferias"),
            os.path.join(destination_dir, "Holerites"),
            os.path.join(destination_dir, "Extratos"),
            os.path.join(destination_dir, "Liquidos"),
        ]

    for search_string, destination_dir in zip(search_strings, destination_dirs):
        __move_files_relatorios(source_dir, destination_dir, search_string)
