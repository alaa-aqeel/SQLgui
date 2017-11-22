from SQLgui.model import (QDialog,QLineEdit,QVBoxLayout,QCheckBox,
							QHBoxLayout,QPushButton,
							Qt,SaveData
						)


# Dailog Connect *'Run Fierst App'	
class DConnect(QDialog):
	def __init__(self,main,mysql):

		super(DConnect,self).__init__(main)
		self.resize(250,280)
		self.setWindowFlags( Qt.Tool|Qt.FramelessWindowHint)
		self.my_sql = mysql
		self.setWindowTitle("Connect MySQL")
		self.host = QLineEdit();self.user = QLineEdit();self.Pass = QLineEdit();self.dbs= QLineEdit();self.Cbox = QCheckBox("Remmber Me !!")
		self.host.setPlaceholderText("HostName . . .")
		self.user.setPlaceholderText("UserName . . .")
		self.Pass.setPlaceholderText("Password . . .")
		self.dbs.setPlaceholderText ("DataBase . . .")
		vbox = QVBoxLayout(self);hbox = QHBoxLayout()
		lis  = (self.host,self.user,self.Pass,self.dbs,self.Cbox)
		vbox.addWidget(lis[0]);vbox.addWidget(lis[1]);vbox.addWidget(lis[2]);vbox.addWidget(lis[3]);vbox.addWidget(lis[4])
		
		
		con = QPushButton("Connect ");con.setFixedSize(140,25);SaveData().login(self)
		exit = QPushButton("Exit ");exit.setFixedSize(80,25)
		hbox.addWidget(exit);hbox.addWidget(con)
		exit.clicked.connect(self.close)
		con.clicked.connect(self.setConfig)
		con.setFlat(True)
		exit.setFlat(True)
		vbox.addLayout(hbox)
		self.show()
		self.exec_()

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			event.accept()
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()

	def setConfig(self):
		self.config = {"host":self.host.text(),"user":self.user.text(),"password":self.Pass.text(),"database":self.dbs.text()}
		if self.Cbox.isChecked():
			SaveData().login(self,config_s=(self.config["host"],self.config["user"],self.config["password"],self.config["database"]))
		sh = self.my_sql.connect(**self.config)
		if self.my_sql.do:
			self.close()
