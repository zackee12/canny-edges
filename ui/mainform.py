from PyQt4 import QtGui, QtCore
from ui_mainform import Ui_MainForm
from edges import CannyEdges
import cv2


class MainForm(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.ui.btn_browse.clicked.connect(self.handle_btn_browse)
        self.ui.cb_disable_gaussian.stateChanged.connect(self.handle_cb_disable_smooth)
        self.ui.spin_sigma.valueChanged.connect(self.handle_spinner_sigma)
        self.ui.spin_kernel_size.valueChanged.connect(self.handle_spinner_kernel)
        self.ui.slider_threshold1.valueChanged.connect(self.handle_slider_t1)
        self.ui.slider_threshold2.valueChanged.connect(self.handle_slider_t2)

        self.edges = CannyEdges()
        self.edges.input_image_changed.connect(self.update_input_image)
        self.edges.smoothed_image_changed.connect(self.update_smooth_image)
        self.edges.edge_image_changed.connect(self.update_edge_image)
        self.ui.lbl_thresholds.setText('({thres[0]}, {thres[1]})'.format(thres=self.edges.canny_thresholds))

        self.update_input_image()
        self.update_smooth_image()
        self.update_edge_image()

    def update_input_image(self):
        self.ui.lbl_original_image.setPixmap(self.edges.input_image(CannyEdges.FORMAT_QPIXMAP))

    def update_smooth_image(self):
        self.ui.lbl_smooth_image.setPixmap(self.edges.smoothed_image(CannyEdges.FORMAT_QPIXMAP))

    def update_edge_image(self):
        self.ui.lbl_edge_image.setPixmap(self.edges.edge_image(CannyEdges.FORMAT_QPIXMAP))

    def handle_btn_browse(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self,
                                                      'Open File', '',
                                                      'Images (*.bmp *.jpeg *.jpg *.png *.tiff *.tif)')
        self.ui.line_path.setText(file_name)
        if len(file_name) == 0:
            return
        # try loading image
        img = cv2.imread(str(file_name), cv2.IMREAD_GRAYSCALE)
        if img is None:
            QtGui.QMessageBox.critical(self,
                                       'Error loading image',
                                       'failed to load image file at "{}"'.format(file_name))
            return
        self.edges.update_input_image(img)

    def handle_cb_disable_smooth(self):
        self.edges.smoothed = not self.ui.cb_disable_gaussian.isChecked()

    def handle_spinner_sigma(self, value):
        self.edges.gaussian_sigma = value

    def handle_spinner_kernel(self, value):
        self.edges.gaussian_kernel_size = value

    def handle_slider_t1(self, value):
        self.edges.canny_threshold1 = value
        self.ui.lbl_thresholds.setText('({thres[0]}, {thres[1]})'.format(thres=self.edges.canny_thresholds))

    def handle_slider_t2(self, value):
        self.edges.canny_threshold2 = value
        self.ui.lbl_thresholds.setText('({thres[0]}, {thres[1]})'.format(thres=self.edges.canny_thresholds))