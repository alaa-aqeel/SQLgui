from . import QFont,QTableWidgetItem
import SQLgui.gui 
import mysql.connector as db,sys

class MySQL():
	def __init__(self):
		self.do = None
		self.msg = SQLgui.gui.MsgBox()

	def connect(self,**conf):
		try:
			
			self.con = db.connect(**conf)
			# dictionary=True  named_tuple
			self.cur = self.con.cursor(dictionary=True)
			self.do = True
		except:
			self.do = False
			self.msg.setMsg("Can't connect to MySQL server on '%s'"%conf["host"])

	# Close Connect
	def close_all(self):
		if self.do:
			self.con.close()
			self.cur.close()

	def query(self,sql,tbs,console):
		
		if self.do:
			try:
				tbs.clear();console.clear()
				countTab = 0
				command = ""
				for i in sql.split("*/"):
					if not i.startswith("/*"):
						for j in i.split(";"):
							a = j.strip().strip("\n")
							if not a.strip().startswith("/*"):
								if a != "":
									command += a+";"
						
				for i in self.cur.execute("%s"%command,multi=True):
					tb = SQLgui.gui .Table()
					if i.with_rows:
						cols = i.column_names;
						rows = i.fetchall()
						tb.setColumnCount(len(cols));count = 0
						for col in cols :
							item = QTableWidgetItem
							tb.setHorizontalHeaderItem(count,item(col))
							count+=1
						rowsCount = 0
						for row in rows:
							colCount = 0;
							tb.setRowCount(rowsCount+1)
							for col in cols:
								text = row[col]
								try:
									item = QTableWidgetItem(row[col].decode("u8"))
								except:
									item = QTableWidgetItem(str(row[col]))
								item.setFont(QFont("andalus",12))
								tb.setItem(rowsCount,colCount,item)
								colCount+=1
							rowsCount+=1
						titleTb = str(i).split(":")[1].upper()
						tbs.setTabToolTip(countTab,str(i).split(":")[1])
						tbs.insertTab(countTab,tb,titleTb)
		
						countTab+=1
					console.append("<span style='color:green;'>Successfully > </span>%s ;\n"%str(str(i).split(":")[1]).split("*/")[-1].strip("\n"))
				self.con.commit()
			except db.Error as er:
				console.append("<span style='color:red;'>Error > </span>%s  "%er.msg.split("(")[0])
		else:
			self.msg.setMsg("\n No Connect To MySQL")
