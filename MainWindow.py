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
        self.plainTextEdit.appendPlainText(result)
        if self.status==2:
            if "WireSock LightWeight WireGuard VPN Client is running already. Exit the second instance" in result:
                self.instance_exist.emit()
                DTFrame.DTMessageBox(
                    self.window(),
                    "Warning",
                    "WireSock LightWeight WireGuard VPN Client is running already.\n\nPlease exit the first instance please.",
                    DTIcon.Warning()
                )
    
    def initializeSignal(self):

        self.pushButton_wg_file.clicked.connect(self.setWGDir)
        self.lineEdit_wg_private_key.textEdited.connect(self.setWGPriKey)
        self.comboBox_wg.activated.connect(self.setWGServer)

        self.checkBox_sock5.stateChanged.connect(lambda :self.setSockEnable(self.checkBox_sock5.isChecked()))
        self.pushButton_sock_file.clicked.connect(self.setSockDir)
        self.lineEdit_sock_un.textEdited.connect(self.setSockUN)
        self.lineEdit_sock_pw.textEdited.connect(self.setSockPW)
        self.comboBox_sock.activated.connect(self.setSockServer)

        self.comboBox_log.activated.connect(self.setLogLevel)
        self.comboBox_connection_check.activated.connect(self.setConnectionCkeckKey)
        self.lineEdit_connection_check.textEdited.connect(self.setConnectionCkeckValue)
        self.lineEdit_extra_CMD.textEdited.connect(self.setExtraCMD)
        self.plainTextEdit_extra_conf.editingFinished.connect(self.setExtraConfig)
        self.pushButton_switch.clicked.connect(self.Switch)
        
        self.actionUpdate.triggered.connect(self.refresh)
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
        self.setStyleSheet("QLabel { font-size:12pt; }")
        self.plainTextEdit.setStyleSheet("font-size:10pt")
        self.plainTextEdit_extra_conf.setStyleSheet("font-size:10pt")
        self.plainTextEdit_extra_conf.setPlaceholderText("""AllowedApps = firefox
DisallowedApps = TIM
AllowedIPs = 
DisallowedIPs = 
""")

        self.splitter.setStretchFactor(0,1)
        self.splitter.setStretchFactor(1,10)

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

        self.sock_enable=self.Headquarter.UserSetting().value("Setting/SockEnable")
        if self.sock_enable=="true":
            self.sock_enable=True
        else:
            self.sock_enable=False
        self.Headquarter.UserSetting().setValue("Setting/SockEnable",self.sock_enable)
        self.checkBox_sock5.setChecked(self.sock_enable)
        self.setSockEnable(self.sock_enable)
        
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

        cck=self.Headquarter.UserSetting().value("Setting/ConnectionCheckKey")
        if cck==None:
            cck=0
            self.Headquarter.UserSetting().setValue("Setting/ConnectionCheckKey",cck)
        else:
            self.comboBox_connection_check.setCurrentText(cck)

        ccv=self.Headquarter.UserSetting().value("Setting/ConnectionCheckValue")
        self.lineEdit_connection_check.setText(ccv)

        extraCMD=self.Headquarter.UserSetting().value("Setting/ExtraCMD")
        self.lineEdit_extra_CMD.setText(extraCMD)

        extra_conf=self.Headquarter.UserSetting().value("Setting/ExtraConfig")
        self.plainTextEdit_extra_conf.setPlainText(extra_conf)
    
    def refresh(self):
        try:
            self.updateWGServers()
        except:
            pass
        try:
            self.updateSockServers()
        except:
            pass
        
        QTimer.singleShot(0, self.updateStatus)
    
    def updateStatus(self):
        
        info=get_current_info("all")
        if info=="Failed":
            status_text=f"   Tunnel {self.status_list[self.status]}  | Failed   "
        else:
            status_text=f"   Tunnel {self.status_list[self.status]}  | {info['ip']}  |  {info['country']}, {info['region']}, {info['city']}  |  {info['loc']}  |  {info['org']}  |  {info['timezone']}   "
        
        self.Headquarter.setStatusTip(status_text)
        
        if self.status==1:

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
                try:
                    name,ip,pubkey=map(str.strip,line.strip().split(","))
                    self.wg_servers.append({
                        "name":name,
                        "ip":ip,
                        "pubkey":pubkey
                    })
                    self.comboBox_wg.addItem(name+" | "+ip)
                except:
                    pass
        self.comboBox_wg.setCurrentIndex(self.current_wg_index)
    
    def setWGPriKey(self,pk):
        self.wg_prikey=pk
        self.Headquarter.UserSetting().setValue("Setting/WGPriKey",self.wg_prikey)
    
    def setWGServer(self,index):
        self.current_wg_index=index
        self.Headquarter.UserSetting().setValue("Setting/WGIndex",self.current_wg_index)

    ########################################################################
    
    def setSockEnable(self, enable):
        self.sock_enable=enable
        self.Headquarter.UserSetting().setValue("Setting/SockEnable",self.sock_enable)
        self.pushButton_sock_file.setEnabled(self.sock_enable)
        self.lineEdit_sock_un.setEnabled(self.sock_enable)
        self.lineEdit_sock_pw.setEnabled(self.sock_enable)
        self.comboBox_sock.setEnabled(self.sock_enable)

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
                try:
                    name,ip=map(str.strip,line.strip().split(","))
                    self.sock_servers.append({
                        "name": name,
                        "ip": ip
                    })
                    self.comboBox_sock.addItem(name+" | "+ip)
                except:
                    pass
        
        self.comboBox_sock.setCurrentIndex(self.current_sock_index)

    def setSockServer(self,index):
        self.current_sock_index=index
        self.Headquarter.UserSetting().setValue("Setting/SockIndex",self.current_sock_index)
    
    ########################################################################

    def setLogLevel(self,index):
        self.log_level=self.comboBox_log.itemText(index)
        self.Headquarter.UserSetting().setValue("Setting/LogLevel",self.log_level)
    
    def setConnectionCkeckKey(self,index):
        cck=self.comboBox_connection_check.itemText(index)
        self.Headquarter.UserSetting().setValue("Setting/ConnectionCheckKey",cck)
    
    def setConnectionCkeckValue(self,value):
        self.Headquarter.UserSetting().setValue("Setting/ConnectionCheckValue",value)
    
    def setExtraCMD(self):
        self.Headquarter.UserSetting().setValue("Setting/ExtraCMD",self.lineEdit_extra_CMD.text())
    
    def setExtraConfig(self):
        self.Headquarter.UserSetting().setValue("Setting/ExtraConfig",self.plainTextEdit_extra_conf.toPlainText())

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
                QTimer.singleShot(0, self.updateStatus)
                self.rolllling=False
                return
            
            self.Headquarter.setStatusTip("   Tunnel %s %s"%(self.status_list[self.status], rolling[i]))
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
        
        self.status=0
        
        self.pushButton_wg_file.setEnabled(True)
        self.lineEdit_wg_private_key.setEnabled(True)
        self.comboBox_wg.setEnabled(True)
        
        self.checkBox_sock5.setEnabled(True)
        if self.sock_enable:
            self.pushButton_sock_file.setEnabled(True)
            self.lineEdit_sock_un.setEnabled(True)
            self.lineEdit_sock_pw.setEnabled(True)
            self.comboBox_sock.setEnabled(True)

        self.comboBox_log.setEnabled(True)
        self.lineEdit_extra_CMD.setEnabled(True)
        self.plainTextEdit_extra_conf.setEnabled(True)
        
        self.comboBox_connection_check.setEnabled(True)
        self.lineEdit_connection_check.setEnabled(True)
        
        self.plainTextEdit.clear()
        
        QTimer.singleShot(0, self.refresh)

        self.Headquarter.app.showMessage(
            "Information",
            "Tunnel Disconnected",
            DTIcon.Information()
        )
    
    def TunnelConnect(self):

        self.pushButton_wg_file.setEnabled(False)
        self.lineEdit_wg_private_key.setEnabled(False)
        self.comboBox_wg.setEnabled(False)

        self.checkBox_sock5.setEnabled(False)
        if self.sock_enable:
            self.pushButton_sock_file.setEnabled(False)
            self.lineEdit_sock_un.setEnabled(False)
            self.lineEdit_sock_pw.setEnabled(False)
            self.comboBox_sock.setEnabled(False)

        self.comboBox_log.setEnabled(False)
        self.lineEdit_extra_CMD.setEnabled(False)
        self.plainTextEdit_extra_conf.setEnabled(False)
        
        self.comboBox_connection_check.setEnabled(False)
        self.lineEdit_connection_check.setEnabled(False)

        with open("temp.conf","w") as f:
            f.write(f"""[Interface]
PrivateKey = {self.wg_prikey}
Address = 10.5.0.2/32
DNS = 103.86.99.98, 103.86.96.98

[Peer]
PublicKey = {self.wg_servers[self.current_wg_index]["pubkey"]}
AllowedIPs = 0.0.0.0/0
Endpoint = {self.wg_servers[self.current_wg_index]["ip"]}:51820
{self.plainTextEdit_extra_conf.toPlainText()}
""")
            if self.sock_enable:
                f.write(f"""
Socks5ProxyUsername = {self.sock_un}
Socks5ProxyPassword = {self.sock_pw}
Socks5Proxy = {self.sock_servers[self.current_sock_index]["ip"]}
""")
        self.plainTextEdit.clear()

        self.plainTextEdit.appendPlainText("Connecting to WireGuard Server %s: %s"%(self.wg_servers[self.current_wg_index]["name"],self.wg_servers[self.current_wg_index]["ip"]))
        if self.sock_enable:
            self.plainTextEdit.appendPlainText("Using Socks5 Server %s: %s"%(self.sock_servers[self.current_sock_index]["name"],self.sock_servers[self.current_sock_index]["ip"]))
        self.plainTextEdit.appendPlainText("\nwiresock-client.exe run -log-level %s -config temp.conf %s\n"%(self.log_level, self.lineEdit_extra_CMD.text()))
        self.plainTextEdit.appendPlainText("WireSock LightWeight WireGuard VPN Client is running as a regular process.")
        
        os.system("ipconfig.exe /flushdns")
        self.process.start("wiresock-client.exe", ["run","-log-level" ,self.log_level, "-config", "temp.conf", self.lineEdit_extra_CMD.text()])
        
        self.status=2
        self.rolling(5)
        
        old_value=self.lineEdit_connection_check.text()
        while True:
            new_value=get_current_info(self.comboBox_connection_check.currentText())

            if old_value!=new_value and new_value!="Failed":
                self.status=1
                break
            else:
                if self.status==2:
                    self.rolling(5)
                else:
                    return
        
        QTimer.singleShot(0, self.updateStatus)
    
        self.Headquarter.app.showMessage(
            "Information",
            "Tunnel Connected",
            DTIcon.Information()
        )
    
    def Switch(self):
        if self.lineEdit_sock_pw.text()!="" and self.comboBox_wg.currentIndex()!=-1 and self.lineEdit_sock_un.text()!="" and self.lineEdit_sock_pw.text()!="" and self.comboBox_sock.currentIndex()!=-1 and self.lineEdit_connection_check.text()!="":
            if self.status==1 or self.status==2:
                self.TunnelDisconnect()
            elif self.status==0:
                self.TunnelConnect()
        else:
            DTFrame.DTMessageBox(self,"Warning","Information incomplete!",DTIcon.Warning())