import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import platform



# Obtenir les dimensions de l'écran de l'utilisateur
def get_screen_dimensions():
    system = platform.system()
    if system == 'Windows':
        root = tk.Tk()
        root.withdraw()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
    elif system == 'Linux':
        try:
            from Xlib import display
            screen = display.Display().screen()
            screen_width = screen.width_in_pixels
            screen_height = screen.height_in_pixels
        except ImportError:
            raise Exception("La bibliothèque Xlib est requise pour obtenir les dimensions de l'écran sur Linux.")
    elif system == 'Darwin':
        try:
            from AppKit import NSScreen
            screen = NSScreen.mainScreen()
            screen_frame = screen.frame()
            screen_width = int(screen_frame.size.width)
            screen_height = int(screen_frame.size.height)
        except ImportError:
            raise Exception("Obtenir les dimensions de l'écran sur macOS n'est pas pris en charge actuellement.")
    else:
        raise Exception(f"Obtenir les dimensions de l'écran n'est pas pris en charge pour le système {system}.")

    return screen_width, screen_height


# Définir la taille de la fenêtre principale (30% plus petit que l'écran de l'utilisateur)
screen_width, screen_height = get_screen_dimensions()
window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)


def open_game(game_name):
    # Cette fonction est appelée lorsque vous cliquez sur l'un des rectangles de jeu
    # Ajoutez ici le code pour ouvrir le script correspondant au jeu sélectionné
    messagebox.showinfo("Ouverture du jeu", "Vous avez ouvert le jeu : " + game_name)


# Création de la fenêtre principale
window = tk.Tk()
window.title("PyGames")

# Ajuster la taille de la fenêtre principale
window.geometry(f"{window_width}x{window_height}")

# Création d'un style de police personnalisé pour les titres des jeux
title_font = tkfont.Font(family="Arial", size=14, weight="bold")

# Création de la vitrine des jeux
game_frame = tk.Frame(window)
game_frame.pack(expand=True, padx=20, pady=20)

# Liste des noms de jeux (remplacez-les par vos propres noms de jeux)
games = ["Jeu 1", "Jeu 2", "Jeu 3", "Jeu 4", "Jeu 5", "Jeu 6"]

# Calcul des dimensions d'un rectangle de jeu en fonction du nombre de colonnes et de lignes souhaitées
num_columns = 4  # Nombre de colonnes dans la vitrine
num_rows = 3  # Nombre de lignes dans la vitrine
game_width = int(window_width / num_columns)
game_height = int(window_height / num_rows)

# Positionnement des jeux dans la vitrine
for i, game_name in enumerate(games):
    row = i // num_columns
    column = i % num_columns

    game_button = ttk.Button(
        game_frame,
        text=game_name,
        command=lambda name=game_name: open_game(name)
    )
    game_button.grid(row=row, column=column, padx=10, pady=10)

    # Personnalisation de la police du titre
    game_button['style'] = 'GameButton.TButton'
    window.option_add('*TButton*font', title_font)

# Personnalisation du style des boutons de jeu
style = ttk.Style()
style.configure('GameButton.TButton', font=('Arial', 12))

# Lancement de la boucle principale
window.mainloop()
