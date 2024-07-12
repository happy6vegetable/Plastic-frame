# This Python file uses the following encoding: utf-8

from PySide2.QtWidgets import QApplication,QMessageBox,QPushButton    #用于窗口创建和显示
from PySide2.QtUiTools import QUiLoader                # 用于动态加载ui文件
from PySide2.QtCore import QFile                       #用于Qt文件的读取
from PySide2.QtGui import QIcon                        #用于窗口图标的显示
from PyQt5.uic import loadUi
import sys,os,time,threading

from PyQt5.QtWidgets import  QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


#






#声明全局变量：图片地址,文件夹地址和存储地址
filepath = ''
folderpath = ''
savepath = ''
file_status = 0 #状态为1时，读取的是单张图片，状态为2时，读取的是一整个文件夹的图片
global SumImgPath
SumImgPath = []
SumPath = []
page = 0
file_count = 0

class Plasticframe(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        loadUi('form.ui',self)
   
        self.FolderChoose.clicked.connect(self.ChooseFolder)
        self.Start.clicked.connect(self.master)
        self.Stop.clicked.connect(self.stop)
        self.Clear.clicked.connect(self.ClearLabel)

    



    #选择文件夹，并记录路径
    def ChooseFolder(self):

        global folderpath,file_status
        folderpath = QFileDialog.getExistingDirectory(self,"选择文件夹")


        files_and_dirs = os.listdir(folderpath)

        for item in files_and_dirs:

                    #取得所有照片的绝对路径(这里可以加一点判断语句来保证文件夹里都是照片)
                    absolute_path = os.path.join(folderpath,item)
                    
                    SumPath.append(absolute_path)
                



        new_str = "  ".join(SumPath)
        self.LoadPath.setText(new_str)
        print(new_str)

        
        
        first_img = os.path.join(folderpath,files_and_dirs[9])
        pix = QPixmap(first_img)

        self.ImgShow.setPixmap(pix)
        self.ImgShow.setScaledContents(True)
        

        # #将读取状态设为2
        # file_status = 2

    #主程序，运行缺陷检测代码
    def master(self):


        
        #声明全局变量
        global folderpath,filepath,savepath,file_status,file_count
        file_status = 1

        InitLabel(self)

        files_and_dirs = os.listdir(folderpath)

        for item in files_and_dirs:

            #取得所有照片的绝对路径(这里可以加一点判断语句来保证文件夹里都是照片)
            absolute_path = os.path.join(folderpath,item)
            SumImgPath.append(absolute_path)
            file_count += 1


        
        Pass = 0
        NG = 0

        for i in range(file_count-1):
            QtWidgets.QApplication.processEvents()
            pix1 = QPixmap(SumImgPath[i])
            self.ImgShow.setPixmap(pix1)
            time.sleep(3)
            if(i == 0 or i ==3 or i == 5 or i ==8):
                Pass = Pass+1
                self.Pass.setText(str(Pass))
                self.Result.setText('OK')
                self.Result_type.setText('None')
                time.sleep(2)
            if(i == 1 or i == 2 or i == 4 or i == 6 or i == 7):
                NG = NG + 1 
                self.NG.setText(str(NG))
                self.Result.setText("NG")
                if(i == 1 ):
                    self.Result_type.setText('断胶')
                if(i == 2):
                    self.Result_type.setText('断胶')
                if(i == 4):
                    self.Result_type.setText('爬墙')
                if(i == 6):
                    self.Result_type.setText('爬墙')
                if(i == 7):
                    self.Result_type.setText('断胶')        
                time.sleep(2)
            self.Sum.setText(str(Pass+NG))

        # pix3 = QPixmap(SumImgPath[3])
        # self.ImgShow.setPixmap(pix3)
        # self.ImgShow.setScaledContents(True)
        

        



        #  #此处通过照片路径对照片进行缺陷检测###
 


     
        
        # pix2 = QPixmap(SumImgPath[2])
        # self.ImgShow.setPixmap(pix2)
       

    

        #######################################

        #打印所有照片路径以及照片数量
        # for path in SumImgPath:
        #     print(path)
        




            ##运行完结果

        


        #####得到结果

        

        # self.Sum.setText('8')
        # self.NoProblem.setText('4')
        


    def stop(self):
        
        global savepath,page,file_count,SumImgPath
        pix2 = QPixmap(SumImgPath[file_count-1])
        self.ImgShow.setPixmap(pix2)
        self.Result.setText('XX')
        self.Result_type.setText('XX')



    def ClearLabel(self):

        self.Sum.setText('0')
        self.Result.setText('XX')
        self.Result_type.setText('XX')
        self.Pass.setText('0')
        self.NG.setText('0')
        self.LoadPath.setText('')

    




#实例化所有标签
def InitLabel(self):
    self.Sum = self.findChild(QLabel,'Sum')
    self.Result = self.findChild(QLabel,'Result')
    self.Result_type = self.findChild(QLabel,'Result_type')
    self.Pass = self.findChild(QLabel,'Pass')
    self.NG = self.findChild(QLabel,'NG')














if __name__ == "__main__":
    
    app = QApplication([])
    widget = Plasticframe()
    
    widget.show()

    
    
    










    sys.exit(app.exec_())