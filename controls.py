from PyQt5.QtWidgets import QFileDialog, QListWidgetItem
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class Controls:
    def __init__(self, main_window, player):
        self.main_window = main_window
        self.player = player

    def connect_controls(self):
        # 连接播放、暂停、停止按钮
        self.main_window.play_button.clicked.connect(self.player.play)
        print("Play button connected.")
        self.main_window.pause_button.clicked.connect(self.player.pause)
        self.main_window.stop_button.clicked.connect(self.player.stop)

        # 连接音量滑动条
        self.main_window.volume_slider.valueChanged.connect(self.set_volume)

        # 连接打开文件按钮
        self.main_window.open_button.clicked.connect(self.load_music)

        # 连接播放列表选择功能
        self.main_window.playlist_widget.itemClicked.connect(self.play_from_playlist)

    def set_volume(self):
        volume = self.main_window.volume_slider.value()
        self.player.media_player.setVolume(volume)
        print(f"Volume set to: {volume}")

    def load_music(self):
        # 弹出文件选择对话框，选择音乐文件
        file_paths, _ = QFileDialog.getOpenFileNames(self.main_window, "选择音乐文件", "", "音频文件 (*.mp3 *.wav)")
        if file_paths:
            for file_path in file_paths:
                try:
                    self.player.load_music(file_path)  # 加载文件
                    self.add_song_to_playlist(file_path)  # 添加到播放列表
                    print(f"Added {file_path} to playlist.")
                except Exception as e:
                    print(f"Failed to load {file_path}: {e}")

    def add_song_to_playlist(self, file_path):
        # 将歌曲添加到列表中
        song_name = file_path.split('/')[-1]  # 获取文件名
        item = QListWidgetItem(song_name)
        item.setData(Qt.UserRole, file_path)  # 存储文件路径
        self.main_window.playlist_widget.addItem(item)

    def play_from_playlist(self, item):
        if item:
            file_path = item.data(QtCore.Qt.UserRole)  # 获取歌曲路径
            try:
                self.player.load_music(file_path)
                self.player.play()
                print(f"Playing {file_path}")
            except Exception as e:
                print(f"Failed to play {file_path}: {e}")
