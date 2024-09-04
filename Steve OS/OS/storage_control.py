import json

def read(path):
    keys = path.split('/')
    entry = storage
    try:
        for key in keys:
            entry = entry[key]
        return entry
    except KeyError:
        return None
    except TypeError:
        return '• ERROR: CANNOT READ SINGLE-VALUE FILE AS DIRECTORY'

def write(path, value, entry_type='file'):
    keys = path.split('/')
    entry = storage
    try:
        for key in keys[:-1]:  # Traverse to the second last key
            if key not in entry:
                entry[key] = {}  # Create a new dictionary if the key doesn't exist
            entry = entry[key]

        if entry_type == 'file':
            entry[keys[-1]] = value  # Set the value at the final key
        elif entry_type == 'dir':
            if keys[-1] not in entry:
                entry[keys[-1]] = {}  # Create a new directory
            else:
                return '• ERROR: DIRECTORY ALREADY EXISTS'

        # Persist the changes back to the JSON file
        with open('OS/storage.json', 'w') as file:
            json.dump(storage, file, indent=4)

        return True
    except (KeyError, TypeError):
        return False

def new(path, entry_type='file'):
    keys = path.split('/')
    entry = storage
    try:
        for key in keys[:-1]:  # Traverse to the second last key
            if key not in entry:
                entry[key] = {}  # Create a new dictionary if the key doesn't exist
            entry = entry[key]

        if entry_type == 'file':
            if keys[-1] not in entry:
                entry[keys[-1]] = ""  # Create an empty file
            else:
                return '• ERROR: FILE ALREADY EXISTS'
        elif entry_type == 'dir':
            if keys[-1] not in entry:
                entry[keys[-1]] = {}  # Create a new directory
            else:
                return '• ERROR: DIRECTORY ALREADY EXISTS'

        # Persist the changes back to the JSON file
        with open('OS/storage.json', 'w') as file:
            json.dump(storage, file, indent=4)

        return True
    except (KeyError, TypeError):
        return False

def delete(path):
    keys = path.split('/')
    entry = storage
    try:
        for key in keys[:-1]:  # Traverse to the second last key
            entry = entry[key]
        
        if keys[-1] in entry:
            del entry[keys[-1]]  # Delete the final key
        else:
            return '• ERROR: FILE OR DIRECTORY NOT FOUND'

        # Persist the changes back to the JSON file
        with open('OS/storage.json', 'w') as file:
            json.dump(storage, file, indent=4)

        return True
    except (KeyError, TypeError):
        return False

# Load the JSON data
with open('OS/storage.json', 'r') as file:
    storage = json.load(file)
