from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
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
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'

class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        direction = 1 if self.color == "white" else -1
        if self.is_position_on_board((row + direction, col)):
            moves.append((row + direction, col))
        if (self.color == "white" and row == 2) or (self.color == "black" and row == 7):
            if self.is_position_on_board((row + 2 * direction, col)):
                moves.append((row + 2 * direction, col))
        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'

class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if not self.is_position_on_board((r, c)):
                    break
                moves.append((r, c))
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'

class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if not self.is_position_on_board((r, c)):
                    break
                moves.append((r, c))
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'

class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if not self.is_position_on_board((r, c)):
                    break
                moves.append((r, c))
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'

class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if self.is_position_on_board((r, c)):
                moves.append((r, c))
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'

class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if self.is_position_on_board((r, c)):
                moves.append((r, c))
        return moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'

if __name__ == "__main__":
    knight = Knight("black", (4, 4))
    print(knight)
    print(knight.possible_moves())
