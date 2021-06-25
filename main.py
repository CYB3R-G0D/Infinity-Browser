import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction(QIcon('res/backward.png'), 'Back', self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setShortcut('Ctrl+B')
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('res/forward.png'), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('res/refresh.png'), 'Refresh', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setShortcut('Ctrl+R')
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('res/home.png'), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        home_btn.setShortcut('H')
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setPlaceholderText('Enter address: http://')
        navbar.addWidget(self.url_bar)

        search_btn = QAction(QIcon('res/search.png'), 'Search', self)
        search_btn.triggered.connect(self.navigate_home)
        navbar.addAction(search_btn)

        history = QAction(QIcon('res/history.png'), 'History', self)
        history.triggered.connect(self.navigate_home)
        navbar.addAction(history)

        quit = QAction(self)
        quit.triggered.connect(self.quit)
        quit.setShortcut('Ctrl+Q')
        navbar.addAction(quit)        

        self.browser.urlChanged.connect(self.update_url)
        

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))

    def navigate_to_url(self):
        url = self.url_bar.text().replace(' ','+')
        self.browser.setUrl(QUrl('https://duckduckgo.com/?q='+url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def history(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
    
    def quit(self):
        reply = QMessageBox.question(self, 'Confirm close',
        "You are about to exit. Are you sure you want to exit?", QMessageBox.Yes | 
        QMessageBox.No, QMessageBox.Yes) # parent, title, message, buttons, default button

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            pass            


app = QApplication(sys.argv)
QApplication.setApplicationName('Infinity Browser')
QApplication.setWindowIcon(QIcon('res/ico.png'))
window = MainWindow()
app.exec_()