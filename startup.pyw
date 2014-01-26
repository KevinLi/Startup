import subprocess

from PyQt4 import QtCore, QtGui

class StartupGUI(QtGui.QMainWindow):
	def __init__(self):
		super(StartupGUI, self).__init__()

		hbtn = QtGui.QPushButton('Home', self)
		QtCore.QObject.connect(hbtn, QtCore.SIGNAL('clicked()'), self.home)
		hbtn.move(10, 10)

		wbtn = QtGui.QPushButton('Work', self)
		QtCore.QObject.connect(wbtn, QtCore.SIGNAL('clicked()'), self.work)
		wbtn.move(120, 10)

		self.resize(230,50)
		fg = self.frameGeometry()
		fg.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
		self.move(fg.topLeft())

		self.setWindowTitle(' ')
		self.show()

	def home(self):
		QtCore.QCoreApplication.instance().quit()

	def work(self):
		#subprocess.Popen(["calc.exe"])
		QtCore.QCoreApplication.instance().quit()

if __name__ == '__main__':

	import sys

	app = QtGui.QApplication(sys.argv)
	QtGui.QApplication.setQuitOnLastWindowClosed(True)
	window = StartupGUI()
	window.show()
	sys.exit(app.exec_())
