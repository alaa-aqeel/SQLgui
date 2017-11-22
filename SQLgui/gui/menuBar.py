from SQLgui.model import QMenuBar,QLabel,Qt,QFont,QCursor

class menuBar(QMenuBar):
	def __init__(self,main):
		super(menuBar,self).__init__(main)

		self.main = main
		self.setWindowTitle("SQLgui")
		self.setToolTip("SQLgui")

		
		self.label = QLabel("<span style='color:#66CCCC;'>SQL</span><span style='color:white;'>gui</span>",self)
		self.label.setFont(QFont("Arial Rounded MT Bold",25))

		self.label.setGeometry(700,10,self.label.width()+40,self.label.height()+15)
		
	def resizeEvent(self,event):
		self.label.setGeometry(self.width()-170,self.label.y(),self.label.width(),self.label.height())
		# print(dir(event.size()))

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.main.frameGeometry().topLeft()
			event.accept()
		super(menuBar,self).mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		self.setCursor(QCursor(Qt.ArrowCursor))
		super(menuBar,self).mouseReleaseEvent(event)

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:

			self.setCursor(QCursor(Qt.SizeAllCursor))
			self.main.move(event.globalPos() - self.dragPosition)
			event.accept()
		super(menuBar,self).mouseMoveEvent(event)
