from DTPySide import *

class MainSession(DTSession.DTMainSession):

    def __init__(self, app):
        super().__init__(app)
    
    def initializeWindow(self):
        super().initializeWindow()
        
        from MainWindow import MainWindow
        self.mainwindow=MainWindow(self)
        self.setCentralWidget(self.mainwindow)
    
    def initializeSignal(self):
        super().initializeSignal()

        self.addAction(self.mainwindow.actionUpdate)

    def initializeMenu(self):
        self.addActionToMainMenu(self.mainwindow.actionToggle_Connection)
        self.addActionToMainMenu(self.mainwindow.actionUpdate)
        super().initializeMenu()
    
    def saveWindowStatus(self):
        super().saveWindowStatus()
    
    def quit(self):
        
        if self.mainwindow.status!=0:
            self.mainwindow.TunnelDisconnect(showmessage=False)
        
        super().quit()