import os
import shutil


def move_files_GFIP():
    source_folder = r"C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\RPA GFIP"
    destination_folder = r"C:\DOCUMENTOS ROTINA"

    # Check if the destination folder exists and create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all subfolders of the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check if the file name contains the specified pattern
            if "-012023-GRF" in file:
                # Copy the file to the destination folder
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_folder, file)
                shutil.copy2(source_file_path, destination_file_path)


def move_folha(source_dir="C:\\DOCUMENTOS ROTINA",
               destinations=None):
    if destinations is None:
        destinations = [("ProgramaçãodeFérias",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"),
                        ("ExtratoMensal",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"),
                        ("RecibodePagamento",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"),
                        ("RelatóriodeLíquidos",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos")]
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break
