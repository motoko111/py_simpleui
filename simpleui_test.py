from this import d
from py_simpleui import py_simpleui as UI
import PySimpleGUI as sg

def change_theme(x):
    sg.theme(x)
    sg.popup_get_text('This is {}'.format(x), default_text=x)

def create_window_1(window):
    window.AddOpenWindow("タイトル2", "タイトル2")
    
    panel = UI.SimpleUIPanel("パネル")
    btn1 = UI.SimpleUIButton("A", lambda : print("onclick1"))
    btn2 = UI.SimpleUIButton("B", lambda : print("onclick2"))
    btn3 = UI.SimpleUIButton("C", lambda : print("onclick3"))
    panel.add(btn1)
    panel.add(btn2)
    panel.add(btn3)
    window.AddItem(panel)

    window.AddItem(UI.SimpleUIDropDown("ドロップダウン", ["A","B","C","D"], "C", lambda x: print(str(x))))
    window.AddItem(UI.SimpleUIList("リスト1", sg.theme_list(), change_theme))
    window.AddItem(UI.SimpleUIButton("ボタン", lambda : print("onclick")))
    window.AddItem(UI.SimpleUIInputField("インプット", "テストデフォルト", lambda txt: print(str(txt))))
    window.AddItem(UI.SimpleUIToggle("トグル", False, lambda x: print(str(x))))
    window.AddItem(UI.SimpleUISlider("スライダー", 0, 0, 100, lambda x: print(str(x))))

def create_window_2(window):
    window.AddItem(UI.SimpleUIButton("ボタン1", lambda : print("onclick1")))
    window.AddItem(UI.SimpleUIButton("ボタン2", lambda : print("onclick2")))
    window.AddItem(UI.SimpleUIInputField("インプット1", "テストデフォルト", lambda txt: print(str(txt))))
    window.AddItem(UI.SimpleUIToggle("トグル", False, lambda x: print(str(x))))

def test_ui():
    ui = UI.SimpleUI()

    ui.AddWindow("タイトル", create_window_1)
    ui.AddWindow("タイトル2", create_window_2)

    ui.OpenTopWindow()
    ui.Run()

test_ui()