'''
Created on Nov 17, 2010

@author: ramdac
'''

import wx
from GUI.Panels import StatePanel
from GUI.Panels import ProblemPanel
from GUI.Panels import Log
from engine import driver

class MainFrame(wx.Frame):
    def __init__(self, parent, _id, title, _size, iconName):
        wx.Frame.__init__(self, parent, _id, title, size = _size)
        self.SetIcon(wx.Icon(iconName, wx.BITMAP_TYPE_XPM ))
        self.Centre()
        
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.newItem = wx.MenuItem(self.fileMenu, wx.ID_NEW, '&New\tCtrl+N')
        self.logItem = wx.MenuItem(self.fileMenu, wx.ID_OPEN, '&Log\tCtrl+L')
        self.quitItem = wx.MenuItem(self.fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        self.fileMenu.AppendItem(self.newItem)
        self.fileMenu.AppendItem(self.logItem)
        self.fileMenu.AppendItem(self.quitItem)
        self.menuBar.Append(self.fileMenu, '&File')
        self.SetMenuBar(self.menuBar)
        
        self.stateValue = None
        
        self.Bind(wx.EVT_MENU, self.OnQuit, id = wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.onLog, id = wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnNew, id = wx.ID_NEW)
        
        self.statePanel = StatePanel(self, _id)
        self.statePanel.comboBox.Bind(wx.EVT_COMBOBOX, self.OnStateSelect)
        
        self.problemPanel = ProblemPanel(self, wx.ID_ANY)
        self.problemPanel.Show(False)
         
    def OnQuit(self, event):
        self.Close()
        
    def onLog(self, event):
        frame = wx.Frame(None,-1,size = (800,600))
        log = Log(frame,-1)
        frame.Show()
        
        
    def OnNew(self, event):
       
    
        driver.reset()
        self.stateValue =  None
        self.statePanel.comboBox.SetValue('')
        if self.problemPanel.IsShown():
            self.problemPanel.Show(False)
        self.statePanel.Show(True)
        
    def OnStateSelect(self, event):
        self.stateValue = self.statePanel.comboBox.GetValue()
        self.OnStateValue()
        
    def OnStateValue(self):
        if self.stateValue == 'Switched On':
            self.statePanel.Show(False)
            self.problemPanel.Show(True)
        elif self.stateValue == 'Switched Off':
            self.statePanel.Show(True)
            driver.run()