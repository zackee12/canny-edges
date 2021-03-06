# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zack2\PycharmProjects\canny-edges\ui\mainform.ui'
#
# Created: Fri Sep 11 20:47:29 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(600, 338)
        self.verticalLayout = QtGui.QVBoxLayout(MainForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lbl_kernel_size = QtGui.QLabel(MainForm)
        self.lbl_kernel_size.setObjectName(_fromUtf8("lbl_kernel_size"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl_kernel_size)
        self.lbl_sigma = QtGui.QLabel(MainForm)
        self.lbl_sigma.setObjectName(_fromUtf8("lbl_sigma"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl_sigma)
        self.lbl_gaussian_title = QtGui.QLabel(MainForm)
        self.lbl_gaussian_title.setObjectName(_fromUtf8("lbl_gaussian_title"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lbl_gaussian_title)
        self.spin_kernel_size = QtGui.QSpinBox(MainForm)
        self.spin_kernel_size.setMinimum(3)
        self.spin_kernel_size.setMaximum(999)
        self.spin_kernel_size.setSingleStep(2)
        self.spin_kernel_size.setProperty("value", 11)
        self.spin_kernel_size.setObjectName(_fromUtf8("spin_kernel_size"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spin_kernel_size)
        self.spin_sigma = QtGui.QDoubleSpinBox(MainForm)
        self.spin_sigma.setMaximum(999.99)
        self.spin_sigma.setProperty("value", 1.0)
        self.spin_sigma.setObjectName(_fromUtf8("spin_sigma"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spin_sigma)
        self.cb_disable_gaussian = QtGui.QCheckBox(MainForm)
        self.cb_disable_gaussian.setObjectName(_fromUtf8("cb_disable_gaussian"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.cb_disable_gaussian)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        self.lbl_original_image = QtGui.QLabel(MainForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_original_image.sizePolicy().hasHeightForWidth())
        self.lbl_original_image.setSizePolicy(sizePolicy)
        self.lbl_original_image.setScaledContents(False)
        self.lbl_original_image.setObjectName(_fromUtf8("lbl_original_image"))
        self.gridLayout.addWidget(self.lbl_original_image, 0, 0, 1, 1)
        self.lbl_edge_image = QtGui.QLabel(MainForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edge_image.sizePolicy().hasHeightForWidth())
        self.lbl_edge_image.setSizePolicy(sizePolicy)
        self.lbl_edge_image.setScaledContents(False)
        self.lbl_edge_image.setObjectName(_fromUtf8("lbl_edge_image"))
        self.gridLayout.addWidget(self.lbl_edge_image, 0, 2, 1, 1)
        self.lbl_smooth_image = QtGui.QLabel(MainForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_smooth_image.sizePolicy().hasHeightForWidth())
        self.lbl_smooth_image.setSizePolicy(sizePolicy)
        self.lbl_smooth_image.setScaledContents(False)
        self.lbl_smooth_image.setObjectName(_fromUtf8("lbl_smooth_image"))
        self.gridLayout.addWidget(self.lbl_smooth_image, 0, 1, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.btn_browse = QtGui.QPushButton(MainForm)
        self.btn_browse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_browse.setObjectName(_fromUtf8("btn_browse"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.btn_browse)
        self.line_path = QtGui.QLineEdit(MainForm)
        self.line_path.setReadOnly(True)
        self.line_path.setObjectName(_fromUtf8("line_path"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_path)
        self.lbl_input_title = QtGui.QLabel(MainForm)
        self.lbl_input_title.setObjectName(_fromUtf8("lbl_input_title"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lbl_input_title)
        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.lbl_canny_title = QtGui.QLabel(MainForm)
        self.lbl_canny_title.setObjectName(_fromUtf8("lbl_canny_title"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lbl_canny_title)
        self.lbl_threshold1 = QtGui.QLabel(MainForm)
        self.lbl_threshold1.setObjectName(_fromUtf8("lbl_threshold1"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl_threshold1)
        self.slider_threshold1 = QtGui.QSlider(MainForm)
        self.slider_threshold1.setMaximum(500)
        self.slider_threshold1.setProperty("value", 100)
        self.slider_threshold1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_threshold1.setObjectName(_fromUtf8("slider_threshold1"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.slider_threshold1)
        self.lbl_threshold2 = QtGui.QLabel(MainForm)
        self.lbl_threshold2.setObjectName(_fromUtf8("lbl_threshold2"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl_threshold2)
        self.slider_threshold2 = QtGui.QSlider(MainForm)
        self.slider_threshold2.setMaximum(500)
        self.slider_threshold2.setProperty("value", 200)
        self.slider_threshold2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_threshold2.setObjectName(_fromUtf8("slider_threshold2"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.slider_threshold2)
        self.lbl_thresholds = QtGui.QLabel(MainForm)
        self.lbl_thresholds.setObjectName(_fromUtf8("lbl_thresholds"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.SpanningRole, self.lbl_thresholds)
        self.gridLayout.addLayout(self.formLayout_3, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(_translate("MainForm", "Form", None))
        self.lbl_kernel_size.setText(_translate("MainForm", "Kernel Size", None))
        self.lbl_sigma.setText(_translate("MainForm", "Sigma", None))
        self.lbl_gaussian_title.setText(_translate("MainForm", "Gaussian Blur", None))
        self.cb_disable_gaussian.setText(_translate("MainForm", "Disable", None))
        self.lbl_original_image.setText(_translate("MainForm", "TextLabel", None))
        self.lbl_edge_image.setText(_translate("MainForm", "TextLabel", None))
        self.lbl_smooth_image.setText(_translate("MainForm", "TextLabel", None))
        self.btn_browse.setText(_translate("MainForm", "Browse", None))
        self.lbl_input_title.setText(_translate("MainForm", "Input", None))
        self.lbl_canny_title.setText(_translate("MainForm", "Canny Edges", None))
        self.lbl_threshold1.setText(_translate("MainForm", "Threshold 1", None))
        self.lbl_threshold2.setText(_translate("MainForm", "Threshold 2", None))
        self.lbl_thresholds.setText(_translate("MainForm", "TextLabel", None))

