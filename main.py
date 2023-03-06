import subprocess
from colorama import init
init()
from colorama import Fore, Back, Style
def win():
    print("введи ip того, кого хочешь взловать")
    print('чтобы узнать ip скинь ссылку http://вирус.ру тому, кого хочешь взломать')
    print('P.S. Для этого введи "отправить http://вирус.ру Джамшуту"')
    console = input("ip >>> ")
    if console == "отправить http://вирус.ру Джамшуту":
        print("ip Джамшута -> 192.888.0.255")
        console = input("ip >>> ")
        if console == "192.888.0.255":
            print('введи свой ip, чтобы его узнать введи "ifconfig"')
            console = input("ip >>> ")
            if console == "ifconfig":
                print("192.555.0.255")
                console = input("ip >>> ")
                if console == "192.555.0.255":
                    print("введи порт, например: 8080")
                    port = input("port >>> ")
                    print("взлом удался")
                    if console == "192.555.0.255":
                        print("введи порт, например: 8080")
                        port = input("port >>> ")
                        print("взлом удался")
                        subprocess.call("pause", shell=True)
def hack():
    print("введи ip того, кого хочешь взловать")
    print('чтобы узнать ip скинь ссылку http://вирус.ру тому, кого хочешь взломать')
    print('P.S. Для этого введи "отправить http://вирус.ру Джамшуту"')
    console = input("ip >>> ")
    if console == "отправить http://вирус.ру Джамшуту":
        print("ip Джамшута -> 192.888.0.255")
        console = input("ip >>> ")
        if console == "192.888.0.255":
            print('введи свой ip, чтобы его узнать введи "ifconfig"')
            console = input("ip >>> ")
            if console == "ifconfig":
                print("192.555.0.255")
                console = input("ip >>> ")
                if console == "192.555.0.255":
                    print("введи порт, например: 8080")
                    port = input("port >>> ")
                    print("взлом удался")
                    if console == "192.555.0.255":
                        print("введи порт, например: 8080")
                        port = input("port >>> ")
                        print("не получилось, выбери другую уязвимость")
print(" ___")
print(f"|{Fore.RED}@ @{Fore.WHITE}| Джамшут - письмо от херня.ру")
print("|_^_| - Надо хакнуть комп!!!")
print('чтобы открыть хакерское ПО введи "хакерское ПО"')
console = input(f"{Fore.RED}хакер@комп_хакера{Fore.WHITE}:{Fore.BLUE}~{Fore.WHITE}${Fore.GREEN}")
if console == "хакерское ПО":
    print("Добро пожаловать в хакерское ПО")
    print('если не шаришь напиши "help"')
    console = input(f"{Fore.RED}хакерское ПО >>> {Fore.GREEN}")
    if console == "help":
        print("посмотреть уязвимости - пу")
        print("юзать уязвимость - юу [имя_уязвимости] например: юу Трушный Гусь")
        print("чё дальше делать сам знаешь :)")
        console = input(f"{Fore.RED}хакерское ПО >>> {Fore.GREEN}")
        if console == "пу":
            print("имя: Мы ходили на завооод")
            print("имя: Взлом компа")
            print("имя: Hack PC")
            console = input(f"{Fore.RED}хакерское ПО >>> {Fore.GREEN}")
            if console == "юу Мы ходили на завооод":
                hack()
            elif console == "юу Взлом компа":
                win()
            elif console == "юу Hack PC":
                hack()
            else:
                print()
        elif console == "юу Мы ходили на завооод":
            hack()
        elif console == "юу Взлом компа":
            win()
        if console == "юу Hack PC":
            hack()
        else:
            print()
    elif console == "пу":
        print("имя: Мы ходили на завооод")
        print("имя: Взлом компа")
        print("имя: Hack PC")
        console = input(f"{Fore.RED}хакерское ПО >>> {Fore.GREEN}")
        if console == "юу Мы ходили на завооод":
            hack()
        elif console == "юу Взлом компа":
            win()
        elif console == "юу Hack PC":
            hack()
        else:
            print()
    elif console == "юу Мы ходили на завооод":
        hack()
    elif console == "юу Взлом компа":
        win()
    if console == "юу Hack PC":
        hack()
    else:
        print()
else:
    print()        
