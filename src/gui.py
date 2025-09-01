from PyQt6 import QtWidgets, QtCore
from encryption import encrypt_file, decrypt_file
from tamper_protection import start_tamper_watcher
from decoy import create_decoy_files

def launch_gui():
    app = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    window.setWindowTitle('Pendrive Guardian Ultimate')
    window.setGeometry(300, 300, 400, 300)

    layout = QtWidgets.QVBoxLayout()

    btn_encrypt = QtWidgets.QPushButton('Encrypt USB')
    btn_encrypt.clicked.connect(lambda: QtWidgets.QMessageBox.information(window, 'Info', 'Encrypt Function Called'))
    btn_decrypt = QtWidgets.QPushButton('Decrypt USB')
    btn_decrypt.clicked.connect(lambda: QtWidgets.QMessageBox.information(window, 'Info', 'Decrypt Function Called'))
    btn_decoy = QtWidgets.QPushButton('Create Decoy Files')
    btn_decoy.clicked.connect(lambda: create_decoy_files())

    layout.addWidget(btn_encrypt)
    layout.addWidget(btn_decrypt)
    layout.addWidget(btn_decoy)

    window.setLayout(layout)
    window.show()

    # Start tamper watcher
    start_tamper_watcher()

    app.exec()
