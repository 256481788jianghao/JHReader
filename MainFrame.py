
from BaseMainFrame import BaseMainFrame

class MainFrame(BaseMainFrame):

    def __init__(self,parent):
        BaseMainFrame.__init__(self,parent)

    def onMenuItemFileFileNewSelected( self, event ):
        print('mainFrame')
        
    def __del__(self):
        pass
    pass
