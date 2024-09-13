import backend
import styling as S
import boots
boot_methods = [
    boots.Retro,
    boots.Lacy
]


boot_help_message = f"""{S.RST}{S.BLUE}
╔═════╦═════════════╦════════════╦═════════╗
║ KEY ║ APPLICATION ║ AUTHOR     ║ VERSION ║
╠═════╬═════════════╬════════════╬═════════╣
║ 0   ║ RETRO       ║ TOM MARTIN ║ 0.10    ║
║ 1   ║ LACY        ║ TOM MARTIN ║ 0.00    ║
║ 2   ║ --          ║ --         ║ 0.00    ║
║ 3   ║ --          ║ --         ║ 0.00    ║
║ 4   ║ --          ║ --         ║ 0.00    ║
║ 5   ║ --          ║ --         ║ 0.00    ║
║ 6   ║ --          ║ --         ║ 0.00    ║
║ 7   ║ --          ║ --         ║ 0.00    ║
║ 8   ║ --          ║ --         ║ 0.00    ║
╚═════╩═════════════╩════════════╩═════════╝
"""

print(f'{S.RED}ENTER BOOT KEY ({S.YELLOW + S.BOLD}!{S.RST + S.RED} FOR KEYS)')
while True:
    entry = input(f'{S.RST + S.BLUE + S.BOLD}>>:{S.BRIGHT_YELLOW}')

    match entry:
        case '!':
            print(boot_help_message)
            
        case _:
            boot_method = boot_methods[int(entry)]
            break

input(f'[ENTER] TO BOOT WITH {S.WHITE + S.UNDERLINE}{boot_method.__name__}{S.RST}')
backend.os.system('cls')
backend.boot = boot_method
boot_method.run()

