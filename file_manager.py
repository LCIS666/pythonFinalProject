from PyQt5.QtWidgets import QFileDialog
def open_file_dialog():
    file_path, _ = QFileDialog.getOpenFileName(None, "选择音乐文件", "", "音频文件 (*.mp3 *.wav)")
    return file_path
