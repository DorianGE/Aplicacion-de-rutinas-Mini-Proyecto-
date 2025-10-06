import redis
import json
client = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)

def save_habit(habit_id: int, habit_name: str, frecuency: str, status: str = "Pendiente"):
    habit_data = {
        "Id del Habito": habit_id,
        "Nombre del habito": habit_name,
        "Frecuencia":frecuency,
        "estado": status
    }

    client.set(f"habit:{habit_id}",json.dumps(habit_data))
    return True

def read_habit(habit_id: int):
    data = client.get(f"habit:{habit_id}")
    return json.loads(data) if data else None

def update_habit_status(habit_id: int, New_status : str):
    habit = read_habit(habit_id)
    if habit:
        habit["estado"] = New_status
        client.set(f"habit:{habit_id}",json.dumps(habit))

