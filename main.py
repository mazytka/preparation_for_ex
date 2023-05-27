import sys
from App import App
from mainwindow import MainWindow


app = App(sys.argv)

main_window = MainWindow()
main_window.show()

result = app.exec()
sys.exit(result)
