class Controls:
    def __init__(self, main_window, player):
        self.main_window = main_window
        self.player = player

    def connect_controls(self):
        self.main_window.play_button.clicked.connect(self.player.play)
        self.main_window.pause_button.clicked.connect(self.player.pause)
        self.main_window.stop_button.clicked.connect(self.player.stop)
        # 添加更多控件连接逻辑（如音量调节、进度条更新）


    #添加音量控制功能
    def __init__(self, main_window, player):
        self.main_window = main_window
        self.player = player

    def connect_controls(self):
        # 播放、暂停、停止按钮连接
        self.main_window.play_button.clicked.connect(self.player.play)
        self.main_window.pause_button.clicked.connect(self.player.pause)
        self.main_window.stop_button.clicked.connect(self.player.stop)

        # 音量滑动条连接
        self.main_window.volume_slider.valueChanged.connect(self.set_volume)

    def set_volume(self):
        volume = self.main_window.volume_slider.value()
        self.player.media_player.setVolume(volume)