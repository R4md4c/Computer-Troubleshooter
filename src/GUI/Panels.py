'''
Created on Nov 20, 2010

@author: ramdac
'''
"""This module contains the panels which are going to be used
to ask the questions so that the question & answers feat begins"""

from GUI.GenericPanel import GenericPanel
import wx
import sqlite3
import sys
from engine import driver

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
        GenericPanel.__init__(self, parent, _id, ('Screen', 'Sound', 'Network'))
        self.staticText.SetLabel('What do you think the problem is from ?')
        self.Layout()
        self.stateValue = None
        
        self.comboBox.Bind(wx.EVT_COMBOBOX, self.OnSelect)
    
    def OnSelect(self, event):
        self.stateValue = self.comboBox.GetValue()
        if self.stateValue == 'Screen':
            driver.engine.reset()
            driver.run_on_state_screen()
        
class Log(GenericPanel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)   
        self.logData = self.logConnect("log.sqlite", "log")      
        self.table = wx.ListCtrl(parent,-1,style=wx.LC_REPORT,size = (800,600))
        self.table.InsertColumn(0, '#', width=200)
        self.table.InsertColumn(1, 'Problem', width=200)
        self.table.InsertColumn(2, 'Solution', width=200)
        self.table.InsertColumn(3, 'Date', wx.LIST_FORMAT_LEFT, 200)
        self.addData(self.logData)


 #------------------ Connect to SQLite database -------------       
    def logConnect(self,databaseName,tableName):
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        sql = "select * from "+tableName
        cursor.execute(sql)
        return cursor.fetchall()


#------------------- Put log data on the table --------------
    def addData(self,list):
       for i in list:
            index = self.table.InsertStringItem(sys.maxint, str(i[0]))
            self.table.SetStringItem(index, 1, i[1])
            self.table.SetStringItem(index, 2, i[2])
            self.table.SetStringItem(index, 3, i[3])