# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore

class Merger(QtGui.QWidget):
    """
    defines methods and properties used to send an application to
    lm_tabbor.Tabbor class
    """ 
    
    sTabName = 'string, name of the tab'
    oParent = 'object, container of the application'  
    
    def setParent(self, oLayer):
        """
        QTabWidget accepts only widget,so we parent 
        the main layout of the application to a QWidget (oParent),
        and it is this QWidget we link to QTabWidget
        @type oLayer: object 
        @param oLayer: any type of QT layout (Q*BoxLayout())
        """
        self.oParent = QtGui.QWidget()
        self.__oLayout = QtGui.QVBoxLayout()
        self.__oLayout.addLayout(oLayer)
        self.oParent.setLayout(self.__oLayout)
        
# Ni!
        