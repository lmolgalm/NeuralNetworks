import sys
from PyQt4 import QtGui, QtCore
import os

class BoxLayout(QtGui.QWidget):

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

	def on_clicked_add(self):
#Создание 5 файлов для обучения нейронной сети
		text = self.titleEdit.text()
		for i in range (1, 5):
			os.system('chmod +x ./audio/catching_audio.py')		
			os.system('python3 ./audio/catching_audio.py')
			os.system('chmod +x ./audio/audio_graph.py')
			os.system('python2 ./audio/audio_graph.py')
			os.system('cp ./audio/test_bye.txt ./audio/' + text + str(i))
			print('cp ./audio/test_bye.txt ./audio/' + text + str(i))

	#	os.system('chmod +r ./voice_create/xor_float.net')
	#	os.system('make -f ./Voice_test/Makeme')
	#	os.system('./a')
		print ("on_clicked_add")

	def __init__(self, parent=None):

        	QtGui.QWidget.__init__(self, parent)
	
        	self.setWindowTitle('Identification of the human voice')
		#Хрень с надписью
        	label = QtGui.QLabel('Enter your login', self)
        	#label.move(15, 80)

        	self.record = QtGui.QPushButton("Record")
        	self.add = QtGui.QPushButton("Add")
        	self.buttonex = QtGui.QPushButton("Exit")
        	self.titleEdit = QtGui.QLineEdit()
        	hbox = QtGui.QHBoxLayout()
        	hbox.addStretch(1)
        	hbox.addWidget(self.record)
        	hbox.addWidget(self.add)
        	hbox.addWidget(self.buttonex)

        	vbox = QtGui.QVBoxLayout()
        	vbox.addStretch(1)
        	vbox.addWidget(label)
        	vbox.addWidget(self.titleEdit)
        	vbox.addLayout(hbox)

        	self.setLayout(vbox)
        	print ("_init_")
        	#record.clicked.connect(QtCore.QCoreApplication.instance().quit)
        	self.record.clicked.connect(self.on_clicked_rec)
        	self.add.clicked.connect(self.on_clicked_add)
        	self.record.clicked.connect(self.identEvent)
        	self.add.clicked.connect(self.addEvent)
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

