from PyQt5.Qt import QApplication

from  Graph.Help.Util import *
from GraphView.GraphicsItem.Parts.KeyItem import FFKeyItem

from GraphView.Help.ResUtil import FFResUtil

class FFPinItem(FFKeyItem):
    def __init__(self, pinRef):
        super(FFKeyItem, self).__init__(None)
        self.setPixmap(FFResUtil.PinPixmap())
        self._PinRef = pinRef

    def IsKeyIn(self):
        return self._PinRef._PinFlag == FFFlag.FLAG_PIN_IN

    def IsCompatibilityPinItem(self, pinItem):
        return self._PinRef.IsCompatibility(pinItem._PinRef)

    def OnHoverItems(self, items):
        QApplication.restoreOverrideCursor()
        for item in items:
            if isinstance(item, FFPinItem):
                if self.IsCompatibilityPinItem(item):
                    QApplication.setOverrideCursor(FFResUtil.OkCursor())
                else:
                    QApplication.setOverrideCursor(FFResUtil.ErrorCursor())
                break

    def OnReleaseItems(self, items):
        QApplication.restoreOverrideCursor()
        for item in items:
            if isinstance(item, FFPinItem) and self.IsCompatibilityPinItem(item):
                self.parentItem().AddPinLink(self, item)
                break