import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PyQt App")
        self.setGeometry(100, 100, 400, 200)

        # Add a label
        label = QLabel("Hello, PyQt!", self)
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget
        layout = QVBoxLayout()
        layout.addWidget(label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
