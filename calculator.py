#coding=utf-8
import math
import wx

class CalcFrame(wx.Frame):

	def __init__(self,title):
		super(CalcFrame, self).__init__(None, title = title, size = (300, 250))
		self.InitUI()
		self.Centre()
		self.Show()

	def InitUI(self):
		vbox = wx.BoxSizer(wx.VERTICAL)
		self.textprint = wx.TextCtrl(self, -1,'', style=wx.TE_RIGHT)
		self.equation = ""

		vbox.Add(self.textprint, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)      
		gridBox = wx.GridSizer(5, 4, 5, 5)##行数，列数，垂直间隔，水平间隔
		labels=['AC','DEL','PI','CLOSE','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
		for label in labels: 
			buttonItem = wx.Button(self,label = label)
			self.createHandler(buttonItem,label)
   			gridBox.Add(buttonItem, 1, wx.EXPAND)

   		vbox.Add(gridBox, proportion=1, flag=wx.EXPAND)
		self.SetSizer(vbox)

   	def createHandler(self,button,labels):
   		item = ['del','AC','=','CLOSE']
   		if labels not in item:
   			self.Bind(wx.EVT_BUTTON,self.OnAppend,button)
   		elif labels == 'DEL':
   			self.Bind(wx.EVT_BUTTON,self.OnDel,button)
   		elif labels == 'AC':
   			self.Bind(wx.EVT_BUTTON,self.OnAc,button)
   		elif labels == '=':
   			self.Bind(wx.EVT_BUTTON,self.OnTarget,button)
   		elif labels == 'CLOSE':
   			self.Bind(wx.EVT_BUTTON,self.OnExit,button)

   	def OnAppend(self,event):
   		eventbutton = event.GetEventObject()
   		label = eventbutton.GetLabel()
   		self.equation += label
   		self.textprint.SetValue(self.equation)

   	def OnDel(self,event):
   		self.equation = self.equation[:-1]
   		self.textprint.SetValue(self.equation)

   	def OnAc(self,event):
   		self.textprint.Clear()
   		self.equation=""
   		self.textprint.SetValue(self.equation)

   	def OnTarget(self,event):
   		string = self.equation
   		try:
   			target = eval(string) #eval会计算字符串形式的Python表达式,并返回结果的值
   			self.equation = str(target)
   			self.textprint.SetValue(self.equation)
   		except SyntaxError:
   			dlg = wx.MessageDialog(self,u'格式错误，请输入正确的等式!',wx.OK|wx.ICON_INFORMATION)#消息对话框
   			dlg.ShowModal()
   			dlg.Destroy()

   	def OnExit(self,event):
   		self.Close()

if __name__ == '__main__':

	app = wx.App()
	CalcFrame(title='Calculator')
	app.MainLoop()
