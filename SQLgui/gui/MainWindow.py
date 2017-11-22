from SQLgui.model import Qt,QMainWindow,QAction,QCursor,QIcon,QTabWidget,QFileDialog,SaveData,MySQL

from . import DConnect,dockEdit,Console,Table,menuBar,Edit,About

# Main Window
class Main(QMainWindow):
	def __init__(self,sql=None):
		super(Main,self).__init__()
		self.setWindowFlags(Qt.CustomizeWindowHint)
		
		self.setMinimumWidth(850)
		self.setMinimumHeight(400)
		self.do = False
		self.setWindowTitle("SQLgui")
		self.setWindowIcon(QIcon("SQLgui/static/img/SQL.ico"))	
		
		# get Style Form file.css # For all 
		self.setStyleSheet(open("SQLgui/static/style.css","r").read())

		# SQL Editor       command SQl     Table                  Console
		self.edit = Edit(self);
		self.sql = sql;
		self.tb = QTabWidget();
		self.console = Console()

		#Run Dialog Connect; set menuBar ;set Tools To Window
		DConnect(self,self.sql);
		self.action();self.setTools()
		

	def action(self):
		
		self.bar = menuBar(self)
		
		file = self.bar.addMenu("File");file.setCursor(QCursor(Qt.PointingHandCursor))
		main = self.bar.addMenu("build");main.setCursor(QCursor(Qt.PointingHandCursor))
		self.view = self.bar.addMenu("View");self.view.setCursor(QCursor(Qt.PointingHandCursor))
		help_ = self.bar.addMenu("Help");help_.setCursor(QCursor(Qt.PointingHandCursor))
	
			
		#help	
		About = QAction("&About",self,triggered=self.about);

        #file#
		open = QAction("O&pen .sql ",self,triggered=self.open,shortcut="CTRL+O")
		
		saveAs = QAction("&SaveAS .sql ",self,triggered=self.saveAs,shortcut="SHIFT+CTRL+S")
		exit = QAction("E&xit",self,triggered=self.close_all)

		#buikd
		con = QAction("&Connect",self,triggered=lambda:dcon(self,self.sql))
		run = QAction("&Run",self,shortcut="CTRL+B",triggered=lambda:self.sql.query(self.edit.toPlainText(),self.tb,self.console))
		

		
		file.addAction(open)
		file.addAction(saveAs)
		file.addAction(exit)
		
		main.addAction(con)
		main.addAction(run)

		
		help_.addAction(About)

		self.setMenuBar(self.bar)
		

	def close_all(self):
		self.sql.close_all()
		SaveData().saveWidgetSittings(self,self.sql_e,self.console_e)
		self.close()

		
	# Dialog 'Open File'
	def open(self):
		path ,c = QFileDialog.getOpenFileName(self,"Open File ","","SQL File(*.sql )")
		if len(path) > 2:  
			file = open(path,"r").read()
			self.edit.setPlainText(file)

	# Dialog 'SaveAs File'
	def saveAs(self):
		get = self.edit.toPlainText()
		if len(get) != 0:
			path ,c = QFileDialog.getSaveFileName(self,"Open File ","*.sql","SQL File(*.sql )")
			if len(path) > 2:  
				file = open(path,"w")
				file.write(get)

	# set Console AND SQL Editor 
	def setTools(self):
		# Set SQL AND Console >> In dock
		self.sql_e = dockEdit(self);
		self.console_e = dockEdit(self)
	
		# set Table >> From File sql_command
		self.setCentralWidget(self.tb);self.tb.insertTab(1,Table(),"Null")


		# set ToolBar(Console,SQL) To dock (show , hibe) 
		self.view.addAction(self.sql_e.toggleViewAction())
		self.view.addAction(self.console_e.toggleViewAction())
		
		# set Settings
		SaveData().setWidgetSittings(self)

	# Dialog About
	def about(self):
		about = About()
		about.show();about.exec_()
	
	# This call Whene Close Windwo	
	def closeEvent(self,event):
		self.close_all()
		
