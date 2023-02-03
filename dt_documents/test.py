import os
import shutil

# Function to move files from one folder to another based on keyword
def move_files(source_dir, destinations):
    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            # Check if keyword is in the filename
            if keyword in filename.split("-")[1]:
                # Move the file to the destination folder
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
                break

# Move files from Extratos folder
source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"
destinations = [("ExtratoMensal", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Extratos")]
move_files(source_dir, destinations)

# Move files from Holerites folder
source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\\3@ DOING\\Holerites"
destinations = [("RecibodePagamento", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Holerites")]
move_files(source_dir, destinations)

# Move files from Liquidos folder
source_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\\3@ DOING\\Liquidos"
destinations = [("RelatóriodeLíquidos", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Liquidos")]
move_files(source_dir, destinations)
