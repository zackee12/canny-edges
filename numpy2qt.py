import numpy as np
import cv2
from PyQt4 import QtGui


def numpy2qt(matrix, as_pixmap=False):
    # convert matrix to RGB order
    if len(matrix.shape) == 2:
        matrix = cv2.cvtColor(matrix, cv2.COLOR_GRAY2RGB)
    elif len(matrix.shape) == 3:
        matrix = cv2.cvtColor(matrix, cv2.COLOR_BGR2RGB)
    else:
        raise ValueError('{} can only convert 2d/3d arrays to qt images'.format(numpy2qt.__name__))

    height, width, _ = matrix.shape
    line_width = matrix.strides[0]
    image = QtGui.QImage(matrix.data, width, height, line_width, QtGui.QImage.Format_RGB888)

    # convenience pixmap option
    if as_pixmap:
        image = QtGui.QPixmap.fromImage(image)

    # keep reference to matrix from being gc (image doesn't make copy)
    image.ndarray = matrix
    return image


def imread(file_path, grayscale=False, as_pixmap=False):
    code = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
    img = cv2.imread(file_path, code)
    if img is None:
        raise IOError('file could not be read from {}'.format(file_path))

    return numpy2qt(img, as_pixmap)
