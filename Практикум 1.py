import sys
import math
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QTimer


class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Движущаяся окружность')

        # Основная окружность
        self.radius = 200
        self.angle = 0
        self.speed = 2  # Скорость движения (градусы за кадр)


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(30)

    def update_position(self):
        self.angle = (self.angle + self.speed) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setBrush(QColor(220, 220, 220))
        painter.drawRect(self.rect())

        center = self.rect().center()
        painter.setBrush(QColor(20, 70, 10))
        painter.drawEllipse(center.x() - self.radius, center.y() - self.radius,
                            self.radius * 2, self.radius * 2)

        angle_rad = math.radians(self.angle)
        point_x = center.x() + self.radius * math.cos(angle_rad)
        point_y = center.y() + self.radius * math.sin(angle_rad)

        painter.setBrush(QColor(20, 100, 10))
        painter.drawEllipse(int(point_x - 15), int(point_y - 15), 30, 30)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = DrawingWidget()
    window.resize(600, 600)
    window.show()

    sys.exit(app.exec())
