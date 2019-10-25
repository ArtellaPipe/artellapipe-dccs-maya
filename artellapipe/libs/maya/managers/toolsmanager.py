import tpDccLib as tp

import artellapipe.register
from artellapipe.utils import tool


class MayaToolsManager(tool.ToolsManager, object):
    def __init__(self, parent=None):
        if parent is None:
            parent = tp.Dcc.get_main_window()
        super(MayaToolsManager, self).__init__(parent=parent)


artellapipe.register.register_class('ToolsManager', MayaToolsManager)
