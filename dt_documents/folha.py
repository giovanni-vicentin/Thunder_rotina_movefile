import os
import shutil

"""
This function moves files with specific names to their corresponding destination directories.
The source directory is specified in the source_dir parameter and the destinations are specified in the destinations parameter as a list of tuples, where each tuple consists of the keyword to search in the file name and the destination directory.
The function iterates through all files in the source directory and for each file, it checks if the keyword is in the second part of the filename after the first "-" and moves the file to the corresponding destination directory.
"""


def move_files_folha(source_dir, destinations):
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break


# source directory containing the files to be moved
source_dir = "C:\\DOCUMENTOS ROTINA"

# list of tuples, each tuple consists of the keyword to search in the file name and the destination directory
destinations = [("ProgramaçãodeFérias",
                 "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"),
                ("ExtratoMensal",
                 "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"),
                ("RecibodePagamento",
                 "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"),
                ("RelatóriodeLíquidos",
                 "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos")]

# call the function to move the files
move_files_folha(source_dir, destinations)
