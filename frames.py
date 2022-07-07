# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"阿里云OSS图床", pos = wx.DefaultPosition, size = wx.Size( 400,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_upload = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_upload_file = wx.Button( self.m_panel_upload, wx.ID_ANY, u"从文件上传", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_upload_file.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

		bSizer4.Add( self.m_button_upload_file, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button_upload_paste = wx.Button( self.m_panel_upload, wx.ID_ANY, u"从粘贴板上传", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_upload_paste.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )
		self.m_button_upload_paste.SetToolTip( u"仅支持图片" )

		bSizer4.Add( self.m_button_upload_paste, 1, wx.ALL, 5 )


		bSizer31.Add( bSizer4, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel_upload, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		m_radioBox_copyTypeChoices = [ u"文件链接", u"MarkDown" ]
		self.m_radioBox_copyType = wx.RadioBox( self.m_panel_upload, wx.ID_ANY, u"复制形式", wx.DefaultPosition, wx.DefaultSize, m_radioBox_copyTypeChoices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox_copyType.SetSelection( 1 )
		bSizer31.Add( self.m_radioBox_copyType, 0, wx.EXPAND, 5 )

		self.m_grid_history = wx.grid.Grid( self.m_panel_upload, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid_history.CreateGrid( 2, 4 )
		self.m_grid_history.EnableEditing( False )
		self.m_grid_history.EnableGridLines( True )
		self.m_grid_history.EnableDragGridSize( False )
		self.m_grid_history.SetMargins( 0, 0 )

		# Columns
		self.m_grid_history.EnableDragColMove( False )
		self.m_grid_history.EnableDragColSize( True )
		self.m_grid_history.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_history.EnableDragRowSize( True )
		self.m_grid_history.SetRowLabelSize( 25 )
		self.m_grid_history.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid_history.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer31.Add( self.m_grid_history, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_upload.SetSizer( bSizer31 )
		self.m_panel_upload.Layout()
		bSizer31.Fit( self.m_panel_upload )
		self.m_notebook1.AddPage( self.m_panel_upload, u"上传", True )
		self.m_panel_config = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText_region = wx.StaticText( self.m_panel_config, wx.ID_ANY, u"区域", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_region.Wrap( -1 )

		fgSizer1.Add( self.m_staticText_region, 0, wx.ALL, 5 )

		m_comboBox_regionChoices = []
		self.m_comboBox_region = wx.ComboBox( self.m_panel_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), m_comboBox_regionChoices, 0 )
		fgSizer1.Add( self.m_comboBox_region, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText_accessKeyId = wx.StaticText( self.m_panel_config, wx.ID_ANY, u"accessKeyId", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_accessKeyId.Wrap( -1 )

		fgSizer1.Add( self.m_staticText_accessKeyId, 0, wx.ALL, 5 )

		self.m_textCtrl_accessKeyId = wx.TextCtrl( self.m_panel_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl_accessKeyId, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText_accessKeySecret = wx.StaticText( self.m_panel_config, wx.ID_ANY, u"accessKeySecret", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_accessKeySecret.Wrap( -1 )

		fgSizer1.Add( self.m_staticText_accessKeySecret, 0, wx.ALL, 5 )

		self.m_textCtrl_accessKeySecret = wx.TextCtrl( self.m_panel_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl_accessKeySecret, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel_config, wx.ID_ANY, u"bucket", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl_bucket = wx.TextCtrl( self.m_panel_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl_bucket, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel_config, wx.ID_ANY, u"使用固定路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_checkBox_fixpath = wx.CheckBox( self.m_panel_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox_fixpath, 0, wx.ALL, 5 )

		self.m_staticText_path = wx.StaticText( self.m_panel_config, wx.ID_ANY, u"路径位置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_path.Wrap( -1 )

		self.m_staticText_path.Hide()

		fgSizer1.Add( self.m_staticText_path, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_path = wx.TextCtrl( self.m_panel_config, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl_path.Hide()

		fgSizer1.Add( self.m_textCtrl_path, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( fgSizer1, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel_config, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_save = wx.Button( self.m_panel_config, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button_save, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel_config.SetSizer( bSizer3 )
		self.m_panel_config.Layout()
		bSizer3.Fit( self.m_panel_config )
		self.m_notebook1.AddPage( self.m_panel_config, u"配置", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.evt_OnClose )
		self.m_button_upload_file.Bind( wx.EVT_BUTTON, self.evt_m_button_upload_file_OnButtonClick )
		self.m_button_upload_paste.Bind( wx.EVT_BUTTON, self.evt_m_button_upload_paste_OnButtonClick )
		self.m_radioBox_copyType.Bind( wx.EVT_RADIOBOX, self.evt_m_radioBox_copyType_OnRadioBox )
		self.m_grid_history.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.evt_m_grid_history_OnGridCellLeftClick )
		self.m_checkBox_fixpath.Bind( wx.EVT_CHECKBOX, self.evt_m_checkBox_fixpath_OnCheckBox )
		self.m_button_save.Bind( wx.EVT_BUTTON, self.evt_m_button_save_OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def evt_OnClose( self, event ):
		event.Skip()

	def evt_m_button_upload_file_OnButtonClick( self, event ):
		event.Skip()

	def evt_m_button_upload_paste_OnButtonClick( self, event ):
		event.Skip()

	def evt_m_radioBox_copyType_OnRadioBox( self, event ):
		event.Skip()

	def evt_m_grid_history_OnGridCellLeftClick( self, event ):
		event.Skip()

	def evt_m_checkBox_fixpath_OnCheckBox( self, event ):
		event.Skip()

	def evt_m_button_save_OnButtonClick( self, event ):
		event.Skip()


