from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QGraphicsProxyWidget, QLabel

from  Graph.Help.Util import *
from GraphView.GraphicsItem.Parts.KeyItem import FFKeyItem

from GraphView.Help.ResUtil import FFResUtil

class FFFlowItem(FFKeyItem):
    def __init__(self, flowRef):
        super(FFKeyItem, self).__init__(None)
        self.setPixmap(FFResUtil.FlowPixmap())
        self._FlowRef = flowRef

    def IsKeyIn(self):
        return self._FlowRef._FlowFlag == FFFlag.FLAG_FLOW_IN

    def IsCompatibilityFlowItem(self, flowItem):
        return self._FlowRef.IsCompatibility(flowItem._FlowRef)

    def OnHoverItems(self, items):
        QApplication.restoreOverrideCursor()
        for item in items:
            if isinstance(item, FFFlowItem):
                if self.IsCompatibilityFlowItem(item):
                    QApplication.setOverrideCursor(FFResUtil.OkCursor())
                else:
                    QApplication.setOverrideCursor(FFResUtil.ErrorCursor())
                break

    def GetNodeParent(self):
        from GraphView.GraphicsItem.Base.NodeItem import FFNodeGraphicsItem
        item = self
        while True:
            parent = item.parentItem()
            if not parent:
                return None
            if isinstance(parent, FFNodeGraphicsItem):
                return parent
            item = parent
        return None

    def OnReleaseItems(self, items):
        QApplication.restoreOverrideCursor()
        for item in items:
            if isinstance(item, FFFlowItem) and self.IsCompatibilityFlowItem(item):
                nodeItem = self.GetNodeParent()
                if nodeItem:
                    nodeItem.addFlowLink(self, item)
                break