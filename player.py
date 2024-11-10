from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer

class Player:
    def __init__(self):
        self.media_player = QMediaPlayer()

    def load_music(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        self.media_player.setMedia(QMediaContent(url))

    def play(self):
        self.media_player.play()

    def pause(self):
        self.media_player.pause()

    def stop(self):
        self.media_player.stop()


# 在 player.py 中更新进度条

    def __init__(self):
        self.media_player = QMediaPlayer()
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)

    def play(self):
        self.media_player.play()
        self.progress_timer.start(1000)  # 每秒更新一次进度条

    def stop(self):
        self.media_player.stop()
        self.progress_timer.stop()

    def update_progress(self):
        position = self.media_player.position()  # 获取当前播放进度（毫秒）
        self.main_window.progress_slider.setValue(position / 1000)  # 更新进度条（以秒为单位）

    def set_progress(self, position):
        self.media_player.setPosition(position * 1000)  # 将进度条的值转化为毫秒
