from cProfile import label
from pickle import TRUE
import PySimpleGUI as sg
# =================================================
class SimpleUIItem:
    def __init__(self):
        self.label = None
        self.func = None
    def layout(self):
        return []
    def update(self,event,values):
        if self.label == event:
            self.handler(values)
    def handler(self,args):
        return self.func(args)
# =================================================
class SimpleUICustom(SimpleUIItem):
    def __init__(self,label, layout_func, func):
        self.label = None
        self.layout_func = layout_func
        self.func = func
    def layout(self):
        return self.layout_func()
    def update(self,event,values):
        if self.label == event:
            self.handler(values)
    def handler(self,args):
        return self.func(args)
# =================================================
class SimpleUIPanel(SimpleUIItem):
    def __init__(self, label):
        self.label = label
        self.func = None
        self.items = []
        pass
    def layout(self):
        ret = []
        for item in self.items:
            for i in item.layout():
                ret.append(i)
        return ret
    def update(self,event,values):
        for item in self.items:
            if item.label == event:
                item.handler(values)
    def add(self,item):
        self.items.append(item)
    def remove(self,key):
        for item in self.items:
            if item.label == key:
                self.items.remove(item)
    def clear(self):
        self.items.clear()
# =================================================
class SimpleUIButton(SimpleUIItem):
    def __init__(self, label, onclick):
        self.label = label
        self.func = onclick
        pass
    def layout(self):
        return [sg.Button(self.label, key=self.label)]
    def handler(self,args):
        return self.func()
# =================================================
class SimpleUIToggle(SimpleUIItem):
    def __init__(self, label, default_value, onchange_value):
        self.label = label
        self.func = onchange_value
        self.default_value = default_value
        self.value = default_value
        pass
    def layout(self):
        return [sg.Text(self.label, size=(15, 1)), sg.Checkbox(text="",default=self.default_value, key=self.label, enable_events=True)]
    def handler(self,args):
        self.value = args[self.label]
        self.func(self.value)
# =================================================
class SimpleUISlider(SimpleUIItem):
    def __init__(self, label, default_value, min, max, onchange_value):
        self.label = label
        self.func = onchange_value
        self.default_value = default_value
        self.value = default_value
        self.min = min
        self.max = max
    def layout(self):
        return [sg.Text(self.label, size=(15, 1)), sg.Slider(default_value=self.default_value, range=(self.min, self.max), orientation = "h", key=self.label, enable_events=True)]
    def handler(self,args):
        self.value = args[self.label]
        self.func(self.value)
# =================================================
class SimpleUIList(SimpleUIItem):
    def __init__(self, label, items, onclick):
        self.label = label
        self.func = onclick
        self.items = items
        self.value = items[0]
    def layout(self):
        return [sg.Listbox(values=self.items, size=(20, 20), key=self.label, enable_events=True)]
    def handler(self,args):
        self.value = args[self.label][0]
        self.func(self.value)
# =================================================
class SimpleUIDropDown(SimpleUIItem):
    def __init__(self, label, items, default_value, onselect):
        self.label = label
        self.func = onselect
        self.items = items
        self.default_value = default_value
        self.value = self.default_value
    def layout(self):
        return [sg.Combo(values=self.items, default_value=self.default_value ,size=(20, 20), key=self.label, enable_events=True)]
    def handler(self,args):
        self.value = args[self.label]
        self.func(self.value)
# =================================================
class SimpleUIInputField(SimpleUIItem):
    def __init__(self, label, default_value, onchange_value):
        self.label = label
        self.func = onchange_value
        self.default_value = default_value
        self.value = default_value
        pass
    def layout(self):
        return [sg.Text(self.label, size=(15, 1)), sg.InputText(self.default_value, key=self.label, enable_events=True )]
    def handler(self,args):
        self.value = args[self.label]
        self.func(self.value)
# =================================================
class SimpleUIWindow:
    '''
    ?????????????????????????????????????????????
    '''

    def __init__(self, title):
        '''
        ?????????????????????
        '''
        self.window = None
        self.items = {}
        self.title = title
        self.mger = None
        self.onopen_func = None
        self.isOpen = False
        self.theme = "Dark Amber"

    def __init__(self, mger, title, onopen_func):
        '''
        ?????????????????????
        '''
        self.window = None
        self.items = {}
        self.title = title
        self.mger = mger
        self.isOpen = False
        self.onopen_func = onopen_func
        self.theme = "Dark Amber"

    def Open(self):
        '''
        ????????????????????????
        '''
        # ??????????????????
        sg.theme(self.theme)

        self.OnOpen()

        # ????????????????????????
        layout = []

        for v in self.items.values():
            layout.append(v.layout())

         # ????????????????????????
        self.window = sg.Window(self.title, layout, finalize=True)
        self.isOpen = True

    def OnOpen(self):
        '''
        ???????????????????????????
        '''
        if self.onopen_func != None:
            self.items.clear()
            self.onopen_func(self)

    def IsOpen(self):
        '''
        ?????????????????????????????????
        '''
        return self.isOpen

    def Close(self):
        '''
        ???????????????????????????
        '''
        self.window.close()
        self.isOpen = False

    def Run(self):
        '''
        ??????????????????????????????
        '''
        event, values = self.window.read()
        while self.Update(event, values):
            pass

    def Update(self, event, values):
        '''
        @return True:?????? False:??????
        '''
        if event is None:
            print('Exit Window:' + str(self.title))
            self.Close()
            return False
        for v in self.items.values():
            v.update(event,values)
        return True

    def AddOpenWindow(self, label, windowKey):
        '''
        ????????????????????????????????????????????????
        '''
        func = lambda : self.mger.OpenWindow(windowKey)
        self.AddItem(SimpleUIButton(label, func))


    def CloseWindow(self, windowKey):
        '''
        ?????????????????????????????????
        '''
        self.mger.CloseWindow(windowKey)

    def AddItem(self, item):
        '''
        ??????????????????
        '''
        self.items[item.label] = item

    def GetItem(self, label):
        '''
        ??????????????????
        '''
        return self.items[label]

    def PopUp(self, message):
        '''
        ????????????????????????
        '''
        sg.popup(message)
# =================================================
class SimpleUI:
    '''
    ???????????????UI???????????????
    '''

    def __init__(self):
        '''
        ?????????????????????
        '''
        self.windows = {}
        self.topWindowKey = ""
    
    def Clear(self):
        '''
        ????????????????????????????????????
        '''
        for window in self.windows.values():
            if window.IsOpen():
                window.Close()
        self.windows.clear()

    def AddWindow(self, title, onopen_func):
        '''
        ?????????????????????
        '''
        return self.AddWindowDynamic(SimpleUIWindow(self, title, onopen_func))

    def AddWindowDynamic(self, window):
        '''
        ?????????????????????
        '''
        if self.topWindowKey == "":
            self.topWindowKey = window.title
        self.windows[window.title] = window
        return self.windows[window.title]

    def Run(self):
        '''
        ????????????????????????????????????????????????????????????????????????
        '''
        while self.Update():
            pass

    def Update(self):
        '''
        ??????????????????????????????????????????
        '''
        isRetry = False
        window_instance, event, values = sg.read_all_windows()
        for window in self.windows.values():
            if window_instance == window.window:
                window.Update(event, values)
        for window in self.windows.values():
            if window.IsOpen():
                isRetry = True
            elif window.title == self.topWindowKey:
                self.AllCloseWindow()
                isRetry = False
        return isRetry

    def RemoveWindow(self, key):
        '''
        ?????????????????????????????????
        '''
        if self.windows[key].IsOpen():
            self.windows[key].Close()
        self.windows.pop(key)

    def OpenTopWindow(self):
        '''
        ??????????????????????????????????????????????????????
        '''
        self.OpenWindow(self.topWindowKey)

    def OpenWindow(self, key):
        '''
        ????????????????????????
        '''
        self.GetWindow(key).Open()
        if key != self.topWindowKey:
            print(key)
            print(self.topWindowKey)
            self.GetWindow(key).window.move(self.GetWindow(self.topWindowKey).window.current_location()[0], self.GetWindow(self.topWindowKey).window.current_location()[1]+220)
        
    def CloseWindow(self, key):
        '''
        ???????????????????????????
        '''
        self.GetWindow(key).Close()

    def AllCloseWindow(self):
        '''
        ???????????????????????????????????????
        '''
        for window in self.windows.values():
            if window.IsOpen():
                window.Close()

    def GetWindow(self, key):
        '''
        ????????????????????????
        '''
        return self.windows[key]


# =================================================
