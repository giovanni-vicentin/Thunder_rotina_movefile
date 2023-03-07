import os
import shutil
import sys


RESET = '\033[0m'
WHITE = '\033[97m'
TURQUOISE = '\033[96m'
LEMON_GREEN = '\033[92m'


def move_files_GFIP():
    source_folder = r"C:\Users\TALST-GiovanniVicent\OneDrive - TALST CONTABILIDADE\5.7.2 AUTOMACAO\RPA GFIP"
    destination_folder = r"C:\DOCUMENTOS ROTINA"

    # Ask user for the desired value to search for
    phrase = 'Put the month with 2 digits and the year with 4.\nFor example "072023"\n'
    final_phrase = 'Enter the value to search for: '
    error_message = f"{LEMON_GREEN}{phrase}{RESET}{WHITE}{final_phrase}{RESET}"
    print(error_message, file=sys.stderr)

    value = input('')

    # Check if the destination folder exists and create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all subfolders of the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check if the file name contains the specified pattern
            if f'-{value}-GRF' in file:
                # Copy the file to the destination folder
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_folder, file)
                shutil.copy2(source_file_path, destination_file_path)


def move_folha(source_dir="C:\\DOCUMENTOS ROTINA",
               destinations=None):
    if destinations is None:
        destinations = [("ProgramaçãodeFérias",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"),
                        ("ExtratoMensal",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"),
                        ("RecibodePagamento",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"),
                        ("RelatóriodeLíquidos",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos"),
                        ("AV",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\AvisosVencimento")]
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
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"
    destinations = [("ExtratoMensal",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Extratos")]
    move_files_done(source_dir, destinations)

    # Move files from Holerites folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"
    destinations = [("RecibodePagamento",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Holerites")]
    move_files_done(source_dir, destinations)

    # Move files from Liquidos folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos"
    destinations = [("RelatóriodeLíquidos",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Liquidos")]
    move_files_done(source_dir, destinations)

    # Move files from Ferias folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"
    destinations = [("ProgramaçãodeFérias",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Ferias")]
    move_files_done(source_dir, destinations)

    # Move files from AvisosVencimento folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\AvisosVencimento"
    destinations = [("AV",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\AvisosVencimento")]
    move_files_done(source_dir, destinations)


def move_files_dctfweb():
    source_folder = r'C:\Users\TALST-GiovanniVicent\OneDrive - TALST CONTABILIDADE\5.7.2 AUTOMACAO\RPA DCTFWEB'
    destination_folder = r'C:\DOCUMENTOS ROTINA'

    # Ask user for the desired value to search for
    phrase = 'Put the month with 2 digits and the year with 4.\nFor example "072023"\n'
    final_phrase = 'Enter the value to search for: '
    error_message = f"{TURQUOISE}{phrase}{RESET}{WHITE}{final_phrase}{RESET}"
    print(error_message, file=sys.stderr)

    value = input('')

    print('You entered:', value)

    # Check if the destination folder exists and create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all subfolders of the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if f'-{value}-Guia' in file:
                # Copy the file to the destination folder
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)
                shutil.copy(source_file, destination_file)


def move_folha_adto(source_dir="C:\\DOCUMENTOS ROTINA",
                    destinations=None):
    if destinations is None:
        destinations = [("ExtratoMensal",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA"),
                        ("RecibodePagamento",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA"),
                        ("RelatóriodeLíquidos",
                         "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA")]
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break


def move_folha_adto_done():
    # Move files from Extratos folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\ExtratosA"
    destinations = [("ExtratoMensal",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\ExtratosA")]
    move_files_done(source_dir, destinations)

    # Move files from Holerites folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\HoleritesA"
    destinations = [("RecibodePagamento",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\HoleritesA")]
    move_files_done(source_dir, destinations)

    # Move files from Liquidos folder
    source_dir = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\LiquidosA"
    destinations = [("RelatóriodeLíquidos",
                     "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\LiquidosA")]
    move_files_done(source_dir, destinations)


def move_impostos():
    # Directory where the files are located
    source_dir = "C:\\DOCUMENTOS ROTINA"

    # Directories where the files should be moved to
    dest_dir1 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS"
    dest_dir2 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS"
    dest_dir3 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\DAE"
    dest_dir4 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\IRRF"

    # Loop through the files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file name contains "Guia" and move it to dest_dir1
        if "Guia" in filename and "-" in filename:
            name_parts = filename.split("-")
            if len(name_parts) > 2 and "Guia" in name_parts[2]:
                source_path = os.path.join(source_dir, filename)
                shutil.move(source_path, dest_dir1)

        # Check if the file name contains "GRF" and move it to dest_dir2
        elif "GRF" in filename and "-" in filename:
            name_parts = filename.split("-")
            if len(name_parts) > 2 and "GRF" in name_parts[2]:
                source_path = os.path.join(source_dir, filename)
                shutil.move(source_path, dest_dir2)

        # Check if the file name contains "DAE" and move it to dest_dir3
        elif "DAE" in filename and "-" in filename:
            name_parts = filename.split("-")
            if "DAE" in name_parts[1]:
                source_path = os.path.join(source_dir, filename)
                shutil.move(source_path, dest_dir3)

        # Check if the file name contains "IRRF" and move it to dest_dir4
        elif "IRRF" in filename and "-" in filename:
            name_parts = filename.split("-")
            if "IRRF" in name_parts[1]:
                source_path = os.path.join(source_dir, filename)
                shutil.move(source_path, dest_dir4)

        # If the file name does not match any of the above conditions, skip it
        else:
            print('f')


def move_impostos_done():
    # Directories where the files are located
    source_dir1 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS"
    source_dir2 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS"
    source_dir3 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\DAE"
    source_dir4 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\IRRF"

    # Directories where the files should be moved to
    dest_dir1 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\INSS"
    dest_dir2 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\FGTS"
    dest_dir3 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\DAE"
    dest_dir4 = "C:\\Users\\TALST-GiovanniVicent\\OneDrive - TALST CONTABILIDADE\\5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\IRRF"

    # Loop through the files in the source directories

    # For files in source_dir1
    for filename in os.listdir(source_dir1):
        if "-" in filename:
            name_parts = filename.split("-")
            if len(name_parts) > 2 and "Guia" in name_parts[2]:
                source_path = os.path.join(source_dir1, filename)
                shutil.move(source_path, dest_dir1)

    # For files in source_dir2
    for filename in os.listdir(source_dir2):
        if "-" in filename:
            name_parts = filename.split("-")
            if len(name_parts) > 2 and "GRF" in name_parts[2]:
                source_path = os.path.join(source_dir2, filename)
                shutil.move(source_path, dest_dir2)

    # For files in source_dir3
    for filename in os.listdir(source_dir3):
        if "-" in filename:
            name_parts = filename.split("-")
            if "DAE" in name_parts[1]:
                source_path = os.path.join(source_dir3, filename)
                shutil.move(source_path, dest_dir3)

    # For files in source_dir4
    for filename in os.listdir(source_dir4):
        if "-" in filename:
            name_parts = filename.split("-")
            if "IRRF" in name_parts[1]:
                source_path = os.path.join(source_dir4, filename)
                shutil.move(source_path, dest_dir4)
