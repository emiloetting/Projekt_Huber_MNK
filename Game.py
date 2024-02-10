from Board import Board                                            
from Player import Player
from Bot_Random import Bot_Random
from Bot_HighLevel import Bot_HighLevel
from Bot_LowLevel import Bot_LowLevel


class Game:
    def __init__(self, m=5, n=5, k=4, player1=None, player2=None):                                                              
        self.m = m                                                                                  
        self.n = n                                                                                  
        self.k = k                                                                                  
        self.board = Board()                                                                        
        self.player1 = player1                             
        self.player2 = player2                           
        self.winner = None
        
    def print_einleitung(self):
        print(
            " \n",
            "Einleitung:\n",
            " \n",
            "Das Spielfeld besteht aus 5x5 Feldern.\n",
            "Ein leeres Feld wird durch eine 0 gekennzeichnet, ein belegtes Feld durch eine 1 oder 2.\n",
            "Spielt ihr zu zweit, so belegt Spieler 1 das Feld mit einer 1 und Spieler 2 mit einer 2.\n", 
            "Spielst du alleine, so legst du automatisch die 1 und der Computer die 2.\n",
            "Du kannst Werte zwischen 1 und 5 angeben.\n",
            "Der erste Wert beschreibt die Horizontale, der zweite die Vertikale\n",
            "Die Eingabe ähnelt der bei 'Schiffe versenken'\n",
            "Die Werte dürfen nicht in einer Klammer stehen!\n", 
            " "
            )

    def start(self):
        '''Startet den Initialisierungsprozess eines Spiels
        
        Fragt zunächst, welche Art von Partie gewünscht ist (Mensch vs. Bot oder Bot vs. Bot)
        Anschließend werden je nach Eingabe weitere Methoden zur genaueren Festlegung
        der SPielparameter ausgeführt'''

        while True:
            print()
            print("Willkommen! Wie möchtest du spielen?\nPlayer vs. Player [1] / Player vs. Bot [2]")    
            choice_gamemode = input(">>> ")
            print() 
            if choice_gamemode == "1":
                self.start_player_vs_player()
                break
            elif choice_gamemode == "2":
                self.start_player_vs_bot()
                break
            else:
                print("Ungültige Eingabe! Wähle 1 oder 2")
            
    def start_player_vs_player(self):
        '''Startet das Spiel Player vs. Player'''
        self.player1 = Player(name=input("Name Spieler 1: \n>>> "), number=1)                             
        self.player2 = Player(name=input("Name Spieler 2: \n>>> "), number=2)                                                                                                                                                
        return self.game_loop()
    
    def choose_bot(self, bot_number):
        '''Legt Bot fest, gegen den gespielt werden soll.'''

        while True:
            print("Welches Level soll der Bot haben? Random [1] / Low-Level [2] / High-Level [3]")
            bot_level = input(">>> ")
            print()
            if bot_level == "1":
                return Bot_Random(number=bot_number)
            elif bot_level == "2":
                return Bot_LowLevel(number=bot_number)
            elif bot_level == "3":
                return Bot_HighLevel(number=bot_number)
            else:
                print("Ungültige Eingabe! Wähle 1, 2 oder 3")

    def choose_starter(self):
        '''Ermöglicht Bestimmung des Startspielers'''
        while True:
            print("Möchtest du den ersten Zug spielen? Ja [1] / Nein [2]")
            choice_begin = input(">>> ")
            print()
            if choice_begin == "1":
                return choice_begin
            elif choice_begin == "2":
                return choice_begin
            else:
                print("Ungültige Eingabe! Wähle 1 oder 2")
        
    def start_player_vs_bot(self):
        '''Initialisiert Spiel Mensch vs. Maschine'''
        starter_choice = self.choose_starter()
        if starter_choice == "1":
            self.player2 = self.choose_bot(bot_number=2)
            self.player1 = Player(name=input("Spielername: \n>>> "), number=1)
            print() 
            self.game_loop()
        else:
            self.player1 = self.choose_bot(bot_number=1)
            self.player2 = Player(name=input("Spielername: \n>>> "), number=2)
            print()
            self.game_loop()
        
    def game_loop(self):        
        '''Startet die Partie
        
        Solange kein Gewinner feststeht und Spielfeld nicht voll ist, wird das Spiel fortgesetzt.
        Board wird angezeigt, Spieler setzt Stein, Board prüft auf Gewinner und volles Spielfeld.
        Wenn Gewinner feststeht oder Spielfeld voll ist, wird das Board angezeigt und das Spiel beendet.
        Andernfalls zieht der nächste Spieler.
        '''   
        self.print_einleitung()                           
        print("Lasset die Spiele beginnen!")                 
        winner = False                                       
        full_board = False                                    
        while winner == False and full_board == False:       
            self.board.display()                             
            print()
            self.player1.make_move(board=self.board)          
            winner = self.board.has_won()                   
            full_board = self.board.board_full()
            if winner == True:                               
                self.board.display()
                print(f"\n {self.player1.name} hat gewonnen!")
                break                                         
            if full_board == True:                            
                self.board.display()                          
                print("\n Unentschieden!")                       
                break                                         
            self.board.display()                              
            print()
            full_board = self.board.board_full()             
            self.player2.make_move(board=self.board)          
            winner = self.board.has_won()                    
            full_board = self.board.board_full()
            if winner == True:                               
                self.board.display()               
                print(f"\n {self.player2.name} hat gewonnen!")
                break                                        
            if full_board == True:                           
                print("\n Unentschieden!")                       
                self.board.display()
                break                                         
        print("\nDas Spiel ist vorbei.")                               

def game_sim(number):
    '''Simuliert Spiele zwischen Bots
    
    Simuliert eine bestimmte Anzahl an Spielen zwischen zwei Bots.
    Gibt die Ergebnisse als print-statement im Terminal aus.
    '''
    
    count_bot_1 = 0
    count_bot_2 = 0
    count_draw = 0
    for i in range(number):
        game=Game(player1=Bot_Random(number=1), player2=Bot_HighLevel(number=2))
        game.game_loop()
        if game.winner == game.player1:
            count_bot_1 += 1
        elif game.winner == game.player2:
            count_bot_2 += 1
        elif game.board.board_full():
            count_draw += 1

    print("\nSieger:")
    print(f"Bot 1: {count_bot_1}\nBot 2: {count_bot_2}\nDraw: {count_draw}")


if __name__ == "__main__":
    game=Game()
    game.start()

