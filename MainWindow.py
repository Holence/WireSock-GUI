from DTPySide import *

from utils import *
from MainSession import MainSession

class RollingThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.papa=parent
    
    def run(self):
        
        wait=2
        self.papa.rolling(wait)
        
        old_value=self.papa.lineEdit_connection_check.text()
        while True:
            info=get_current_info('all')
            if info!="Failed":
                new_value=info[self.papa.comboBox_connection_check.currentText()]
                if old_value!=new_value:
                    self.papa.status=1
                    break
                else:
                    if self.papa.status==2:
                        self.papa.rolling(wait)
                        wait+=2
                    else:
                        return
            else:
                self.papa.rolling(wait)
                wait+=2
        
        self.papa.updateStatus(info=info)

class InfoThread(QThread):

    def __init__(self, parent):
        super().__init__(parent)
        self.papa=parent
    
    def run(self):
        info=get_current_info('all')

        if self.papa.status!=0:
            if info=="Failed":
                status_text=f"   Tunnel {self.papa.status_list[self.papa.status]}  | Failed   "
            else:
                status_text=f"   Tunnel {self.papa.status_list[self.papa.status]}  | {info['ip']}  |  {info['country']}, {info['region']}, {info['city']}  |  {info['loc']}  |  {info['org']}  |  {info['timezone']}   "
        else:
            status_text=f"   Tunnel {self.papa.status_list[self.papa.status]}"
        
        self.papa.Headquarter.setStatusTip(status_text)


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
        self.wg_servers=[]
        self.sock_servers=[]

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
        self.pushButton_openwg.clicked.connect(self.openWG)
        self.lineEdit_wg_private_key.textEdited.connect(self.setWGPriKey)
        self.comboBox_wg.activated.connect(self.setWGServer)

        self.checkBox_socks5.stateChanged.connect(lambda :self.setSockEnable(self.checkBox_socks5.isChecked()))
        self.pushButton_sock_file.clicked.connect(self.setSockDir)
        self.pushButton_opensock.clicked.connect(self.openSock)
        self.pushButton_getsock.clicked.connect(self.getSock)
        self.comboBox_nordapi.activated.connect(lambda :self.Headquarter.UserSetting().setValue("Socks/SocksAPI", self.comboBox_nordapi.currentIndex()))
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
        
        self.actionToggle_Connection.triggered.connect(self.Switch)
        
        self.actionEnable_Socks5.triggered.connect(lambda : self.setSockEnable( not self.sock_enable))

        self.action_log_level_list=[]
        for index, text  in enumerate(["none","debug","all"]):
            action=QAction(text,checkable=True)
            action.triggered.connect( partial(self.setLogLevel,index) )
            self.action_log_level_list.append(action)
            self.Headquarter.menu_log_level.addAction(action)
        self.action_log_level_list[self.comboBox_log.currentIndex()].setChecked(True)
        
        self.instance_exist.connect(self.TunnelDisconnect)

        self.actionPing_Tool.triggered.connect(self.ping_tool)
        self.actionPing_Tool.setIcon(IconFromCurrentTheme("activity.svg"))
    
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
        self.setStyleSheet("QLabel { font-size:12pt; } QCheckBox,QLineEdit,QComboBox,QPlainTextEdit {font-size: 11pt;}")
        self.lineEdit_extra_CMD.setPlaceholderText("-lac")
        self.plainTextEdit_extra_conf.setPlaceholderText("""AllowedApps = firefox
DisallowedApps = TIM
AllowedIPs = 
DisallowedIPs = 
""")
        self.pushButton_getsock.setIcon(IconFromCurrentTheme("download-cloud.svg"))

        self.pushButton_openwg.setStyleSheet("QPushButton{ min-height:16px; max-height:16px; min-width:16px; max-width:16px; icon-size:12px; }")
        self.pushButton_openwg.setIcon(IconFromCurrentTheme("external-link.svg"))
        self.pushButton_opensock.setStyleSheet("QPushButton{ min-height:16px; max-height:16px; min-width:16px; max-width:16px; icon-size:12px; }")
        self.pushButton_opensock.setIcon(IconFromCurrentTheme("external-link.svg"))

        ##########################################################

        self.wg_dir=self.Headquarter.UserSetting().value("WireGuard/WGDir")
        self.lineEdit_wg_file.setText(self.wg_dir)

        self.current_wg_index=self.Headquarter.UserSetting().value("WireGuard/WGIndex")
        if self.current_wg_index==None:
            self.current_wg_index=-1
            self.Headquarter.UserSetting().setValue("WireGuard/WGIndex",self.current_wg_index)
        else:
            self.current_wg_index=int(self.current_wg_index)
        self.comboBox_wg.setCurrentIndex(self.current_wg_index)

        self.wg_prikey=self.Headquarter.UserSetting().value("WireGuard/WGPriKey")
        if self.wg_prikey==None:
            self.wg_prikey=""
            self.Headquarter.UserSetting().setValue("WireGuard/WGPriKey",self.wg_prikey)
        self.lineEdit_wg_private_key.setText(self.wg_prikey)

        if self.wg_dir:
            self.updateWGServers()

        ##########################################################

        self.sock_enable=self.Headquarter.UserSetting().value("Socks/SocksEnable")
        if self.sock_enable=="true":
            self.sock_enable=True
        else:
            self.sock_enable=False
        self.Headquarter.UserSetting().setValue("Socks/SocksEnable",self.sock_enable)
        self.checkBox_socks5.setChecked(self.sock_enable)
        self.setSockEnable(self.sock_enable)
        
        self.sock_dir=self.Headquarter.UserSetting().value("Socks/SocksDir")
        self.lineEdit_sock_file.setText(self.sock_dir)

        sockapi=self.Headquarter.UserSetting().value("Socks/SocksAPI")
        if not sockapi:
            sockapi=0
            self.Headquarter.UserSetting().setValue("Socks/SocksAPI",sockapi)
        self.comboBox_nordapi.setCurrentIndex(int(sockapi))
        
        self.sock_un=self.Headquarter.UserSetting().value("Socks/SocksUN")
        self.lineEdit_sock_un.setText(self.sock_un)
        
        self.sock_pw=self.Headquarter.UserSetting().value("Socks/SocksPW")
        self.lineEdit_sock_pw.setText(self.sock_pw)

        self.current_sock_index=self.Headquarter.UserSetting().value("Socks/SocksIndex")
        if self.current_sock_index==None:
            self.current_sock_index=-1
            self.Headquarter.UserSetting().setValue("Socks/SocksIndex",self.current_sock_index)
        else:
            self.current_sock_index=int(self.current_sock_index)
        self.comboBox_sock.setCurrentIndex(self.current_sock_index)
        
        if self.sock_dir:
            self.updateSockServers()
        
        ##########################################################

        self.log_level=self.Headquarter.UserSetting().value("WireSock/LogLevel")
        if self.log_level==None:
            self.log_level="none"
            self.Headquarter.UserSetting().setValue("WireSock/LogLevel",self.log_level)
        self.comboBox_log.setCurrentText(self.log_level)

        cck=self.Headquarter.UserSetting().value("WireSock/ConnectionCheckKey")
        if cck==None:
            cck=0
            self.Headquarter.UserSetting().setValue("WireSock/ConnectionCheckKey",cck)
        else:
            self.comboBox_connection_check.setCurrentText(cck)

        ccv=self.Headquarter.UserSetting().value("WireSock/ConnectionCheckValue")
        self.lineEdit_connection_check.setText(ccv)

        extraCMD=self.Headquarter.UserSetting().value("WireSock/ExtraCMD")
        self.lineEdit_extra_CMD.setText(extraCMD)

        extra_conf=self.Headquarter.UserSetting().value("WireSock/ExtraConfig")
        self.plainTextEdit_extra_conf.setPlainText(extra_conf)
    
    def refresh(self):
        if self.status==2 or self.status==3:
            return
        
        try:
            self.updateWGServers()
        except:
            pass
        try:
            self.updateSockServers()
        except:
            pass
        
        self.updateStatus()
    
    def updateStatus(self, info=None):
                
        if self.status!=0:
            if info==None:
                status_text=f"   Tunnel {self.status_list[self.status]}  | Updating Info...   "
                self.Headquarter.setStatusTip(status_text)

                try:
                    self.info_thread
                    if not self.info_thread.isRunning():
                        self.info_thread = InfoThread(self)
                        self.info_thread.start()
                        self.info_thread.finished.connect(self.info_thread.deleteLater)
                except:
                    self.info_thread = InfoThread(self)
                    self.info_thread.start()
                    self.info_thread.finished.connect(self.info_thread.deleteLater)
            
            else:
                if info=="Failed":
                    status_text=f"   Tunnel {self.status_list[self.status]}  | Failed   "
                else:
                    status_text=f"   Tunnel {self.status_list[self.status]}  | {info['ip']}  |  {info['country']}, {info['region']}, {info['city']}  |  {info['loc']}  |  {info['org']}  |  {info['timezone']}   "
                
                self.Headquarter.setStatusTip(status_text)
        else:
            status_text=f"   Tunnel {self.status_list[self.status]}"

            self.Headquarter.setStatusTip(status_text)
        
        if self.status==1:

            self.Headquarter.statusBar.setStyleSheet("color: #7af64a")

            self.pushButton_switch.setIcon(IconFromCurrentTheme("wifi.svg"))
            self.pushButton_switch.setStyleSheet("""
                background: #7af64a;
                border: none;
                icon-size: 22px;
                max-height: 26px;
                min-height: 26px;
                min-width: 26px;
                max-width: 26px;
            """)
        
            self.Headquarter.app.TrayIcon.setIcon(QIcon(QPixmap("icon/icon-on.ico")))
            self.actionToggle_Connection.setIcon(IconFromCurrentTheme("wifi.svg"))
            self.actionToggle_Connection.setText("Disconnected")

        elif self.status==0:
            
            self.Headquarter.statusBar.setStyleSheet("color: #f54b79")

            self.pushButton_switch.setIcon(IconFromCurrentTheme("wifi-off.svg"))
            self.pushButton_switch.setStyleSheet("""
                background: #f54b79;
                border: none;
                icon-size: 22px;
                max-height: 26px;
                min-height: 26px;
                min-width: 26px;
                max-width: 26px;
            """)
            
            self.Headquarter.app.TrayIcon.setIcon(QIcon(QPixmap("icon/icon-down.ico")))
            self.actionToggle_Connection.setIcon(IconFromCurrentTheme("wifi-off.svg"))
            self.actionToggle_Connection.setText("Connected")
    
    def setWGDir(self):
        dir_dlg=QFileDialog(self,"Select WireGuard IP List File Directory")
        dir=dir_dlg.getOpenFileUrl(filter="Text files (*.txt);;")
        
        if not dir[0].isEmpty():
            dir=dir[0].toString()[8:]
            dir=dir.replace("/","\\")
            self.wg_dir=dir
            self.lineEdit_wg_file.setText(self.wg_dir)
            self.Headquarter.UserSetting().setValue("WireGuard/WGDir",self.wg_dir)

            self.updateWGServers()
    
    def openWG(self):
        if not self.wg_dir:
            DTFrame.DTMessageBox(self,"Warning","Please select WireGuard IP List File first!",DTIcon.Warning())
            return
        
        try:
            os.startfile(self.wg_dir)
        except Exception as e:
            DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Error())


    def updateWGServers(self):
        self.comboBox_wg.clear()
        with open(self.wg_dir,"r") as f:
            for line in f.readlines():
                try:
                    comment=""
                    if ";" in line:
                        line,comment=line.strip().split(";")
                    
                    name,ip,pubkey=map(str.strip,line.strip().split(","))
                    self.wg_servers.append({
                        "name":name,
                        "ip":ip,
                        "pubkey":pubkey
                    })

                    if not comment:
                        self.comboBox_wg.addItem(name+" - "+ip)
                    else:
                        self.comboBox_wg.addItem(name+" - "+ip+" - "+comment)
                except:
                    pass

        self.action_WG_list=[]
        for index in range(self.comboBox_wg.count()):
            text=self.comboBox_wg.itemText(index)
            action=QAction(text,checkable=True)
            action.triggered.connect( partial(self.setWGServer,index) )
            self.action_WG_list.append(action)
        self.action_WG_list[self.comboBox_wg.currentIndex()].setChecked(True)

        self.Headquarter.menu_wireguard.clear()
        for action in self.action_WG_list:
            self.Headquarter.menu_wireguard.addAction(action)

        if self.current_wg_index==-1 or self.comboBox_wg.count()-1<self.current_wg_index:
            self.current_wg_index=0
        self.setWGServer(self.current_wg_index)

    def setWGPriKey(self,pk):
        self.wg_prikey=pk
        self.Headquarter.UserSetting().setValue("WireGuard/WGPriKey",self.wg_prikey)
    
    def setWGServer(self,index):
        self.current_wg_index=index
        self.Headquarter.UserSetting().setValue("WireGuard/WGIndex",self.current_wg_index)

        self.comboBox_wg.setCurrentIndex(index)
        self.action_WG_list[index].setChecked(True)
        for i in range(len(self.action_WG_list)):
            if i!=index:
                self.action_WG_list[i].setChecked(False)

    ########################################################################
    
    def setSockEnable(self, enable):
        self.sock_enable=enable
        self.checkBox_socks5.setChecked(self.sock_enable)
        self.Headquarter.UserSetting().setValue("Socks/SocksEnable",self.sock_enable)
        self.pushButton_sock_file.setEnabled(self.sock_enable)
        self.comboBox_nordapi.setEnabled(self.sock_enable)
        self.pushButton_getsock.setEnabled(self.sock_enable)
        self.lineEdit_sock_un.setEnabled(self.sock_enable)
        self.lineEdit_sock_pw.setEnabled(self.sock_enable)
        self.comboBox_sock.setEnabled(self.sock_enable)

        self.Headquarter.menu_sock.setEnabled(self.sock_enable)
        if self.sock_enable:
            self.actionEnable_Socks5.setText("Socks5 Enabled")
            self.actionEnable_Socks5.setIcon(IconFromCurrentTheme("toggle-right.svg"))
        else:
            self.actionEnable_Socks5.setText("Socks5 Disabled")
            self.actionEnable_Socks5.setIcon(IconFromCurrentTheme("toggle-left.svg"))

    def setSockDir(self):
        dir_dlg=QFileDialog(self,"Select Socks5 Servers List File Directory")
        dir=dir_dlg.getOpenFileUrl(filter="Text files (*.txt);;")

        if not dir[0].isEmpty():
            dir=dir[0].toString()[8:]
            dir=dir.replace("/","\\")
            self.sock_dir=dir
            self.lineEdit_sock_file.setText(self.sock_dir)
            self.Headquarter.UserSetting().setValue("Socks/SocksDir",self.sock_dir)

            self.updateSockServers()

    def openSock(self):
        if not self.sock_dir:
            DTFrame.DTMessageBox(self,"Warning","Please select Socks5 Servers List File first!",DTIcon.Warning())
            return
        
        try:
            os.startfile(self.sock_dir)
        except Exception as e:
            DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Error())
    
    def getSock(self):
        if not self.sock_dir:
            DTFrame.DTMessageBox(self,"Warning","Please select Socks5 Servers List File first!",DTIcon.Warning())
            return
        
        try:
            url="%s/v1/servers?limit=20000"%self.comboBox_nordapi.currentText()
            pool=urllib3.connection_from_url(url,timeout=8)
            r=pool.urlopen("GET",url)
            text=r.data.decode("utf-8")
            servers = json.loads(text)

            socks5_list=[]
            for i in servers:
                if "socks" in i["hostname"]:
                    socks5_list.append((i["hostname"].replace("socks-","").replace(".nordvpn.com",""),i["station"]+":1080",i["load"]))
            socks5_list.sort(key=lambda x:x[-1])

            with open(self.sock_dir,"w") as f:
                for i in socks5_list:
                    f.write("%s,\t\t%s\t\t;%s\n"%(i[0],i[1],i[2]))
        
            self.updateSockServers()
            DTFrame.DTMessageBox(self,"Information","Success",DTIcon.Happy())

        except Exception as e:
            DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Error())
    
    def setSockUN(self,un):
        self.sock_un=un
        self.Headquarter.UserSetting().setValue("Socks/SocksUN",self.sock_un)

    def setSockPW(self,pw):
        self.sock_pw=pw
        self.Headquarter.UserSetting().setValue("Socks/SocksPW",self.sock_pw)

    def updateSockServers(self):
        self.comboBox_sock.clear()
        with open(self.sock_dir,"r") as f:
            for line in f.readlines():
                try:
                    comment=""
                    if ";" in line:
                        line,comment=line.strip().split(";")
                    
                    name,ip=map(str.strip,line.split(","))
                    self.sock_servers.append({
                        "name": name,
                        "ip": ip
                    })
                    if not comment:
                        self.comboBox_sock.addItem(name+" - "+ip)
                    else:
                        self.comboBox_sock.addItem(name+" - "+ip+" - "+comment)
                except:
                    pass
        
        self.action_Sock_list=[]
        for index in range(self.comboBox_sock.count()):
            text=self.comboBox_sock.itemText(index)
            action=QAction(text,checkable=True)
            action.triggered.connect( partial(self.setSockServer,index) )
            self.action_Sock_list.append(action)
        self.action_Sock_list[self.comboBox_sock.currentIndex()].setChecked(True)

        self.Headquarter.menu_sock.clear()
        for action in self.action_Sock_list:
            self.Headquarter.menu_sock.addAction(action)
        
        if self.current_sock_index==-1 or self.comboBox_sock.count()-1<self.current_sock_index:
            self.current_sock_index=0
        self.setSockServer(self.current_sock_index)

    def setSockServer(self,index):
        self.current_sock_index=index
        self.Headquarter.UserSetting().setValue("Socks/SocksIndex",self.current_sock_index)

        self.comboBox_sock.setCurrentIndex(index)
        self.action_Sock_list[index].setChecked(True)
        for i in range(len(self.action_Sock_list)):
            if i!=index:
                self.action_Sock_list[i].setChecked(False)
    
    ########################################################################

    def setLogLevel(self,index):
        self.log_level=self.comboBox_log.itemText(index)
        self.Headquarter.UserSetting().setValue("WireSock/LogLevel",self.log_level)

        self.comboBox_log.setCurrentIndex(index)
        self.action_log_level_list[index].setChecked(True)
        for i in range(len(self.action_log_level_list)):
            if i!=index:
                self.action_log_level_list[i].setChecked(False)
    
    def setConnectionCkeckKey(self,index):
        cck=self.comboBox_connection_check.itemText(index)
        self.Headquarter.UserSetting().setValue("WireSock/ConnectionCheckKey",cck)
    
    def setConnectionCkeckValue(self,value):
        self.Headquarter.UserSetting().setValue("WireSock/ConnectionCheckValue",value)
    
    def setExtraCMD(self):
        self.Headquarter.UserSetting().setValue("WireSock/ExtraCMD",self.lineEdit_extra_CMD.text())
    
    def setExtraConfig(self):
        self.Headquarter.UserSetting().setValue("WireSock/ExtraConfig",self.plainTextEdit_extra_conf.toPlainText())

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

    def TunnelDisconnect(self, showmessage=True):
        self.process.kill()
        
        self.status=0
        
        self.pushButton_wg_file.setEnabled(True)
        self.lineEdit_wg_private_key.setEnabled(True)
        self.comboBox_wg.setEnabled(True)
        self.Headquarter.menu_wireguard.setEnabled(True)
        
        self.checkBox_socks5.setEnabled(True)
        self.actionEnable_Socks5.setEnabled(True)
        if self.sock_enable:
            self.pushButton_sock_file.setEnabled(True)
            self.comboBox_nordapi.setEnabled(True)
            self.pushButton_getsock.setEnabled(True)
            self.lineEdit_sock_un.setEnabled(True)
            self.lineEdit_sock_pw.setEnabled(True)
            self.comboBox_sock.setEnabled(True)
            self.Headquarter.menu_sock.setEnabled(True)

        self.comboBox_log.setEnabled(True)
        self.Headquarter.menu_log_level.setEnabled(True)
        self.lineEdit_extra_CMD.setEnabled(True)
        self.plainTextEdit_extra_conf.setEnabled(True)
        
        self.comboBox_connection_check.setEnabled(True)
        self.lineEdit_connection_check.setEnabled(True)
        
        self.plainTextEdit.clear()
        
        self.refresh()

        if showmessage==True:
            self.Headquarter.app.showMessage(
                "Information",
                "Tunnel Disconnected",
                DTIcon.Information()
            )
    
    def TunnelConnect(self, showmessage=True):

        self.pushButton_wg_file.setEnabled(False)
        self.lineEdit_wg_private_key.setEnabled(False)
        self.comboBox_wg.setEnabled(False)
        self.Headquarter.menu_wireguard.setEnabled(False)

        self.checkBox_socks5.setEnabled(False)
        self.actionEnable_Socks5.setEnabled(False)
        if self.sock_enable:
            self.pushButton_sock_file.setEnabled(False)
            self.comboBox_nordapi.setEnabled(False)
            self.pushButton_getsock.setEnabled(False)
            self.lineEdit_sock_un.setEnabled(False)
            self.lineEdit_sock_pw.setEnabled(False)
            self.comboBox_sock.setEnabled(False)
            self.Headquarter.menu_sock.setEnabled(False)

        self.comboBox_log.setEnabled(False)
        self.Headquarter.menu_log_level.setEnabled(False)
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

        self.Headquarter.app.TrayIcon.setIcon(QIcon(QPixmap("icon/icon-wait.ico")))

        self.plainTextEdit.clear()

        self.plainTextEdit.appendPlainText("Connecting to WireGuard Server %s: %s"%(self.wg_servers[self.current_wg_index]["name"],self.wg_servers[self.current_wg_index]["ip"]))
        if self.sock_enable:
            self.plainTextEdit.appendPlainText("Using Socks5 Server %s: %s"%(self.sock_servers[self.current_sock_index]["name"],self.sock_servers[self.current_sock_index]["ip"]))
        self.plainTextEdit.appendPlainText("\nwiresock-client.exe run -log-level %s -config temp.conf %s\n"%(self.log_level, self.lineEdit_extra_CMD.text()))
        self.plainTextEdit.appendPlainText("WireSock LightWeight WireGuard VPN Client is running as a regular process.")
        
        self.process.start("ipconfig.exe", ["/flushdns"])
        self.process.waitForFinished()
        self.process.start("wiresock-client.exe", ["run","-log-level" ,self.log_level, "-config", "temp.conf", self.lineEdit_extra_CMD.text()])
        self.status=2

        def slot():
            if self.status==1:
                self.Headquarter.app.showMessage(
                    "Information",
                    "Tunnel Connected",
                    DTIcon.Information()
                )
            self.rolling_thread.deleteLater()

        self.rolling_thread=RollingThread(self)
        self.rolling_thread.start()
        self.rolling_thread.finished.connect(slot)
    
    def Switch(self):
        if self.status==1 or self.status==2:
            self.TunnelDisconnect()
        elif self.status==0:
            if self.lineEdit_wg_private_key.text()=="" or self.comboBox_wg.currentIndex()==-1:
                DTFrame.DTMessageBox(self,"Warning","WireGuard info incomplete!",DTIcon.Warning())
                return
            if self.sock_enable:
                if self.lineEdit_sock_un.text()=="" or self.lineEdit_sock_pw.text()=="" or self.comboBox_sock.currentIndex()==-1:
                    DTFrame.DTMessageBox(self,"Warning","Socks5 info incomplete!",DTIcon.Warning())
                    return
            if self.lineEdit_connection_check.text()=="":
                DTFrame.DTMessageBox(self,"Warning","Connection Check incomplete!",DTIcon.Warning())
                return
            else:
                self.TunnelConnect()
    
    def ping_tool(self):
        def slot():
            del self.ping_tool_window
        
        if hasattr(self,"ping_tool_window"):
            ShowUp(self.ping_tool_window)
            return
        
        from PingToolSession import PingToolSession
        self.ping_tool_window=PingToolSession(self.Headquarter.app, self)
        self.ping_tool_window.closed.connect(slot)
        self.ping_tool_window.show()