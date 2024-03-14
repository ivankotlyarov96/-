class Cell():
    def __init__(self, number):
        self.is_occupied = False
        self.number = number
        self.symbol = ' '

class Board():
    def __init__(self):
        self.sel_list = [Cell(i) for i in range(9)]
        self.count = 0


    def cell_changes(self, player):
        if self.sel_list[player.number-1].symbol == ' ':
            self.sel_list[player.number-1].symbol = player.symbols
            self.sel_list[player.number-1].is_occupied = True
            self.count += 1
            return (self.count)
        else:
            print('Клетка занята!')

    def check_win(self, player):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                     (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.sel_list[each[0]].symbol == self.sel_list[each[1]].symbol == self.sel_list[each[2]].symbol:
                if player_1.symbols == self.sel_list[each[0]].symbol:
                    print(f'Победил {player.name}')
                    player.flag = 1
                    return (player)
                else:
                    return False

    def display(self):
        print("-" * 13)
        print(f'{self.sel_list[0].symbol} | {self.sel_list[1].symbol} | {self.sel_list[2].symbol}')
        print("-" * 13)
        print(f'{self.sel_list[3].symbol} | {self.sel_list[4].symbol} | {self.sel_list[5].symbol}')
        print("-" * 13)
        print(f'{self.sel_list[6].symbol} | {self.sel_list[7].symbol} | {self.sel_list[8].symbol}')
        print("-" * 13)





 
class Player():
    def __init__(self, name, symbols):
        self.name = name
        self.symbols = symbols
        self.flag = 0
    def make_move(self):
        self.number = int(input('Введите номер клетки:'))
        if self.number < 1 or self.number > 9:
            print('Ошибка клетка должна быть числом от 1 до 9 ')
            self.number = int(input('Введите номер клетки: '))


class Game():
    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board

    def one_move(self, player):
        player.make_move()
        board.cell_changes(player)
        board.display()
        board.check_win(player)

    def one_game(self):
        board = [Cell(i) for i in range(9)]
        while True:
            self.one_move(player_1)
            if player_1.flag == 1:
                break
            self.one_move(player_2)
            if player_2.flag == 1:
                break
            if self.board.count == 9:
                break






board = Board()
player_1 = Player('Ivan', 'X')
player_2 = Player('Daria', 'O')
game = Game(player_1, player_2, board)

while True:
    x = input('Хотите сыграть в игру ? (да\нет)').lower()
    if x == 'да':
        game.one_game()
    elif x == 'нет':
        break
    else:
        break











