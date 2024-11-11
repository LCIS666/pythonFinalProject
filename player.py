from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer, QObject
from mutagen.mp3 import MP3

class Player(QObject):
    def __init__(self, main_window):
        super().__init__()  # 显式调用父类的构造函数
        self.media_player = QMediaPlayer()
        self.main_window = main_window  # 引入主窗口以便更新进度条等控件
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)  # 连接进度更新信号

    def play(self):
        print("Attempting to play music...")
        self.media_player.play()
        if self.media_player.state() == QMediaPlayer.PlayingState:
            print("Music is playing.")
        else:
            print(f"Failed to play music. State: {self.media_player.state()}")
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

    # 显示歌曲信息
    def load_music(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        self.media_player.setMedia(QMediaContent(url))
        if self.media_player.media().isNull():
            print("Failed to load music.")
        else:
            print(f"Music loaded: {file_path}")

        # 提取歌曲元数据
        audio_file = MP3(file_path)
        title = audio_file.tags.get('TIT2', '未知标题')  # 获取歌曲标题
        artist = audio_file.tags.get('TPE1', '未知艺术家')  # 获取艺术家名称

        # 更新界面显示
        self.main_window.song_label.setText(f"{title} - {artist}")
