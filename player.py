from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


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
