from DTPySide import *
from MainSession import MainSession

app=DTAPP(sys.argv)

app.setWindowIcon(QIcon(QPixmap("icon/icon.ico")))
app.setApplicationName("WireSock GUI")
app.setApplicationVersion("1.0.0.8 build with DTPySide %s"%importlib.metadata.version('DTPySide'))
app.setAuthor("Holence")
app.setQuitOnClickX(False)

mainsession=MainSession(app)
app.setMainSession(mainsession)

app.run(show=False)