from this import d
import simpleui as UI
import PySimpleGUI as sg

ui = UI.SimpleUI()

def btn():
    print("click_btn")

def input(txt):
    print("text = " + str(txt))

def chengeToggle(flag):
    print("chengeToggle = " + str(flag))

def change_theme(x):
    sg.theme(x)
    sg.popup_get_text('This is {}'.format(x), default_text=x)

def create_window_1(window):
    func = lambda : print(str(window.GetItem("テキスト1").value))
    window.AddButton("ボタン1", btn)
    window.AddButton("ボタン2", func)
    window.AddInputField("テキスト1", "", input)
    window.AddToggle("トグル1", False, chengeToggle)
    window.AddOpenWindow("タイトル2", "タイトル2")
    window.AddItem(UI.SimpleUIList("リスト1", sg.theme_list(), change_theme))
    window.AddItem(UI.SimpleUIButton("ボタン", lambda : print("onclick")))
    window.AddItem(UI.SimpleUIInputField("インプット", "テストデフォルト", lambda txt: print(str(txt))))
    window.AddItem(UI.SimpleUIToggle("トグル", False, lambda x: print(str(x))))
    window.AddItem(UI.SimpleUISlider("スライダー", 0, 0, 100, lambda x: print(str(x))))

def create_window_2(window):
    func = lambda : print(str(window.GetItem("テキスト1").value))
    window.AddButton("ボタン1", btn)
    window.AddButton("ボタン2", func)
    window.AddInputField("テキスト1", "", input)
    window.AddToggle("トグル1", False, chengeToggle)

def test_ui():

    ui.AddWindow("タイトル", create_window_1)
    ui.AddWindow("タイトル2", create_window_2)

    ui.OpenTopWindow()
    ui.Run()

test_ui()