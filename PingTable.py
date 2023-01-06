from DTPySide import *

class PingTable(DTWidget.DTHorizontalTabel):

    ping = Signal()

    def __init__(self, parent):
        super().__init__(parent)

    def startDrag(self, actions:Qt.DropActions):
        ######################################################################
        # MIME通信规则：
        # 
        # text: [[name, ip], ..., [name, ip]]
        ######################################################################
        
        indexes = self.selectedIndexes()
        mime = self.model().mimeData(indexes)
        
        servers=[]
        for model_index in self.selectionModel().selectedRows():
            row=model_index.row()
            
            name=self.item(row,0).text()
            ip=self.item(row,1).text()
            servers.append([name, ip])
        
        mime.setObjectName(self.objectName())
        mime.setText(json.dumps(servers))
        drag = QDrag(self)
        drag.setMimeData(mime)
        drag.exec_(actions)
    
    def dragEnterEvent(self, event:QDragEnterEvent):
        # 拖到自己
        if event.mimeData().objectName()==self.objectName():
            event.acceptProposedAction()
        else:
            # 只有test允许添加
            if self.objectName() == "test":
                if event.mimeData().hasText():
                    try:
                        json.loads(event.mimeData().text())
                        event.acceptProposedAction()
                    except:
                        event.ignore()

    def dropEvent(self, event:QDropEvent):
        # 拖到自己，去排序
        if event.mimeData().objectName()==self.objectName():
            super().dropEvent(event)
        else:
            # test里添加
            row=self.rowCount()
            for server in json.loads(event.mimeData().text()):
                self.addRow(row, [QTableWidgetItem(server[0]), QTableWidgetItem(server[1])])
                row+=1
    
    def keyPressEvent(self, event: QKeyEvent):
        if self.objectName() == "test":
            if event.key()==Qt.Key_Delete and not self.window().ping_tool_module.pinging:
                rows = set()
                for model_index in self.selectionModel().selectedRows():
                    rows.add(model_index.row())

                for row in sorted(rows, reverse=True):
                    self.removeRow(row)
        super().keyPressEvent(event)
    
    def mousePressEvent(self, event: QMouseEvent):

        def slotPing():
            self.ping.emit()
        
        def slotDelete():
            rows = set()
            for model_index in self.selectionModel().selectedRows():
                rows.add(model_index.row())

            for row in sorted(rows, reverse=True):
                self.removeRow(row)
        
        if self.objectName()=="test":
            if event.button()==Qt.RightButton:
                if len(self.selectionModel().selectedRows())>0:
                    pos=event.pos()
                    menu=QMenu()

                    actionPing=QAction("Ping Selected")
                    actionPing.triggered.connect(slotPing)
                    actionPing.setIcon(IconFromCurrentTheme("activity.svg"))
                    menu.addAction(actionPing)

                    actionDelete=QAction(QCoreApplication.translate("Library", "Delete Selected"))
                    actionDelete.triggered.connect(slotDelete)
                    actionDelete.setIcon(IconFromCurrentTheme("trash-2.svg"))
                    menu.addAction(actionDelete)
                    
                    if self.window().ping_tool_module.pinging:
                        actionPing.setEnabled(False)
                        actionDelete.setEnabled(False)

                    pos=self.mapToGlobal(pos)+QPoint(0,self.horizontalHeader().height())
                    menu.exec_(pos)
        
        super().mousePressEvent(event)