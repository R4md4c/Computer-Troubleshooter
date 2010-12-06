'''
Created on Nov 17, 2010

@author: ramdac
'''


import wx
import GUI.MainFrame
from engine import driver

class Troubleshooter(wx.App):
    def OnInit(self):
        self.mainFrame = GUI.MainFrame.MainFrame(None, -1, 'Computer Troubleshooter', wx.Size(400, 200), 'icons/icon.xpm')
        self.mainFrame.Show()
        return True

if __name__ == "__main__":
        x = Troubleshooter()
        x.MainLoop()
