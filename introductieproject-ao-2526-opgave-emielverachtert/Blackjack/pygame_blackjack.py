import copy
import random
import pygame

pygame.init()
# game variables
cards = ['2', '3' ,'4' ,'5' ,'6' ,'7' ,'8', '9' ,'10' , 'J' ,'Q' ,'K' ,'A']
one_deck = 4 * cards
decks = 4                   
WIDTH = 600
HEIGHT = 1100
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Blackjack !')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 36)
tiny_font = pygame.font.Font('freesansbold.ttf',24)
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


#deal cards by selecting randomly from ddeck, and make function for one card at a time
def deal_cards(current_hand,current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card-1])
    current_deck.pop(card-1)
    return current_hand, current_deck

# draw scores for player and dealer on screen
def draw_scores(player, dealer):
    screen.blit(font.render(f'score[{player}]', True, 'white'), (350,400))
    if reveal_dealer:
        screen.blit(font.render(f'score[{dealer}]', True, 'white'), (350,100))



#draw cards visually onto screen (Voor elke kaart van de speler wordt een visuele speelkaart getekend met tekst en rand, netjes naast elkaar.)
def draw_cards(player, dealer , reveal):
    for i in range(len(player)):
        pygame.draw.rect(screen, 'white', [70 + (70 * i), 460 + (5 * i), 120, 220] , 0, 5)
        screen.blit(font.render(player[i], True, 'black'),(75 + 70*i, 465 + 5*i))
        screen.blit(font.render(player[i], True, 'black'),(75 + 70*i, 635 + 5*i))
        pygame.draw.rect(screen, 'red', [70 + (70 * i), 460 + (5 * i), 120, 220] , 5, 5)

    #if player hasn't finished turn, dealer will hide one card
    for i in range(len(dealer)):
        pygame.draw.rect(screen, 'white', [70 + (70 * i), 160 + (5 * i), 120, 220] , 0, 5)
        if i != 0 or reveal:
            screen.blit(font.render(dealer[i], True, 'black'),(75 + 70*i, 165 + 5*i))
            screen.blit(font.render(dealer[i], True, 'black'),(75 + 70*i, 335 + 5*i))
        else:
            screen.blit(font.render('???', True, 'black'),(75 + 70*i, 165 + 5*i))
            screen.blit(font.render('???', True, 'black'),(75 + 70*i, 335 + 5*i))
        pygame.draw.rect(screen, 'blue', [70 + (70 * i), 160 + (5 * i), 120, 220] , 5, 5)

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

    #main menu knop (altijd zichtbaar)
    menu_btn = pygame.draw.rect(screen, 'light gray', [390, 10, 200, 40], 0, 5)
    pygame.draw.rect(screen, 'dark gray', [390, 10, 200, 40], 5, 5)
    text = tiny_font.render('Main Menu', True, 'white')
    screen.blit(text, (395, 17))
    button_list.append(menu_btn) 


    #initially on startup (not active) only option is to deal new hand
    if not act:
        deal = pygame.draw.rect(screen, 'white', [150, 150, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [150, 150, 300, 100], 3, 5)
        deal_text = font.render('DEAL HAND', True, 'black')
        screen.blit(deal_text, (165,180))
        button_list.append(deal)
    # once game started, shot hit and stand buttons and win/loss records
    else:
        hit = pygame.draw.rect(screen, 'white', [0, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [0, 700, 300, 100], 3, 5)
        hit_text = font.render('HIT ME', True, 'black')
        screen.blit(hit_text, (55,735))
        button_list.append(hit)
        stand = pygame.draw.rect(screen, 'white', [300, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [300, 700, 300, 100], 3, 5)
        stand_text = font.render('STAND', True, 'black')
        screen.blit(stand_text, (355,735))
        button_list.append(stand)
        score_text = smaller_font.render(f'Wins: {record[0]}  Losses: {record[1]}   Draws:{record[2]}' , True, 'white' )
        screen.blit(score_text, (15, 840))
    # if there is an outcome for the hand that was played, display a restart button and tell user what happened
    if result != 0:
        screen.blit(font.render(results[result], True, 'white'),(15, 25))
        deal = pygame.draw.rect(screen, 'white', [150, 950, 300, 60], 0, 5)
        pygame.draw.rect(screen, 'green', [150, 950, 300, 60], 3, 5)
        pygame.draw.rect(screen, 'black', [153, 953, 294, 54], 3, 5)
        deal_text = font.render('NEW HAND', True, 'black')
        screen.blit(deal_text, (195,965))
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
    screen.fill('black')

    start_btn = pygame.draw.rect(screen, 'green', [240, 310, 260, 60], 0, 5)
    text = smaller_font.render('START GAME', True, 'white')
    screen.blit(text, (255, 322))

    return start_btn
    

# main game loop
run = True
while run:
    # run game at our framerate and fill screen with bg color
    timer.tick(fps)
    screen.fill('black')

    if game_state == "MENU":
        start_btn = draw_menu()

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

        #Game events
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                if not active:
                    if buttons[1].collidepoint(event.pos):
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

