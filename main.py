from DTPySide import *
from MainSession import MainSession

app=DTAPP(sys.argv)

app.setWindowIcon(QIcon(QPixmap("icon.ico")))
app.setApplicationName("WireSock for NordVPN")
app.setApplicationVersion("1.0.0.1")
app.setAuthor("鍵山狐")
app.setQuitOnClickX(False)

mainsession=MainSession(app)
app.setMainSession(mainsession)

app.run()