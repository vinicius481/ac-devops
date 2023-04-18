from flask import Flask, request

app = Flask(__name__)

def primo(x):
    qtd=0
    for n in range (1,x+1):
        if x % n == 0: 
            qtd+=1
    return qtd == 2 or x == 1

@app.route('/')
def numero():
    cont = 0
    n = 0
    primos=""
    while cont <= 100:
        n += 1
        if primo(n) == True:
            cont += 1
            primos = primos + str(n) + ", "
            if cont % 10 == 0:
                primos += "<br>"
    return  (primos)

if __name__ == ("__main__"):
    app.run (host='0.0.0.0', port=5000,debug=True)