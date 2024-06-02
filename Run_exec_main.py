from io import StringIO
import sys
from Run_exec import Ui_MainWindow
from PyQt5 import QtWidgets
import threading


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.m_thread = threading.Thread()
        self.pushB_exec.clicked.connect(self.run_exec)

    def run_exec(self):
        original_stdout = sys.stdout
        if not self.checkB_cons.isChecked():
            sys.stdout = StringIO()
        try:
            if not self.checkB_cons.isChecked():
                exec(self.text_exec.toPlainText())
            else:
                if not self.m_thread.is_alive():
                    self.m_thread = threading.Thread(target=self.run_exec_t, daemon=True)
                    self.m_thread.start()
        except Exception as err:
            print("!!! Ошибка")
            print(err)
        if not self.checkB_cons.isChecked():
            output = sys.stdout.getvalue()
            self.text_print.setText(output)
            sys.stdout = original_stdout

    def closeEvent(self, event):
        if self.m_thread.is_alive():
            QtWidgets.QMessageBox.information(self,
                                                    'ВНИМАНИЕ',
                                                    'Не пытайтесь закрыть окно - выполняется процесс!')
            event.ignore()
        else:
            event.accept()  # Закрываем окно


    def run_exec_t(self):
        exec(self.text_exec.toPlainText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
