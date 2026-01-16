import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

# create

def test_create_task():
  new_task_data = { 
    "title":"Nova tarefa",
    "description":"Descrição da nova tarefa"
  }
  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  assert response.status_code == 200
  response_json = response.json()
  assert "mensagem" in response_json
  assert "id" in response_json
  tasks.append(response_json['id'])

# Read
# Temos dois emdpoint para validar, o primeiro para recuperar todas as atividades cadastradas e o segundo para recuperar uma expecífica.
# teste para todas as atividasdes

def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  # valida se recebe o codigo 200 que deu certo o que estava fazendo.
  assert response.status_code == 200
  # cria a variavel 
  response.json = response.json()
  # validade se tem as duas chaves dentro dessa varival
  assert "tasks" in response.json
  assert "total_tasks" in response.json

# validando uma tarefa expecífica
def test_get_task():
  # usando a lista que está sendo alimentada desde o início
  if tasks:
    # vamos pegar a primeira atividade que foi criada (priemira posição)
    task_id = tasks[0]
    # faz uma requisição para fazer as recuperações 
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200 
    response_json = response.json()
    # compara os id do task_id com o corpo da mensagem do postman 
    assert task_id == response_json['id']

#Testando as atualização
def test_update_task():
  # enviar uma requisição para o endpoint (url) de atualização
  if tasks:
    task_id = tasks[0]
    payload = {
      "completed":False,
      "description":"Nova descrição",
      "title":"Título atualizado"
    }
    response = requests.put(f"{BASE_URL}/tasks/{task_id}",json= payload)
    response.status_code == 200
    # recupera o json que recebe na resposta
    response_json = response.json()
    assert "mensagem" in response_json 

    # Nova requisição a tarefa específica 
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200 
    response_json = response.json()
    # compara os id do task_id com o corpo da mensagem do postman 
    assert response_json["title"] == payload["title"]
    assert response_json["description"] == payload["description"]
    assert response_json["completed"] == payload["completed"]

# Delete
def test_delete_task():
  if tasks:
    task_id = tasks[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    response.status_code == 200
    
    # requisição específica, tem que dar 404 já que acima a tarefa foi deletada.
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404 
    










































