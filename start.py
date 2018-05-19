import wx
from MainFrame import MainFrame

App = wx.App()

#Main Frame.
MainFrame = MainFrame(None)

# Show it.
MainFrame.Show()

# Start the event loop.
App.MainLoop()
