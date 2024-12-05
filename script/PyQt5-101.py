from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("My Simple Gui")


    layout = QVBoxLayout()
    label = QLabel("Press The Button Below")
    textbox = QTextEdit()
    button = QPushButton("Press ME!")

    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec()


def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
