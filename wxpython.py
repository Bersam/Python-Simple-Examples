import wx

def load(event):
    file = open(filename.GetValue())
    content.SetValue(file.read())
    file.close()
def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(content.GetValue())
    file.close()

bersam = wx.App()
linux = wx.Frame(None, title="Simple Text Editor", size=(410,335))

bkg = wx.Panel(linux)

loader = wx.Button(bkg, label='Open')
loader.Bind(wx.EVT_BUTTON, load)

saver = wx.Button(bkg, label='Save')
saver.Bind(wx.EVT_BUTTON, load)

filename = wx.TextCtrl(bkg)
content = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loader, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saver, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(content, proportion=1, flag=wx.EXPAND |wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
linux.Show()
bersam.MainLoop()
