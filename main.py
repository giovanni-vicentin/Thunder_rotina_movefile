import os
import shutil
from dt_documents.move_RPAGFIP import move_files_GFIP
from dt_documents.move_RPAGFIP import move_folha


def main():
    move_folha()
    move_files_GFIP()


if __name__ == '__main__':
    main()
