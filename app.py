from flask import Flask 

# Quando ela for executada de froma manual a forma muda de __name__ para "__main__"
app = Flask(__name__)

# Rota(como vai conseguir comunicar com outros clientes. recebe e devolve informações)
@app.route("/")
# o que será executado a partir da rota 
def helo_world():
  return "Hello World!"

@app.route("/about")
def about():
  return "Página sobre"

if __name__ == "__main__": 
  app.run(debug=True)