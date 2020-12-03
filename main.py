import sys

from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Solution(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('UI.ui', self)
		self.setFixedSize(self.size())
		self.initUI()

	def initUI(self):
		self.btn.clicked.connect(self.run)
		self.to_draw = False

	def run(self):
		self.to_draw = True
		self.repaint()

	def paintEvent(self, event):
		if self.to_draw:
			qp = QPainter()
			qp.begin(self)
			self.draw(event, qp)
			qp.end()

	def draw(self, event, qp):
		x, y = self.size().height(), self.size().width()
		r = randint(10, 200)

		qp.setBrush(QColor(255, 255, 0))
		qp.drawEllipse(x // 2, y // 3, r, r)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Solution()
	ex.show()
	sys.exit(app.exec())
