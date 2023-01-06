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
        self.addActionToMainMenu(self.mainwindow.actionPing_Tool)
        
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
        
        try:
            self.mainwindow.ping_tool_window.close()
        except:
            pass
        
        super().quit()
    
    def about(self):
        about_text=""
        
        self.UserSetting().beginGroup("MetaData")
        for key in self.UserSetting().allKeys():
            about_text+="%s: %s\n"%(key,self.UserSetting().value(key))
        self.UserSetting().endGroup()

        about_text+="""\nThis is a SHELL without GHOST, so you must install WireSock VPN Client first!

Download WireSock at https://www.wiresock.net/"""

        DTFrame.DTMessageBox(self,"About",about_text,icon=DTIcon.Holo01())