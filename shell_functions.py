import os
import signal
import subprocess

def show_help():
    print("\n\033[38;5;98mCommandes de gestion des utilisateurs:\033[0m")

    print("- whoami     : Afficher l'utilisateur actuel")
    print("- list users : lister tous les utilisateurs")

    print("\n\033[38;5;98mCommandes de gestion des fichiers:\033[0m")

    print("- cd <dir>   : Changer le répertoire courant vers <dir>")
    print("- ls         : Lister les fichiers et répertoires dans le répertoire courant")
    print("- read <file>: Lire le contenu d'un fichier")
    print("- mkdir <dir>: Créer un nouveau répertoire <dir>")
    print("- rmdir <dir>: Supprimer le répertoire <dir>")
    print("- mk <file>  : Créer un fichier vide <file>")
    print("- rm <file>  : Supprimer un fichier <file>")

    print("\n\033[38;5;98mCommandes de gestion des processus:\033[0m")
    
    print("- ps         : Lister tous les processus en cours")
    print("- start cmd : Lancer un processus <cmd>")
    print("- stop <pid> : Terminer un processus par son <pid>")

    print("\n\033[38;5;98mCommande d'informations système:\033[0m")
    
    print("- systeminfo : Afficher les informations système telles que les détails de l'OS, l'utilisation du CPU, etc.")
    print("- run <path> : Exécuter un script ou un fichier exécutable au chemin spécifié <path>.")
    
# Gestion des utilisateurs
def whoami():
    print(os.getlogin())

def list_users():
    result = subprocess.run(['net', 'user'], capture_output=True, text=True, check=True)
    print(result.stdout)
        
# Gestion des fichiers
def cd(args):
    try:
        os.chdir(args[1]) 
    except IndexError:
        print("cd : argument manquant")
    except FileNotFoundError:
        print("Aucun fichier ou répertoire de ce type.")

def ls(args):
    try:
        if len(args) > 1:
            path = args[1]
        else:
            path = '.'
        entries = os.listdir(path)
        print("\n".join(entries))
    except FileNotFoundError:
        print("Aucun fichier ou répertoire de ce type")

def read(args):
    try:
        with open(args[1], 'r') as file:
            print(file.read())
    except IndexError:
        print("read : argument manquant.")
    except FileNotFoundError:
        print("Aucun fichier de ce type")

def mkdir(args):
    try:
        os.mkdir(args[1])  
        print("Répertoire créé")
    except IndexError:
        print("mkdir : argument manquant")
    except FileExistsError:
        print("Le répertoire existe déjà.")

def rmdir(args):
    try:
        os.removedirs(args[1]) 
        print("Répertoire supprimé")
    except IndexError:
        print("rmdir : argument manquant")
    except FileNotFoundError:
        print("Le répertoire n'existe pas.")  

def mk(args):
    if len(args) < 2:  
        print("mk : argument manquant")
        return
    try:
        with open(args[1], 'w') as file:
            pass 
        print(f"Fichier '{args[1]}' créé.")
    except Exception as e: 
        print(f"Erreur lors de la création du fichier : {e}")

def rm(args):
    try:
        os.remove(args[1]) 
        print("Fichier supprimé")
    except IndexError:
        print("rm : argument manquant")
    except FileExistsError:
        print("Le répertoire n'existe pas.") 

# Gestion des processus 
def ps():
    os.system("tasklist")

def start(args):
    try:
        process = subprocess.Popen(args, shell=True)
        print(f"Processus '{args}' lancé")
        return process.pid
    except Exception as e:
        print(f"Erreur lors du lancement du processus : {e}")

def stop(args):
    try:
        pid = int(args[1])
        os.kill(pid, signal.SIGTERM)
        print(f"Processus {pid} terminé avec succès.")
    except ProcessLookupError:
        print(f"Le processus {pid} n'existe pas.")
    except PermissionError:
        print(f"Permission refusée pour tuer le processus {pid}.")
    except Exception as e:
        print(f"Erreur inconnue: {e}")

# Informations système 
def systeminfo():
    os.system("systeminfo")

def run_script(args):
    if len(args) < 2:
        print("run : argument de script manquant.")
        return
    script_path = args[1]
    if not os.path.isfile(script_path):
        print(f"Erreur : {script_path} introuvable.")
        return
    file_extension = os.path.splitext(script_path)[1]
    if file_extension == ".ps1":
        try:
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution du script PowerShell : {e}")
    else:
        print(f"Type de script non supporté : {file_extension}. Seuls les fichiers .ps1 sont supportés.")
