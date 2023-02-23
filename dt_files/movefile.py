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


# fuction to move files to use in move_folha_done
def move_files_done(source_dir, destinations):
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break


def move_folha_done():
    # Move files from Extratos folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"
    destinations = [("ExtratoMensal",
                     "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Extratos")]
    move_files_done(source_dir, destinations)

    # Move files from Holerites folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"
    destinations = [("RecibodePagamento",
                     "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Holerites")]
    move_files_done(source_dir, destinations)

    # Move files from Liquidos folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos"
    destinations = [("RelatóriodeLíquidos",
                     "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Liquidos")]
    move_files_done(source_dir, destinations)

    # Move files from Ferias folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"
    destinations = [("ProgramaçãodeFérias",
                     "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Ferias")]
    move_files_done(source_dir, destinations)


def move_files_dctfweb():
    source_folder = r'C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\RPA DCTFWEB'
    destination_folder = r'C:\DOCUMENTOS ROTINA'

    # Check if the destination folder exists and create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all subfolders of the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if '-122022-Guia' in file:
                # Copy the file to the destination folder
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)
                shutil.copy(source_file, destination_file)


def move_folha_adto(source_dir="C:\\DOCUMENTOS ROTINA",
                    destinations=None):
    if destinations is None:
        destinations = [("ExtratoMensal",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA"),
                        ("RecibodePagamento",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA"),
                        ("RelatóriodeLíquidos",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA")]
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break


def move_folha_adto_done():
    # Move files from Extratos folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA"
    destinations = [("ExtratoMensal",
                     "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\ExtratosA")]
    move_files_done(source_dir, destinations)

    # Move files from Holerites folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA"
    destinations = [("RecibodePagamento",
                     "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\HoleritesA")]
    move_files_done(source_dir, destinations)

    # Move files from Liquidos folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA"
    destinations = [("RelatóriodeLíquidos",
                     "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\LiquidosA")]
    move_files_done(source_dir, destinations)
