from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
from MainMenu import MainMenu


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = 'Managing tasks for students'

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)

    @pyqtSlot()
    def about(self):
        text = 'The program is designed to manage tasks and assignments for students'
        QMessageBox.about(self, self.title, text)

    @pyqtSlot()
    def about_qt(self):
        QMessageBox.aboutQt(self, self.title)
