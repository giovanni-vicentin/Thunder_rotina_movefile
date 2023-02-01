import os
import shutil

def move_ferias():
    source_dir = "C:\\DOCUMENTOS ROTINA"
    destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Ferias"

    for filename in os.listdir(source_dir):
        if "ProgramaçãodeFérias" in filename.split("-")[1]:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

move_ferias()

def move_holerites():
    source_dir = "C:\\DOCUMENTOS ROTINA"
    destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Holerites"

    for filename in os.listdir(source_dir):
        if "RecibodePagamento" in filename.split("-")[1]:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

move_holerites()

def move_extrato():
    source_dir = "C:\\DOCUMENTOS ROTINA"
    destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Extratos"

    for filename in os.listdir(source_dir):
        if "ExtratoMensal" in filename.split("-")[1]:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

move_extrato()

def move_liquidos():
    source_dir = "C:\\DOCUMENTOS ROTINA"
    destination_dir = "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\3@ DOING\\Liquidos"

    for filename in os.listdir(source_dir):
        if "RelatóriodeLíquidos" in filename.split("-")[1]:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

move_liquidos()