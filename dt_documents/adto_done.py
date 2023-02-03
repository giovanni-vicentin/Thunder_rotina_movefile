import os
import shutil

def move_files(src_dir, dst_dir, file_name):
    for filename in os.listdir(src_dir):
        if filename.startswith(file_name) and "-" in filename:
            src_path = os.path.join(src_dir, filename)
            dst_path = os.path.join(dst_dir, filename)
            shutil.move(src_path, dst_path)

# Define source and destination directories
src_dir_extratos = r"C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\3@ DOING\ExtratosA"
dst_dir_extratos = r"C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\4@ DONE\ExtratosA"

src_dir_holerites = r"C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\3@ DOING\HoleritesA"
dst_dir_holerites = r"C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\4@ DONE\HoleritesA"

src_dir_liquidos = r"C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\3@ DOING\LiquidosA"
dst_dir_liquidos = r"C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\4@ DONE\LiquidosA"

# Move files from source to destination
move_files(src_dir_extratos, dst_dir_extratos, "ExtratoMensal")
move_files(src_dir_holerites, dst_dir_holerites, "RecibodePagamento")
move_files(src_dir_liquidos, dst_dir_liquidos, "RelatóriodeLíquidos")
