from . import Qt,sqlite3,sys,os

class SaveData():
	data = "SQLgui/static/gui.db"
	def __init__(self):
		if os.path.exists(self.data):
			self.con = sqlite3.connect(self.data)
			self.cur = self.con.cursor()
		else:
			sys.exit();


	def quiry(self,commands,*tup):
		resulty = []
		try:
			for i in commands.split(";"):
				if i.strip() == '':
					continue
				self.cur.execute(i.strip(),tuple(tup))
				resul = self.cur.fetchall()
				if resul != []:
					resulty.append(resul)
				self.con.commit()
		except sqlite3.Error as er:
			return er
		return resulty

	#*new  ^ old Name "save" ^
	def login(self,main,configLogin=""): 
		if configLogin == "":
			# main = SQLgui.py > class< dcon >
			# setDataLoing 
			data = self.quiry("select * from login")[0][-1]
			main.host.setText(data[0]);main.user.setText(data[1])
			main.Pass.setText(data[2]);main.dbs.setText(data[3])  
		else:
			# saveDataLoing 
			self.cur.quiry("INSERT INTO login (HOST,USER,PASS,DATABASE)VALUES (?,?,?,?);",tuple(configLogin))
			self.con.commit()

	#*new ^ oldName="wsave" ^
	def saveWidgetSittings(self,main,sql,console):
		# main = SQLgui.py.class < Main >
		# saveWidgetSittings Save(size,pos<x,y>,dock)
		areaDock = {"RightDockWidgetArea":"0","LeftDockWidgetArea":"1","TopDockWidgetArea":"2","BottomDockWidgetArea":"3"}
		size = main.geometry();main_v = "%s,%s,%s,%s"%(size.x(),size.y(),size.width(),size.height())

		sql_v = ["%s,%s,%s,%s"%(sql.x()+8,sql.y()+31,sql.width(),sql.height()),areaDock[str(main.dockWidgetArea(sql)).split(".")[-1]],
								sql.isVisible(),sql.isFloating()]

		console_v = ["%s,%s,%s,%s"%(console.x()+8,console.y()+31,console.width(),console.height()),
						areaDock[str(main.dockWidgetArea(console)).split(".")[-1]],console.isVisible(),console.isFloating()]

		self.quiry("""

			insert into main(size)values("%s");
			insert into sql(Area,visibil,Floating,size)values("%s","%s","%s","%s");
			insert into console(Area,visibil,Floating , size)values("%s","%s","%s","%s");

		"""%(main_v,sql_v[1],sql_v[2],sql_v[3],sql_v[0],console_v[1],console_v[2],console_v[3],console_v[0]))

	#*new ^ oldName="set" ^
	def setWidgetSittings(self,main):
		areaDock = {0:Qt.RightDockWidgetArea,1:Qt.LeftDockWidgetArea,2:Qt.TopDockWidgetArea,
		                3:Qt.BottomDockWidgetArea,"True":True,"False":False}

		st = self.getWidgetSittings()
		mainSize = st["main"]["size"].split(",")
		main.setGeometry(int(mainSize[0]),int(mainSize[1]),int(mainSize[2]),int(mainSize[3]))

		mainSize = st["sql"]["size"].split(",")
		main.addDockWidget(areaDock[int(st["sql"]["Area"])],main.sql_e);main.sql_e.setWindowTitle("SQL");main.sql_e.setWidget(main.edit)
		main.sql_e.setVisible(areaDock[st["sql"]["visibil"]]);main.sql_e.setFloating(areaDock[st["sql"]["Floating"]]);
		main.sql_e.setGeometry(int(mainSize[0]),int(mainSize[1]),int(mainSize[2]),int(mainSize[3]));

		mainSize = st["console"]["size"].split(",")
		main.addDockWidget(areaDock[int(st["console"]["Area"])],main.console_e);main.console_e.setWindowTitle("Console");main.console_e.setWidget(main.console)
		main.console_e.setVisible(areaDock[st["console"]["visibil"]]);main.console_e.setFloating(areaDock[st["console"]["Floating"]]);
		main.console_e.setGeometry(int(mainSize[0]),int(mainSize[1]),int(mainSize[2]),int(mainSize[3]))
    
	def getWidgetSittings(self):

		datas = {"sql":{},"console":{},"main":{}};key = ["Area","visibil","Floating","size"]
		get = self.quiry("select * from main;select * from console;select * from sql;")
		
		c = 0
		for i in ["main","console","sql"]:
		    k=0
		    for j in get[c][-1]:
		    	if i == "main":
		    		datas[i].update({key[-1]:j})
		    	else:
		    		datas[i].update({key[k]:j})
		    	k+=1
		    c+=1

		return datas 
