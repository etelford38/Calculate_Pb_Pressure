# -*- coding: utf-8 -*-
"""
Written by Evan Telford (ejt2133@columbia.edu)
"""
#load pertinent packages
import numpy as np
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
    QGroupBox,
    QGridLayout
)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Pressure Calculator'
        self.left = 0
        self.top = 0
        self.width = 200
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.layout=QGridLayout()
        self.box = QGroupBox()
        temperature= QLabel("Enter the Pb Tc in Kelvin") 
        temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature = QLineEdit()
        l_button=QPushButton('Calculate Pressure') 
        l_button.clicked.connect(lambda: self.calc_pressure()) 
        self.pressure=QLabel('')    
        self.pressure.setAlignment(QtCore.Qt.AlignCenter)    
        
        self.layout.addWidget(temperature, 0,0,1,1) 
        self.layout.addWidget(self.temperature, 1,0,1,1)
        self.layout.addWidget(l_button, 2,0,1,1)
        self.layout.addWidget(self.pressure,3,0,1,1)
        self.box.setLayout(self.layout)
        
        self.widget=QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
    def calc_pressure(self):
        Tc=self.temperature.text()
        Tc=float(Tc)
        P=(7.18-Tc)/0.379
        if P<0:
            self.pressure.setText('An invalid Pb Tc was entered')
        else:    
            self.pressure.setText('The pressure is ' + str(np.round(P,3)) + ' GPa')
              
app = QApplication(sys.argv)
window = App()
window.show()
app.exec()