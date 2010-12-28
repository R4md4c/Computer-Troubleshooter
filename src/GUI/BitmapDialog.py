'''
Created on Dec 28, 2010

@author: ramdac
'''
import wx

class BitmapDialog ( wx.Dialog ):
    
    def __init__( self, labelText, bitmapPath ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, labelText, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( 200 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        
        bSizer2.AddSpacer( ( 70, 0), 1, wx.EXPAND, 5 )
        
        self.m_bitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_JPEG), wx.DefaultPosition, wx.DefaultSize, 0 )
        
        bSizer2.Add( self.m_bitmap, 0, wx.ALL, 5 )
        
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetDefault() 
        bSizer1.Add( self.m_button2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        bSizer1.Fit( self )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnButtonClick( self, event ):
        self.Destroy()
