import copy
import random
import pygame
import os

os.environ['SDL_VIDEO-CENTERED'] = '1'

pygame.init()
pygame.mixer.init()

# game variables
cards = ['2', '3' ,'4' ,'5' ,'6' ,'7' ,'8', '9' ,'10' , 'J' ,'Q' ,'K' ,'A']
one_deck = 4 * cards
decks = 4                   
WIDTH = 600
HEIGHT = 1100
pygame.display.set_caption('Pygame Blackjack !')
fps = 60
timer = pygame.time.Clock()
active = False
#Win, Loss, draw/push
records =[0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
outcome = 0
add_score = False
results = ['','PLAYER BUSTED o_0', 'PLAYER WINS 8 :)',' DEALER WINS :(', 'TIE GAME...']
game_state = "MENU"


#scherm aanmaken

screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)

#Basis resolutie
BASE_W = 600
BASE_H = 1100

#Huidige schermgrooteophalen
SW, SH = screen.get_size()

#schaalfactoren berekenen

#[dn] variabele namen kunnen better, als ik SX in je code zie, weet ik niet waarover het gaat. Dat gaat ook op voor de volgende functies
SX = SW / BASE_W
SY = SH / BASE_H

def s(x, y, w, h):
    return [int(x* SX), int(y* SY), int(w* SX), int(h * SY)]

def sx(x): return int(x * SX)
def sy(y): return int(y * SY)

font = pygame.font.Font('freesansbold.ttf', int(32 * SY))
smaller_font = pygame.font.Font('freesansbold.ttf', int(36 * SY))
tiny_font = pygame.font.Font('freesansbold.ttf', int(24 * SY))


#load img
img = pygame.image.load('openclipart-vectors-card-games-146687_1280.png') #[dn] je mag gerust files renamen 
img = pygame.transform.scale(img, (screen.get_width(), screen.get_height()))


    

#[dn] typo in comment. Zorg dat je altijd je spellcheck aan hebt staan in vscode
#deal cards by selecting randomly from ddeck, and make function for one card at a time
def deal_cards(current_hand,current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card-1])
    current_deck.pop(card-1)
    return current_hand, current_deck

# draw scores for player and dealer on screen
def draw_scores(player, dealer):
    screen.blit(font.render(f'score[{player}]', True, 'white'),  (sx(370), sy(420)))
    if reveal_dealer:
        screen.blit(font.render(f'score[{dealer}]', True, 'white'), (sx(370), sy(100)))


#draw cards visually onto screen (Voor elke kaart van de speler wordt een visuele speelkaart getekend met tekst en rand, netjes naast elkaar.)
def draw_cards(player, dealer , reveal):
    card_w = int(40 * SX)
    card_h = int(200* SY)
    gap = int(card_w + 6)

     # Centreer BEIDE rijen apart
    player_start_x = (SW - (len(player) * gap - 6)) // 2
    dealer_start_x = (SW - (len(dealer) * gap - 6)) // 2

    dealer_y = int(SH * 0.10)   # dealer BOVENAAN
    player_y = int(SH * 0.42)   # speler in het MIDDEN

    for i in range(len(player)):
        x = player_start_x + gap * i
        y = player_y
        pygame.draw.rect(screen, 'white', [x, y, card_w, card_h], 0, 5)
        pygame.draw.rect(screen, 'red',   [x, y, card_w, card_h], 3, 5)
        screen.blit(font.render(player[i], True, 'Black'), (x + 4, y + 4))
        screen.blit(font.render(player[i], True, 'Black'), (x + 4, y + card_h - int(38 * SY)))

    #if player hasn't finished turn, dealer will hide one card
    for i in range(len(dealer)):
        #[dn] zelfde opmerking met gap. Welke gap? Een betere variabelenaam zou hier helpen
        x = dealer_start_x + gap * i 
        y = dealer_y
        pygame.draw.rect(screen, 'white', [x, y, card_w, card_h], 0, 5)
        pygame.draw.rect(screen, 'blue',  [x, y, card_w, card_h], 3, 5) 
        if i != 0 or reveal:
            screen.blit(font.render(dealer[i], True, 'Black'), (x + 4, y + 4))
            screen.blit(font.render(dealer[i], True, 'Black'), (x + 4, y + card_h - int(38 * SY)))
        else:
            screen.blit(font.render('???', True, 'Black'), (x + 4, y + 4))
            screen.blit(font.render('???', True, 'Black'), (x + 4, y + card_h - int(38 * SY)))

#pass in player or dealer hand and get best score possible 
def calculate_score(hand):
    #calculate hand score fresh every time, check how many aces we heave
    hand_score = 0
    aces_count = hand.count('A')
    for i in range(len(hand)):
        #for 2,3,4,5,6,7,8,9, - just add the number to totall
        for j in range(8):
            if hand[i] == cards[j]:
                hand_score += int(hand[i])
         # for 10 and face cards, add 10
        if hand[i] in ['10', 'J', 'Q', 'K',]:
            hand_score += 10
         # for aces started by adding 11, we'll check if we need to reduce afterwards
        elif hand[i] == 'A':
            hand_score += 11
    #determine how many aces need to be 1 instead of 11 to get under 21 if 
    if hand_score > 21 and aces_count > 0:
        for i in range(aces_count):
            if hand_score > 21:
                hand_score-= 10
    return hand_score


#draw game conditions and buttons
def draw_game(act, record,result):
    button_list = []

    #main menu knop (altijd zichtbaar) rechts bovenaan
    menu_btn = pygame.draw.rect(screen, 'light gray', [SW - 170, 15, 155, 35], 0, 5)
    pygame.draw.rect(screen, 'dark gray', [SW - 170, 15, 155, 35], 3, 5)
    menu_text = tiny_font.render('Main Menu', True, 'white')
    screen.blit(menu_text, menu_text.get_rect(center=(SW - 93, 32)))
    button_list.append(menu_btn)


    #initially on startup (not active) only option is to deal new hand
    if not act:
        btn_w = 250
        btn_h = int(60 * SY)
        btn_x = (SW - btn_w) // 2
        btn_y = int(SH * 0.45)
        deal = pygame.draw.rect(screen, 'white', [btn_x, btn_y, btn_w, btn_h], 0, 8)
        pygame.draw.rect(screen, 'black', [btn_x, btn_y, btn_w, btn_h], 3, 8)
        deal_text = font.render('DEAL HAND', True, 'black')
        screen.blit(deal_text, deal_text.get_rect(center=(btn_x + btn_w // 2, btn_y + btn_h // 2)))
        button_list.append(deal) #[dn] consistentie: gebruik ofwel alijd btn, ofwel altijd button
    # once game started, shot hit and stand buttons and win/loss records
    else:
        btn_h = int(60 * SY)
        btn_w = 200 #[dn] vreemd dat je verticaal scaled, maar niet horizontaal
        btn_y = int(SH * 0.82)

        # HIT ME links gecentreerd
        hit_x = (SW // 2 - btn_w) -20
        hit = pygame.draw.rect(screen, 'white', [hit_x, btn_y, btn_w, btn_h], 0, 8)
        pygame.draw.rect(screen, 'white', [hit_x, btn_y, btn_w, btn_h], 3, 8)
        text = font.render('HIT ME', True, 'black')
        screen.blit(text, text.get_rect(center=(hit_x + btn_w // 2, btn_y + btn_h // 2)))
        button_list.append(hit)

         # STAND rechts gecentreerd
        stand_x = SW // 2 + 20
        stand = pygame.draw.rect(screen, 'white', [stand_x, btn_y, btn_w, btn_h], 0, 8)
        pygame.draw.rect(screen, 'White', [stand_x, btn_y, btn_w, btn_h], 3, 8)
        text = font.render('STAND', True, 'black')
        screen.blit(text, text.get_rect(center=(stand_x + btn_w // 2, btn_y + btn_h // 2)))
        button_list.append(stand)

        score_text = smaller_font.render(f'Wins: {record[0]}  Losses: {record[1]}   Draws:{record[2]}' , True, 'white' )
        screen.blit(score_text,(sx(15), int(SH * 0.92)))

    # if there is an outcome for the hand that was played, display a restart button and tell user what happened
    if result != 0:
        screen.blit(font.render(results[result], True, 'white'), (20, int(SH * 0.05)))
        btn_w = 250
        btn_h = int(60 * SY)
        btn_x = (SW - btn_w) // 2
        btn_y = int(SH * 0.88)
        deal = pygame.draw.rect(screen, 'white', [btn_x, btn_y, btn_w, btn_h], 0, 8)
        pygame.draw.rect(screen, 'green', [btn_x, btn_y, btn_w, btn_h], 3, 8)
        text = font.render('NEW HAND', True, 'black')
        screen.blit(text, text.get_rect(center=(btn_x + btn_w // 2, btn_y + btn_h // 2)))
        button_list.append(deal)

    return button_list

#check endgame conditions function
def check_endgame(hand_act, dealer_score, player_score, result, totals, add):
    #check end game scenarios is player had stood, busted or blackjacked
    #result 1- player bust , 2_win, 3-loss, 4-push
    if not hand_act and dealer_score >= 17:
        if player_score > 21:
            result = 1
        elif dealer_score < player_score <= 21 or dealer_score > 21:
            result = 2
        elif player_score < dealer_score <= 21:
            result = 3
        else:
            result = 4
            
        if add:
            if result == 1 or result == 3:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else:
                totals[2] += 1
            add = False
    return result, totals, add


def draw_menu():
    screen.fill('darkgreen')

    # Titel + img
    title = font.render('BLACKJACK ', True, 'white')
    screen.blit(title, title.get_rect(center=( screen.get_size()[0] / 2 , sy(50))))
    screen.blit(img, (0, 0)) 

    btn_w = 300
    btn_x = screen.get_size()[0] / 2 - btn_w / 2
    start_btn = pygame.draw.rect(screen, 'green',  (btn_x, sy(420), btn_w, sy(65)), 0, 8)
    pygame.draw.rect(screen, 'dark green', (btn_x, sy(420), btn_w, sy(65)), 3, 8)
    start_text = smaller_font.render('START GAME', True, 'white')
    screen.blit(start_text, start_text.get_rect(center=(btn_x + btn_w / 2, sy(420) + sy(65) / 2)))

    btn_w = 300
    btn_x = screen.get_size()[0] / 2 - btn_w / 2
    quit_btn = pygame.draw.rect(screen, 'red', (btn_x, sy(510), btn_w, sy(65)), 0, 8)
    pygame.draw.rect(screen, 'dark red', (btn_x, sy(510), btn_w, sy(65)), 3, 8)
    quit_text = smaller_font.render('QUIT GAME', True, 'white')
    screen.blit(quit_text, quit_text.get_rect(center=(btn_x + btn_w / 2, sy(510) + sy(65) / 2)))


    return start_btn, quit_btn

    

pygame.mixer.music.load('toucanmusic-nevada-night-516840.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

# main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
    # run game at our framerate and fill screen with bg color
    timer.tick(fps)
    screen.fill('darkgreen')


    if game_state == "MENU":
        start_btn, quit_btn = draw_menu()

    else:
        buttons = draw_game(active,records,outcome)

        #initial deal (ALLEEN GAME)
        if initial_deal:
            for i in range(2):
                my_hand, game_deck =  deal_cards(my_hand, game_deck)
                dealer_hand, game_deck =  deal_cards(dealer_hand, game_deck)
            initial_deal = False

        #Gameplay
        if active:
            player_score = calculate_score(my_hand)
            draw_cards(my_hand, dealer_hand, reveal_dealer)

            if reveal_dealer:
                dealer_score = calculate_score(dealer_hand)
                if dealer_score < 17:
                    dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)

            draw_scores(player_score, dealer_score)

            #bust check
            if hand_active and player_score >= 21:
                hand_active = False
                reveal_dealer = True
                dealer_score = 17

            outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score , outcome, records, add_score) 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        #MENU EVENTS
        if game_state == "MENU":
            if event.type == pygame.MOUSEBUTTONUP:
                if start_btn.collidepoint(event.pos):
                    game_state ="GAME"
                if quit_btn.collidepoint(event.pos):
                    run = False

        #Game events
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                if not active:
                    if buttons[1].collidepoint(event.pos):
                        #[dn] hier ben je wel idep aan het nesten. Je kan met 'and' meerdere condities checken in 1 if. 
                        #[dn] probeer maximaal 3 'levels' te indenteren
                        #[dn] gebruik eventueel kleinere functies
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * one_deck)
                        my_hand = []
                        dealer_hand = []
                        outcome = 0
                        hand_active = True
                        add_score = True
                else:#if player can hit, allow them to draw a card
                    if buttons [1].collidepoint(event.pos) and player_score < 21 and hand_active:
                        my_hand, game_deck = deal_cards(my_hand, game_deck)
                #allow player to end turn (stand)
                    elif buttons[2].collidepoint(event.pos) and not reveal_dealer:
                        reveal_dealer = True 
                        hand_active = False

                    elif len(buttons) == 4 and buttons[3].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * one_deck)
                        my_hand = []
                        dealer_hand = []
                        outcome = 0
                        hand_active = True
                        add_score = True
                        dealer_score = 0
                        player_score = 0
                        reveal_dealer = False

                if buttons[0].collidepoint(event.pos):
                    game_state = "MENU"
                    active = False

    

    pygame.display.flip()
pygame.quit()

