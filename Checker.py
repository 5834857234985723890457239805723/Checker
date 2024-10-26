import socket
import ssl
import os
import platform
from pystyle import Colorate, Colors

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  

def get_ip_and_port(site):
    try:
        ip_address = socket.gethostbyname(site)
        print(Colorate.Horizontal(Colors.purple_to_red,f"L'adresse IP de {site} est {ip_address}"))

        context = ssl.create_default_context()

        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=site) as s:
            s.connect((site, 443))
            print(Colorate.Horizontal(Colors.purple_to_red,f"{site} utilise HTTPS sur le port 443"))
            return ip_address, 443
    except ssl.SSLError:
        print(Colorate.Horizontal(Colors.purple_to_red,f"{site} utilise HTTP sur le port 80"))
        return ip_address, 80
    except socket.gaierror:
        return None, None
    except Exception as e:
        print(Colorate.Horizontal(Colors.purple_to_red,f"Erreur lors de la vérification : {e}"))
        return None, None

def display_ascii_art():
    ascii_art = """

                  _____ _               _             
                 /  __ \ |             | |            
                 | /  \/ |__   ___  ___| | _____ _ __ 
                 | |   | '_ \ / _ \/ __| |/ / _ \ '__|
                 | \__/\ | | |  __/ (__|   <  __/ |   
                  \____/_| |_|\___|\___|_|\_\___|_|                                                                           
    """
    colored_ascii_art = Colorate.Horizontal(Colors.purple_to_red, ascii_art)
    print(colored_ascii_art)

def display_menu():
    ascii_art = """
            \[+]====================================[+]/
             \      [+] By Ես գալիս եմ Կավկազից       /
               ---------------------------------------             
                      
    
                  [+]=====================[+]
                    [1] Tester un site web
                           [00] EXIT
                  [+]=====================[+] """
    colored_ascii_art = Colorate.Horizontal(Colors.purple_to_red, ascii_art)
    print(colored_ascii_art)

def main():
    while True:
        clear_screen()  
        display_ascii_art()
        display_menu()
        print()
        choix = input(Colorate.Horizontal(Colors.purple_to_red, "\nSélectionnez une option: "))

        if choix == "1":
            site = input(Colorate.Horizontal(Colors.purple_to_red, "Entrez le nom du site web (e.g., www.example.com): "))
            print("")
            ip_address, port = get_ip_and_port(site)
            if ip_address is None:
                print(Colorate.Horizontal(Colors.red_to_purple, "Erreur : Le nom de domaine est invalide ou introuvable."))
            input(Colorate.Horizontal(Colors.red_to_purple,"Appuyez sur Entrée pour revenir au menu..."))
        elif choix == "00":
            print(Colorate.Horizontal(Colors.red_to_purple,"Au revoir "))
        elif choix == "0":
            print(Colorate.Horizontal(Colors.red_to_purple,"Au revoir "))
            break     
        else:
            input(Colorate.Horizontal(Colors.red_to_purple,"Option invalide. Appuyez sur Entrée pour essayer à nouveau..."))

if __name__ == "__main__":
    main()
