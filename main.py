from flask import Flask, json, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    file = open('dados.json')
    dados_Usuario = json.load(file)
    file.close()

   
    return render_template("index.html", dados_Usuario = dados_Usuario)


@app.route("/boleto", methods=["GET"])
def boleto():

    return render_template("boleto.html")

@app.route("/cobranca", methods=["GET"])
def cobranca():

  return render_template("cobranca.html")

@app.route("/calculo", methods=["POST"])
def calc_Cobranca():
    valor = request.form.get("valor")
    print(request.form)
    file = open("dados.json")
    dados = json.load(file)
  
    dados["saldo"] = int(dados["saldo"]) + int(valor)
  
    with open("dados.json", "w") as newFile:
      json.dump(dados, newFile)
    file.close()
    
    return render_template("sucesso.html")


@app.route("/pagamento", methods=["GET"])
def pagamento():
    
    codigo = request.args["codigo"]

    file = open("boleto.json")
    boletos = json.load(file)
    file = open("dados.json")
    dados = json.load(file)
    file.close()

    for boleto in boletos:
      if boleto["codigo"] == codigo:
          valor = boleto["valor"]
    file.close()
    
    novoSaldo = int(dados["saldo"]) - int(valor)
    return render_template("pagamento.html", valor = valor , dados = dados, novoSaldo = novoSaldo)

@app.route("/pagar", methods=["POST"])
def calculoSaldo():

  print(request.form)
  valor = request.form.get("saldo")
  print(valor)
  
  file = open("dados.json")
  dados = json.load(file)
  dados["saldo"] = str(valor)
  with open("dados.json", "w") as newFile:
    json.dump(dados, newFile)
  file.close()
  return render_template("sucesso.html")
app.run(host='0.0.0.0', port=81)