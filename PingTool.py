from DTPySide import *

from utils import *
from Ui_PingTool import Ui_PingTool
from MainWindow import MainWindow

class PingThread(QThread):

    inform = Signal(str)

    def __init__(self, parent, servers, count, timeout):
        super().__init__(parent)
        self.servers=servers
        self.count=count
        self.timeout=timeout
        self.result=[]
    
    def run(self):
        for server in self.servers:
            name=server[0]
            ip=server[1]
            
            rtt, ratio=ping_ip(ip, self.count, self.timeout)
            if ratio!=-1:
                ratio=int(ratio*100)
                if rtt!="inf":
                    rtt=int(rtt)
                    info="%s - %s\nRTT: %sms\nRatio: %s%%\n"%(name, ip, rtt, ratio)
                else:
                    info="%s - %s\nRTT: %s\nRatio: %s%%\n"%(name, ip, rtt, ratio)
            else:
                ratio = 0
                info="!! Cannot resolve:\n%s - %s\n"%(name, ip)
            
            self.inform.emit(info)
            self.result.append([name, ip, rtt, ratio])

class PingTool(Ui_PingTool,QWidget):
    
    def __init__(self, parent, Headquarter: MainWindow) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.Headquarter=Headquarter
    
        self.tableWidget_wireguard.setObjectName("wg")
        self.tableWidget_wireguard.setColumn(["Name", "IP"])
        self.tableWidget_wireguard.setColumnHidden(2,True)
        self.tableWidget_wireguard.setColumnWidth(0,100)
        self.tableWidget_wireguard.sortReset.connect(self.loadWG)
    
        self.tableWidget_socks.setObjectName("socks")
        self.tableWidget_socks.setColumn(["Name", "IP"])
        self.tableWidget_socks.setColumnHidden(2,True)
        self.tableWidget_socks.setColumnWidth(0,100)
        self.tableWidget_socks.sortReset.connect(self.loadSocks)
    
        self.tableWidget_test.setObjectName("test")
        self.tableWidget_test.setColumn(["Name", "IP", "RTT", "Ratio"])
        self.tableWidget_test.setColumnHidden(4,True)
        self.tableWidget_test.setColumnWidth(0,100)
        self.tableWidget_test.setColumnWidth(1,150)
        self.tableWidget_test.setColumnWidth(2,100)
        self.tableWidget_test.setColumnWidth(3,100)

        self.pushButton_ping.clicked.connect(lambda: self.ping_test("all"))
        self.tableWidget_test.ping.connect(lambda: self.ping_test("selected"))

        self.loadWG()
        self.loadSocks()
        self.loadTest()
        
        self.pinging=False
    
    def loadWG(self):
        self.tableWidget_wireguard.Clear()
        row=0
        for server in self.Headquarter.wg_servers:
            self.tableWidget_wireguard.addRow(row, [QTableWidgetItem(server["name"]), QTableWidgetItem(server["ip"])])
            row+=1
    
    def loadSocks(self):
        self.tableWidget_socks.Clear()
        row=0
        for server in self.Headquarter.socks_servers:
            self.tableWidget_socks.addRow(row, [QTableWidgetItem(server["name"]), QTableWidgetItem(server["ip"][:server["ip"].index(":")])])
            row+=1
    
    def loadTest(self):
        self.tableWidget_test.Clear()
        try:
            servers=Json_Load("test.json")
            row=0
            for server in servers:
                self.tableWidget_test.addRow(row, [QTableWidgetItem(server[0]), QTableWidgetItem(server[1])])
                row+=1
        except:
            pass

    def ping_test(self, mode):
        self.pushButton_ping.setEnabled(False)
        self.plainTextEdit.clear()

        count=self.spinBox_count.value()
        timeout=self.spinBox_timeout.value()
        
        servers=[]
        if mode=="all":
            for row in range(self.tableWidget_test.rowCount()):
                name=self.tableWidget_test.item(row, 0).text()
                ip=self.tableWidget_test.item(row, 1).text()
                servers.append([name, ip])
        elif mode=="selected":
            for model_index in self.tableWidget_test.selectionModel().selectedRows():
                row=model_index.row()
                name=self.tableWidget_test.item(row, 0).text()
                ip=self.tableWidget_test.item(row, 1).text()
                servers.append([name, ip])
        
        def slot():
            for res in self.ping_thread.result:
                for row in range(self.tableWidget_test.rowCount()):
                    name=self.tableWidget_test.item(row, 0).text()
                    ip=self.tableWidget_test.item(row, 1).text()
                    # 修改原来的那个
                    if name==res[0] and ip==res[1]:
                        self.tableWidget_test.setItem(row, 2, QTableWidgetItem("%4sms"%res[2] if res[2]!="inf" else " inf"))
                        self.tableWidget_test.setItem(row, 3, QTableWidgetItem("%3s%%"%res[3]))
            
            self.ping_thread.deleteLater()
            self.pushButton_ping.setEnabled(True)
            self.pinging=False

        self.ping_thread=PingThread(self, servers, count, timeout)
        self.ping_thread.start()
        self.pinging=True
        self.ping_thread.inform.connect(self.plainTextEdit.appendPlainText)
        self.ping_thread.finished.connect(slot)