import cv2
import numpy as np
from PyQt4 import QtCore
from numpy2qt import numpy2qt


class CannyEdges(QtCore.QObject):
    FORMAT_NUMPY = 0
    FORMAT_QIMAGE = 1
    FORMAT_QPIXMAP = 2

    input_image_changed = QtCore.pyqtSignal()
    smoothed_image_changed = QtCore.pyqtSignal()
    edge_image_changed = QtCore.pyqtSignal()

    def __init__(self, image=None, smoothed=True, gaussian_sigma=1.0, gaussian_kernel_size=11, canny_threshold1=100, canny_threshold2=200):
        QtCore.QObject.__init__(self)
        self._input_image = None
        self._smoothed_image = None
        self._edge_image = None
        self._dummy_image = (np.zeros((400, 400), dtype=np.uint8)
                             if image is None
                             else np.zeros((min(400, image.shape[0]), min(400, image.shape[1])), np.uint8))
        self._smoothed = smoothed
        self._gaussian_sigma = gaussian_sigma
        self._gaussian_kernel_size = (gaussian_kernel_size, gaussian_kernel_size)
        self._canny_threshold1 = canny_threshold1
        self._canny_threshold2 = canny_threshold2

        if image is None:
            image = self._dummy_image
        self.update_input_image(image)

    @classmethod
    def _format_image(cls, image, format_type=0, scale=True):
        if scale:
            if image.shape[1] > 400.0:
                fx = 400.0/float(image.shape[1])
                image = cv2.resize(image, (0, 0), None, fx, fx)
            if image.shape[0] > 400.0:
                fy = 400.0/float(image.shape[0])
                image = cv2.resize(image, (0, 0), None, fy, fy)

        if format_type == cls.FORMAT_NUMPY:
            return image
        elif format_type == cls.FORMAT_QIMAGE:
            return numpy2qt(image, as_pixmap=False)
        elif format_type == cls.FORMAT_QPIXMAP:
            return numpy2qt(image, as_pixmap=True)
        else:
            raise ValueError('format "{}" is not supported'.format(format_type))

    def update_input_image(self, image):
        self._input_image = image
        self._dummy_image = np.zeros((min(400, image.shape[0]), min(400, image.shape[1])), dtype=np.uint8)
        self.input_image_changed.emit()
        self._update_smoothed_image()
        self._update_edge_image()

    def _update_smoothed_image(self):
        if self.smoothed:
            self._smoothed_image = cv2.GaussianBlur(self._input_image, self.gaussian_kernel_size, self.gaussian_sigma)
        else:
            self._smoothed_image = self._dummy_image
        self.smoothed_image_changed.emit()
        self._update_edge_image()

    def _update_edge_image(self):
        if self.smoothed:
            self._edge_image = cv2.Canny(self._smoothed_image, self.canny_threshold1, self.canny_threshold2)
        else:
            self._edge_image = cv2.Canny(self._input_image, self.canny_threshold1, self.canny_threshold2)
        self.edge_image_changed.emit()

    def input_image(self, format_type=0):
        return self._format_image(self._input_image, format_type)

    def smoothed_image(self, format_type=0):
        return self._format_image(self._smoothed_image, format_type)

    def edge_image(self, format_type=0):
        return self._format_image(self._edge_image, format_type)

    @property
    def smoothed(self):
        return self._smoothed

    @smoothed.setter
    def smoothed(self, value):
        self._smoothed = value
        self._update_smoothed_image()

    @property
    def gaussian_sigma(self):
        return self._gaussian_sigma

    @gaussian_sigma.setter
    def gaussian_sigma(self, value):
        self._gaussian_sigma = value
        self._update_smoothed_image()

    @property
    def gaussian_kernel_size(self):
        return self._gaussian_kernel_size

    @gaussian_kernel_size.setter
    def gaussian_kernel_size(self, value):
        self._gaussian_kernel_size = (value, value)
        self._update_smoothed_image()

    @property
    def canny_threshold1(self):
        return self._canny_threshold1

    @canny_threshold1.setter
    def canny_threshold1(self, value):
        self._canny_threshold1 = value
        self._update_edge_image()

    @property
    def canny_threshold2(self):
        return self._canny_threshold2

    @canny_threshold2.setter
    def canny_threshold2(self, value):
        self._canny_threshold2 = value
        self._update_edge_image()

    @property
    def canny_thresholds(self):
        t1 = self.canny_threshold1
        t2 = self.canny_threshold2
        return min(t1, t2), max(t1, t2)
