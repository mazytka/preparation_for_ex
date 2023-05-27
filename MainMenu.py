from PyQt5.QtWidgets import QMenuBar


class MainMenu(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        help_menu = self.addMenu('Help')

        self.__about = help_menu.addAction('About the program...')
        self.about_qt = help_menu.addAction('about Qt...')

    @property
    def about(self):
        return self.__about


