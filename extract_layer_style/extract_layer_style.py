from krita import *
from PyQt5.QtWidgets import QWidget, QAction, QMessageBox

class ExtractLayerStyle(Extension):

    def __init__(self, parent):
        super().__init__(parent)

        self.krita = None

    # Krita.instance() exists, so do any setup work
    def setup(self):
        self.krita = Krita.instance()

    def extract_action(self):
        doc = self.krita.activeDocument()
        if doc == None:
            self.display_error_message("There is no document open.")
            return
        
        cLayer = doc.activeNode()
        if cLayer == None:
            self.display_error_message("There is no active layer.")
            return
        
        self.extract_layer_style(doc, cLayer)

    def display_error_message(self, msg):
        messageBox = QMessageBox()
        messageBox.setWindowTitle('Error')
        messageBox.setText(msg)
        messageBox.setStandardButtons(QMessageBox.Close)
        messageBox.setIcon(QMessageBox.Information)
        messageBox.exec()

    def extract_layer_style(self, doc, cLayer):
        parent = cLayer.parentNode()

        dupl = cLayer.duplicate()
        dupl.setName(dupl.name()+" copy")
        group = doc.createGroupLayer(cLayer.name()+" style")

        parent.addChildNode(group, cLayer)
        group.addChildNode(dupl, None)

        dupl.setBlendingMode("erase")

        g2 = doc.createVectorLayer("dummy")
        parent.addChildNode(g2, group)

        g2.mergeDown()

    # called after setup(self)
    def createActions(self, window):
        action = window.createAction('extract_layer_style', 'Extract Layer Style')
        action.triggered.connect(self.extract_action)