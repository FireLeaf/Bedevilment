from PyQt5.QtWidgets import QMainWindow, QDockWidget, QTreeView, QTableWidget
from PyQt5.Qt import *

from GraphView.TabGraph import FFTabWidget, FFTabBar
from GraphView.StateGraphView import FFStateGraphView
from Graph.Node.SwitchNode import FFSwitchNode
from Graph.Node.ArithmeticNode import FFArithmeticNode
from Graph.Node.LogicNode import FFLogicNode
from Graph.Node.RelationNode import FFRelationNode
from Graph.Node.CallNode import FFCallNode
from Graph.Node.ForNode import FFForNode
from Graph.Node.WhileNode import FFWhileNode
from Graph.Help.Util import *

class FFMainWindow(QMainWindow):
    def __init__(self):
        super(FFMainWindow, self).__init__()

    def createMenus(self):
        self.menuBar().addMenu(self.tr("&File"))

    def createToolbar(self):
        self.addToolBar(self.tr("&File"))

    def setUp(self):
        self.resize(1024, 768)
        self.createMenus()
        self.createToolbar()

        tabWidget = FFTabWidget(self)
        self.setCentralWidget(tabWidget)

        graphView = FFStateGraphView()
        tabWidget.addGraphViewTab("Test", graphView)
        graphScene = graphView._GraphScene
        node = FFSwitchNode()
        node.SetPos(5000, 5000, 0)
        nodeItem = graphScene.AddNode(node)
        graphView.centerOn(nodeItem)
        node = FFSwitchNode()
        node.SetPos(5080, 5080, 0)
        nodeItem = graphScene.AddNode(node)

        node = FFArithmeticNode(FFNodeSubType.NST_ARITHMETIC_ADD, FFType.TYPE_INT)
        node.SetPos(4850, 4850, 0)
        nodeItem = graphScene.AddNode(node)
        node = FFLogicNode(FFNodeSubType.NST_LOGIC_OR)
        node.SetPos(5050, 4850, 0)
        nodeItem = graphScene.AddNode(node)
        node = FFRelationNode(FFNodeSubType.NST_RELATION_LE, FFType.TYPE_STRING)
        node.SetPos(4850, 5050, 0)
        nodeItem = graphScene.AddNode(node)
        node = FFForNode()
        node.SetPos(5150, 5050, 0)
        nodeItem = graphScene.AddNode(node)
        node = FFWhileNode()
        node.SetPos(4450, 5050, 0)
        nodeItem = graphScene.AddNode(node)

        dockProject = QDockWidget(self.tr("工程"), self)
        treeView = QTreeView(self)
        dockProject.setWidget(treeView)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockProject)
        dockProject.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
        dockProject.setFeatures(QDockWidget.DockWidgetMovable)

        dockInspector = QDockWidget(self.tr("属性"), self)
        tableWidget = QTableWidget(0, 2)
        dockInspector.setWidget(tableWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, dockInspector)
        dockInspector.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
        dockInspector.setFeatures(QDockWidget.DockWidgetMovable)