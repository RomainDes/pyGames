import pygame
import pygame.freetype
import functions as f

# Obtenir les dimensions de l'écran de l'utilisateur
def get_screen_dimensions():
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return screen_width, screen_height



# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre principale (30% plus petit que l'écran de l'utilisateur)
screen_width, screen_height = get_screen_dimensions()
window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)

# Création de la fenêtre principale
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("PyGames")

# Création d'un style de police personnalisé pour les titres des jeux
title_font = pygame.freetype.Font(None, 14)

# Liste des fichiers py des jeux
games = f.getGames()

# Calcul des dimensions d'un rectangle de jeu en fonction du nombre de colonnes et de lignes souhaitées
num_columns = 4  # Nombre de colonnes dans la vitrine
num_rows = 3  # Nombre de lignes dans la vitrine
game_width = int(window_width / num_columns)
game_height = int(window_height / num_rows)

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            # Vérification des clics sur les boutons de jeu
            mouse_pos = pygame.mouse.get_pos()
            for i, game_name in enumerate(games):
                row = i // num_columns
                column = i % num_columns
                button_rect = pygame.Rect(column * game_width, row * game_height, game_width, game_height)
                if button_rect.collidepoint(mouse_pos):
                    f.open_game(game_name)

    # Affichage des boutons de jeu
    for i, game_name in enumerate(games):
        row = i // num_columns
        column = i % num_columns
        button_rect = pygame.Rect(column * game_width, row * game_height, game_width, game_height)

        # Dessiner le rectangle du bouton avec l'image en fond
        bg = pygame.image.load("../Games/Images/" + game_name + ".jpg")
        bg = pygame.transform.scale(bg, (game_width, game_height))
        window.blit(bg,button_rect)

    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()

