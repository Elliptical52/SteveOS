import storage_control
import apps

def run(n):
    cmd = n.split(' ')[0]
    data_list = n.split(' ')[1:len(n.split(' '))]
    
    match cmd:
        case 'read':
            print(storage_control.read(data_list[0]))
            
        case 'write':
            path = data_list[0]
            entry_type = data_list[1]  # 'file' or 'dir'
            value = data_list[2] if len(data_list) > 2 else ""
            if entry_type in ['f', 'file']:
                storage_control.write(path, value, 'file')
            elif entry_type in ['d', 'dir']:
                storage_control.write(path, value, 'dir')
            
            print(f'Wrote `{value}` to {entry_type} at path `{path}`')
                
        case 'new':
            path = data_list[0]
            entry_type = data_list[1]  # 'file' or 'dir'
            if entry_type in ['f', 'file']:
                storage_control.new(path, 'file')
            elif entry_type in ['d', 'dir']:
                storage_control.new(path, 'dir')
            
            print(f'Created new {entry_type} at path `{path}`')
            
        case 'delete':
            path = data_list[0]
            print(storage_control.delete(path))
            
            print(f'Deleted file / directory at path `{path}`')
        
        case 'run':
            if len(data_list) == 1:
                apps.run(data_list[0])
            if len(data_list) >= 2:
                apps.run(data_list[0], data_list[1])
            
            
        case _:
            print(f'• ERROR: NO SUCH COMMAND OR PREFIX "{cmd}"')
