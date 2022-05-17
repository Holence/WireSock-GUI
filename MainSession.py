from DTPySide import *

class MainSession(DTSession.DTMainSession):

    def close(self):
        self.UserSetting().setValue("WindowStatus/Hidden",self.isHidden())
        super().close()
    
    def __init__(self, app):
        super().__init__(app)

        self.menu_wireguard=QMenu("WireGuard")
        self.menu_wireguard.setIcon(IconFromCurrentTheme("server.svg"))
        self.menu_sock=QMenu("Socks5")
        self.menu_sock.setIcon(IconFromCurrentTheme("umbrella.svg"))
        self.menu_log_level=QMenu("Log Level")
        self.menu_log_level.setIcon(IconFromCurrentTheme("file-text.svg"))
    
    def initializeWindow(self):
        super().initializeWindow()
        
        from MainWindow import MainWindow
        self.mainwindow=MainWindow(self)
        self.setCentralWidget(self.mainwindow)

        hidden=self.UserSetting().value("WindowStatus/Hidden")
        if hidden=="true":
            self.hide()
        else:
            self.show()
    
    def initializeSignal(self):
        super().initializeSignal()

        self.addAction(self.mainwindow.actionUpdate)

    def initializeMenu(self):
        self.addActionToMainMenu(self.mainwindow.actionToggle_Connection)
        self.addActionToMainMenu(self.mainwindow.actionUpdate)
        
        self.addSeparatorToMainMenu()
        self.addMenuToMainMenu(self.menu_wireguard)
        self.addActionToMainMenu(self.mainwindow.actionEnable_Socks5)
        self.addMenuToMainMenu(self.menu_sock)
        self.addMenuToMainMenu(self.menu_log_level)
        self.addSeparatorToMainMenu()
        
        super().initializeMenu()

    def saveWindowStatus(self):
        super().saveWindowStatus()
    
    def quit(self):
        
        if self.mainwindow.status!=0:
            self.mainwindow.TunnelDisconnect(showmessage=False)
        
        super().quit()