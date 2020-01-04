
import sys
from corer import create_file, create_folder, copy_file_fol, delete_fol_files, filter_folders, save_info, guess

save_info('start')
command = sys.argv[1]

if command == 'list':
    filter_folders()
elif command == 'create_folder':
    name = sys.argv[2]
    create_folder(name)
elif command == 'create_file':
    try:
        name = sys.argv[2]
        tex = sys.argv[3]
    except IndexError as a:
        print('Забыли ввести имя файла')
    except TypeError as t:
        print(f'------>{t}')
    else:
        create_file(name, tex)
elif command == 'copy_file_fol':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError as i:
        print('Забыли ввести имя файла')
    else:
        copy_file_fol(name, new_name)
elif command == 'delete_fol_files':
    name = sys.argv[2]
    delete_fol_files(name)
elif command == 'save_info':
    mess = sys.argv[2]
    save_info(mess)
elif command == 'help':
    print('help')
elif command == 'guu':
    puz = sys.argv[2]
    guess(puz)
save_info('finish')