from SQLgui.model import QDockWidget,QTextEdit,QTableWidget,QMessageBox,QFont

	
#Main
class dockEdit(QDockWidget):
	def __init__(self,self_m):
		super(dockEdit,self).__init__(self_m)
		self.setFont(QFont("",10))

#Main
class Console(QTextEdit):
	def __init__(self):
		super(Console,self).__init__()
		self.setReadOnly(True)


#SQL
class Table(QTableWidget):
	def __init__(self):
		super(Table,self).__init__()
		self.rowResized(1,100,50)
		self.setColumnCount(5);self.setRowCount(3)

#SQL
class MsgBox():
	def __init__(self):
		self.msg = QMessageBox()

	def setMsg(self,msg):
		self.msg.setIcon(self.msg.Warning)
		self.msg.setText("<h4> %s </h4>"%msg)
		self.msg.setWindowTitle("Warning")
		self.msg.setStandardButtons(self.msg.Ok)
		self.msg.show()
		self.msg.exec_()


