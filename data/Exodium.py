from pystyle import *
from colorama import *
import os
import shutil
import time
import wmi

wf = wmi.WMI()

version = "V1.0"
currentVersionNumber = 2

def clear():
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")
	else:
		pass

def check_update():
	versionFile = requests.get("https://github.com/AstrenOX/Exodium/releases/latest/download/updater-version.txt")
	updatedVersion = int(versionFile.text)

	if updatedVersion > currentVersionNumber:
		return True
	else:
		return False

def self_update():
	updateManifestFile = requests.get("https://github.com/AstrenOX/Exodium/releases/latest/download/update-manifest.json")

def game_is_running():
	for process in wf.Win32_Process():
		if process.Name == "plutonium-bootstrapper-win32.exe":
			return True
	return False

def teletype_print(text, delay, addNewLine = True):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(delay)
    if addNewLine:
        print("\n", end = "", flush = True)

if os.name == "nt":
	os.system("mode con LINES=35 COLS=145")

def list(directory):
	entries = []

	entryIterator = os.scandir(directory)

	with entryIterator as dirEntries:
		for dirEntry in dirEntries:
			entries.append(dirEntry.name)

	return entries

def copy(sources, destination, sourcesPath = ""):
	for source in sources:
		shutil.copy(sourcesPath + source, destination)

def copyDirectory(source, destination):
	shutil.copytree(source, destination)

splash = """
 ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
 ║  ██████╗ ██╗     ██╗   ██╗████████╗ ██████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗    ███████╗██╗  ██╗ ██████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗ ║
 ║  ██╔══██╗██║     ██║   ██║╚══██╔══╝██╔═══██╗████╗  ██║██║██║   ██║████╗ ████║    ██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██║██║   ██║████╗ ████║ ║
 ║  ██████╔╝██║     ██║   ██║   ██║   ██║   ██║██╔██╗ ██║██║██║   ██║██╔████╔██║    █████╗   ╚███╔╝ ██║   ██║██║  ██║██║██║   ██║██╔████╔██║ ║
 ║  ██╔═══╝ ██║     ██║   ██║   ██║   ██║   ██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║    ██╔══╝   ██╔██╗ ██║   ██║██║  ██║██║██║   ██║██║╚██╔╝██║ ║
 ║  ██║     ███████╗╚██████╔╝   ██║   ╚██████╔╝██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║    ███████╗██╔╝ ██╗╚██████╔╝██████╔╝██║╚██████╔╝██║ ╚═╝ ██║ ║
 ║  ╚═╝     ╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ║
 ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
	    	(Appuyez sur entrer)                                                                                      (Appuyez sur entrer)

                                                                 :%@&&@%:
                                                               :$§§&$$&§§$:
                                                              :#§&:    :&§#:
                                                             :/§$        $§/:
                                                            :#§@          @§#:
                                                            $§#           :#§$
                                            :*$@&&&&@$$%*!::§§!            !§§::!*%$$@&&&&@$*:
                                          :@//#@@$$@@&##////§/*!:        :!*/§////##&@@$$@@#//@:
                                          @§&:          :!*§§#/§/#$*::*$#/§/#§§*!:          :&§@
                                          &§@             !§/: :*@§§§§§§@*: :/§!             @§&
                                          !§§*            $§&:*@#//&%%&//#@*:&§$            *§§!
                                           */§$           &§//§#$!:    :!$#§//§&           $§/*
                                            :&§#*      :%&§§#%:            :%#§§&%:      *#§&:
                                              %/§&!  *@/§&§§*                *§§&§/@*  !&§/%
                                               :%/§&#§#%: /§!                !§/ :%#§#&§/%:
                                                :@§§§§$:  /§!                *§/  :$§§§§@:
                                              :$§§@!!@§§&*/§*                *§/*&§§@!!@§§$:
                                             %/§@!    :%#§§§$:              :$§§§#%:    !@§/*
                                           :@§#*         :&§§/&%!        !%&/§§&:         *#§@:
                                          :&§&:           %§#%&/§#$*::*$#§/&%#§%           :&§&:
                                          $§&             !§§:  *@§§§§§§@*  :§§!             #§$
                                          &§$              #§@$&///&$$&///&$@§#              $§&
                                          !/§&%!!!!!!*%$@&#§§§#@%!:    :!%@#§§§#&@$%*!!!!!!%&§/!
                                           :%&#///////##&$%*/§*            *§/*%$&##///////#&%:
                                               ::::::       %§/:          :/§*       ::::::
                                                             @§&          &§@
                                                             :&§&:      :&§&:
                                                              :@§#*    *#§@:
                                                                *#§/&&/§#*
                                                                  !%$$%!
"""

glovesDirectory = "../t6r/data/images"
camouflagesDirectory = "../t6r/data/images"
modsDirectory = "../t6r/data/maps"

def install_gloves(type):
	if type == "default":
		filesPath = "../data/gloves"
		filelist = list(filesPath)
	elif type == "custom":
		filesPath = "../data/glovespf"
		filelist = list(filesPath)

	copy(filelist, glovesDirectory, filesPath)

	if game_is_running():
		print("Nous avons détecté que votre jeu est ouvert, n'oubliez pas de le relancer pour y appliquer les modifications apportées. ")
		input()

	print("Retour au menu principal...")
	time.sleep(3)

	main_menu()

def install_camouflages(type):
	if type == "default":
		filesPath = "../data/camo"
		filelist = list(filesPath)
	elif type == "custom":
		filesPath = "../data/camopf"
		filelist = list(filesPath)

	copy(filelist, camouflagesDirectory, filesPath)

	if game_is_running():
		print("Nous avons détecté que votre jeu est ouvert, n'oubliez pas de le relancer pour y appliquer les modifications apportées. ")
		input()

	print("Retour au menu principal...")
	time.sleep(3)

	main_menu()

modMenusDirectory = "../data/mods"

def install_mod():
	clear()
	print(Colorate.Horizontal(Colors.blue_to_red,"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  ██████╗ ██╗     ██╗   ██╗████████╗ ██████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗    ███████╗██╗  ██╗ ██████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗ ║
║  ██╔══██╗██║     ██║   ██║╚══██╔══╝██╔═══██╗████╗  ██║██║██║   ██║████╗ ████║    ██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██║██║   ██║████╗ ████║ ║
║  ██████╔╝██║     ██║   ██║   ██║   ██║   ██║██╔██╗ ██║██║██║   ██║██╔████╔██║    █████╗   ╚███╔╝ ██║   ██║██║  ██║██║██║   ██║██╔████╔██║ ║
║  ██╔═══╝ ██║     ██║   ██║   ██║   ██║   ██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║    ██╔══╝   ██╔██╗ ██║   ██║██║  ██║██║██║   ██║██║╚██╔╝██║ ║
║  ██║     ███████╗╚██████╔╝   ██║   ╚██████╔╝██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║    ███████╗██╔╝ ██╗╚██████╔╝██████╔╝██║╚██████╔╝██║ ╚═╝ ██║ ║
║  ╚═╝     ╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
	"""))
	print("""
""" + Fore.BLUE + """ ╔══════════════════════════════╗
""" + Fore.BLUE + """ ║             !%%!             ║
""" + Fore.BLUE + """ ║           :@@**@@:           ║""" + Fore.MAGENTA + """Created By """ + Fore.BLUE + "Plutonium-T6-France " + Fore.MAGENTA + """/ DISCORD : """ + Fore.YELLOW + """https://discord.gg/6BCRW7NNuy
""" + Fore.BLUE + """ ║           &@    @&           ║
""" + Fore.BLUE + """ ║  :*****!:$#      #%:!*****:  ║   """ + Fore.YELLOW + """1""" + Fore.CYAN + """ - JiggyV777  | Multijoueur
""" + Fore.BLUE + """ ║ !#%***%%$§&$*!!*$&§$%%***%#! ║
""" + Fore.BLUE + """ ║ */:     !/*@/&&/$*/!     :/* ║   """ + Fore.YELLOW + """2""" + Fore.CYAN + """ - BossamV5 | Multijoueur
""" + Fore.BLUE + """ ║  %#%   !@/$*:  :*$/@!   %#%  ║
""" + Fore.BLUE + """ ║   !@&$@$&&        &&$@$&@!   ║   """ + Fore.YELLOW + """3""" + Fore.CYAN + """ - Hells Vangance V4 | Zombie
""" + Fore.BLUE + """ ║    %#@&%@&        &@%&&#%    ║
""" + Fore.BLUE + """ ║  !#$: :*&/%!    !%/&*: :$#!  ║
""" + Fore.BLUE + """ ║ !/!     !/%@#@@#@%/!     !/! ║
""" + Fore.BLUE + """ ║ */*!!!!*%/&$$%%$$&/%*!!!!*/* ║
""" + Fore.BLUE + """ ║  !%$$$%%*%/:    :/%*%%$$$%!  ║
""" + Fore.BLUE + """ ║           @&:  :&@           ║
""" + Fore.BLUE + """ ║            $&%%&$            ║
""" + Fore.BLUE + """ ║             :**:             ║
""" + Fore.BLUE + """ ╚══════════════════════════════╝
	""")
	choix = input("Vos Choix → ")

	filesPath = "../data/mods"

	if choix == "1":
		if os.path.exists(modsDirectory + "/mp"):
			shutil.rmtree(modsDirectory + "/mp")
		copyDirectory(filesPath + "/jiggy/mp", modsDirectory + "/mp")
	elif choix == "2":
		if os.path.exists(modsDirectory + "/mp"):
			shutil.rmtree(modsDirectory + "/mp")
		copyDirectory(filesPath + "/bossam/mp", modsDirectory + "/mp")
	elif choix == "3":
		if os.path.exists(modsDirectory + "/mp"):
			shutil.rmtree(modsDirectory + "/mp")
		copyDirectory(filesPath + "/hellsv/mp", modsDirectory + "/mp")
	elif choix == "4":
		if os.path.exists(modsDirectory + "/mp"):
			shutil.rmtree(modsDirectory + "/mp")
	else:
		install_mod()

	clear()
	teletype_print("Mod Menu injecter avec succes !", 0.05, True)

	if game_is_running():
		print("Nous avons détecté que votre jeu est ouvert, n'oubliez pas de le relancer pour y appliquer les modifications apportées. ")
		input()

	teletype_print("Retour au menu principal...", 0.05, True)
	time.sleep(2)

	main_menu()

def main_menu():
	print(Colorate.Horizontal(Colors.blue_to_red,"""
	 ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
	 ║  ██████╗ ██╗     ██╗   ██╗████████╗ ██████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗    ███████╗██╗  ██╗ ██████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗ ║
	 ║  ██╔══██╗██║     ██║   ██║╚══██╔══╝██╔═══██╗████╗  ██║██║██║   ██║████╗ ████║    ██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██║██║   ██║████╗ ████║ ║
	 ║  ██████╔╝██║     ██║   ██║   ██║   ██║   ██║██╔██╗ ██║██║██║   ██║██╔████╔██║    █████╗   ╚███╔╝ ██║   ██║██║  ██║██║██║   ██║██╔████╔██║ ║
	 ║  ██╔═══╝ ██║     ██║   ██║   ██║   ██║   ██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║    ██╔══╝   ██╔██╗ ██║   ██║██║  ██║██║██║   ██║██║╚██╔╝██║ ║
	 ║  ██║     ███████╗╚██████╔╝   ██║   ╚██████╔╝██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║    ███████╗██╔╝ ██╗╚██████╔╝██████╔╝██║╚██████╔╝██║ ╚═╝ ██║ ║
	 ║  ╚═╝     ╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ║
	 ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
	"""))
	print("""
""" + Fore.BLUE + """  ╔══════════════════════════════╗
""" + Fore.BLUE + """  ║             """ + Fore.WHITE + """!%%!             """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║           """ + Fore.WHITE + """:@@**@@:           """ + Fore.BLUE + """║      """ + Fore.MAGENTA + """Created By """ + Fore.BLUE + "Plutonium-T6-France " + Fore.MAGENTA + """/ DISCORD : """ + Fore.YELLOW + """https://discord.gg/6BCRW7NNuy
""" + Fore.BLUE + """  ║           """ + Fore.WHITE + """&@    @&           """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║  :*****!:""" + Fore.WHITE + """$#      #%""" + Fore.RED + """:!*****:  """ + Fore.BLUE + """║         """ + Fore.YELLOW + """1""" + Fore.CYAN + """ - Désactiver ou Rétablir Gants Personnalisée \"Plutonium France\"
""" + Fore.BLUE + """  ║ !#%***%%""" + Fore.WHITE + """$§&$*!!*$&§""" + Fore.RED + """$%%***%#! """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║ */:     """ + Fore.WHITE + """!/*@/&&/$*/!""" + Fore.RED + """     :/* """ + Fore.BLUE + """║         """ + Fore.YELLOW + """2""" + Fore.CYAN + """ - Désactiver ou Rétablir Camouflage Personnalisée \"Plutonium France\"
""" + Fore.BLUE + """  ║  %#%   """ + Fore.WHITE + """!@/$*:  :*$/@""" + Fore.RED + """!   %#%  """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║   !@&$@""" + Fore.WHITE + """$&&        &&""" + Fore.RED + """$@$&@!   """ + Fore.BLUE + """║         """ + Fore.YELLOW + """3""" + Fore.CYAN + """ - Injecteur Mod Menu [Partie Personnalisée] [5]
""" + Fore.BLUE + """  ║    %#@&""" + Fore.WHITE + """%@&        &@""" + Fore.RED + """%&&#%    """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║  !#$: :""" + Fore.WHITE + """*&/%!    !%/&""" + Fore.RED + """*: :$#!  """ + Fore.BLUE + """║         """ + Fore.YELLOW + """4""" + Fore.CYAN + """ - Injecteur Camouflage Personnalisée [18]
""" + Fore.BLUE + """  ║ !/!     """ + Fore.WHITE + """!/%@#@@#@%/!""" + Fore.RED + """     !/! """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║ */*!!!!*""" + Fore.WHITE + """%/&$$%%$$&/""" + Fore.RED + """%*!!!!*/* """ + Fore.BLUE + """║         """ + Fore.YELLOW + """5""" + Fore.CYAN + """ - Injecteur Gants Personnalisée [12]
""" + Fore.BLUE + """  ║  !%$$$%%""" + Fore.WHITE + """*%/:    :/%""" + Fore.RED + """*%%$$$%!  """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║           """ + Fore.WHITE + """@&:  :&@""" + Fore.RED + """           """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║            """ + Fore.WHITE + """$&%%&$ """ + Fore.RED + """           """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ║             """ + Fore.WHITE + """:**: """ + Fore.RED + """            """ + Fore.BLUE + """║
""" + Fore.BLUE + """  ╚══════════════════════════════╝
	""")
	choix = input("Vos Choix → ")

	if choix == "1":
		action = input("Souhaitez-vous [S]UPPRIMER ou [R]ETABLIR les gants personnalisés \"Plutonium France\" ? ")
		if action.upper() == "S":
			install_gloves("default")
		elif action.upper() == "R":
			install_gloves("custom")
	elif choix == "2":
		action = input("Souhaitez-vous [S]UPPRIMER ou [R]ETABLIR les camouflages personnalisés \"Plutonium France\" ? ")
		if action.upper() == "S":
			install_camouflages("default")
		elif action.upper() == "R":
			install_camouflages("custom")
	elif choix == "3":
		install_mod()
	elif choix == "4":
		pass
	elif choix == "5":
		pass
	else:
		pass
	main_menu()

if os.name == "nt":
	os.system("mode con LINES=50 COLS=145")
Anime.Fade((splash), Colors.red_to_blue, Colorate.Vertical, interval=0.025, enter=True)
if os.name == "nt":
	os.system("mode con LINES=30 COLS=145")

if len(os.sys.argv) < 2:
	main_menu()
else:
	argv1 = os.sys.argv[1]
	if os.path.exists(argv1):
		install_mod(argv1)
	else:
		main_menu()
