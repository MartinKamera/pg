from abc import ABC, abstractmethod

def SeradSouradnice(souradnice):
    row, col = souradnice
    rows = []



class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        final_moves = []
        if self.color == "black":
            moves = [(row + 1, col)]
            if self.position == (2 , col):
                moves = [(row + 1, col), (row + 2, col)]
        else:
            moves = [(row - 1, col)]
            if self.position == (7, col):
                moves = [(row- 1, col), (row - 2, col)]
        
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return sorted(final_moves, key=lambda x: (x[0], x[1]))
                

            
        
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return sorted(final_moves, key=lambda x: (x[0], x[1]))

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        final_moves = []
        x = -7

        while x <= 7:
            if x != 0:
                moves.append((row + x, col + x))
            x += 1
        
        x = -7
        
        while x <= 7:
            y  = 0 - x
            if x != 0:
                moves.append((row + x, col + y))
            x += 1

    
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        
        return sorted(final_moves, key=lambda x: (x[0], x[1]))
    
    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        final_moves= []
        x = -7
        while x <= 7:

            if self.is_position_on_board((row + x, col)) and x != 0:
                final_moves.append((row + x, col))

            if self.is_position_on_board((row, col +x)) and x!= 0:
                final_moves.append((row, col + x))
            x += 1

        return sorted(final_moves, key=lambda x: (x[0], x[1]))
    
    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        final_moves = Rook.possible_moves(self) + Bishop.possible_moves(self)
        return final_moves

    
    def __str__(self):
        return f'Queen({self.color} at position {self.position})'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col),     
            (row - 1, col),     
            (row, col + 1),     
            (row, col - 1),     
            (row + 1, col + 1), 
            (row + 1, col - 1), 
            (row - 1, col + 1), 
            (row - 1, col - 1)  
        ]

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):  
                final_moves.append(move)

        return sorted(final_moves, key=lambda x: (x[0], x[1]))  # Seřazení pohybů
    def __str__(self):
        return f'King({self.color}) at position {self.position}'
        

if __name__ == "__main__":
    jezdec = Knight("black", (1, 2))
    print(jezdec)
    print(jezdec.possible_moves())

    pesak = Pawn("black", (2, 3))
    print(pesak)
    print(pesak.possible_moves())

    strelec = Bishop("black",(1, 8))
    print(strelec)
    print(strelec.possible_moves())
    
    vez = Rook("black", (1, 8))
    print(vez)
    print(vez.possible_moves())

    dama = Queen("black", (4, 1))
    print(dama)
    print(dama.possible_moves())

    kral = King("black", (1,5))
    print(kral)
    print(kral.possible_moves())

