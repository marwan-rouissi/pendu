import pygame
from pygame.locals import *
import time
import random

def difficulty():

    # stock les coor (x,y) dans une variable sous forme de tuple
    mouse = pygame.mouse.get_pos()
    if easy_btn.isOver(mouse):
        difficulty_state = "easy"
        # print(difficulty_state)
    elif medium_btn.isOver(mouse):
        difficulty_state = "medium"
        # print(difficulty_state)
    elif hard_btn.isOver(mouse):
        difficulty_state = "hard"
        # print(difficulty_state)
    return difficulty_state

# fonction pour choisir un mot random depuis la liste de jeu
def display_scores():
    
    with open("scores.txt", "r", encoding="UTF-8") as file:
        text = file.read()

        return(text)

# fonction  pour ajouter nom du joueur dans fichier scores.txt
def add_score(name):
    # variable globale du score du joueur
    global score_var

    with open("scores.txt", "a", encoding="UTF-8") as file:
        element_to_add = name +" : "+ str(score_var) + " mots " + "(mode: " + difficulty_var + ")"
        # element_to_add = (name , score_var)
        file.write(element_to_add)
        file.write("\n")

# fonction pour choisir un mot random depuis la liste de jeu
def random_word(difficulty_var):

    # si difficultÃ© facile
    if difficulty_var == 'easy':
        # ouverture du fichier de mots faciles
        with open("mots-faciles.txt", "r", encoding="UTF-8") as file:
            text = file.read()
            words = text.split()
        
    # sinon si difficultÃ© moyenne    
    elif difficulty_var == 'medium':
        # ouverture du fichier de mots moyens
        with open("mots-inter.txt", "r", encoding="UTF-8") as file:
            text = file.read()
            words = text.split()

    # sinon si difficultÃ© difficile
    elif difficulty_var == 'hard':
        # ouverture du fichier de mots difficiles
        with open("mots-difficiles.txt", "r", encoding="UTF-8") as file:
            text = file.read()
            words = text.split()

    #selection alÃ©atoire d'un mot depuis le fichier ouvert
    word_pos = random.randint(0, len(words)-1)
    # print("mot numÃ©ro:", (word_pos)+1)

    # la fonction prend pour valeur le mot piochÃ©
    return(words[word_pos])

# fonction pour ajouter un nouveau mot Ã  la liste de jeu
def add_word(mot):
    #si le mot ajoutÃ© est (strictement) infÃ©rieur Ã  6 caractÃ¨res
    if len(mot) < 6:
        # ajouter le mot au fichier mots-faciles.txt
        with open("mots-faciles.txt", "a", encoding="UTF-8") as txt:
            txt.write("\n")
            txt.write(mot)
    # sinon si le mot ajoutÃ© est -strictement supÃ©rieur Ã  11 caractÃ¨res
    elif len(mot) > 11:
        # ajouter le mot au fichier mots-difficiles.txt
        with open("mots-difficiles.txt", "a", encoding="UTF-8") as txt:
            txt.write("\n")
            txt.write(mot)
    #sinon 
    else:
        #ajouter le mot au fichier mots-inter.txt
        with open("mots-inter.txt", "a", encoding="UTF-8") as txt:
            txt.write("\n")
            txt.write(mot)


class Difficuty:
    # crÃ©ation d'un objet Difficulty (choix de la difficultÃ©)

    def __init__(self):

        title = "Mode "

        # police du texte 
        font = pygame.font.SysFont(None, 60)
        # 
        # image du titre Ã  afficher sur l'Ã©cran
        img_title = font.render(title, True, BLACK)
        rect_title = img_title.get_rect()
        rect_title.topleft = (20, 20)

        running = True

        # boucle princiale de l'affichage du menu/objet Ajouter
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                
                # check si la souris est cliquÃ©e
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # variable globale pour terminant la dificultÃ© de jeu
                    global difficulty_var

                    # si le bouton easy est cliquÃ©
                    if easy_btn.isOver(mouse):

                        # stocker la valeur retournÃ©e par la fonction difficulty() qui derterminera le mode de jeu choisi dans la variable difficulty_var        
                        difficulty_var = difficulty()
                        
                        # lancer le jeu
                        Game()
                    # si le bouton easy est cliquÃ©
                    if medium_btn.isOver(mouse):

                        # stocker la valeur retournÃ©e par la fonction difficulty() qui derterminera le mode de jeu choisi dans la variable difficulty_var
                        difficulty_var = difficulty()
                        
                        # lancer le jeu
                        Game()

                    # si le bouton easy est cliquÃ©
                    if hard_btn.isOver(mouse):

                        # stocker la valeur retournÃ©e par la fonction difficulty() qui derterminera le mode de jeu choisi dans la variable difficulty_var
                        difficulty_var = difficulty()
                        
                        # lancer le jeu
                        Game()
                    
                    #si le bouton sortir est cliquÃ©
                    if exit_btn.isOver(mouse):
                        # retour au menu
                        Menu().run()

            # affichage des Ã©lements (scores) Ã  l'Ã©cran
            screen.fill(pygame.Color('white'))
            #
            screen.blit(img_title, rect_title)
            # bouton menu
            easy_btn.draw(screen, 5)
            #
            medium_btn.draw(screen, 5)
            #
            hard_btn.draw(screen, 5)
            #
            exit_btn.draw(screen, 5)

            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()

            # MAJ affichage
            pygame.display.update()

class Score:
    # crÃ©ation d'un objet Score pour la consulatation des scores enregistrÃ©s 
    def __init__(self):

        # recupÃ©ration du fichier scores.txt depuis sa fonciton
        text = display_scores()
        
        # police du texte 
        font = pygame.font.SysFont(None, 60)
        #
        # image du mot Ã  ajouter 
        img = font.render(display_scores(), True, WHITE)
        rect_text = img.get_rect()
        rect_text.topleft = (250, 250)
        #
        running = True

        # fonction pour afficher le text score.txt line par ligne
        def blit_text(surface, text, pos, font, color=pygame.Color('black')):

            # variable pour rÃ©cuperer chaque ligne sous forme d'objet dans une liste
            words = [word.split(' ') for word in text.splitlines()]
            
            # variable pour la largeur de l'espacement entre chaque mot
            space = font.size(' ')[0] 
            # variable position dÃ©finie par coordonnÃ©es x et y 
            x, y = pos
            
            # pour chaque objet (line) dans la liste (words)
            for line in words:

                # pour chaque mot/string (word) dans l'objet (ligne)
                for word in line:
                    
                    # variable de la surface du mot (string)
                    word_surface = font.render(word, 0, color)
                    # dÃ©finition de la largeur ainsi que la hauteur du mot (string)
                    word_width, word_height = word_surface.get_size()
                
                    # affichage du mot (string)
                    surface.blit(word_surface, (x, y))
                    # incrÃ©mentation de la position x ainsi qu'ajout d'un espace
                    x += word_width + space
                
                # reset de la position x
                x = pos[0]
                # retour Ã  la ligne
                y += word_height

        # boucle princiale de l'affichage du menu/objet Ajouter
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                
                # check si la souris est cliquÃ©e
                if event.type == pygame.MOUSEBUTTONDOWN:

                # si le bouton menu est cliquÃ©
                    if exit_btn.isOver(mouse):

                        # l'objet menu est appelÃ© via sa fonction run()
                        Menu().run()

            # affichage des Ã©lements (scores) Ã  l'Ã©cran
            screen.fill(pygame.Color('white'))
            blit_text(screen, text, (130, 20), font)
            # bouton menu
            exit_btn.draw(screen, 5)

            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()

            # MAJ affichage
            pygame.display.update()

class Ajouter_nom:
    # crÃ©ation d'un objet pour le menu Ajouter un mot

    def __init__(self):

        # variable texte, invitation Ã  ajouter nom du joueur
        add_invite = "Entrez votre nom: "
        # variable pour stocker le nom du joueur Ã  ajouter
        name = ''
        # police du texte 
        font = pygame.font.SysFont(None, 60)
        #
        # image du mot Ã  ajouter 
        img = font.render(name, True, WHITE)
        rect_text = img.get_rect()
        rect_text.topleft = (20, 100)
        #
        # image du texte d'invitation
        img_invite = font.render(add_invite, True, WHITE)
        rect_invite = img_invite.get_rect()
        rect_invite.topleft = (20, 20)

        # curseur
        cursor = Rect(rect_text.topright, (3, rect_text.height))

        # variable de vÃ©rification d'Ã©tat (actif/inactif)
        running = True

        # variable arriÃ¨re plan
        background = BLACK

        # boucle princiale de l'affichage du menu/objet Ajouter
        while running:

            for event in pygame.event.get():
                # si fermeture demandÃ©e (bouton croix, alt+f4, ..) 
                if event.type == QUIT:
                    # variable running n'est plus active, retour au menu
                    running = False
                    # pygame.quit()

                # pour tout event du clavier
                if event.type == KEYDOWN:

                    # si la touche "effacer"/"retour en arriÃ¨re" 
                    if event.key == K_BACKSPACE:

                        # si longueur du mot > Ã  0
                        if len(name)>0:

                            # effacer le dernier caractÃ¨re
                            name = name[:-1]
                    # sinon
                    else:
                        # incrÃ©mentÃ© au mot tout nouvel event du clavier
                        name += event.unicode

                    # MAJ affichage Ã  l'Ã©cran
                    img = font.render(name, True, WHITE)
                    rect_text.size=img.get_size()

                    # curseur
                    cursor.topleft = rect_text.topright

                # check si la souris est cliquÃ©e
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # si le bouton ajouter est cliquÃ©
                    if add_btn.isOver(mouse):
                        # si le nom Ã  ajouter est supÃ©rieur Ã  une lettre
                        if len(name)>0:
                            # appel de la fonction add_score (ajouter le nom du joueur ainsi que son score au fichier scores.txt)
                            add_score(name)
                            # retour au menu
                            Menu().run()

            # Ã©lÃ©ments Ã  afficher Ã  l'Ã©cran du menu Ajouter
            screen.fill(background)
            screen.blit(img, rect_text)
            screen.blit(img_invite, rect_invite)
            add_btn.draw(screen, 5)

            # condition de timing pour le curseur
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, RED, cursor)
            
            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()
            
            # MAJ affichage de l'Ã©cran
            pygame.display.update()


class Ajouter_mot:
    # crÃ©ation d'un objet pour le menu Ajouter un mot

    def __init__(self):

        # variable texte, invitation Ã  ajouter un nouveau mot
        add_invite = "Ajouter un mot: "
        # variable pour stocker le nouveau mot Ã  ajouter
        text = ''
        # police du texte 
        font = pygame.font.SysFont(None, 60)
        #
        # image du mot Ã  ajouter 
        img = font.render(text, True, WHITE)
        rect_text = img.get_rect()
        rect_text.topleft = (20, 100)
        #
        # image du texte d'invitation
        img_invite = font.render(add_invite, True, WHITE)
        rect_invite = img_invite.get_rect()
        rect_invite.topleft = (20, 20)

        # curseur
        cursor = Rect(rect_text.topright, (3, rect_text.height))

        # variable de vÃ©rification d'Ã©tat (actif/inactif)
        running = True

        # variable arriÃ¨re plan
        background = GRAY

        # boucle princiale de l'affichage du menu/objet Ajouter
        while running:

            for event in pygame.event.get():
                # si fermeture demandÃ©e (bouton croix, alt+f4, ..) 
                if event.type == QUIT:
                    # variable running n'est plus active, retour au menu
                    running = False
                    # pygame.quit()

                # pour tout event du clavier
                if event.type == KEYDOWN:

                    # si la touche "effacer"/"retour en arriÃ¨re" 
                    if event.key == K_BACKSPACE:

                        # si longueur du mot > Ã  0
                        if len(text)>0:

                            # effacer le dernier caractÃ¨re
                            text = text[:-1]
                    # sinon
                    else:
                        # incrÃ©mentÃ© au mot tout nouvel event du clavier
                        text += event.unicode

                    # MAJ affichage Ã  l'Ã©cran
                    img = font.render(text, True, WHITE)
                    rect_text.size=img.get_size()

                    # curseur
                    cursor.topleft = rect_text.topright

                # check si la souris est cliquÃ©e
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # si le bouton ajouter est cliquÃ©
                    if add_btn.isOver(mouse):
                        # si le mot Ã  ajouter est supÃ©rieur Ã  une lettre
                        if len(text)>1:

                            # le mot Ã  l'Ã©cran est ajoutÃ© Ã  la liste de mots (fonction add_word())
                            add_word(text)
                            # retour au menu une fois le mot ajoutÃ©
                            Menu().run()

                    # si le bouton menu est cliquÃ©
                    if exit_btn.isOver(mouse):

                        # l'objet menu est appelÃ© via sa fonction run()
                        Menu().run()

            # Ã©lÃ©ments Ã  afficher Ã  l'Ã©cran du menu Ajouter
            screen.fill(background)
            screen.blit(img, rect_text)
            screen.blit(img_invite, rect_invite)
            add_btn.draw(screen, 5)
            exit_btn.draw(screen, 5)
            # condition de timing pour le curseur
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, RED, cursor)
            
        # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()
            
            # MAJ affichage de l'Ã©cran
            pygame.display.update()


class Game:
    # crÃ©ation de la boucle de jeu
    
    def __init__(self):
        
        # variable titre 
        title = "Le Pendu "
        
        difficulty_state = difficulty_var

        # variable mot alÃ©atoire piochÃ© depuis la liste de mots
        word  = random_word(difficulty_var)
        # variable mot masquÃ© Ã  afficher
        masked_word = len(word) * "_"
        # variables 
        faute = "faute(s): "
        #
        score_txt = "score: "
        #
        global score_var
        score_var = 0
        #
        score = score_txt + str(score_var)
        #
        game_over = ""
        #
        strike = 0
        

        # police du texte 
        font = pygame.font.SysFont(None, 60)
        # image du mot cachÃ© Ã  afficher sur l'Ã©cran 
        img_word = font.render(masked_word, True, BLACK)
        rect_word = img_word.get_rect()
        rect_word.topleft = (50, 250)
        # 
        # image du titre Ã  afficher sur l'Ã©cran
        img_title = font.render(title, True, BLACK)
        rect_title = img_title.get_rect()
        rect_title.topleft = (20, 20)
        # 
        # image du nombre de fautes Ã  afficher sur l'Ã©cran
        img_faute = font.render(faute, True, BLACK)
        rect_faute = img_faute.get_rect()
        rect_faute.topleft = (20, 450)
        # 
        # image du score Ã  afficher sur l'Ã©cran
        img_score = font.render(score, True, BLACK)
        rect_score = img_score.get_rect()
        rect_score.topleft = (580, 20)
        #
        # image du message de fin de partie Ã  afficher sur l'Ã©cran
        img_gameOver = font.render(game_over, True, BLACK)
        rect_gameOver = img_gameOver.get_rect()
        rect_gameOver.topleft = (300, 250)
        #
        # image potence
        pot_img = potence

        # variable de vÃ©rification d'Ã©tat (actif/inactif)
        running = True

        # fonction pour espacer les caractrÃ¨res entre eux lors de l'affichager sur l'Ã©cran
        def space_text(surface, text, pos, font, color=BLACK):
                # 
                # words = text
                space = font.size(' ')[0]  # The width of a space.
                # max_width, max_height = surface.get_size()
                x, y = pos
                for line in text:
                    for word in line:
                        word_surface = font.render(word, 0, color)
                        word_width, word_height = word_surface.get_size()
                       
                    surface.blit(word_surface, (x, y))
                    x += word_width + space

        while running:
        # boucle principale

            for event in pygame.event.get():
                
                difficulty_state = difficulty_state

                # si la croix (fermer page) est cliquÃ©e ou alt+f4 ..  
                if event.type == pygame.QUIT:

                    ## variable running n'est plus active, retour au menu
                    running = False
                    # fermeture du programme
                    pygame.quit()
                
                # si toute les lettres du mot Ã  deviner sont rÃ©velÃ©es 
                elif word == masked_word and strike < 7:
                    
                    # variable victoire
                    game_over = "BRAVO !"
                    # Affichage du msg victoire Ã  l'Ã©cran 
                    
                    img_gameOver = font.render(game_over, True, RED)
                    
                    # si mot trouvÃ© 
                    if game_over == "BRAVO !":
                        # RESET de l'Ã©cran en gardant le score incrÃ©mentÃ©
                        strike = 0
                        
                        # incrÃ©mentation du score +1
                        score_var += 1 

                        # conditon pour rendre l'incrÃ©mentation du score clean aprÃ¨s le 10e points 
                        if score_var > 9:
                            score = score[:-2] + str(score_var)
                        else:    
                            # MAJ du message de score
                            score = score[:-1] + str(score_var)
                        
                        # MAJ de l'affichage du message Ã  l'Ã©cran
                        img_score = font.render(score, True, RED)
                        game_over = ""
                        img_gameOver = font.render(game_over, True, RED)
                        
                        # variable du mot random Ã  jouer pour la partie suivante
                        word = random_word(difficulty_var)
                        
                        # variable mot masquÃ© Ã  afficher
                        masked_word = len(word) * "_"
                        
                        # image du mot cachÃ© Ã  afficher sur l'Ã©cran 
                        img_word = font.render(masked_word, True, BLACK)
             
                        # variable fautes
                        faute = "faute(s): "
                        # MAJ du message de tentatives Ã©chouÃ©e

                        # image du nombre de fautes Ã  afficher sur l'Ã©cran
                        img_faute = font.render(faute, True, BLACK)

                        # RESET image potence
                        pot_img = potence
                        screen.blit(pot_img, (600, 150))
                       
                
                # sinon si toutes les lettres du mots Ã  deviner ne sont pas rÃ©velÃ©es et que le nombre d'essaies est Ã©gal Ã  7 ou 
                elif word != masked_word and strike == 7 or word != masked_word and game_over != "BRAVO !" and strike ==7:
                        
                        # variable game over
                        game_over = "GAME OVER !"
                        # Affichage du msg de game over Ã  l'Ã©cran
                        img_gameOver = font.render(game_over, True, RED)
                        # si jeu terminÃ©
                        if game_over == "GAME OVER !" and score_var > 2:
                            # appel de l'objet Ajouter_nom
                            Ajouter_nom()

                # pour tout event (touche clavier)
                if event.type == pygame.KEYDOWN:
                    # print(event)
                    
                    # si la touche pressÃ©e n'est pas prÃ©sente dans le mot jouÃ© et que le dÃ©compte de tentatives est infÃ©rieur Ã  7
                    if event.unicode not in word and strike < 7 and game_over == "":
                        
                        # variable strike incrÃ©mentÃ©e d'1 
                        strike += 1
                        
                        # # MAJ du message de tentatives Ã©chouÃ©e et affichage des mauvaises lettres jouÃ©es 
                        # faute = faute[:-1] + str(strike)

                        faute = faute + event.unicode + " "

                        # condition de MAJ de l'image du pendu 
                        if strike == 1:
                            pot_img = pendu_1
                        if strike == 2:
                            pot_img = pendu_2
                        if strike == 3:
                            pot_img = pendu_3
                        if strike == 4:
                            pot_img = pendu_4
                        if strike == 5:
                            pot_img = pendu_5
                        if strike == 6:
                            pot_img = pendu_6
                        if strike == 7:
                            pot_img = pendu_7
                        
                        # MAJ du message dans la fenÃªtre
                        img_faute = font.render(faute, True, RED)
                

                    # pour chacune des lettres prÃ©sentent dans la variable word
                    for char in word:

                        # si la touche pressÃ©e est prÃ©sente dans le mot jouÃ© et que le nombre de tentatives est infÃ©rieur Ã  7 
                        if event.unicode != char and strike < 7:
                            pass

                        # si la touche pressÃ©e est prÃ©sente dans le mot jouÃ© et que le nombre de tentatives est infÃ©rieur Ã  7 
                        if event.unicode == char and strike < 7:

                            # dÃ©commanter les lignes suivantes pour tester le code sans avoir Ã  jouer et deviner les mots
                            
                            # # print la lettre
                            # print("lettre jouÃ©e:", char)
                            # # print le mot
                            # print("mot Ã  deviner:", word)

                            # pour i dans l'interval (longueur du mot)
                            for i in range(len(word)):
                                
                                # si la lettre est prÃ©sente dans le mot jouÃ©
                                if word[i] == char:
                                    
                                    # mot masquÃ© est remplacÃ©/MAJ Ã  l'endroit oÃ¹ la lettre existe 
                                    masked_word = masked_word[:i]+char+masked_word[i+1:]
                                    # MAJ de l'affichage du mot masquÃ© sur l'Ã©cran
                                    img_word = font.render(masked_word, True, BLACK)
                                      
                # pour tout event (souris)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # si bouton start cliquÃ©
                    if new_btn.isOver(mouse):
                        # l'objet Game est appelÃ©/lancÃ©
                        Game()

                    # si bouton menu cliquÃ©
                    if menu_btn.isOver(mouse):
                        # la fonction (run) de l'objet menu est appelÃ©/lancÃ©
                        Menu().run()

                    # si bouton score est cliquÃ©
                    if scores_btn.isOver(mouse):
                        # l'objet Score est appelÃ©/lancÃ©
                        Score()


            ## Ã©lÃ©ments Ã  afficher sur l'Ã©cran
            # arrÃ¨re plan
            screen.fill(WHITE)
            # titre
            screen.blit(img_title, rect_title)
            # mot Ã  deviner
            space_text(screen, masked_word, (50, 250), font)
            # info nombre d'faute
            screen.blit(img_faute,rect_faute)
            # info score
            screen.blit(img_score, rect_score)
            # message fin de partie
            screen.blit(img_gameOver, rect_gameOver)
            # image potence
            screen.blit(pot_img, (600, 150))
            # bouton start
            new_btn.draw(screen, 5)
            # bouton menu
            menu_btn.draw(screen, 5)
            # bouton scores
            scores_btn.draw(screen, 5)
            
            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()

            # MAJ afin d'actualier la fÃªnetre
            pygame.display.update()
        
        pygame.quit()


class Button:
    # crÃ©ation d'un objet bouton
    
    def __init__(self, color, x,y, width, height, text=""):
        
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    # fonction pour dessiner le bouton
    def draw(self, screen, outline=None):
        # option pour dÃ©finir une bordure de bouton
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        # la police du text dans le bouton
        if self.text != "":
            font = pygame.font.SysFont("comicsans", 50)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # pos = la position de la souris ou (x,y)
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        
        return False


# dÃ©finition d'une variable pour la fÃªnetre d'affichage
screen = pygame.display.set_mode((860,600))

# variable img menu
menu_img = pygame.image.load("Pendu_img/le-jeu.jpg")

# variables images du jeu
potence = pygame.image.load("Pendu_img/pendu_1.jpg")
pendu_1 = pygame.image.load("Pendu_img/pendu_2.jpg")
pendu_2 = pygame.image.load("Pendu_img/pendu_3.jpg")
pendu_3 = pygame.image.load("Pendu_img/pendu_4.jpg")
pendu_4 = pygame.image.load("Pendu_img/pendu_5.jpg")
pendu_5 = pygame.image.load("Pendu_img/pendu_6.jpg")
pendu_6 = pygame.image.load("Pendu_img/pendu_7.jpg")
pendu_7 = pygame.image.load("Pendu_img/pendu_8.jpg")

# variable couleurs
BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# variable arriÃ¨re plan
background = GRAY

# variables boutons 

play_btn = Button(WHITE, 40, 500, 160, 80, "Jouer")
add_word_btn = Button(WHITE, 230, 500, 380, 80, "Ajouter un mot")
add_btn = Button(WHITE, 200, 500, 190, 80, "Ajouter")
new_btn = Button(WHITE, 200, 500, 190, 80, "Rejouer")

menu_btn = Button(WHITE, 420, 500, 180, 80, "Menu")
scores_btn = Button(WHITE, 640, 500, 180, 80, "Scores")
exit_btn = Button(WHITE, 640, 500, 180, 80, "Sortir")

easy_btn = Button(WHITE, 300, 50, 200, 80, "Facile")
medium_btn = Button(WHITE, 300, 150, 200, 80, "Moyen")
hard_btn = Button(WHITE, 300, 250, 200, 80, "Difficile")

class Menu:
    # crÃ©ation d'une interface possÃ¨dant plusieurs scÃ¨nes

    def __init__(self):
        # initialisation de pygame
        pygame.init()
        
        # affichage de la fenÃªtre 
        self.screen = pygame.display.set_mode((860, 600))

        # variable d'Ã©tat pour derterminer quand l'Menuli est active
        self.running = True

    
    def run(self):
        
        # Lancer la boucle principale du menu
        while self.running:
            # condition de sortie de boucle
            for event in pygame.event.get():
                # si la croix (fermer Menu) est cliquÃ©e
                if event.type == QUIT:
                    # variable d'Ã©tat actif passe Ã  l'Ã©tat inactif
                    self.running = False
                

                # check si la souris est cliquÃ©e
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # si bouton Jouer est cliquÃ©
                    if play_btn.isOver(mouse):

                        # appel de l'objet Difficulty (choix du mode) 
                        Difficuty()

                    # si bouton Ajouter est cliquÃ©
                    if add_word_btn.isOver(mouse):

                        # appel de l'objet Ajouter
                        Ajouter_mot()
                    
                    # si bouton score est cliquÃ©
                    if scores_btn.isOver(mouse):
                        Score()
                           

            # Ã©lÃ©ments Ã  afficher sur l'Ã©cran
            ## fond
            self.screen.fill(Color("black"))
            ## image du menu
            self.screen.blit(menu_img, (50,50))
            ## boutons
            play_btn.draw(self.screen, 5)
            add_word_btn.draw(self.screen, 5)
            # option_btn.draw(self.screen, 5)
            scores_btn.draw(self.screen, 5)
        

            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()
            
            # MAJ de l'affichage
            pygame.display.update()

        # quitter proprement le programme 
        pygame.quit()


# si le programme est executÃ© directement (et non importÃ© comme module)
if __name__ == "__main__":
    # Lancer le Menu
    Menu().run()