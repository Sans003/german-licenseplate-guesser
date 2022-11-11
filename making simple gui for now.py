import PySimpleGUI as sg
import time
import pylightxl as xl
import random

db = xl.readxl(fn='Kennzeichen.xlsx')

active = True
font = ("Overlock", 15, "bold")
sg.theme("DarkBlue3")
sg.set_options(font=font)
lives = 3
wins = 0

def getting_info():
    global ans3, ans1, ans2, answers
    randnum1 = str(random.randrange(2,724))
    ans1 = db.ws(ws='All').row(row=int(randnum1))
    randnum2 = str(random.randrange(2,724))
    ans2 = db.ws(ws='All').row(row=int(randnum2))
    randnum3 = str(random.randrange(2,724))
    ans3 = db.ws(ws='All').row(row=int(randnum3))
    #print(randnum1, randnum2, randnum3)

    answers = [ans1[1],ans2[1],ans3[1]]
    #generate correct answer
    random.shuffle(answers)
    
    print(ans1,ans2,ans3)
    return ans1, ans2, ans3, answers

def qupdate():
    info = getting_info()
    window["A1"].update(text=answers[0])
    window["A2"].update(text=answers[1])
    window["A3"].update(text=answers[2])
    window["license"].update(value=ans1[0])

def losing():
    global lives, wins
    lives -= 1
    print(lives)
    check(lives, wins)
    qupdate()

def winning():
    global wins, lives
    wins += 1
    print(wins)
    check(lives, wins)
    qupdate()

def reset(lives, wins):
    lives, wins = 0, 3
    return wins, lives

def check(lives, wins):
    if lives <= 0:
        qupdate()
        window["game"].update(visible=False)
        window["menu"].update(visible=False)
        window["winner"].update(visible=False)
        window["gameover"].update(visible=True)
        lives, wins = reset(lives, wins)
        print('lives equal ', str(lives))
        
        return wins, lives
    elif wins >= 15:
        qupdate()
        window["game"].update(visible=False)
        window["menu"].update(visible=False)
        window["gameover"].update(visible=False)
        window["winner"].update(visible=True)
        lives, wins = reset(lives, wins)
        print('lives equal ', str(lives))
        
        return wins, lives
    
    return wins, lives
        

info = getting_info()

winner = [
    [sg.Text('''YOU WON!!!''')],
    [sg.Text('''YOU ARE REALLY SMART''')],
    [sg.Text("")],
    #[sg.VPush()],
    [sg.Button(button_text="MENU", size=(10,2), key="_MENU_", border_width=0)],
    [sg.Button(button_text="EXIT", size=(10,2), key="_EXIT_", border_width=0)]]



gameover = [
    [sg.Text('''GAME OVER''')],
    [sg.Text('''BETTER LUCK NEXT TIME''')],
    [sg.Text("SCORE " + str(wins))],
    #[sg.VPush()],
    [sg.Button(button_text="MENU", size=(10,2), key="_MENU_", border_width=0)],
    [sg.Button(button_text="EXIT", size=(10,2), key="_EXIT_", border_width=0)]]


menu = [
    [sg.Text('''Press Start to generate a random licenseplate''')],
    #[sg.VPush()],
    [sg.Button(button_text="START", size=(10,2), key="_START_", border_width=0)],
    [sg.Button(button_text="EXIT", size=(10,2), key="_EXIT_", border_width=0)]]

game = [
    [sg.Text("Von welcher Stadt ist dieses Nummernschild: \n")],
    [sg.Text(ans1[0], size=10, key="license",font="bold",justification='center')],

    [sg.VPush()],
    [sg.Button(button_text=answers[0], auto_size_button=True, key="A1", border_width=0)],
    [sg.Button(button_text=answers[1], auto_size_button=True, key="A2", border_width=0)],
    [sg.Button(button_text=answers[2], auto_size_button=True, key="A3", border_width=0)],
    ]



layout = [
    [sg.Frame("", menu, size=(600, 300), visible=True,  key='menu',  element_justification='center', border_width=0),
     sg.Frame("", game, size=(600, 300), visible=False, key='game',  element_justification='center', border_width=0),
     sg.Frame("", winner, size=(600, 300), visible=False, key='winner',  element_justification='center', border_width=0),
     sg.Frame("", gameover, size=(600, 300), visible=False, key='gameover',  element_justification='center', border_width=0)],
]



title = "Kennzeichen_GUI_Test"

window = sg.Window(title, layout, size=(600, 300), finalize=True)
menu, game, gameover, winner = window['menu'], window['game'], window['gameover'], window['winner']
sg.theme("DarkGrey")

while True:
    event, values = window.read()
    print(event)
    if "_EXIT_" in str(event) or event == sg.WIN_CLOSED:
        break
    elif "_MENU_" in event:
        lives, wins = reset(lives, wins)
        window["gameover"].update(visible=False)
        window["game"].update(visible=False)
        window["winner"].update(visible=False)
        window["menu"].update(visible=True)
        
    elif event == "_START_":
        lives, wins = reset(lives, wins)
        window["game"].update(visible=True)
        window["menu"].update(visible=False)
        window["winner"].update(visible=False)
        window["gameover"].update(visible=False)
    # and window[event].GetText() == "ans1[1]"
    elif event == "A1" and window[event].GetText() == ans1[1]:
        winning()
    elif event == "A2" and window[event].GetText() == ans1[1]:
        winning()
    elif event == "A3" and window[event].GetText() == ans1[1]:
        winning()
    #elif event == "A1" , event == "A2" , event == "A3" and window[event].GetText() != ans1[1]:
    elif window["A1"].GetText() != ans1[1]:
        losing()
    elif window["A2"].GetText() != ans1[1]:
        losing()
    elif window["A3"].GetText() != ans1[1]:
        losing()

window.close()
