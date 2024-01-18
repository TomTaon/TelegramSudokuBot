from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def generate_sudoku():
    return [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


class Board:

    LABELS_X = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
    LABELS_Y = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    def __init__(self, player_id: str, font_color="black"):
        self.player_id = str(player_id)
        self.font_color = font_color
        self.game_active = True
        self.board = generate_sudoku()

    def generate_starting_board_img(self):
        x_cord = 64
        y_cord = 42

        # Open an Image
        img = Image.open('board.jpeg')
        draw = ImageDraw.Draw(img)

        # Setting font
        font = ImageFont.truetype('my_font.ttf', 45)

        # Draw grid numbers on board image
        for x in range(9):
            for y in range(9):
                if self.board[x][y] != 0:
                    text = str(self.board[x][y])
                    draw.text((x_cord + 50 * y, y_cord + 50 * x),
                              text=text,
                              font=font,
                              fill=self.font_color)

        path = self.player_id + ".png"
        img.save(path)

        return path

    @staticmethod
    def position_to_tuple(position_str):

        if position_str[0] in Board.LABELS_X and position_str[1] in Board.LABELS_Y:
            x = ord(position_str[0]) - ord("A")
            y = int(position_str[1]) - 1

            return True, (x, y), "all good"

        if position_str[0] in Board.LABELS_Y and position_str[1] in Board.LABELS_X:
            x = ord(position_str[1]) - ord("A")
            y = int(position_str[0]) - 1

            return True, (x, y), "all good"

        return False, (0, 0), "wrong input try A1 3, 1a 3 ,A13 or 1a3"

    def space_is_empty(self, x, y):
        if self.board[y][x] == 0:
            return True, "all good"
        else:
            return False, "position is not empty"

    @staticmethod
    def number_check(number_str):
        if number_str in Board.LABELS_Y:
            return True, "all good"
        else:
            return False, "second parameter is not a number 1-9"

    @staticmethod
    def check_str(string: str):

        string = string.upper()
        parameters = string.split(" ")

        if len(parameters) == 2 and len(parameters[0]) == 2 and len(parameters[1]) == 1:
            position_str, number_str = parameters
            return True, position_str, number_str, "all good"

        if len(parameters) == 1 and len(parameters[0]) == 3:
            position_str = parameters[0][:2]
            number_str = parameters[0][2:]
            return True, position_str, number_str, "all good"

        else:
            return False, 0, 0, "wrong input try A1 3, 1a 3 ,A13 or 1a3"

    def move(self, string: str):

        print(string)

        works, position_str, number_str, response = self.check_str(string)
        if not works:
            print("error 0")
            return False, response

        works, xy_tuple, response = self.position_to_tuple(position_str)
        print(xy_tuple)
        if not works:
            print("error 1")
            return False, response

        works, response = self.space_is_empty(xy_tuple[0], xy_tuple[1])
        if not works:
            print("error 2")
            return False, response

        works, response = self.number_check(number_str)
        if not works:
            print("error 3")
            return False, response

        self.board[xy_tuple[1]][xy_tuple[0]] = int(number_str)

        return True, "all good"
