from flask import Flask,render_template,redirect,request,session
from random import randrange

app=Flask(__name__)

app.secret_key = "super secret key"


#The lists will be understood when you go further into the code
Player_Options=["1","2","3"]
Choices=["rock.","paper.","scissors."]
AI_Loses=["scissors.","rock.","paper."]
AI_Wins=["paper.","scissors.","rock."]
Difficulties=Player_Options






#AI's roll will result in the outcome, we manipulate AI's choice using indexing
#Hence why the lists were arranged in that manner
def Win(P1ayer):

    Message(Choices,AI_Loses,"You win!",P1ayer)

def Draw(P1ayer):

    Message(Choices,Choices,"It's a draw!",P1ayer)

def Lose(P1ayer):
   
    Message(Choices,AI_Wins,"You lost!",P1ayer)




def Message(PlayerChoice,AIChoice,OutcomeMessage,P1ayer):
    print("You chose",PlayerChoice[P1ayer],"AI chose",AIChoice[P1ayer])
    
    print(OutcomeMessage)
    
    session['p_choice']=PlayerChoice[P1ayer]
    session['ai_choice']=AIChoice[P1ayer]
    session['out_msg']=OutcomeMessage
#AI will not choose, each difficulty has a different probability of outcome
#AI's roll will result in a win, lose or draw

def Play(P1ayer,x,y):
    AI=randrange(1,11)
    if AI in range(1,x):
        Win(P1ayer)
    elif AI in range(x,y):
        Draw(P1ayer)
    else:
        Lose(P1ayer)

def easy(Player):
    if Player in Player_Options:
        print(Player)
        P1ayer=int(Player)-1
        print(P1ayer)
        Play(P1ayer,6,9)

def medium(Player):
    if Player in Player_Options:
        print(Player)
        P1ayer=int(Player)-1
        print(P1ayer)
        Play(P1ayer,5,9)
    

def hard(Player):
    if Player in Player_Options:
        print(Player)
        P1ayer=int(Player)-1
        print(P1ayer)
        Play(P1ayer,4,9)


    


@app.route('/')
def hello():
    return render_template("r_p_s.html")



@app.route("/home")
def home():
    return redirect('/')

@app.route('/select',methods=['POST'])
def difficulty():
    if request.method == 'POST':
        q=request.form.get('difficulty')
        session['key']=q
        return render_template("r_p_s.html") ,'OK'
      

    
@app.route('/Rock',methods=['POST'])
def submit_data():
    difficulty
    if request.method == 'POST':
        d=int(session['key'])
        f=request.form['Rock']
        print(f)
        Player=str(1)
        if d==1:
            easy(Player)
        if d==2:
            medium(Player)
        if d==3:
            medium(Player)
        p_choice=session['p_choice']
        ai_choice=session['ai_choice']
        msg=session['out_msg']
        return render_template("r_p_s.html" , p_choice=p_choice,ai_choice=ai_choice,msg=msg) 


    
@app.route('/Paper',methods=['POST'])
def submit_data1():
    if request.method == 'POST':
        d=int(session['key'])
        f=request.form['Paper']
        print(f)
        Player=str(2)
        if d==1:
            easy(Player)
        if d==2:
            medium(Player)
        if d==3:
            medium(Player)
        print(f)
        p_choice=session['p_choice']
        ai_choice=session['ai_choice']
        msg=session['out_msg']
        return render_template("r_p_s.html" , p_choice=p_choice,ai_choice=ai_choice,msg=msg)


@app.route('/Scissor',methods=['POST'])
def submit_data2():
    if request.method == 'POST':
        d=int(session['key'])
        f=request.form['Scissor']
        print(f)
        Player=str(3)
        if d==1:
            easy(Player)
        if d==2:
            medium(Player)
        if d==3:
            medium(Player)
        p_choice=session['p_choice']
        ai_choice=session['ai_choice']
        msg=session['out_msg']
        return render_template("r_p_s.html" , p_choice=p_choice,ai_choice=ai_choice,msg=msg)


    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ =="__main__":

    
    app.run()