import storage_control
import apps
import os
import styling as S
import boots

boot = None
welcome_message = """
  ____  _                    ___  ____  
 / ___|| |_ _____   _____   / _ \/ ___| 
 \___ \| __/ _ \ \ / / _ \ | | | \___ \ 
  ___) | ||  __/\ V /  __/ | |_| |___) |
 |____/ \__\___| \_/ \___|  \___/|____/ 

=========== • VERSION 0.10 • ============
"""

if False:
    welcome_message = """

    /$$$$$$   /$$                                          /$$$$$$   /$$$$$$ 
    /$$__  $$ | $$                                         /$$__  $$ /$$__  $$
    | $$  \__//$$$$$$    /$$$$$$  /$$    /$$ /$$$$$$       | $$  \ $$| $$  \__/
    |  $$$$$$|_  $$_/   /$$__  $$|  $$  /$$//$$__  $$      | $$  | $$|  $$$$$$ 
    \____  $$ | $$    | $$$$$$$$ \  $$/$$/| $$$$$$$$      | $$  | $$ \____  $$
    /$$  \ $$ | $$ /$$| $$_____/  \  $$$/ | $$_____/      | $$  | $$ /$$  \ $$
    |  $$$$$$/ |  $$$$/|  $$$$$$$   \  $/  |  $$$$$$$      |  $$$$$$/|  $$$$$$/
    \______/   \___/   \_______/    \_/    \_______/       \______/  \______/ 
                                                                            
    """

def run(n):
    if n.lower() == 'hello world' or n.lower() == 'hello world!':
        print('Hello!')
        return
    cmd = n.split(' ')[0]
    data_list = n.split(' ')[1:len(n.split(' '))]
    
    match cmd:
        case ('read'|'open'|'get'):
            if len(data_list) == 1:
                print(storage_control.read(data_list[0]))
            elif len(data_list) == 3:
                match data_list[1]:
                    case 'with':
                        apps.run(data_list[2], data_list[0])
                    case 'as':
                        code = data_list[2]
                        app = storage_control.read(f'system/pairings/{code}')
                        apps.run(app, data_list[0])

        case ('write'|'set'):
            path = data_list[0]
            entry_type = data_list[1]  # 'file' or 'dir'
            value = data_list[2] if len(data_list) > 2 else ""
            if entry_type in ['f', 'file']:
                storage_control.write(path, value, 'file')
            elif entry_type in ['d', 'dir']:
                storage_control.write(path, value, 'dir')
            
            print(f'Wrote `{value}` to {entry_type} at path `{path}`')
                
        case ('new'|'create'):
            path = data_list[0]
            entry_type = data_list[1]  # 'file' or 'dir'
            if entry_type in ['f', 'file']:
                storage_control.new(path, 'file')
            elif entry_type in ['d', 'dir']:
                storage_control.new(path, 'dir')
            
            print(f'Created new {entry_type} at path `{path}`')
            
        case ('delete'|'remove'):
            path = data_list[0]
            print(storage_control.delete(path))
            
            print(f'Deleted file / directory at path `{path}`')
        
        case ('execute'|'run'):
            if len(data_list) == 1:
                apps.run(data_list[0])
            if len(data_list) >= 2:
                apps.run(data_list[0], data_list[1])

        case ('update'|'burn'):
            if not storage_control.exists('system'):
                storage_control.new('system', 'dir')
            if not storage_control.exists('system/pairings'):
                storage_control.new('system/pairings', 'dir')
                
        case 'pair':
            code = data_list[0]
            app = data_list[1]
            if not storage_control.exists(f'system/pairings/{code}'):
                storage_control.new(f'system/pairings/{code}')
            storage_control.write(f'system/pairings/{code}', app)
        
        case ('clear'|'cls'):
            os.system('cls')
        
        case ('print'|'echo'|'return'):
            print(' '.join(data_list))
            
        case ('kill'|'exit'|'quit'|'end'):
            quit()
            
        case 'welcome':
            print(welcome_message)
        
        case 'reset':
            os.system('cls')
            print(welcome_message)
            
        case _:
            print(f'{boot.cERROR}   • • !> ERROR: NO SUCH COMMAND OR PREFIX "{cmd}"')
