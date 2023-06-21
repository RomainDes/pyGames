from os import listdir

def getGames():
    fichiers = listdir("Games")
    fichiers_pythons = [fichier[:-3] for fichier in fichiers if fichier.endswith('.py')]
    return fichiers_pythons


def open_game(game_name):
    # Cette fonction est appelée lorsque vous cliquez sur l'un des rectangles de jeu
    # Ajoutez ici le code pour ouvrir le script correspondant au jeu sélectionné
    exec(open("Games/" + game_name + ".py").read())