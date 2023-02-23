import sys, os
from private_data import Private
from PySide2.QtWidgets import QFileDialog, QApplication, QMainWindow


absolute_path = os.path.dirname(__file__)
ui_import_path = os.path.join(os.path.dirname(__file__), "..", "ui", "ui_python")

sys.path.append(ui_import_path)

stylesheet_path = "..\\ui\\stylesheet\\"

from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()                                                                   #create MainWindow
        self.ui.setupUi(self)  
        self.ui.button_open_file.clicked.connect(self.filedialog)  
        

    def filedialog(self):
        directory = os.path.join(os.path.dirname(__file__),"..", "private")        
        filename = QFileDialog().getOpenFileName(self, ('load image'),directory, 'YAML (*.yaml)')[0]
        print(f'filename: {filename}')
        x = Private(filename)
        key = x.get('key')
        print (key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
    
    
#TODO add possibility to change Font Type. Change in .qss file but create a new file. If file exists, use custom file, otherwise use default file
