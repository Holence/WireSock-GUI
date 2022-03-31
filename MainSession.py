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

        self.addAction(self.mainwindow.actionCheck_Status)

    def initializeMenu(self):
        self.addActionToMainMenu(self.mainwindow.actionCheck_Status)
        super().initializeMenu()
    
    def saveWindowStatus(self):
        super().saveWindowStatus()
    
    def quit(self):
        
        if self.mainwindow.status!=0:
            self.mainwindow.process.kill() # 然而并没有什么卵用
        
        super().quit()