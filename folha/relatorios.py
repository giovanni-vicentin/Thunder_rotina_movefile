import os
import shutil

def move_files_relatorios(source_dir, destination_dir, search_string, adiantamento=False):
    def __move_files_relatorios(source_dir, destination_dir, search_string):
        for filename in os.listdir(source_dir):
            if search_string in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

    source_dir = "C:\\DOCUMENTOS ROTINA"

    if adiantamento:
        __move_files_relatorios(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA", "else:RecibodePagamento")

        __move_files_relatorios(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA", "else:ExtratoMensal")

        __move_files_relatorios(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA", "RelatóriodeLíquidos")
    else:
        __move_files_relatorios(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias", "ProgramaçãodeFérias")

        __move_files_relatorios(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites", "RecibodePagamento")

        __move_files_relatorios(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos", "ExtratoMensal")

        __move_files_relatorios(source_dir, "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos", "RelatóriodeLíquidos")

