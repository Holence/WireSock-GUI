from DTPySide import *
from MainWindow import MainWindow

class PingToolSession(DTFrame.DTMainWindow):
    
    closed=Signal()

    def closeEvent(self, event):        
        super().closeEvent(event)
        
        # save test servers
        servers=[]
        for row in range(self.ping_tool_module.tableWidget_test.rowCount()):
            name=self.ping_tool_module.tableWidget_test.item(row, 0).text()
            ip=self.ping_tool_module.tableWidget_test.item(row, 1).text()
            servers.append([name, ip])
        Json_Save(servers, "test.json")
        
        self.deleteLater()
        self.closed.emit()
    
    def __init__(self, app: DTAPP, Headquarter: MainWindow):
        super().__init__(app)
        self.Headquarter=Headquarter
        self.initialize()

    def initializeWindow(self):
        super().initializeWindow()
        self.setWindowTitle("Ping Tool")

        from PingTool import PingTool
        self.ping_tool_module=PingTool(self, self.Headquarter)
        self.setCentralWidget(self.ping_tool_module)

        self.resize(self.minimumWidth(),self.minimumHeight())
        self.adjustSize()
        MoveToCenterOfScreen(self)
