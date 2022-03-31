import os
import shutil


def deepin(base):
	
	base=os.path.abspath(base)
	os.chdir(base)

	for i in os.listdir("./"):
		if os.path.isdir(i):
			if i=="__pycache__":
				shutil.rmtree(os.path.abspath(i))
				continue
			deepin(i)
			os.chdir(base)
		else:
			name=os.path.splitext(i)[0]
			ext=os.path.splitext(i)[1]
			if ext==".ui":
				os.system("pyside2-uic %s.ui -o %s.py"%(name,name))
				with open("%s.py"%name,"r+",encoding="utf-8") as f:
					s=f.read()
					s=s.replace("import DT_rc","import DTPySide.DT_rc")
					s=s.replace("from DT","from DTPySide.DT")
					f.seek(0)
					f.write(s)

base=os.getcwd()
deepin(base)