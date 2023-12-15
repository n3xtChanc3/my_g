import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor
import random

class TetrisGame(QWidget):
    def __init__(self, speed):
        super().__init__()

        self.board = [[0] * 10 for _ in range(20)]  # 10x20 grid for Tetris
        self.current_tetromino = self.generate_tetromino()
        self.current_position = (0, 3)  # Starting position
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_down)
        self.set_speed(speed)

        self.initUI()

    def set_speed(self, speed):
        speeds = {'easy': 100, 'medium': 60, 'hard': 30}
        self.timer_interval = speeds.get(speed.lower(), 100)
        self.timer.start(self.timer_interval)

    def initUI(self):
        self.setGeometry(100, 100, 300, 600)
        self.setWindowTitle('Tetris Game')
        self.setStyleSheet("background-color: black;")

        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_board(qp)
        self.draw_tetromino(qp)
        qp.end()

    def draw_board(self, qp):
        colors = [(0, 0, 0), (255, 255, 255)]  # Define colors (black and white)
        for i in range(20):
            for j in range(10):
                color = colors[self.board[i][j]]
                qp.fillRect(j * 30, i * 30, 30, 30, QColor(*color))

    def draw_tetromino(self, qp):
        color = (255, 255, 255)
        for i, row in enumerate(self.current_tetromino):
            for j, cell in enumerate(row):
                if cell:
                    qp.fillRect((self.current_position[1] + j) * 30, (self.current_position[0] + i) * 30, 30, 30, QColor(*color))

    def generate_tetromino(self):
        tetrominos = [
            [[1, 1, 1, 1]],
            [[1, 1, 1], [1]],
            [[1, 1, 1], [0, 0, 1]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1], [1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1]]
        ]
        return random.choice(tetrominos)

    def move_down(self):
        new_position = (self.current_position[0] + 1, self.current_position[1])
        if self.is_valid_position(self.current_tetromino, new_position):
            self.current_position = new_position
        else:
            self.freeze_tetromino()
            self.clear_lines()
            self.current_tetromino = self.generate_tetromino()
            self.current_position = (0, 3)  # Starting position

        self.update()

    def freeze_tetromino(self):
        for i, row in enumerate(self.current_tetromino):
            for j, cell in enumerate(row):
                if cell:
                    self.board[self.current_position[0] + i][self.current_position[1] + j] = 1

    def is_valid_position(self, tetromino, position):
        for i, row in enumerate(tetromino):
            for j, cell in enumerate(row):
                if cell:
                    if (
                        position[0] + i >= 20 or
                        position[1] + j < 0 or
                        position[1] + j >= 10 or
                        self.board[position[0] + i][position[1] + j]
                    ):
                        return False
        return True

    def clear_lines(self):
        for i in range(19, -1, -1):
            if all(self.board[i]):
                del self.board[i]
                self.board.insert(0, [0] * 10)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            new_position = (self.current_position[0], self.current_position[1] - 1)
            if self.is_valid_position(self.current_tetromino, new_position):
                self.current_position = new_position
        elif event.key() == Qt.Key_Right:
            new_position = (self.current_position[0], self.current_position[1] + 1)
            if self.is_valid_position(self.current_tetromino, new_position):
                self.current_position = new_position

    def check_game_over(self):
        if any(self.board[0]):
            self.timer.stop()
            return True
        return False

def get_speed_from_user():
    items = ['easy', 'medium', 'hard']
    item, okPressed = QInputDialog.getItem(None, "Select Speed", "Choose speed level:", items, 0, False)
    if okPressed and item:
        return item
    else:
        return 'easy'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    speed = get_speed_from_user()
    tetris = TetrisGame(speed)
    sys.exit(app.exec_())
