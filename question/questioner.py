import os
import shutil
from folha.test import move_files_relatorios

def ask_adiantamento():
    adiantamento = input("Existe adiantamento? (s/n) ").lower()
    if adiantamento == "S":
        return True
    else:
        return False

if __name__ == "__main__":
    source_dir = "Caminho da pasta de origem"
    destination_dir = "Caminho da pasta de destino"
    adiantamento = ask_adiantamento()
    move_files_relatorios(source_dir, destination_dir, "", adiantamento)