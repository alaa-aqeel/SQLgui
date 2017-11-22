try:
	from PySide.QtGui import (
				QMainWindow,QMessageBox,QFont,QAction,QIcon,
				QDialog,QPushButton,QLabel,QGroupBox,QHBoxLayout,QCursor,
				QCheckBox,QLineEdit,QTextEdit,QWidget,QPainter,QColor,QVBoxLayout,
				QPlainTextEdit,QStringListModel,QTextCharFormat,QCompleter,QFontMetrics,
				QTabWidget,QFileDialog,QMenuBar,QDockWidget,QTableWidget,QTextFormat,QSyntaxHighlighter,
				)
	from PySide.QtCore import Qt,QSize,QRegExp,SIGNAL,QRect
except:
	from PyQt4.QtGui import (
				QMainWindow,QMessageBox,QFont,QAction,QIcon,
				QDialog,QPushButton,QLabel,QGroupBox,QHBoxLayout,QCursor,
				QCheckBox,QLineEdit,QTextEdit,QWidget,QPainter,QColor,QVBoxLayout,
				QPlainTextEdit,QStringListModel,QTextCharFormat,QCompleter,QFontMetrics,
				QTabWidget,QFileDialog,QMenuBar,QDockWidget,QTableWidget,QTextFormat,QSyntaxHighlighter,
				)
	from PyQt4.QtCore import Qt,QSize,QRegExp,SIGNAL,QRect

import sqlite3,os,sys,re
