import sys
from PyQt4 import QtGui, QtCore
import os

def on_clicked_rec():
	os.system('chmod +x ./audio/catching_audio.py')		
	os.system('python3 ./audio/catching_audio.py')
	os.system('chmod +x ./audio/audio_graph.py')
	os.system('python2 ./audio/audio_graph.py')
	os.system('chmod +r ./voice_create/xor_float.net')
	os.system('make -f ./Voice_test/Makeme > /dev/null')
	os.system('./Voice_test/a1')
	#os.system('./a2')
	print ("on_clicked_rec")

def on_clicked_add():
	os.system('chmod +x ./audio/catching_audio.py')		
	os.system('python3 ./audio/catching_audio.py')
	os.system('chmod +x ./audio/audio_graph.py')
	os.system('python2 ./audio/audio_graph.py')
#	os.system('chmod +r ./voice_create/xor_float.net')
#	os.system('make -f ./Voice_test/Makeme')
#	os.system('./a')
	print ("on_clicked_add")

class BoxLayout(QtGui.QWidget):

	def __init__(self, parent=None):

        	QtGui.QWidget.__init__(self, parent)
	
        	self.setWindowTitle('Identification of the human voice')

        	record = QtGui.QPushButton("Record")
        	add = QtGui.QPushButton("Add")
        	self.buttonex = QtGui.QPushButton("Exit")

        	hbox = QtGui.QHBoxLayout()
        	hbox.addStretch(1)
        	hbox.addWidget(record)
        	hbox.addWidget(add)
        	hbox.addWidget(self.buttonex)

        	vbox = QtGui.QVBoxLayout()
        	vbox.addStretch(1)
        	vbox.addLayout(hbox)

        	label = QtGui.QLabel('Let\'s start', self)
        	label.move(15, 10)

        	self.setLayout(vbox)
        	print ("_init_")
        	#record.clicked.connect(QtCore.QCoreApplication.instance().quit)
        	record.clicked.connect(on_clicked_rec)
        	add.clicked.connect(on_clicked_add)
        	record.clicked.connect(self.identEvent)
        	add.clicked.connect(self.addEvent)
        	self.connect(self.buttonex, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        	self.setFocus()

	def addEvent(self, event):
        	reply1 = QtGui.QMessageBox.question(self, 'Message',
        	"Do you want repeat", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        	if reply1 == QtGui.QMessageBox.No:
        		QtGui.qApp.quit 
        		print("exit")
        	else:
        		on_clicked
        	

	def identEvent(self, event):
        	reply = QtGui.QMessageBox.question(self, 'Message',
        	"Is identification success?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        	if reply == QtGui.QMessageBox.Yes:
        		QtGui.qApp.quit 
        		print("exit")
        	
        	#else:
		#Добавить аудиофаил к нейронной сети и предложить заново
        		

app = QtGui.QApplication(sys.argv)
qb = BoxLayout()
qb.show()
sys.exit(app.exec_())

