import random, sys

# 2048 class
class game_2048:
    def __init__(self, mode=None):
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        # flag for win condition
        self.is_2048 = False

        if mode == 'full':
            self.board = [[i for i in range(4)] for j in range(4)]
            # flag for win condition
            self.is_2048 = False

        elif mode == 'won_game':
            self.board = [[0 for _ in range(4)] for _ in range(4)]
            # flag for win condition
            self.is_2048 = False
            self.board[0][0] = 2048

    # randomly generate 2 in one of the empty cells
    def add_two(self):
        empty_cells = []
        for i, row in enumerate(self.board):
            for j, num in enumerate(row):
                if num == 0:
                    empty_cells.append((i, j))

        # there is no empty cells / introduce options
        # if empty_cells is None:
        #     print("No empty cell left")
        #     return

        try:
            row_chosen, col_chosen = random.choice(empty_cells)
            self.board[row_chosen][col_chosen] = 2
        except:
            self.new_game()

        return
    
    # display current game board
    def display_board(self):

        res_list = []
        for i in range(4):
            
            row_list = []
            for j in range(4):

                item = self.board[i][j]
                if item == 0:
                    row_list.append(' ')
                else:
                    row_list.append(str(self.board[i][j]))
            
            row = '\t|'.join(row_list)
            res_list.append(row)
        
        res = '\n---------------------------------\n'.join(res_list)
        print(res)

    # initialize a game
    def initialize_game(self):
        is_starting = input('Welcome. Start playing 2048? Answer Yes or No: ').lower()
        
        while True:
            if is_starting == 'yes':
                print('Starting a new game')
                self.add_two()
                self.add_two()
                self.display_board()
                self.game_play()
                break
            
            elif is_starting == 'no':
                print('Until next time')
                break
            else:
                is_starting = input('Please enter a valid response: ').lower()
    
    # prompt a new game
    def new_game(self):
        is_starting = ''
        if self.is_2048:
            is_starting = input('You reached 2048! Another game? Answer Yes or No: ').lower()
        else:
            is_starting = input('You lost. Another 2048? Answer Yes or No: ').lower()
        
        while True:
            if is_starting == 'yes':
                print('Starting a new game')
                self.is_2048 = False
                self.clear_board()
                self.add_two()
                self.add_two()
                self.display_board()
                self.game_play()
                break
            
            elif is_starting == 'no':
                print('Until next time')
                sys.exit()
            else:
                is_starting = input('Please enter a valid response: ').lower()

    # clear the board
    def clear_board(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j] = 0
    
    def game_play(self):
            
        while True:
            move = input('Choose your next move.\nw: up\ts: down\ta: left\td: right\nYour move: ')

            match move:
                case 'w':
                    print('moving up\n')

                    # update board
                    aggregated = []
                    for j in range(4):
                        
                        agg_col = []
                        for i in range(4):
                            if self.board[i][j] == 2048:
                                agg_col.append(self.board[i][j])
                                self.is_2048 = True
                            elif self.board[i][j] != 0:
                                agg_col.append(self.board[i][j])
                        
                        # if adjacent cells include same number, add them
                        if len(agg_col) > 1:
                            k = 1
                            while k < len(agg_col):
                                if agg_col[k - 1] == agg_col[k]:
                                    agg_col[k - 1] = agg_col[k - 1] * 2
                                    agg_col = agg_col[: k] + agg_col[k + 1:]
                                    k += 1
                                else:
                                    k += 1
                        aggregated.append(agg_col)

                    self.clear_board()

                    for j in range(4):
                        col_curr = aggregated[j]

                        for i, entry in enumerate(aggregated[j]):
                            self.board[i][j] = entry

                    # display the updated board with new entry 2
                    self.add_two()
                    self.display_board()

                    if self.is_2048:
                        self.new_game()

                case 's':
                    print('moving down\n')

                    # update board
                    aggregated = []
                    for j in range(4):
                        
                        agg_col = []
                        for i in range(3, -1, -1):
                            if self.board[i][j] == 2048:
                                agg_col.append(self.board[i][j])
                                self.is_2048 = True
                            elif self.board[i][j] != 0:
                                agg_col.append(self.board[i][j])
                        
                        # if adjacent cells include same number, add them
                        if len(agg_col) > 1:
                            k = 1
                            while k < len(agg_col):
                                if agg_col[k - 1] == agg_col[k]:
                                    agg_col[k - 1] = agg_col[k - 1] * 2
                                    agg_col = agg_col[: k] + agg_col[k + 1:]
                                    k += 1
                                else:
                                    k += 1
                        aggregated.append(agg_col)

                    self.clear_board()

                    for j in range(4):
                        col_curr = aggregated[j]

                        for i, entry in enumerate(aggregated[j]):
                            self.board[3 - i][j] = entry

                    # display the updated board with new entry 2
                    self.add_two()
                    self.display_board()

                    if self.is_2048:
                        self.new_game()
                    
                case 'a':
                    print('moving left\n')

                    # update board
                    aggregated = []
                    for i in range(4):
                        
                        agg_col = []
                        for j in range(4):
                            if self.board[i][j] == 2048:
                                agg_col.append(self.board[i][j])
                                self.is_2048 = True
                            elif self.board[i][j] != 0:
                                agg_col.append(self.board[i][j])
                        
                        # if adjacent cells include same number, add them
                        if len(agg_col) > 1:
                            k = 1
                            while k < len(agg_col):
                                if agg_col[k - 1] == agg_col[k]:
                                    agg_col[k - 1] = agg_col[k - 1] * 2
                                    agg_col = agg_col[: k] + agg_col[k + 1:]
                                    k += 1
                                else:
                                    k += 1
                        aggregated.append(agg_col)

                    self.clear_board()

                    for i in range(4):
                        col_curr = aggregated[i]

                        for j, entry in enumerate(aggregated[i]):
                            self.board[i][j] = entry

                    # display the updated board with new entry 2
                    self.add_two()
                    self.display_board()

                    if self.is_2048:
                        self.new_game()

                case 'd':
                    print('moving rigt\n')

                    # update board
                    aggregated = []
                    for i in range(4):
                        
                        agg_col = []
                        for j in range(3, -1, -1):
                            if self.board[i][j] == 2048:
                                agg_col.append(self.board[i][j])
                                self.is_2048 = True
                            elif self.board[i][j] != 0:
                                agg_col.append(self.board[i][j])
                        
                        # if adjacent cells include same number, add them
                        if len(agg_col) > 1:
                            k = 1
                            while k < len(agg_col):
                                if agg_col[k - 1] == agg_col[k]:
                                    agg_col[k - 1] = agg_col[k - 1] * 2
                                    agg_col = agg_col[: k] + agg_col[k + 1:]
                                    k += 1
                                else:
                                    k += 1
                        aggregated.append(agg_col)

                    self.clear_board()

                    for i in range(4):
                        col_curr = aggregated[i]

                        for j, entry in enumerate((aggregated[i])):
                            self.board[i][3 - j] = entry

                    # display the updated board with new entry 2
                    self.add_two()
                    self.display_board()

                    if self.is_2048:
                        self.new_game()

                case _:
                    print('Please enter a valid move.')