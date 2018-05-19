# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class BaseMainFrame
###########################################################################

class BaseMainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 579,382 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar_top = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menu_file_project = wx.Menu()
		self.m_menuItem_file_project_new = wx.MenuItem( self.m_menu_file_project, wx.ID_ANY, u"new", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file_project.Append( self.m_menuItem_file_project_new )
		
		self.m_menu_file_project.AppendSeparator()
		
		self.m_menuItem_file_project_open = wx.MenuItem( self.m_menu_file_project, wx.ID_ANY, u"open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file_project.Append( self.m_menuItem_file_project_open )
		
		self.m_menu_file.AppendSubMenu( self.m_menu_file_project, u"project" )
		
		self.m_menu_file.AppendSeparator()
		
		self.m_menuItem_about = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"about", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_about )
		
		self.m_menubar_top.Append( self.m_menu_file, u"File" ) 
		
		self.SetMenuBar( self.m_menubar_top )
		
		self.m_toolBar_top = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolBar_top.Realize() 
		
		self.m_statusBar_bottom = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer_b0 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer_b1_1 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer_b0.Add( bSizer_b1_1, 1, wx.EXPAND, 5 )
		
		bSizer_b1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_richText_editor = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer_b1_2.Add( self.m_richText_editor, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer_b0.Add( bSizer_b1_2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_b0 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

