import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor
import random

class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.generate_food()
        self.direction = Qt.Key_Right

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move)
        self.set_speed(speed)

        self.initUI()

	def set_speed(self, speed):
		speeds = {'easy': 100, 'medium': 60, 'hard': 30}
		self.timer_interval = speeds.get(speed.lower(), 100)
		self.timer.start(self.timer_interval)


    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Snake Game')
        self.setStyleSheet("background-color: black;")

        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawSnake(qp)
        self.drawFood(qp)
        qp.end()

    def drawSnake(self, qp):
        qp.setBrush(QColor(255, 255, 255))

        for x, y in self.snake:
            qp.drawRect(x, y, 10, 10)

    def drawFood(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(self.food[0], self.food[1], 10, 10)

    def generate_food(self):
        return random.randint(0, 79) * 10, random.randint(0, 59) * 10

    def move(self):
        x, y = self.snake[0]

        if self.direction == Qt.Key_Left:
            x -= 10
        elif self.direction == Qt.Key_Right:
            x += 10
        elif self.direction == Qt.Key_Up:
            y -= 10
        elif self.direction == Qt.Key_Down:
            y += 10

        self.snake.insert(0, (x, y))

        if self.check_collision():
            self.timer.stop()
            return

        if self.food == self.snake[0]:
            self.food = self.generate_food()
        else:
            self.snake.pop()

        self.update()

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down]:
            self.direction = event.key()

    def check_collision(self):
        x, y = self.snake[0]
        return (
            x < 0 or x >= 800 or
            y < 0 or y >= 600 or
            (x, y) in self.snake[1:]
        )

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
    ex = SnakeGame(speed)
    sys.exit(app.exec_())
