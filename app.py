from flask import Flask, request, jsonify
from models.task import Task

# Quando ela for executada de froma manual a forma muda de __name__ para "__main__"
app = Flask(__name__)

# CRUD= Creat (crear), Read(ler), Update(atualizar) and Dalete(deletar)
# Tabela: Tarefa 

# Está sendo usada em memória, porém pode e vai ser substituido por um banco de dados.
tasks = []
task_id_control = 1

# Create (criando atividades)
@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control,title=data['title'], description=data.get("decription", ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({"mensagem":"Nova tarefa criada com sucesso", "id": new_task.id})

# Read (ler as atividades)
@app.route('/tasks', methods= ['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks ]
  output= {
            "tasks": task_list,
            "total_tasks": len(task_list)  
          }   
  return jsonify(output)
  
# Também sobre o read 
@app.route('/tasks/<int:id>', methods = ['GET'])
def get_task(id):
  task = None
  for t in tasks:
    if t.id == id: 
      return jsonify(t.to_dict())
    
  return jsonify({"mensagem":"Não foi posível encontrar a atividade"}), 404

# Update = atualizar 
@app.route('/tasks/<int:id>', methods = ['PUT'])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t 
      break 

  if task == None:
    return jsonify({"mensagem":"Não foi possível encontrar a atividade"}), 404
  
  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  print(task)
  return jsonify({"mensagem":"Tarefa atualizada com sucesso"})

# Delete= deletar 
@app.route('/tasks/<int:id>', methods = ['DELETE'])
def delete_task(id):
  task = None 
  for t in tasks:
    if t.id == id:
      task = t
      break
      

  if not task:
    return jsonify({"mensagem":"Não foi possível encontrar a atividade"}), 404
  
  tasks.remove(task)
  return jsonify({"mensagem":"Tarefa deletada com sucesso"})

if __name__ == "__main__": 
  app.run(debug=True)