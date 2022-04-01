from DTPySide import *

from utils import *
from MainSession import MainSession
from Ui_MainWindow import Ui_MainWindow
class MainWindow(Ui_MainWindow,QWidget):

    instance_exist=Signal()

    def __init__(self, Headquarter:MainSession) -> None:
        super().__init__(Headquarter)
        self.setupUi(self)
        self.Headquarter=Headquarter
        self.status_list=["Disconnected","Connected","Connecting","Disconnecting"]
        self.rolllling=False
        self.status=0
        self.current_ip=get_current_ip()

        self.initializeWindow()
        self.initializeSignal()

        self.process = QProcess()
        self.process.readyReadStandardError.connect(self.onReadyReadStandardError)
        self.process.readyReadStandardOutput.connect(self.onReadyReadStandardOutput)

        self.updateStatus()
    
    def onReadyReadStandardError(self):
        error = self.process.readAllStandardError().data().decode()
        self.plainTextEdit.appendPlainText(error)

    def onReadyReadStandardOutput(self):
        result = self.process.readAllStandardOutput().data().decode()
        if self.status==2 and "WireSock LightWeight WireGuard VPN Client is running already. Exit the second instance" in result:
            self.instance_exist.emit()
            DTFrame.DTMessageBox(
                self.window(),
                "Warning",
                "WireSock LightWeight WireGuard VPN Client is running already.\n\nPlease exit the first instance please.",
                DTIcon.Warning()
            )
        else:
            self.plainTextEdit.appendPlainText(result)
    
    def initializeSignal(self):

        self.pushButton_wg_file.clicked.connect(self.setWGDir)
        self.lineEdit_wg_private_key.textEdited.connect(self.setWGPriKey)
        self.comboBox_wg.activated.connect(self.setWGServer)

        self.pushButton_sock_file.clicked.connect(self.setSockDir)
        self.lineEdit_sock_un.textEdited.connect(self.setSockUN)
        self.lineEdit_sock_pw.textEdited.connect(self.setSockPW)
        self.comboBox_sock.activated.connect(self.setSockServer)

        self.comboBox_log.activated.connect(self.setLogLevel)
        self.pushButton_switch.clicked.connect(self.Switch)

        def update():
            self.updateStatus()
            self.updateWGServers()
            self.updateSockServers()
            
            self.current_ip=get_current_ip()
            self.Headquarter.app.showMessage(
                "Information",
                "Current IP: %s\nTunnel %s"%(self.current_ip,self.status_list[self.status]),
                DTIcon.Information()
            )
        
        self.actionUpdate.triggered.connect(update)
        self.actionUpdate.setIcon(IconFromCurrentTheme("refresh-cw.svg"))
        
        self.instance_exist.connect(self.TunnelDisconnect)
    
    def initializeWindow(self):
        self.pushButton_switch.setFlat(True)
        self.pushButton_switch.setStyleSheet("""
            border: none;
            icon-size: 22px;
            max-height: 26px;
            min-height: 26px;
            min-width: 26px;
            max-width: 26px;
        """)

        self.plainTextEdit.setStyleSheet("font-size:10pt")

        self.splitter.setStretchFactor(0,1)
        self.splitter.setStretchFactor(1,3)

        ##########################################################

        self.wg_dir=self.Headquarter.UserSetting().value("Setting/WGDir")
        self.lineEdit_wg_file.setText(self.wg_dir)

        self.current_wg_index=self.Headquarter.UserSetting().value("Setting/WGIndex")
        if self.current_wg_index==None:
            self.current_wg_index=-1
            self.Headquarter.UserSetting().setValue("Setting/WGIndex",self.current_wg_index)
        else:
            self.current_wg_index=int(self.current_wg_index)
        self.comboBox_wg.setCurrentIndex(self.current_wg_index)

        self.wg_prikey=self.Headquarter.UserSetting().value("Setting/WGPriKey")
        if self.wg_prikey==None:
            self.wg_prikey=""
            self.Headquarter.UserSetting().setValue("Setting/WGPriKey",self.wg_prikey)
        self.lineEdit_wg_private_key.setText(self.wg_prikey)

        if self.wg_dir:
            self.updateWGServers()

        ##########################################################

        self.sock_dir=self.Headquarter.UserSetting().value("Setting/SockDir")
        self.lineEdit_sock_file.setText(self.sock_dir)
        
        self.sock_un=self.Headquarter.UserSetting().value("Setting/SockUN")
        self.lineEdit_sock_un.setText(self.sock_un)
        
        self.sock_pw=self.Headquarter.UserSetting().value("Setting/SockPW")
        self.lineEdit_sock_pw.setText(self.sock_pw)

        self.current_sock_index=self.Headquarter.UserSetting().value("Setting/SockIndex")
        if self.current_sock_index==None:
            self.current_sock_index=-1
            self.Headquarter.UserSetting().setValue("Setting/SockIndex",self.current_sock_index)
        else:
            self.current_sock_index=int(self.current_sock_index)
        self.comboBox_sock.setCurrentIndex(self.current_sock_index)
        
        if self.sock_dir:
            self.updateSockServers()
        
        ##########################################################

        self.log_level=self.Headquarter.UserSetting().value("Setting/LogLevel")
        if self.log_level==None:
            self.log_level="none"
            self.Headquarter.UserSetting().setValue("Setting/LogLevel",self.log_level)
        self.comboBox_log.setCurrentText(self.log_level)
    
    def updateStatus(self):
        
        if self.status==1:
            self.Headquarter.setStatusTip("  Tunnel Connected  |  Current IP: %s"%self.current_ip)
            self.Headquarter.statusBar.setStyleSheet("color: #66d589")

            self.pushButton_switch.setIcon(IconFromCurrentTheme("wifi.svg"))
            self.pushButton_switch.setStyleSheet("""
                background: #66d589;
                border: none;
                icon-size: 22px;
                max-height: 26px;
                min-height: 26px;
                min-width: 26px;
                max-width: 26px;
            """)
        
        elif self.status==0:
            self.Headquarter.setStatusTip("  Tunnel Disconnected  |  Current IP: %s"%self.current_ip)
            self.Headquarter.statusBar.setStyleSheet("color: #fe5c5d")

            self.pushButton_switch.setIcon(IconFromCurrentTheme("wifi-off.svg"))
            self.pushButton_switch.setStyleSheet("""
                background: #fe5c5d;
                border: none;
                icon-size: 22px;
                max-height: 26px;
                min-height: 26px;
                min-width: 26px;
                max-width: 26px;
            """)
    
    def setWGDir(self):
        dir_dlg=QFileDialog(self,"Select WireGuard IP List File Directory")
        dir=dir_dlg.getOpenFileUrl(filter="Text files (*.txt);;")
        
        if not dir[0].isEmpty():
            dir=dir[0].toString()[8:]
            dir=dir.replace("/","\\")
            self.wg_dir=dir
            self.lineEdit_wg_file.setText(self.wg_dir)
            self.Headquarter.UserSetting().setValue("Setting/WGDir",self.wg_dir)

        self.updateWGServers()
    
    def updateWGServers(self):
        self.wg_servers=[]
        self.comboBox_wg.clear()
        with open(self.wg_dir,"r") as f:
            for line in f.readlines():
                name,ip,pubkey=map(str.strip,line.strip().split(","))
                self.wg_servers.append({
                    "name":name,
                    "ip":ip,
                    "pubkey":pubkey
                })
                self.comboBox_wg.addItem(name+" | "+ip)
        self.comboBox_wg.setCurrentIndex(self.current_wg_index)
    
    def setWGPriKey(self,pk):
        self.wg_prikey=pk
        self.Headquarter.UserSetting().setValue("Setting/WGPriKey",self.wg_prikey)
    
    def setWGServer(self,index):
        self.current_wg_index=index
        self.Headquarter.UserSetting().setValue("Setting/WGIndex",self.current_wg_index)

    ########################################################################

    def setSockDir(self):
        dir_dlg=QFileDialog(self,"Select Socks5 Servers List File Directory")
        dir=dir_dlg.getOpenFileUrl(filter="Text files (*.txt);;")
        if not dir[0].isEmpty():
            dir=dir[0].toString()[8:]
            dir=dir.replace("/","\\")
            self.sock_dir=dir
            self.lineEdit_sock_file.setText(self.sock_dir)
            self.Headquarter.UserSetting().setValue("Setting/SockDir",self.sock_dir)

        self.updateSockServers()
    
    def setSockUN(self,un):
        self.sock_un=un
        self.Headquarter.UserSetting().setValue("Setting/SockUN",self.sock_un)

    def setSockPW(self,pw):
        self.sock_pw=pw
        self.Headquarter.UserSetting().setValue("Setting/SockPW",self.sock_pw)

    def updateSockServers(self):
        self.sock_servers=[]
        self.comboBox_sock.clear()
        with open(self.sock_dir,"r") as f:
            for line in f.readlines():
                name,ip=map(str.strip,line.strip().split(","))
                self.sock_servers.append({
                    "name": name,
                    "ip": ip
                })
                self.comboBox_sock.addItem(name+" | "+ip)
        
        self.comboBox_sock.setCurrentIndex(self.current_sock_index)

    def setSockServer(self,index):
        self.current_sock_index=index
        self.Headquarter.UserSetting().setValue("Setting/SockIndex",self.current_sock_index)
    
    ########################################################################

    def setLogLevel(self,index):
        self.log_level=self.comboBox_log.itemText(index)
        self.Headquarter.UserSetting().setValue("Setting/LogLevel",self.log_level)
    
    def rolling(self, delay_sec):
        
        if self.rolllling==True:
            return
        
        self.rolllling=True
        
        rolling=["|","/","-","\\"]
        i=0
        rolls_per_second=2
        steps_per_sec=rolls_per_second*len(rolling)
        for j in range(steps_per_sec*delay_sec):
            
            if self.status==0 or self.status==1:
                self.updateStatus()
                self.rolllling=False
                return
            
            self.Headquarter.setStatusTip("  Tunnel %s %s |  Current IP: %s"%(self.status_list[self.status], rolling[i], self.current_ip))
            if i==len(rolling)-1:
                i=0
            else:
                i+=1
            Delay_Msecs(int(1000/steps_per_sec))
        
        self.rolllling=False

    def TunnelDisconnect(self):
        self.process.kill()
            
        self.status=3

        self.rolling(2)
        
        self.current_ip=get_current_ip()
        
        self.status=0
        
        self.pushButton_wg_file.setEnabled(True)
        self.lineEdit_wg_private_key.setEnabled(True)
        self.comboBox_wg.setEnabled(True)

        self.pushButton_sock_file.setEnabled(True)
        self.lineEdit_sock_un.setEnabled(True)
        self.lineEdit_sock_pw.setEnabled(True)
        self.comboBox_sock.setEnabled(True)

        self.comboBox_log.setEnabled(True)

        self.plainTextEdit.clear()
        
        self.updateStatus()

        self.Headquarter.app.showMessage(
            "Tunnel Disconnected",
            "Current IP: %s"%self.current_ip,
            DTIcon.Information()
        )
    
    def TunnelConnect(self):
        if self.current_ip=="Failed":
            DTFrame.DTMessageBox(self.window(),"Warning","Please press ctrl+r to update current ip first!",DTIcon.Warning())
            return

        self.pushButton_wg_file.setEnabled(False)
        self.lineEdit_wg_private_key.setEnabled(False)
        self.comboBox_wg.setEnabled(False)

        self.pushButton_sock_file.setEnabled(False)
        self.lineEdit_sock_un.setEnabled(False)
        self.lineEdit_sock_pw.setEnabled(False)
        self.comboBox_sock.setEnabled(False)

        self.comboBox_log.setEnabled(False)
        
        with open("temp.conf","w") as f:
            f.write(f"""[Interface]
PrivateKey = {self.wg_prikey}
Address = 10.5.0.2/32
DNS = 103.86.99.98, 103.86.96.98

[Peer]
PublicKey = {self.wg_servers[self.current_wg_index]["pubkey"]}
AllowedIPs = 0.0.0.0/0
Endpoint = {self.wg_servers[self.current_wg_index]["ip"]}:51820
Socks5ProxyUsername = {self.sock_un}
Socks5ProxyPassword = {self.sock_pw}
Socks5Proxy = {self.sock_servers[self.current_sock_index]["ip"]}
""")

        self.plainTextEdit.setPlainText("WireSock LightWeight WireGuard VPN Client is running as a regular process.")
        
        os.system("ipconfig.exe /flushdns")
        self.process.start("wiresock-client.exe",["run","-log-level" ,self.log_level, "-config", "temp.conf"])
        
        self.status=2
        self.rolling(5)
        
        old_ip=self.current_ip
        while True:
            self.current_ip=get_current_ip()

            if old_ip!=self.current_ip and self.current_ip!="Failed":
                self.status=1
                break
            else:
                if self.status==2:
                    self.rolling(5)
                else:
                    return
        
        self.updateStatus()
    
        self.Headquarter.app.showMessage(
            "Tunnel Connected",
            "Current IP: %s"%self.current_ip,
            DTIcon.Information()
        )
    
    def Switch(self):
        if self.lineEdit_sock_pw.text()!="" and self.comboBox_wg.currentIndex()!=-1 and self.lineEdit_sock_un.text()!="" and self.lineEdit_sock_pw.text()!="" and self.comboBox_sock.currentIndex()!=-1:
            if self.status==1 or self.status==2:
                self.TunnelDisconnect()
            elif self.status==0:
                self.TunnelConnect()
        else:
            DTFrame.DTMessageBox(self,"Warning","Information incomplete!",DTIcon.Warning())