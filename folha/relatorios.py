import os
import shutil

source_dir = "C:\\DOCUMENTOS ROTINA"
destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"

for filename in os.listdir(source_dir):
    if "ProgramaçãodeFérias" in filename.split("-")[1]:
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
source_dir = "C:\\DOCUMENTOS ROTINA"
destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"

for filename in os.listdir(source_dir):
    if "ExtratoMensal" in filename.split("-")[1]:
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"
destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"

for filename in os.listdir(source_dir):
    if "RecibodePagamento" in filename.split("-")[1]:
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"
destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos"

for filename in os.listdir(source_dir):
    if "RelatóriodeLíquidos" in filename.split("-")[1]:
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"
destination_dir = "C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\3@ DOING\AvisosVencimento"

for filename in os.listdir(source_dir):
    if "-AV" in filename.split("-")[1]:
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"
destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\FGTS"

for filename in os.listdir(source_dir):
    if "GRF" in filename.split("-")[2]:
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"
destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\INSS"

for filename in os.listdir(source_dir):
    if "Guia" in filename.split("-")[2]:
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

source_dir = "C:\\DOCUMENTOS ROTINA"
destinations = [("ProgramaçãodeFérias", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"), 
                ("ExtratoMensal", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"),
                ("RecibodePagamento", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"),
                ("RelatóriodeLíquidos", "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos")]

move_files_folha(source_dir, destinations)
