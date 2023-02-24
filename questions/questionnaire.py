from dt_files.movefile import move_files_GFIP
from dt_files.movefile import move_folha
from dt_files.movefile import move_folha_done
from dt_files.movefile import move_files_dctfweb
from dt_files.movefile import move_folha_adto
from dt_files.movefile import move_folha_adto_done
from dt_files.movefile import move_impostos
from dt_files.movefile import move_impostos_done


def questionnaire():

    while True:
        print('Welcome to Thunder_rotina_movefile\n')
        print('Choose an option:\n')
        print('1. Move payroll files to "Doing" folder\n')
        print('2. Move payroll files to "Done" folder\n')
        print('3. Move taxes "FGTS" for example\n')
        print('4. To exit the automation\n')

        option = input('Enter your option "1", "2", "3" or "4": ')

        if option == '1':
            while True:
                print('\nYou chose move payroll files to "Doing" folder.\n')
                print('Choose a sub-option:\n')
                print('1. For prepayments payroll documents\n')
                print('2. For regular payroll documents\n')
                print('3. To exit the automation\n')

                sub_option = input('Enter your sub-option "1", "2" or "3": ')

                if sub_option == '1':
                    print('\nYou chose move prepayments payroll documents to "Doing" folder.\n')
                    move_folha_adto()
                    break

                elif sub_option == '2':
                    print('You chose move regular payroll documents to "Doing" folder.\n')
                    move_folha()
                    break

                elif sub_option == '3':
                    print('You chose to exit the automation.\n')
                    break

                else:
                    print('Invalid sub-option. Please enter a valid sub-option.\n')
            break

        elif option == '2':
            while True:
                print('You chose move payroll files to "Done" folder.\n')
                print('Choose a sub-option:\n')
                print('1. For prepayments payroll documents\n')
                print('2. For regular payroll documents\n')
                print('3. To exit the automation\n')

                sub_option = input('Enter your sub-option "1", "2" or "3": ')

                if sub_option == '1':
                    print('\nYou chose move prepayments payroll documents to "Done" folder.\n')
                    move_folha_adto_done()
                    break

                elif sub_option == '2':
                    print('You chose move regular payroll documents to "Done" folder.\n')
                    move_folha_done()
                    break

                elif sub_option == '3':
                    print('You chose to exit the automation.\n')
                    break

                else:
                    print('Invalid sub-option. Please enter a valid sub-option.\n')
            break

        elif option == '3':
            while True:
                print('You chose move taxes documents.\n')
                print('Choose a sub-option:\n')
                print('1. Pull FGTS docs from "RPAGFIP" to "Documentos Rotina".\n')
                print('2. Pull INSS docs from "RPADCTFWEB" to "Documentos Rotina".\n')
                print('3. Move taxes files to "Doing" folder\n')
                print('4. Move taxes files to "Done" folder\n')
                print('5. To exit the automation\n')

                sub_option = input('Enter your sub-option "1", "2", "3", "4" or "5": ')

                if sub_option == '1':
                    print('\nYou chose move FGTS documents to "Documentos Rotina" folder.\n')
                    move_files_GFIP()
                    break

                elif sub_option == '2':
                    print('You chose move INSS documents to "Documentos Rotina" folder.\n')
                    move_files_dctfweb()
                    break

                elif sub_option == '3':
                    print('You chose move taxes documents to "Doing" folder.\n')
                    move_impostos()
                    break

                elif sub_option == '4':
                    print('You chose move taxes documents to "Done" folder.\n')
                    move_impostos_done()
                    break

                elif sub_option == '5':
                    print('You chose to exit the automation.\n')
                    break

                else:
                    print('Invalid sub-option. Please enter a valid sub-option.\n')
            break

        elif option == '4':
            print('You chose to exit the automation.\n')
            break

        else:
            print('Invalid option. Please enter a valid option.\n')
