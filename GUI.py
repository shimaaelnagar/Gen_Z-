import pandas as pd
convert_Data=pd.read_excel('nasa.xls')
X=convert_Data.iloc[:,:-1].values
y=convert_Data.iloc[:,-1].values


#----------------------------------------------------
#Splitting data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=44, shuffle =True)
#----------------------------------------------------

#Import Libraries
from sklearn.naive_bayes import GaussianNB

GaussianNBModel = GaussianNB()
GaussianNBModel.fit(X_train, y_train)

#Calculating Details
print('GaussianNBModel Train Score is : ' , GaussianNBModel.score(X_train, y_train))
print('GaussianNBModel Test Score is : ' , GaussianNBModel.score(X_test, y_test))
#print('----------------------------------------------------')


#Calculating Prediction

y_pred_prob = GaussianNBModel.predict_proba(X_test)
#print('Predicted Value for GaussianNBModel is : ' , y_pred[:10])
#print('Prediction Probabilities Value for GaussianNBModel is : ' , y_pred_prob[:10])
#----------------------------------------------------
#from sklearn.metrics import classification_report
#Calculating classification Report :  
#ClassificationReport = classification_report(y_test,y_pred)
#print('Classification Report is : ', ClassificationReport )

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton
from PyQt5.QtCore import Qt
a = QApplication(sys.argv)
tree = QWidget()
tree.setGeometry(350, 80, 500, 400)
tree.setWindowTitle('Chase the fire')
tree.setAutoFillBackground(True)
q = tree.palette()
q.setColor(tree.backgroundRole(), Qt.lightGray)
tree.setPalette(q)
l1 = QLabel('X', tree)
l1.move(20, 12)
t1 = QLineEdit(tree)
t1.setGeometry(50, 10, 70, 20)
l2 = QLabel('Y', tree)
l2.move(20, 42)
t2 = QLineEdit(tree)
t2.setGeometry(50, 40, 70, 20)
l3 = QLabel('Month', tree)
l3.move(10, 72)
co1 = QComboBox(tree)
co1.setToolTip("**the numbers are in order for the months from january to december")
co1.addItem('Month')
co1.addItem('1')
co1.addItem('2')
co1.addItem('3')
co1.addItem('4')
co1.addItem('5')
co1.addItem('6')
co1.addItem('7')
co1.addItem('8')
co1.addItem('9')
co1.addItem('10')
co1.addItem('11')
co1.addItem('12')
co1.setGeometry(50, 70, 70, 20)
l4 = QLabel('Day', tree)
l4.move(14, 102)
co2 = QComboBox(tree)
co2.setToolTip("**the numbers are in order of days from saturday to friday")
co2.addItem('Day')
co2.addItem('1')
co2.addItem('2')
co2.addItem('3')
co2.addItem('4')
co2.addItem('5')
co2.addItem('6')
co2.addItem('7')
co2.setGeometry(50, 100, 70, 20)
l5 = QLabel("FFMC", tree)
l5.move(12, 132)
t3 = QLineEdit(tree)
t3.setGeometry(50, 130, 70, 20)
l6 = QLabel('DMC', tree)
l6.move(14, 162)
t4 = QLineEdit(tree)
t4.setGeometry(50, 160, 70, 20)
l7 = QLabel('Rain', tree)
l7.move(13, 192)
t5 = QLineEdit(tree)
t5.setGeometry(50, 190, 70, 20)
l21 = QLabel('DC', tree)
l21.move(360, 12)
t21 = QLineEdit(tree)
t21.setGeometry(400, 10, 70, 20)
l22 = QLabel('ISI', tree)
l22.move(360, 42)
t22 = QLineEdit(tree)
t22.setGeometry(400, 40, 70, 20)
l23 = QLabel('Temp', tree)
l23.move(360, 72)
t23 = QLineEdit(tree)
t23.setGeometry(400, 70, 70, 20)
l24 = QLabel('RH', tree)
l24.move(360, 102)
t24 = QLineEdit(tree)
t24.setGeometry(400, 100, 70, 20)
l25 = QLabel('Wind', tree)
l25.move(360, 132)
t25 = QLineEdit(tree)
t25.setGeometry(400, 130, 70, 20)
l26 = QLabel('Area', tree)
l26.move(360, 162)
t26 = QLineEdit(tree)
t26.setGeometry(400, 160, 70, 20)
p = QPushButton('Result', tree)
p.setGeometry(175, 300, 50, 30)
lab = QLabel('', tree)
lab.setGeometry(240, 299, 50, 30)
lab1= QLabel("**Note Num 1 means there is fire and Num 0 means there is no fire ", tree)
lab1.move(90,350)
def g():
   
    h=str(GaussianNBModel.predict([[int(t1.text()),int(t2.text()),int(co1.currentText()),int(co2.currentText()),int(t3.text()),int(t4.text()),int(t25.text()),int(t21.text()),int(t22.text()),int(t23.text()),int(t24.text()),int(t5.text()),int(t26.text())]]))
    lab.setText(h)
p.pressed.connect(g)
tree.show()
sys.exit(a.exec())