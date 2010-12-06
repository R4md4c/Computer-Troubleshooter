'''
Created on Nov 17, 2010

@author: ramdac
'''



import wx

class GenericPanel(wx.Panel):
    """ A panel contains a question and a combo box to choose from"""
    def __init__(self, parent, _id, init_values):
        wx.Panel.__init__(self, parent, _id)
        
        
        self.MainSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.staticText = wx.StaticText(self, -1, 'What do you think the problem is from user?', style = wx.ST_NO_AUTORESIZE)
        self.comboBox = wx.ComboBox(self, _id, style = wx.CB_READONLY, choices = init_values)
        
        self.MainSizer.Add(self.staticText)
        self.MainSizer.Add(self.comboBox)
        
        self.MainSizer.SetSizeHints(self)
        
        self.SetSizer(self.MainSizer)
        
    def SetText(self, text):
        self.staticText.SetLabel(text)
    
    
