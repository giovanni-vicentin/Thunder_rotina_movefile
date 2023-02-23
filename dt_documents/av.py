import os
import shutil


def move_files_folha_done(source_dir, destinations=None):
    if not os.path.isdir(source_dir):
        raise ValueError(f"Invalid source directory: {source_dir}")

    if destinations is None:
        destinations = [("ProgramaçãodeFérias",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Ferias"),
                        ("ExtratoMensal",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Extratos"),
                        ("RecibodePagamento",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Holerites"),
                        ("RelatóriodeLíquidos",
                         "C:\\Users\\TALST-GiovanniVicent\\TALST CONTABILIDADE\\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\\DominioWebDocumentos\\4@ DONE\\Liquidos")]

    for filename in os.listdir(source_dir):
        for keyword, destination_dir in destinations:
            if keyword in filename.split("-")[1]:
                destination_path = os.path.join(destination_dir, filename)
                if os.path.isfile(destination_path):
                    raise ValueError(f"Destination file already exists: {destination_path}")
                shutil.move(os.path.join(source_dir, filename), destination_path)
                break
