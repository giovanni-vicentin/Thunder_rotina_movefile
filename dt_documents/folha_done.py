import os
import shutil

path_1 = r'C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\3@ DOING'
path_2 = r'C:\Users\TALST-GiovanniVicent\TALST CONTABILIDADE\TALST CONTABILIDADE - 5.7.2 AUTOMACAO\DominioWebDocumentos\4@ DONE'

file_types = [('Extratos', 'ExtratoMensal'),
              ('Holerites', 'RecibodePagamento'),
              ('Liquidos', 'RelatóriodeLíquidos'),
              ('Ferias', 'ProgramaçãodeFérias')]

for file_type in file_types:
    src_dir = os.path.join(path_1, file_type[0])
    dest_dir = os.path.join(path_2, file_type[0])

    for filename in os.listdir(src_dir):
        if filename.startswith(file_type[1]) and "-" in filename:
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            shutil.move(src_file, dest_file)
