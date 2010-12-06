'''
Created on Nov 20, 2010

@author: ramdac
'''
"""This module contains the panels which are going to be used
to ask the questions so that the question & answers feat begins"""

from GUI.GenericPanel import GenericPanel
import wx

class StatePanel(GenericPanel):
    """ A panel for asking for the computer state if its switched on or switched off"""
    def __init__(self, parent, _id):
        GenericPanel.__init__(self, parent, _id, ('Switched On', 'Switched Off'))
        self.staticText.SetLabel('What is your computer\'s state right now?')
        self.stateValue = None
        
class ProblemPanel(GenericPanel):
    """ If the computer is switched on then that panel appears and asks the
    user what he thinks the problem is from"""
    def __init__(self, parent, _id):
        GenericPanel.__init__(self, parent, _id, ('Screen', 'RAM', 'CPU', 'Network'))
        self.staticText.SetLabel('What do you think the problem is from ?')
        self.Layout()
        self.stateValue = None
        
        self.comboBox.Bind(wx.EVT_COMBOBOX, self.OnSelect)
    
    def OnSelect(self, event):
        self.stateValue = self.comboBox.GetValue()