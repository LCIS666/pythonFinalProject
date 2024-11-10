class Controls:
    def __init__(self, main_window, player):
        self.main_window = main_window
        self.player = player

    def connect_controls(self):
        self.main_window.play_button.clicked.connect(self.player.play)
        self.main_window.pause_button.clicked.connect(self.player.pause)
        self.main_window.stop_button.clicked.connect(self.player.stop)
        # 添加更多控件连接逻辑（如音量调节、进度条更新）
