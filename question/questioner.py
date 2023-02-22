from dt_documents.test import Move_files
from dt_documents.test import Move_files_done


def ask_yes_no(input_text):
    while True:
        response = input(f'{input_text}Type your answer (yes/no): ').lower()
        if response == "yes" or response == "y" or response == "sim" or response == "s":
            return False
        elif response == "no" or response == "n" or response == "nao" or response == "não":
            return True
        elif response == "cancelar" or response == "cancel":
            exit()
        else:
            print('Invalid response, please type again.\n\nTo cancel, type "cancel".\n')


def ask_move_files():
    doing_done = ask_yes_no('Do these documents not go in the "DONE" folder?\n')
    is_adto = ask_yes_no('Are these documents not "adiantamento" documents?\n')

    if doing_done:
        Move_files(is_adto)
    else:
        Move_files_done(is_adto)


ask_move_files()
