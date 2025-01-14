import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from objc import objc_object
from AppKit import NSApplication, NSWindowBelow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop-Level Window")
        self.setGeometry(100, 100, 400, 200)

        # Add a label
        label = QLabel("This is a desktop-level window.", self)
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget
        layout = QVBoxLayout()
        layout.addWidget(label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Make the window stay behind all others
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        # Set desktop level on macOS
        if sys.platform == "darwin":
            self.set_mac_desktop_level()

    def set_mac_desktop_level(self):
        from ctypes import cdll, c_void_p

        # Access the native macOS window
        window_handle = self.winId()
        appkit = cdll.LoadLibrary("/System/Library/Frameworks/AppKit.framework/AppKit")
        ns_window = objc_object(c_void_p=window_handle)
        ns_window.setLevel_(NSWindowBelow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
