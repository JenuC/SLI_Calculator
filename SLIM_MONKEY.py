from SLI_CALCULATOR_main import *
if __name__ == '__main__':
    qapp = QtGui.QApplication(sys.argv)
    window_slim_calc = sli_calc()
    window_slim_calc.show()
    qapp.exec_()
