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
        if event.type == pygame.KEYDOWN:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Vérification des clics sur les boutons de jeu
            mouse_pos = pygame.mouse.get_pos()
            for i, game_name in enumerate(games):
                row = i // num_columns
                column = i % num_columns
                button_rect = pygame.Rect(column * game_width + 20*(column+1), row * game_height + 20*(row+1), game_width, game_height)

                if button_rect.collidepoint(mouse_pos):
                    f.open_game(game_name)

    # Affichage des boutons de jeu
    for i, game_name in enumerate(games):
        row = i // num_columns
        column = i % num_columns

        #Création du bouton
        button_rect = pygame.Rect(column * game_width + 20*(column+1), row * game_height + 20*(row+1), game_width, game_height)
        pygame.draw.rect(window, (255, 255, 255), button_rect)


        # Charger l'image
        bg = pygame.image.load("Games/Images/" + game_name + ".jpg")
        # Calcul de la nouvelle largeur en conservant le rapport hauteur/largeur de l'image d'origine
        aspect_ratio = bg.get_width() / bg.get_height()
        new_width = int(window_height * aspect_ratio)
        # Mettre l'image à la bonne dimension
        bg = pygame.transform.scale(bg, ((game_height - 20) * aspect_ratio, game_height - 20))



        # Calculer les coordonnées pour placer l'image au centre du rectangle de destination
        center_image_x = game_width//2 - ((game_height - 20) * aspect_ratio) // 2


        image_rect = pygame.Rect((column * game_width) + center_image_x + 20*(column+1), row * game_height + 20*(row+1) + 10, game_width, game_height)


        # Dessiner le rectangle du bouton avec l'image en fond

        window.blit(bg,image_rect)


    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()

