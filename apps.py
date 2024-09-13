## Used to create applications for SteveOS
import storage_control
import os
import styling as S
import backend

welcome_message = f"""
{S.YELLOW}{S.BOLD}
  ____  _                    ___  ____  
 / ___|| |_ _____   _____   / _ \/ ___| 
 \___ \| __/ _ \ \ / / _ \ | | | \___ \ 
  ___) | ||  __/\ V /  __/ | |_| |___) |
 |____/ \__\___| \_/ \___|  \___/|____/ 

=========== • VERSION 0.10 • ============
{S.RST}
"""



os.system('cls')



def run(name, filepath=None):
    class_reference = globals()[name.capitalize()]
    instance = class_reference()
    if filepath is None: instance.run()
    else: instance.read(filepath)


class Scripter:
    def run(self):
        os.system('cls')
        print(f'{S.BRIGHT_YELLOW}{S.BOLD}SCRIPTER{S.RST}')
        input(f'{S.ITALIC}{S.BOLD}[ENTER]{S.RST}{S.ITALIC} TO BEGIN EDITING FILE:{S.RST}')


