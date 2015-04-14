#!/bin/python3
import sys
from PyQt4 import QtGui, QtCore
import os
import time

class BoxLayout(QtGui.QWidget):

#-------------------------------------------
#Идентификация
#-------------------------------------------

	def on_clicked_rec(self):
		self.clickrec = 1
		os.system('chmod +x ./audio/catching_audio.py')
#---------------Обновление окна процесса	
		self.processEdit.setText("Говорите")
		self.setFocus()
#---------------Очищает буфера и позволяет появиться надписи
		QtCore.QCoreApplication.processEvents()
#-----------------------------------------------------------
		os.system('python3 ./audio/catching_audio.py > /dev/null')
#---------------Обновление окна процесса
		self.processEdit.setText("Запись окончена")
#---------------Очищает буфера и позволяет появиться надписи
		QtCore.QCoreApplication.processEvents()
#-----------------------------------------------------------
		os.system('chmod +x ./audio/audio_graph.py')
		os.system('python2 ./audio/audio_graph.py')
		os.system('chmod +r ./voice_create/xor_float.net')
		os.system('make -f ./voice_test/Makeme > /dev/null')
		os.system('./voice_test/a1')
		f = open('res.txt','r')
		output = f.read()
		f.close()
#---------------Обновление окна процесса
		self.processEdit.setText(output + '\n' + 'Если данные не верны: введите логин, нажмите ok и wrong answer')
		self.setFocus()
#---------------Очищает буфера и позволяет появиться надписи
		QtCore.QCoreApplication.processEvents()	
#-----------------------------------------------------------
		self.img1 = QtGui.QPixmap("./audio/wave.png")
		self.lbl.setPixmap(self.img1)
		QtCore.QCoreApplication.processEvents()
		#print ("on_clicked_rec")

#-------------------------------------------
#Добавление нового пользователя 
#-------------------------------------------

	def on_clicked_add(self):
#Создание 5 файлов для обучения нейронной сети
		text = self.titleEdit.text()
		f = open('./data/login.txt', 'r')
		find = f.read()
		if self.ok.mouse_isPressed == True:
			text = self.titleEdit.text()
			if text != '':			
				if find.rfind(text) == -1 :
					f.close()
					f = open('./data/login.txt', 'a')
					f.write(text+'\n')
					f.close()
					self.processEdit.setText('Сейчас будет 6 раз производиться запись голоса. \n В данном окне будет написано ГОВОРИТЕ[цифра],\n каждый раз нужно произнести слово *ИДЕНТИФИКАЦИЯ* ОДИН раз. \n Через пару секунд начнется запись. Внимательнее !! <3')
					self.setFocus()
#---------------------------------------Очищает буфера и позволяет появиться надписи
					QtCore.QCoreApplication.processEvents()	
					time.sleep(10)
					for i in range (1, 7):
						os.system('chmod +x ./audio/catching_audio.py > /dev/null')
#-----------------------------------------------Обновление окна процесса
						time.sleep(1)
						self.processEdit.setText('Говорите' + ' '+ text + str([i]))
						self.setFocus()
#-----------------------------------------------Очищает буфера и позволяет появиться надписи
						QtCore.QCoreApplication.processEvents()	
#-------------------------------------------------------------------------------------------	
						os.system('python3 ./audio/catching_audio.py')
						self.processEdit.setText(' ')
#-----------------------------------------------Обновление окна процесса
						self.processEdit.setText('Запись закончена' + ' '+ text + str([i]))
						self.setFocus()
#-----------------------------------------------Очищает буфера и позволяет появиться надписи
						QtCore.QCoreApplication.processEvents()	
#--------------------------------------------------------------------------------------------
						os.system('chmod +x ./audio/audio_graph.py')
						os.system('python2 ./audio/audio_graph.py')
						os.system('cp ./audio/test1.txt ./data/' + text + str(i)+'.txt')
						#print('cp ./audio/test.txt ./data/' + text + str(i))
#---------------------------------------Обновление окна процесса
					self.processEdit.setText("Подождите. Обучение нейронной сети")
					self.setFocus()
#---------------------------------------Очищает буфера и позволяет появиться надписи
					QtCore.QCoreApplication.processEvents()
#------------------------------------------------------------------------------------
					os.system('make -f ./voice_create/Makeme > /dev/null')
					os.system('./voice_create/a1')
#---------------------------------------Обновление окна процесса
					self.processEdit.setText("Новый пользователь зарегистрирован")
					self.setFocus()
#---------------------------------------Очищает буфера и позволяет появиться надписи
					QtCore.QCoreApplication.processEvents()
#------------------------------------------------------------------------------------
				else:
#--------------------Обновление окна процесса
					self.processEdit.setText("Логин уже существует")
					self.setFocus()
			#Очищает буфера и позволяет появиться надписи
					QtCore.QCoreApplication.processEvents()
#--------------------Обновление окна процесса
			else :
				self.processEdit.setText("Введите логин")
				self.setFocus()
		#Очищает буфера и позволяет появиться надписи
				QtCore.QCoreApplication.processEvents()
		else:
#--------------------Обновление окна процесса
			self.processEdit.setText("Сначала введите логин и нажмите ok")
			self.setFocus()
			self.ok.mouse_isPressed = False
			self.ok.update()
#Очищает буфера и позволяет появиться надписи
			QtCore.QCoreApplication.processEvents()
		self.ok.mouse_isPressed = False
		self.ok.update()

#-------------------------------------------
#Считывание данных с окна
#-------------------------------------------

	def okEvent(self):
		self.text = self.titleEdit.text()
		self.ok.mouse_isPressed = True
		self.ok.update()
		#self.processEdit.setText("ok")
		#self.setFocus()
#---------------Очищает буфера
		QtCore.QCoreApplication.processEvents()

#-------------------------------------------
#Дообучение сети
#-------------------------------------------
		
	def on_clicked_retrain(self):
		if self.clickrec == 1:
			f = open('./data/login.txt', 'r')
			find = f.read()
			if self.ok.mouse_isPressed == True:	
				if find.rfind(self.text+'\n') != -1 :
					self.processEdit.setText("Подождите")
					QtCore.QCoreApplication.processEvents()
					os.system('make -f ./add_training/Makeme > /dev/null')
					os.system('./add_training/a.out '+self.text)
#---------------------------------------Обновление окна процесса
					self.processEdit.setText("Новые данные добавлены")
					print(find.rfind(self.text))
					QtCore.QCoreApplication.processEvents()
					self.ok.mouse_isPressed = False
					self.ok.update()
				else: 
#---------------------------------------Обновление окна процесса
					self.processEdit.setText("Данного пользователя " + self.text + " не существует, введите заново")
					print(find.rfind(self.text))
					self.setFocus()
#---------------------------------------Очищает буфера и позволяет появиться надписи
					QtCore.QCoreApplication.processEvents() 				
			else:
#-------------------------------Обновление окна процесса
				self.processEdit.setText("Введите логин и нажмите ok")
				self.setFocus()
#-------------------------------Очищает буфера и позволяет появиться надписи
				QtCore.QCoreApplication.processEvents() 
		else:
#-----------------------Обновление окна процесса
			self.processEdit.setText("Сначала запишите голос с помощью record")
			self.setFocus()
#-----------------------Очищает буфера и позволяет появиться надписи
			QtCore.QCoreApplication.processEvents()
		self.ok.mouse_isPressed = False
		self.ok.update() 

	def __init__(self, parent=None):

        	QtGui.QWidget.__init__(self, parent)

        	self.clickrec = 0	
        	self.setWindowTitle('Identification of the human voice')
		#Хрень с надписью
        	label = QtGui.QLabel('Enter your login:', self)
        	labelp = QtGui.QLabel('State of the process:', self)
        	#label.move(15, 80)

        	self.record = QtGui.QPushButton("Record")
        	self.ok = QtGui.QPushButton("ok")
        	self.ok.mouse_isPressed = False
        	add = QtGui.QPushButton("Add")
        	self.wanswer = QtGui.QPushButton("Wrong answer")
        	buttonex = QtGui.QPushButton("Exit")
        	self.titleEdit = QtGui.QLineEdit()

        	self.processEdit = QtGui.QLabel('Let\'s start \n Распознать голос : record \n Добавить нового пользователя : add')
        	self.processEdit.setAlignment(QtCore.Qt.AlignCenter)
        	self.processEdit.setFrameShape(QtGui.QFrame.Box)
        	self.processEdit.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        	self.processEdit.setBackgroundRole(QtGui.QPalette.Base)
        	self.processEdit.setAutoFillBackground(True) 
        	self.processEdit.setMinimumSize(100, 100)

        	self.img = QtGui.QPixmap("./graf/cort.jpg")
        	self.lbl = QtGui.QLabel()
        	self.lbl.setPixmap(self.img)

        	hbox = QtGui.QHBoxLayout()
        	hbox.addStretch(1)
        	#hbox.addWidget(record)
        	hbox.addWidget(add)
        	hbox.addWidget(self.wanswer)

        	hbox.addWidget(buttonex)
  
        	hbox1 = QtGui.QHBoxLayout()
        	#hbox1.addWidget(titleEdit)
        	#hbox1.addWidget(ok)

        	vbox = QtGui.QGridLayout(self)
        	#vbox.addStretch(1)
        	vbox.addWidget(label,1,0)
        	#vbox.addLayout(hbox1,2,0)
        	vbox.addWidget(self.titleEdit,2,0,1,4)
        	vbox.addWidget(self.ok,2,4,1,1)
        	vbox.addWidget(self.record,3,0,1,1)
        	vbox.addLayout(hbox,3,1,1,4)
        	vbox.addWidget(labelp,4,0,1,5)
        	vbox.addWidget(self.processEdit,5,0,1,5)
        	vbox.addWidget(self.lbl,6,0,1,5)

        	self.setLayout(vbox)
        	#print ("_init_")
        	#record.clicked.connect(QtCore.QCoreApplication.instance().quit)
        	self.record.clicked.connect(self.on_clicked_rec)
        	add.clicked.connect(self.on_clicked_add)
        	#Действие при неправильном распознавании
        	#self.wanswer.clicked.connect(self.on_clicked_add)
        	#self.record.clicked.connect(self.identEvent)
        	#self.add.clicked.connect(self.addEvent)
        	self.connect(buttonex, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        	self.setFocus()
        	self.ok.clicked.connect(self.okEvent)
        	self.connect(self.wanswer,QtCore.SIGNAL("clicked()"), self.on_clicked_retrain)

	def addEvent(self, event):
        	reply1 = QtGui.QMessageBox.question(self, 'Message',
        	"Do you want repeat", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        	if reply1 == QtGui.QMessageBox.Yes:
        		QtGui.qApp.quit 
        		#print("exit")
        	#else:
        		#on_clicked
        	

	def identEvent(self, event):
        	f = open('res.txt','r')
        	output = f.read()
        	f.close()
        	reply = QtGui.QMessageBox.question(self, 'Message',
        	output, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        	if reply == QtGui.QMessageBox.Yes:
        		QtGui.qApp.quit
        		sys.exit(app.exec_())
        		#print("exit")
        	
        	#else:
		#Добавить аудиофаил к нейронной сети и предложить заново
#Считывание данных с окна

        		

app = QtGui.QApplication(sys.argv)
qb = BoxLayout()
qb.show()
sys.exit(app.exec_())

