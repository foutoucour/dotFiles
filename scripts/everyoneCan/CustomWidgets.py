import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class AlGroupBox(QtGui.QGroupBox):
    """Qt GroupBox with contentMargin at 0,0,0,0"""
    def __init__(self, sName):
        """
        @type sName: string
        @param sName: Title of the groupBox
        """
        QtGui.QGroupBox.__init__(self)
        self.setTitle(sName)
        self.setContentsMargins(0,0,0,0)

class AlLineEdit(QtGui.QLineEdit):
    """Formated Qt LineEdit with a height of 22"""
    def __init__(self):
        QtGui.QLineEdit.__init__(self)
        self.setMaximumHeight(22)
        oColor = QtGui.QColor(255,255,255)
        self.setStyleSheet(
                        "QWidget { background-color: %s }" % oColor.name())

class AlWheelLineEdit(AlLineEdit):
    """
    AlLineEdit with wheel event
    """

    def __init__(self,  iX=999999999999999999999999,
                        iY=-999999999999999999999999):
        """
        @type iX    : float
        @param iX   : maximum value of the line edit

        @type iY    : float
        @param iY   : minimum value of the line edit
        """
        self.setLimits(iX, iY)
        self.__iFactor                  = 1
        AlLineEdit.__init__(self)

    def setLimits(self, x, y):
        if x<y:
            self.__iUp = y
            self.__iDown = x
        else :
            self.__iUp = x
            self.__iDown = y

    def setMiddleClickTrickFactor(self, iValue):
        self.__iFactor = iValue

    def wheelEvent(self, event):
        iCurrentValue = float(self.text())
        iAdd = event.delta()/120
        iAdd *= self.__iFactor
        iNewValue = iCurrentValue + iAdd
        if iNewValue < self.__iDown:
            iNewValue = self.__iDown
        if iNewValue > self.__iUp:
            iNewValue = self.__iUp
        iNewValue = round(iNewValue,2)
        self.setText(str(iNewValue))

class AlVBoxLayout(QtGui.QVBoxLayout):
    """Qt QVBoxLayout with contentMargin at 0,0,0,0"""
    def __init__(self):
        QtGui.QVBoxLayout.__init__(self)
        self.setContentsMargins(0,0,0,0)

class AlHBoxLayout(QtGui.QHBoxLayout):
    """Qt AlHBoxLayout with contentMargin at 0,0,0,0"""
    def __init__(self):
        QtGui.QHBoxLayout.__init__(self)
        self.setContentsMargins(0,0,0,0)

class AlGroupLabel(QtGui.QWidget):
    """Qt Widget containing a Label and a widget"""
    def __init__(self, sName, oWidget):
        """
        @type sName: string
        @param sName: Title of the Qt Label
        @type oWidget: Qt Widget
        @param oWidget: widget after the Label
        """
        QtGui.QWidget.__init__(self)
        self.setContentsMargins(0,0,0,0)
        self.__oGrid = QtGui.QGridLayout()
        self.__oGrid.setColumnMinimumWidth(0,100)
        self.__oGrid.setContentsMargins(0,0,0,0)
        self.__oGrid.setColumnStretch(0,0)
        self.__oGrid.setColumnStretch(1,1)
        self.__oLabel = QtGui.QLabel(sName)
        self.__oLabel.setAlignment(QtCore.Qt.AlignRight)
        self.__oGrid.addWidget(self.__oLabel,0,0)
        self.__oGrid.addWidget(oWidget,0,1)
        self.setLayout(self.__oGrid)

class AlComboBox(QtGui.QComboBox):
    """Qt ComboBox with add items in it"""
    def __init__(self, listItems):
        """
        @type listItems: list of string
        @param listItems: title of items to add to the widget
        """
        QtGui.QComboBox.__init__(self)
        self.addItems(listItems)

class AlIconPushButton(QtGui.QPushButton):
    """Qt Push Button with Icon and tooltip and contextMenu"""

    def addAction(self, oActionWidget):
        """
        Add an action to the context menu
        @type oActionWidget: Object
        @param oActionWidget: QAction to add to the menu
        """
        self.__oMenu.addAction(oActionWidget)

    def addSeparator(self):
        """
        Add a separator to the context menu
        """
        self.__oMenu.addSeparator()

    def contextMenuEvent(self,event):
        """
        Creation of the context menu
        """
        self.__oMenu.exec_(event.globalPos())


    def __init__(self, sIcon, sToolTipText=''):
        """
        @type sIcon: string
        @param sIcon: Path of a picture
        @type sToolTipText: string
        @param sToolTipText: text of the tooltip
        """
        QtGui.QPushButton.__init__(self)
        self.__oIcon = QtGui.QIcon(sIcon)
        self.setIcon(self.__oIcon)
        self.setIconSize(QtCore.QSize(24,24))
        self.setToolTip(sToolTipText)
        self.setContentsMargins(0,0,0,0)
        self.__oMenu = QtGui.QMenu()

        self.connect(self,
                    QtCore.SIGNAL('clicked()'),
                    self.__emit)

    def __emit(self):
        """
        Emitting "AlIconPushButton_clicked" signal
        """
        self.emit(QtCore.SIGNAL('AlIconPushButton_clicked'), self)

class AlBloc (QtGui.QWidget):
    """
    Qt Widget containing a push button and a groupBox.
    Pushing the button will hide the groupBox
    The mainWindow will be resized after the groupBox is hidden
    """
    def __init__(self, oGui, sIconPath, sName, oWidget, resize=1):
        """
        @type oGui: Qt MainWindow
        @param oGui: Window containing Gui
        @type sIconPath: string
        @param param: path to the picture
        @type sName: string
        @param sName: title of the groupBox
        @type oWidget: Qt Widget
        @param oWidget: Widget contained by the groupBox
        """
        def __oBlocButton_onClicked():
            self.setHidden()

        oColor = QtGui.QColor(222,219,214)
        self.__boolResize = resize
        self.__oGui = oGui
        self.__boolHideState = 0
        QtGui.QWidget.__init__(self)
        self.__oMainLayout = QtGui.QHBoxLayout()
        self.__oMainLayout.setContentsMargins(0,0,0,0)
        #==================================================================
        # left
        #==================================================================
        self.__oLeftLayout = QtGui.QVBoxLayout()
        self.__oLeftLayout.setContentsMargins(0,0,0,0)
        self.__oBlocButton = QtGui.QPushButton()
        self.__oBlocButton.setFlat(1)
        pic = QtGui.QPixmap(sIconPath)
        self.__oIcon = QtGui.QIcon(pic)
        self.__oBlocButton.setIcon(self.__oIcon)
        self.__oBlocButton.setIconSize(QtCore.QSize(32,32))
        self.connect(self.__oBlocButton, QtCore.SIGNAL('clicked()'),
                            __oBlocButton_onClicked)
        self.__oLeftLayout.addWidget(self.__oBlocButton)
        self.__oLeftLayout.addStretch(1)
        #==================================================================
        # right
        #==================================================================
        self.__oRightParent = QtGui.QWidget()
        self.__oRightMainLayout = QtGui.QVBoxLayout()
        self.__oRightMainLayout.setContentsMargins(0,0,0,0)
        self.__oRightGrp = QtGui.QGroupBox(sName)
        self.__oRightGrp.setMinimumWidth(330)
        self.__oRightGrp.setContentsMargins(0,10,0,0)
        self.__oRightLayout = QtGui.QHBoxLayout(self.__oRightGrp)
        self.__oRightLayout.setContentsMargins(20,5,5,5)
        self.__oRightLayout.addWidget(oWidget)
        self.__oRightMainLayout.addWidget(self.__oRightGrp)
        self.__oRightParent.setLayout(self.__oRightMainLayout)
        #======================================================================
        # main
        #======================================================================
        self.__oMainLayout.addLayout(self.__oLeftLayout)
        self.__oMainLayout.addWidget(self.__oRightParent)
        self.__oMainLayout.addStretch(1)
        self.setLayout(self.__oMainLayout)

    def setHidden(self):
        if self.__boolHideState == 0:
                self.__boolHideState = 1
        else :
            self.__boolHideState = 0
        self.__oRightParent.setHidden(self.__boolHideState)
        if self.__boolResize == 1:
            self.__oGui.setMaximumHeight(1)

class AlItemView(QtGui.QWidget):
    """
    Widget in 2 parts :
        - top part is a QPushButton
        - bottom part is a QListWidget
    """
    # name of the list.
    # also the title of the top button.
    title = 'string'

    def setButtonIcon(self, sIcon):
        """
        Change the icon of the top button

        @type sIcon     : string
        @param sIcon    : path of the icon
        """
        self.__oIcon = QtGui.QIcon(sIcon)
        self.oButton.setIcon(self.__oIcon)

    def setListColor(self, r,g,b):
        """
        Set the color of the list.
        @type r: integer
        @param r: value of the red channel
        @type g: integer
        @param g: value of the green channel
        @type b: integer
        @param b: value of the blue channel
        """
        oColor = QtGui.QColor(r,g,b)
        self.oList.setStyleSheet(
                    "QWidget { background-color: %s }" % oColor.name())
        listFinds = self.oList.findItems(QtCore.QString('*'),
                                           QtCore.Qt.MatchWildcard)
        for oFind in listFinds:
            oFind.setBackgroundColor(oColor)

    def setColor(self,r,g,b):
        """
        Set the color of the top button.
        @type r: integer
        @param r: value of the red channel
        @type g: integer
        @param g: value of the green channel
        @type b: integer
        @param b: value of the blue channel
        """
        oColor = QtGui.QColor(r,g,b)
        self.__oTopGrpBox.setStyleSheet(
                    "QWidget { background-color: %s }" % oColor.name())

    def setListMinimumSize(self, width, height):
        """
        Change the minimum size of listview

        @type width     : integer
        @param width    : width of the list

        @type height    : integer
        @param height   : height of the list
        """
        self.oList.setMinimumSize(width, height)

    def enlightItem(self, sName , generation=1):
        """
        Set the background color of an item.
        Generation parameter allow to set different colors.
        @type sName: string
        @param sName: name of the item
        @type generation: interger
        @param generation: level of generation of the item
        """
        oString = QtCore.QString(sName)
        listFinds =  self.oList.findItems(oString,QtCore.Qt.MatchExactly)
        for oFind in listFinds:
            if generation == 1:
                oFind.setBackgroundColor(self.__oEnlightColor)
            else :
                oFind.setBackgroundColor(self.__oEnlightSecondGenerationColor)

    def delightItems(self):
        """
        Set the background color to 255,255,255.
        """
        listFinds = self.oList.findItems(QtCore.QString('*'),
                                           QtCore.Qt.MatchWildcard)
        for oFind in listFinds:
            oFind.setBackgroundColor(self.__oDelightColor)

    def setList(self, list):
        """
        Set elements for the QlistView.
        @type list: list of string
        @param list: name of element to add
        """
        for element in list :
            oElement = QtGui.QListWidgetItem()
            oElement.setText(element[0])
            oIcon = QtGui.QIcon(element[1])
            oElement.setIcon(oIcon)
            self.oList.addItem(oElement)

    def addItem(self, sName, sIcon='', bold=0, italic=0, underline=0):
        """
        Add one item to the list then sort the list.

        @type sName: string
        @param sName: name of the element to add

        @type bold: boolean
        @param bold: set the font as bold

        @type italic: boolean
        @param italic: set the font as italic

        @type underline: boolean
        @param underline: set the font as underline
        """
        oFont = QtGui.QFont()
        oFont.setBold(bold)
        oFont.setItalic(italic)
        oFont.setUnderline(underline)
        oElement = QtGui.QListWidgetItem()
        oElement.setText(sName)
        oIcon = QtGui.QIcon(sIcon)
        oElement.setIcon(oIcon)
        oElement.setFont(oFont)
        self.oList.addItem(oElement)
        self.oList.sortItems()

    def getSelectedItemList(self):
        """
        @rtype: list of objects
        @return: list of selected items
        """
        return self.oList.selectedItems()

    def clearSelection(self):
        """
        Unselect elements
        """
        self.oList.clearSelection()

    def setIconSize (self, x):
        """
        Change the size of Icon

        @type x     : integer
        @param x    : size of icon
        """
        self.oList.setIconSize(QtCore.QSize(x,x))

    def __init__(self, title, list, parent):
        """
        @type title: string
        @param title: name of the widget
        @type list: list of string
        @param list: names of elements to add
        @type parent: object
        @param parent: parent of the widget
        """
        def __oButton_onClicked():
            self.__setHidden()

        def __oList_onChanged():
            self.emit(QtCore.SIGNAL('list_changed'), self)

        self.title                      = title
        self.__boolHideState            = 0
        self.oParent                    = parent
        oColor                                  = QtGui.QColor(242,239,234)
        self.__oEnlightColor                    = QtGui.QColor(202,209,204)
        self.__oEnlightSecondGenerationColor    = QtGui.QColor(202,239,234)
        self.__oDelightColor                    = QtGui.QColor(255,255,255)

        QtGui.QWidget.__init__(self, self.oParent)
        self.setContentsMargins(0,0,0,0)
        oLayout                 = QtGui.QVBoxLayout()
        oLayout.setContentsMargins(0,0,0,0)
        #======================================================================
        # top
        #======================================================================
        self.__oTopGrpBox       = QtGui.QGroupBox()
        self.__oTopGrpBox.setCheckable(0)
        oTopGrpBoxLayout        = QtGui.QVBoxLayout(self.__oTopGrpBox)
        oTopGrpBoxLayout.setContentsMargins(0,0,0,0)
        oButton                 = QtGui.QPushButton(title)
        oButton.setFlat(1)
        oButton.setDisabled(0)
        oTopGrpBoxLayout.addWidget(oButton)
        self.connect(oButton,QtCore.SIGNAL('clicked()'),__oButton_onClicked)
        self.oButton = oButton
        #======================================================================
        # bottom
        #======================================================================
        self.__oBottomParent    = QtGui.QWidget()
        self.__oBottomParent.setContentsMargins(0,0,0,0)
        oBottomLayout           = QtGui.QVBoxLayout()
        oBottomLayout.setContentsMargins(0,0,0,0)
        self.oList              = AlListWidget()
        self.oList.setIconSize(QtCore.QSize(20,20))
        self.connect(self.oList, QtCore.SIGNAL('emit'),__oList_onChanged)
        self.oMenu              = self.oList.oMenu
        for element in list :
            oElement            = QtGui.QListWidgetItem(element)
            self.oList.addItem(oElement)
        self.oList.setSelectionMode(3)
        self.oList.setSelectionRectVisible(1)
        self.oList.setContextMenuPolicy(1)
        oBottomLayout.addWidget(self.oList)
        self.__oBottomParent.setLayout(oBottomLayout)
        #======================================================================
        # end
        #======================================================================
        oLayout.addWidget(self.__oTopGrpBox)
        oLayout.addWidget(self.__oBottomParent)
        oLayout.setStretchFactor(self.__oTopGrpBox,0)
        oLayout.setStretchFactor(self.__oBottomParent,20000)
        oLayout.addStretch(5)
        self.setLayout(oLayout)

    def __setHidden(self):
        """
        Hide the List Widget
        """
        if self.__boolHideState == 0:
                self.__boolHideState = 1
        else :
            self.__boolHideState = 0
        self.__oBottomParent.setHidden(self.__boolHideState)


class AlListWidget(QtGui.QListWidget):
    """
    Custom QListWidget with methods to deal with the context menu
    """

    def addAction(self, oActionWidget):
        """
        Add an action to the context menu
        @type oActionWidget: Object
        @param oActionWidget: QAction to add to the menu
        """
        self.oMenu.addAction(oActionWidget)

    def addSeparator(self):
        """
        Add a separator to the context menu
        """
        self.oMenu.addSeparator()

    def addString(self, oString):
        """
        Adding an string to the menu called by the context menu

        @type oString   : Qstring
        @param oString  : name of the entry
        """

        self.oMenu.addAction(oString)

    def contextMenuEvent(self,event):
        """
        Creation of the context menu
        """
        self.oMenu.exec_(event.globalPos())

    def enableContextMenu(self, iValue):
        """
        Disable (0) or enable (1) context menu

        @type iValue    : integer
        @param iValue   : 0 (disable) or 1 (enable)
        """
        self.__boolContextMenu = iValue

    def __init__(self):
        QtGui.QListWidget.__init__(self)

        # menu used by the context menu
        self.oMenu              = QtGui.QMenu()

        def __emit():
            self.emit(QtCore.SIGNAL('emit'), self, QtCore.Qt.MouseButton)

        self.connect(self,
                     QtCore.SIGNAL('itemClicked(QListWidgetItem*)'),
                     __emit)
# Ni !
