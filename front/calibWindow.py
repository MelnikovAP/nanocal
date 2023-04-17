from silx.gui import qt
from settings import *
from messageWindows import *
import sys
sys.path.append('./')
from shared.constants import *
import requests


class calibWindow(qt.QDialog):
    def __init__(self, parent=None):
        super(calibWindow, self).__init__(parent=parent)

        # ####### UI setup
        # ########################################
        short_line_input_width = 60

        self.setWindowTitle("Calibration info")
        self.setFixedHeight(700)
        self.setFixedWidth(450)
        self.setWindowFlag(qt.Qt.WindowContextHelpButtonHint, False)

        mainLayout = qt.QVBoxLayout()
        mainLayout.setAlignment(qt.Qt.AlignHCenter)
        self.setLayout(mainLayout)
        
        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        labl = qt.QLabel("Calibration info: ")
        labl.setMinimumWidth(75)
        lout_1.addWidget(labl)
        self.calibInfoInput = qt.QLineEdit()
        self.calibInfoInput.setFrame(False)
        lout_1.addWidget(self.calibInfoInput)

        self.ttplBox = qt.QGroupBox("Thermopile temperature")
        mainLayout.addWidget(self.ttplBox)
        lout_0 = qt.QVBoxLayout()
        self.ttplBox.setLayout(lout_0)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        self.ttplBoxLabl1 = qt.QLabel("000.000")
        self.ttplBoxLabl2 = qt.QLabel("000.000")
        self.ttplBoxInput1 = qt.QLineEdit()
        self.ttplBoxInput1.setMaximumWidth(short_line_input_width)
        self.ttplBoxInput1.setFrame(False)
        self.ttplBoxResetButton = qt.QPushButton("->0")
        self.ttplBoxResetButton.setFixedWidth(25)
        self.ttplBoxResetButton.setFocusPolicy(qt.Qt.NoFocus)
        lout_1.setSpacing(0)
        lout_1.addWidget(qt.QLabel("Utpl, mV : "))
        lout_1.addWidget(self.ttplBoxLabl1)
        lout_1.addWidget(qt.QLabel(" = "))
        lout_1.addWidget(self.ttplBoxLabl2)
        lout_1.addWidget(qt.QLabel(" + "))
        lout_1.addWidget(self.ttplBoxInput1)
        lout_1.addStretch()
        lout_1.addWidget(self.ttplBoxResetButton)
        lout_2 = qt.QHBoxLayout()
        lout_0.addLayout(lout_2)
        self.ttplBoxLabl2 = qt.QLabel("000.000")
        self.ttplBoxInput2 = qt.QLineEdit()
        self.ttplBoxInput2.setMaximumWidth(short_line_input_width)
        self.ttplBoxInput2.setFrame(False)
        self.ttplBoxInput3 = qt.QLineEdit()
        self.ttplBoxInput3.setMaximumWidth(short_line_input_width)
        self.ttplBoxInput3.setFrame(False)
        lout_2.setSpacing(0)
        lout_2.addWidget(qt.QLabel(u"Ttpl, \u2103 : "))
        lout_2.addWidget(self.ttplBoxLabl2)
        lout_2.addWidget(qt.QLabel(" = "))
        lout_2.addWidget(self.ttplBoxInput2)
        lout_2.addWidget(qt.QLabel(u" \u2219 Utpl + "))
        lout_2.addWidget(self.ttplBoxInput3)
        lout_2.addWidget(qt.QLabel(u" \u2219 "))
        lout_2.addWidget(qt.QLabel("Utpl<sup>2</sup>"))
        lout_2.addStretch()

        self.uhtrBox = qt.QGroupBox("Modulation heater rel. voltage")
        mainLayout.addWidget(self.uhtrBox)
        lout_0 = qt.QHBoxLayout()
        self.uhtrBox.setLayout(lout_0)
        self.uhtrBoxLabl1 = qt.QLabel("000.000")
        self.uhtrBoxLabl2 = qt.QLabel("000.000")
        self.uhtrBoxInput1 = qt.QLineEdit()
        self.uhtrBoxInput1.setMaximumWidth(short_line_input_width)
        self.uhtrBoxInput1.setFrame(False)
        self.uhtrBoxInput2 = qt.QLineEdit()
        self.uhtrBoxInput2.setMaximumWidth(short_line_input_width)
        self.uhtrBoxInput2.setFrame(False)
        self.uhtrBoxResetButton = qt.QPushButton("->0")
        self.uhtrBoxResetButton.setFixedWidth(25)
        self.uhtrBoxResetButton.setFocusPolicy(qt.Qt.NoFocus)
        lout_0.setSpacing(0)
        lout_0.addWidget(qt.QLabel("Uhtr, mV : "))
        lout_0.addWidget(self.uhtrBoxLabl1)
        lout_0.addWidget(qt.QLabel(" = ( "))
        lout_0.addWidget(self.uhtrBoxLabl2)
        lout_0.addWidget(qt.QLabel(" + "))
        lout_0.addWidget(self.uhtrBoxInput1)
        lout_0.addWidget(qt.QLabel(u" ) \u2219 "))
        lout_0.addWidget(self.uhtrBoxInput2)
        lout_0.addStretch()
        lout_0.addWidget(self.uhtrBoxResetButton)
        
        self.ihtrBox = qt.QGroupBox("Modulation heater current")
        mainLayout.addWidget(self.ihtrBox)
        lout_0 = qt.QHBoxLayout()
        self.ihtrBox.setLayout(lout_0)
        self.ihtrBoxLabl1 = qt.QLabel("000.000")
        self.ihtrBoxInput1 = qt.QLineEdit()
        self.ihtrBoxInput1.setMaximumWidth(short_line_input_width)
        self.ihtrBoxInput1.setFrame(False)
        self.ihtrBoxInput2 = qt.QLineEdit()
        self.ihtrBoxInput2.setMaximumWidth(short_line_input_width)
        self.ihtrBoxInput2.setFrame(False)
        self.ihtrBoxLabl2 = qt.QLabel("000.000")
        lout_0.setSpacing(0)
        lout_0.addWidget(qt.QLabel("Ihtr, mA : "))
        lout_0.addWidget(self.ihtrBoxLabl1)
        lout_0.addWidget(qt.QLabel(" = "))
        lout_0.addWidget(self.ihtrBoxInput1)
        lout_0.addWidget(qt.QLabel(" + "))
        lout_0.addWidget(self.ihtrBoxInput2)
        lout_0.addWidget(qt.QLabel(u" \u2219 "))
        lout_0.addWidget(self.ihtrBoxLabl2)
        lout_0.addStretch()
        
        self.thtrBox = qt.QGroupBox("Modulation heater temperature")
        mainLayout.addWidget(self.thtrBox)
        lout_0 = qt.QVBoxLayout()
        self.thtrBox.setLayout(lout_0)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        self.thtrBoxLabl1 = qt.QLabel("000.000")
        lout_1.setSpacing(0)
        lout_1.addWidget(qt.QLabel(u"R, \u03A9 : "))
        lout_1.addWidget(self.thtrBoxLabl1)
        lout_1.addStretch()
        lout_2 = qt.QHBoxLayout()
        lout_0.addLayout(lout_2)
        self.thtrBoxLabl2 = qt.QLabel("000.000")
        self.thtrBoxInput1 = qt.QLineEdit()
        self.thtrBoxInput1.setMaximumWidth(short_line_input_width)
        self.thtrBoxInput1.setFrame(False)
        self.thtrBoxInput2 = qt.QLineEdit()
        self.thtrBoxInput2.setMaximumWidth(short_line_input_width)
        self.thtrBoxInput2.setFrame(False)
        self.thtrBoxInput3 = qt.QLineEdit()
        self.thtrBoxInput3.setMaximumWidth(short_line_input_width)
        self.thtrBoxInput3.setFrame(False)
        lout_2.setSpacing(0)
        lout_2.addWidget(qt.QLabel(u"Thtr, \u2103 : "))
        lout_2.addWidget(self.thtrBoxLabl2)
        lout_2.addWidget(qt.QLabel(" = "))
        lout_2.addWidget(self.thtrBoxInput1)
        lout_2.addWidget(qt.QLabel(" + "))
        lout_2.addWidget(self.thtrBoxInput2)
        lout_2.addWidget(qt.QLabel(u" \u2219 R + "))
        lout_2.addWidget(self.thtrBoxInput3)
        lout_2.addWidget(qt.QLabel(u" \u2219 ")) 
        lout_2.addWidget(qt.QLabel("R<sup>2</sup>"))
        lout_2.addStretch()

        self.thtrdBox = qt.QGroupBox("Dynamic modulation heater temperature")
        mainLayout.addWidget(self.thtrdBox)
        lout_0 = qt.QVBoxLayout()
        self.thtrdBox.setLayout(lout_0)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        self.thtrdBoxLabl1 = qt.QLabel("000.000")
        self.thtrdBoxLabl2 = qt.QLabel("000.000")
        lout_1.setSpacing(0)
        lout_1.addWidget(qt.QLabel(u"R, \u03A9 : "))
        lout_1.addWidget(self.thtrdBoxLabl1)
        lout_1.addWidget(qt.QLabel(" / "))
        lout_1.addWidget(self.thtrdBoxLabl2)
        lout_1.addStretch()
        lout_2 = qt.QHBoxLayout()
        lout_0.addLayout(lout_2)
        self.thtrdBoxLabl2 = qt.QLabel("000.000")
        self.thtrdBoxInput1 = qt.QLineEdit()
        self.thtrdBoxInput1.setMaximumWidth(short_line_input_width)
        self.thtrdBoxInput1.setFrame(False)
        self.thtrdBoxInput2 = qt.QLineEdit()
        self.thtrdBoxInput2.setMaximumWidth(short_line_input_width)
        self.thtrdBoxInput2.setFrame(False)
        self.thtrdBoxInput3 = qt.QLineEdit()
        self.thtrdBoxInput3.setMaximumWidth(short_line_input_width)
        self.thtrdBoxInput3.setFrame(False)
        lout_2.setSpacing(0)
        lout_2.addWidget(qt.QLabel(u"Thtrd, \u2103 : "))
        lout_2.addWidget(self.thtrdBoxLabl2)
        lout_2.addWidget(qt.QLabel(" = "))
        lout_2.addWidget(self.thtrdBoxInput1)
        lout_2.addWidget(qt.QLabel(" + "))
        lout_2.addWidget(self.thtrdBoxInput2)
        lout_2.addWidget(qt.QLabel(u" \u2219 R + "))
        lout_2.addWidget(self.thtrdBoxInput3)
        lout_2.addWidget(qt.QLabel(u" \u2219 "))
        lout_2.addWidget(qt.QLabel("R<sup>2</sup>"))
        lout_2.addStretch()        
        
        self.theaterBox = qt.QGroupBox("Heater temperature vs heater voltage")
        mainLayout.addWidget(self.theaterBox)
        lout_0 = qt.QVBoxLayout()
        self.theaterBox.setLayout(lout_0)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        lout_2 = qt.QHBoxLayout()
        lout_0.addLayout(lout_2) 
        self.theaterBoxInput1 = qt.QLineEdit()
        self.theaterBoxInput1.setMaximumWidth(short_line_input_width)
        self.theaterBoxInput1.setFrame(False)
        self.theaterBoxInput2 = qt.QLineEdit()
        self.theaterBoxInput2.setMaximumWidth(short_line_input_width)
        self.theaterBoxInput2.setFrame(False)
        self.theaterBoxInput3 = qt.QLineEdit()
        self.theaterBoxInput3.setMaximumWidth(short_line_input_width)
        self.theaterBoxInput3.setFrame(False)
        self.theaterBoxInput4 = qt.QLineEdit()
        self.theaterBoxInput4.setMaximumWidth(short_line_input_width)
        self.theaterBoxInput4.setFrame(False)
        lout_1.setSpacing(0)
        lout_1.addWidget(qt.QLabel(u"Safe voltage, V = "))
        lout_1.addWidget(self.theaterBoxInput1)
        lout_1.addStretch()
        lout_2.setSpacing(0)
        lout_2.addWidget(qt.QLabel(u"Theater, \u2103 = "))
        lout_2.addWidget(self.theaterBoxInput2)
        lout_2.addWidget(qt.QLabel(u" \u2219 U + "))
        lout_2.addWidget(self.theaterBoxInput3)
        lout_2.addWidget(qt.QLabel(u" \u2219 "))
        lout_2.addWidget(qt.QLabel("U<sup>2</sup> + "))
        lout_2.addWidget(self.theaterBoxInput4)
        lout_2.addWidget(qt.QLabel(u" \u2219 "))
        lout_2.addWidget(qt.QLabel("U<sup>3</sup>"))
        lout_2.addStretch()  

        self.rhtrBox = qt.QGroupBox("Heaters resistance")
        mainLayout.addWidget(self.rhtrBox)
        lout_0 = qt.QHBoxLayout()
        self.rhtrBox.setLayout(lout_0)
        lout_0.setSpacing(0)
        lout_0.addWidget(qt.QLabel(u"R<sub>inner</sub>, \u03A9 = "))
        self.rhtrBoxInput1 = qt.QLineEdit()
        self.rhtrBoxInput1.setMaximumWidth(short_line_input_width)
        self.rhtrBoxInput1.setFrame(False)
        lout_0.addWidget(self.rhtrBoxInput1)
        lout_0.addSpacing(20)
        lout_0.addWidget(qt.QLabel(u"R<sub>guard</sub>, \u03A9 = "))
        self.rhtrBoxInput2 = qt.QLineEdit()
        self.rhtrBoxInput2.setMaximumWidth(short_line_input_width)
        self.rhtrBoxInput2.setFrame(False)
        lout_0.addWidget(self.rhtrBoxInput2)
        lout_0.addStretch()

        self.amplcorBox = qt.QGroupBox("Amplitude correction")
        mainLayout.addWidget(self.amplcorBox)
        lout_0 = qt.QHBoxLayout()
        self.amplcorBox.setLayout(lout_0)
        self.amplcorBoxInput1 = qt.QLineEdit()
        self.amplcorBoxInput1.setMaximumWidth(short_line_input_width)
        self.amplcorBoxInput1.setFrame(False)
        self.amplcorBoxInput2 = qt.QLineEdit()
        self.amplcorBoxInput2.setMaximumWidth(short_line_input_width)
        self.amplcorBoxInput2.setFrame(False)
        self.amplcorBoxInput3 = qt.QLineEdit()
        self.amplcorBoxInput3.setMaximumWidth(short_line_input_width)
        self.amplcorBoxInput3.setFrame(False)
        self.amplcorBoxInput4 = qt.QLineEdit()
        self.amplcorBoxInput4.setMaximumWidth(short_line_input_width)
        self.amplcorBoxInput4.setFrame(False)
        lout_0.addWidget(qt.QLabel(u"Ac = "))
        lout_0.addWidget(self.amplcorBoxInput1)
        lout_0.addWidget(qt.QLabel(" + "))
        lout_0.addWidget(self.amplcorBoxInput2)
        lout_0.addWidget(qt.QLabel(u" \u2219 T + "))
        lout_0.addWidget(self.amplcorBoxInput3)
        lout_0.addWidget(qt.QLabel(u" \u2219 "))
        lout_0.addWidget(qt.QLabel("T<sup>2</sup> + "))
        lout_0.addWidget(self.amplcorBoxInput4)
        lout_0.addWidget(qt.QLabel(u" \u2219 "))
        lout_0.addWidget(qt.QLabel("T<sup>3</sup>"))
        lout_0.addStretch()  
        
        mainLayout.addStretch()
        mainLayout.addStretch()
        hline = qt.QFrame()
        hline.setFrameShape(qt.QFrame.HLine)
        hline.setStyleSheet("color: rgb(220, 220, 220);")
        mainLayout.addWidget(hline)

        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        lout_1.setSpacing(1)
        self.loadCalibButton = qt.QPushButton("Load && Apply")
        lout_1.addWidget(self.loadCalibButton)
        self.saveCalibButton = qt.QPushButton("Save && Apply")
        lout_1.addWidget(self.saveCalibButton)
        self.resetCalibButton = qt.QPushButton("Reset")
        self.resetCalibButton.setFocusPolicy(qt.Qt.NoFocus)
        lout_1.addWidget(self.resetCalibButton)


        float_validator = qt.QRegExpValidator(qt.QRegExp("^[-]{0,1}[0-9]{1,5}\.[0-9]{1,10}$|^[-]{0,1}[0-9]{1,5}\.[0-9]{1,10}e[-]{0,1}[+]{0,1}[0-9]{0,2}$"))
        self.update_calib_input_fields()
        for item in self.findChildren(qt.QPushButton):
            item.setFocusPolicy(qt.Qt.NoFocus)
        for item in self.findChildren(qt.QLineEdit):
            item.setAlignment(qt.Qt.AlignCenter)
            item.setCursorPosition(0)
            if item != self.calibInfoInput:
                item.setValidator(float_validator)
                
        # ####### end of UI setup
        # ########################################
        
        self.loadCalibButton.clicked.connect(self.load_calib_from_file)
        self.resetCalibButton.clicked.connect(self.reset_calib)
        self.saveCalibButton.clicked.connect(self.save_calib_to_file)

    def load_calib_from_file(self):
        self.parent().select_calibration_file()
        self.parent().apply_calib()
        self.update_calib_input_fields()

    def save_calib_to_file(self, fpath=False):
        fpath = qt.QFileDialog.getSaveFileName(self, "Select file and path to save calibration:", None, "*.json")[0]
        if fpath:
            self.read_calib_input_fields()
            print(self.parent().calibration.comment)
            self.parent().calibPathInput.setText(os.path.abspath(fpath))
            self.parent().settings.calib_path = fpath
            self.parent().calibPathInput.setCursorPosition(0)
            # self.parent().apply_calib()
            # URL = self.parent().settings.http_host+"settings/calibration.json"
            # response = requests.get(URL, verify=False)
            # with open(fpath, 'wb') as f:
            #     f.write(response.content)

    def reset_calib(self):
        self.parent().apply_default_calib()

    def update_calib_input_fields(self):     
        self.calibInfoInput.setText(str(self.parent().calibration.comment))
        self.ttplBoxInput1.setText(str(round(self.parent().calibration.utpl0, 10)))
        self.ttplBoxInput2.setText(str(round(self.parent().calibration.ttpl0, 10)))
        self.ttplBoxInput3.setText(str(round(self.parent().calibration.ttpl1, 10)))

        self.uhtrBoxInput1.setText(str(round(self.parent().calibration.uhtr0, 10)))
        self.uhtrBoxInput2.setText(str(round(self.parent().calibration.uhtr1, 10)))

        self.ihtrBoxInput1.setText(str(round(self.parent().calibration.ihtr0, 10)))
        self.ihtrBoxInput2.setText(str(round(self.parent().calibration.ihtr1, 10)))

        self.thtrBoxInput1.setText(str(round(self.parent().calibration.thtr0, 10)))
        self.thtrBoxInput2.setText(str(round(self.parent().calibration.thtr1, 10)))
        self.thtrBoxInput3.setText(str(round(self.parent().calibration.thtr2, 10)))

        self.thtrdBoxInput1.setText(str(round(self.parent().calibration.thtrd0, 10)))
        self.thtrdBoxInput2.setText(str(round(self.parent().calibration.thtrd1, 10)))
        self.thtrdBoxInput3.setText(str(round(self.parent().calibration.thtrd2, 10)))

        self.theaterBoxInput1.setText(str(round(self.parent().calibration.safe_voltage, 10)))
        self.theaterBoxInput2.setText(str(round(self.parent().calibration.theater0, 10)))
        self.theaterBoxInput3.setText(str(round(self.parent().calibration.theater1, 10)))
        self.theaterBoxInput4.setText(str(round(self.parent().calibration.theater2, 10)))

        self.rhtrBoxInput1.setText(str(round(self.parent().calibration.rhtr, 10)))
        self.rhtrBoxInput2.setText(str(round(self.parent().calibration.rghtr, 10)))

        self.amplcorBoxInput1.setText(str(round(self.parent().calibration.ac0, 10)))
        self.amplcorBoxInput2.setText(str(round(self.parent().calibration.ac1, 10)))
        self.amplcorBoxInput3.setText(str(round(self.parent().calibration.ac2, 10)))
        self.amplcorBoxInput4.setText(str(round(self.parent().calibration.ac2, 10)))


    def read_calib_input_fields(self):  
        self.parent().calibration.comment = self.calibInfoInput.text()

if __name__ == "__main__":
    import sys
    app = qt.QApplication(sys.argv)
    example = calibWindow()
    example.show()
    sys.exit(app.exec())