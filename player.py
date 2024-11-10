from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer

class Player:
    def __init__(self, main_window):
        self.media_player = QMediaPlayer()
        self.main_window = main_window  # 引入主窗口以便更新进度条等控件
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)

    def load_music(self, file_path):
        # 设置媒体内容并加载音乐
        url = QUrl.fromLocalFile(file_path)
        self.media_player.setMedia(QMediaContent(url))

    def play(self):
        self.media_player.play()
        self.progress_timer.start(1000)  # 每秒更新一次进度条

    def pause(self):
        self.media_player.pause()
        self.progress_timer.stop()

    def stop(self):
        self.media_player.stop()
        self.progress_timer.stop()

    def update_progress(self):
        # 获取当前播放进度（毫秒）并更新进度条
        position = self.media_player.position()
        duration = self.media_player.duration()
        if duration > 0:
            progress_value = (position / duration) * 100  # 计算进度百分比
            self.main_window.progress_slider.setValue(progress_value)

    def set_progress(self, position):
        # 将进度条的值（百分比）转化为毫秒并设置播放位置
        duration = self.media_player.duration()
        if duration > 0:
            new_position = (position / 100) * duration
            self.media_player.setPosition(new_position)
