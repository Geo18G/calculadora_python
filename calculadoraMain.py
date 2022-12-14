from VISTA.calculadora import Ui_Calculadora
from PyQt5.QtWidgets import *
import sys, eventos


class calculadora(QDialog):
    def __init__(self):
        super(calculadora, self).__init__()
        self.calculadora = Ui_Calculadora()
        self.calculadora.setupUi(self)
        self.calculadora.btn0.clicked.connect(lambda: self.btnClicked("0"))
        self.calculadora.btn1.clicked.connect(lambda: self.btnClicked("1"))
        self.calculadora.btn2.clicked.connect(lambda: self.btnClicked("2"))
        self.calculadora.btn3.clicked.connect(lambda: self.btnClicked("3"))
        self.calculadora.btn4.clicked.connect(lambda: self.btnClicked("4"))
        self.calculadora.btn5.clicked.connect(lambda: self.btnClicked("5"))
        self.calculadora.btn6.clicked.connect(lambda: self.btnClicked("6"))
        self.calculadora.btn7.clicked.connect(lambda: self.btnClicked("7"))
        self.calculadora.btn8.clicked.connect(lambda: self.btnClicked("8"))
        self.calculadora.btn9.clicked.connect(lambda: self.btnClicked("9"))
        self.calculadora.btnSuma.clicked.connect(lambda: self.btnClicked("+"))
        self.calculadora.btnRestar.clicked.connect(lambda: self.btnClicked("-"))
        self.calculadora.btnMultiplicar.clicked.connect(lambda: self.btnClicked("*"))
        self.calculadora.btnDividir.clicked.connect(lambda: self.btnClicked("/"))
        self.calculadora.btnPA.clicked.connect(lambda: self.btnClicked("("))
        self.calculadora.btnPC.clicked.connect(lambda: self.btnClicked(")"))
        self.calculadora.btnC.clicked.connect(lambda: self.btnClicked("C"))
        self.calculadora.btnIgual.clicked.connect(lambda: self.btnClicked("="))
        self.calculadora.btnPunto.clicked.connect(lambda: self.btnClicked("."))

    def keyPressEvent(self, event):
        self.validarLabel()
        eventos.teclas(event, 
        self.calculadora.label,
        self.calculadora.lineEdit)

    def btnClicked(self, boton):
        self.validarLabel()
        texto = self.calculadora.label.text()
        if boton.isnumeric() == True or boton.isalnum() == False and boton != "=":
            self.calculadora.label.setText(texto + boton)
        elif boton == "C":
            self.calculadora.lineEdit.clear()
            self.calculadora.label.clear()
        elif boton == "=":
            if self.calculadora.lineEdit.text() != "":
                self.calculadora.lineEdit.clear()        
            try:     
                self.calculadora.lineEdit.insert(str(eval(texto)))
            except:
                self.calculadora.lineEdit.insert("Sintax Error :)")
                
    def validarLabel(self):
        if self.calculadora.label.text() == "CalculadoraQT":
            self.calculadora.label.setText("")

if __name__ == "__main__":
    app = QApplication([])
    myApp = calculadora()
    myApp.show()
    sys.exit(app.exec_())