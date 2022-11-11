import pylightxl as xl
import random

db = xl.readxl(fn='Kennzeichen.xlsx')

active = True
lives = 3
wins = 0



def getting_info():
    global info
    randnum = str(random.randrange(2,724))

    info = db.ws(ws='All').row(row=int(randnum))
    return info

def question(info):
    global Answer, Q_prompt
    info = getting_info()
    prompt = '''Woher kommt dieses kennzeichen? \n'''+ '''          '''+ info[0]+'\n'
    Answer = info[1]
    print(info[1])
    Q_prompt = str(input(prompt)).lower()
    return Q_prompt, Answer

def game_over():
    if wins in range(0,5):
        print('''
            Schade aber nächstes mal bestimmt!

        ''')
    elif wins in range(6,10):
        print('''
            Schade aber du hast das toll gemacht!

        ''')

def win():
    if lives == 3:
        print('Wow! Du hast echt gut gelernt!')
        challenge = input('''
                    Bist du bereit für eine Herausvorderung?
                            
                    Ja klar!

                    Ne Lieber nicht.
                            
                    ''')
    elif lives == 2:
        print('''
                Das war schon fast perfekt!
                Du machst das super!''')
    elif lives == 1:
        print('''
                Das war echt knapp!

                Du hast es aber dennoch gemeistert!
                
        ''')

while active == True:
    getting_info()
    if lives != 0:
        question(info)
        if Q_prompt == Answer:
            if wins == 5:
                win()
                break
            else:
                print('''
                diese Antwort ist RICHTIG! \n
                Das Kennzeichen''', info[0], '''kommt von ''', info[1], info[2])
                wins += 1
                print('Youve won '+ str(wins), ' times!')
        
        elif Q_prompt != Answer:
            if lives == 0:
                game_over()
            else:
                print('''
                Diese Antwort ist leider Falsch weil das Kennzeichen''', info[0], '''kommt von ''', info[1], info[2], "\n"
                )
                lives -= 1
                print('lives = ', lives)
    else:
        game_over()
        break


    
            

#print('''
# Kennzeichen: ''', info[0],'\n',
#'''Ursprung: ''', info[1],'\n',
#'''Bundesland: ''', info[2] )
