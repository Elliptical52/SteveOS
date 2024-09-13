import backend
import styling as S

class Retro:
    def run():
        print(f'{S.ITALIC}{S.GREEN}{S.BOLD}' + backend.welcome_message)
        while True:
            cmd = input(f'{S.ITALIC}{S.GREEN}{S.BOLD}>> ')
            match cmd:
                case _:
                    backend.run(cmd)

class Lacy:
    cERROR = S.BLUE
    
    def run():
        dPREFIX = S.RED
        
        print(f'{S.BLUE}Steve OS{S.RST + S.RED} [Version 0.10]{S.RST}')
        while True:
            if 'cPREFIX' in locals():
                n = cPREFIX
            else: 
                n = dPREFIX
            
            cmd = input(f'{S.ITALIC}{n}{S.BOLD}>> ')
            match cmd:
                case ('build'|'lacy'|'Lacy'):
                    print("Please enter one of the following keywords:\n    • color")
                    keyword = input("::")
                    
                    match keyword:
                        case 'color':
                            option = input("Please enter one of the following keywords:\n    • prefix\n    • input\n:: ")
                            match option:
                                case 'prefix':
                                    cPREFIX = S.colors[input('Enter a color:\n::').upper()]
                        
                            
                case _:
                    backend.run(cmd)
