import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from player import Player
from controls import Controls


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 初始化播放器，传入主窗口
        self.player = Player(self)
        self.controls = Controls(self, self.player)

        # 连接控件与方法
        self.controls.connect_controls()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
