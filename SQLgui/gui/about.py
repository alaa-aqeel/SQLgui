from SQLgui.model import Qt,QIcon,QSize,QCursor,QDialog,QLabel,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout


class label_img(QPushButton):
	def __init__(self,image,url):
		super(label_img,self).__init__()
		self.setToolTip(url)
		self.setIcon(QIcon(image))
		self.setFlat(True)
		self.setIconSize(QSize(50,40))
		self.setCursor(QCursor(Qt.PointingHandCursor))
		self.setFixedSize(50,40)
		self.clicked.connect(self.open_url)
	def open_url(self):
		import webbrowser
		webbrowser.open_new_tab(self.toolTip())

class close_about(QPushButton):
	def __init__(self):
		super(close_about,self).__init__()
		self.setToolTip("close")
		self.setText("X")
		self.setStyleSheet("""
			QPushButton{background-color:#6495ed;border-style: solid;;border-color:#2495ed;font-size:20px;color:lightgray;}
			QPushButton:hover{border-radius:10px;color:white}
			""")
		self.setCursor(QCursor(Qt.PointingHandCursor))
		self.setFlat(True)
		self.setIconSize(QSize(30,20))
		self.setFixedSize(30,20)


class About(QDialog):
	def __init__(dialog):
		super(About,dialog).__init__()
		dialog.resize(400,250)
		dialog.setWindowFlags(Qt.FramelessWindowHint)
		dialog.setWindowTitle("About")
		dialog.setStyleSheet("""
			QDialog{background:#6495ed;}
			QDialog QGroupBox{
				background:#2495ed;	
				border-color:white;
				border-width: 1px;
			    border-style: solid;
			    border-radius: 5px;
			}
			QDialog QPushButton{background-color:#2495ed;border-style: solid;;border-color:#2495ed;}
		""")
		text = """
			<p align='center'>
				<span id="name" style='font-size:40px;color:lightblue;'> SQL</span>
				<span id="name" style='font-size:40px;color:white;'>gui<small> 0.1.1</small>
				</span>
				<br>
				<h3 style="color:#eee;"> Alaa Prog: alaa.21.iraq@gmail.com </h3>
				<h4 style="color:#eee;">Copyright &copy; 2017-2018 <h4>
			</p>
			
		"""
		vbox1   = QVBoxLayout(dialog)

		hbox    = QHBoxLayout()
		facebook      = label_img("SQLgui/static/img/fb.svg","www.facebook.com/Boy.Programmer.3")
		youtube       = label_img("SQLgui/static/img/youtube.svg","https://www.youtube.com/channel/UCSz4UY6mLSibSSqVpk-9tug")
		google_plus   = label_img("SQLgui/static/img/g+.svg","www.google.com/^_^?hhh=Nice")
		hbox.addWidget(facebook);hbox.addWidget(youtube);hbox.addWidget(google_plus)
		hbox.setContentsMargins(90,0,90,0)

		x_    = QHBoxLayout()
		x      = close_about()
		x_.addWidget(x)
		x_.setContentsMargins(300,0,0,0)

		x.clicked.connect(dialog.close)



		grop  = QGroupBox()
		label = QLabel(text)
		vbox   = QVBoxLayout()
		vbox.addWidget(label)
		vbox.addLayout(hbox)
		grop.setLayout(vbox)
		vbox1.addLayout(x_)
		vbox1.addWidget(grop)
