from SQLgui import *

#Run App
def run():
	app = model.QApplication([])
	sql = model.MySQL()
	MainWin = gui.Main(sql)
	if sql.do:
		MainWin.do = True
		MainWin.show();app.exec_();
	else:
		MainWin.close();

if __name__ == '__main__':
	run()