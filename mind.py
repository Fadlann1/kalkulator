from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
import time
from PyQt5.QtGui import QIntValidator, QFont
App = QApplication([])
windows = QWidget()
windows.setWindowTitle('kalkulator')

def press_tombol(simbol):
    inpyut = garis.text()
    garis.setText(inpyut + simbol)

def hasil():
    total = garis.text()
    try:
        if total.find('x') != -1:
            total = total.replace('x','*')
        if total.find(':') != -1:
            total = total.replace(':','/')
        result = eval(total)
        garis.setText(str(result))
    except:
        garis.setText('Errorrrr')
        App.processEvents()
        time.sleep(2)
        kelir()


def operasi(symbol):
    inpyut = garis.text()
    garis.setText(inpyut + ' ' + symbol + ' ')

def kelir():
    garis.clear()

vertikal = QVBoxLayout()
garis = QLineEdit()
garis.setStyleSheet("""
QLineEdit {
    background-color: gray;
    color: black;
}
""")
validator = QIntValidator()
font = QFont()
font.setPointSize(30)
garis.setValidator(validator)
garis.setFont(font)
garis.setMinimumSize(300, 80)
vertikal.addWidget(garis)

nol = QPushButton('0', clicked = lambda : press_tombol('0'))
nol.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
satu = QPushButton('1', clicked = lambda : press_tombol('1'))
satu.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
dua = QPushButton('2', clicked = lambda : press_tombol('2'))
dua.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
tiga = QPushButton('3', clicked = lambda : press_tombol('3'))
tiga.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
empat = QPushButton('4', clicked = lambda : press_tombol('4'))
empat.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
lima = QPushButton('5', clicked = lambda : press_tombol('5'))
lima.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
enam = QPushButton('6', clicked = lambda : press_tombol('6'))
enam.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
tujuh = QPushButton('7', clicked = lambda : press_tombol('7'))
tujuh.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
delapan = QPushButton('8', clicked = lambda : press_tombol('8'))
delapan.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
sembilan = QPushButton('9', clicked = lambda : press_tombol('9'))
sembilan.setStyleSheet("""
QPushButton {
    background-color: darkgray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
ikwal = QPushButton('=', clicked = hasil)
ikwal.setStyleSheet("""
QPushButton {
    background-color: gray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
mines = QPushButton('-', clicked = lambda : operasi('-'))
mines.setStyleSheet("""
QPushButton {
    background-color: gray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
plus = QPushButton('+', clicked = lambda : operasi('+'))
plus.setStyleSheet("""
QPushButton {
    background-color: gray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
bagi = QPushButton(':', clicked = lambda : operasi(':'))
bagi.setStyleSheet("""
QPushButton {
    background-color: gray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
kali = QPushButton('x', clicked = lambda : operasi('x'))
kali.setStyleSheet("""
QPushButton {
    background-color: gray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")
clear = QPushButton('C', clicked = kelir)
clear.setStyleSheet("""
QPushButton {
    background-color: gray;
    color: white;
}

QPushButton:hover {
    border-width: 2px;
    border-style: inset;
}

QPushButton:pressed {
    background-color: darkgray;
}
""")

vertikal_1st = QVBoxLayout()
vertikal_1st.addWidget(tujuh)
vertikal_1st.addWidget(empat)
vertikal_1st.addWidget(satu)
vertikal_1st.addWidget(clear)

vertikal_2st = QVBoxLayout()
vertikal_2st.addWidget(delapan)
vertikal_2st.addWidget(lima)
vertikal_2st.addWidget(dua)
vertikal_2st.addWidget(nol)

vertikal_3st = QVBoxLayout()
vertikal_3st.addWidget(sembilan)
vertikal_3st.addWidget(enam)
vertikal_3st.addWidget(tiga)
vertikal_3st.addWidget(ikwal)

vertikal_4st = QVBoxLayout()
vertikal_4st.addWidget(bagi)
vertikal_4st.addWidget(kali)
vertikal_4st.addWidget(plus)
vertikal_4st.addWidget(mines)

horizontal = QHBoxLayout()
horizontal.addLayout(vertikal_1st)
horizontal.addLayout(vertikal_2st)
horizontal.addLayout(vertikal_3st)
horizontal.addLayout(vertikal_4st)

vertikal.addLayout(horizontal)

windows.setLayout(vertikal)
windows.show()
App.exec_()