from tinydb import TinyDB,Query

db = TinyDB('TinyDB-data/habits.json')
habit = Query()

def save_habit_T(habit_idt: int, habit_namet: str, frecuencyt: str, statust: str = "Pendiente"):
    habit_data = {
       "Id de habito": habit_idt,
        "Nombre del habito": habit_namet,
        "Frecuencia": frecuencyt,
        "Estado": statust
    }
    db.insert(habit_data)
    return True

def read_habit_t(habit_idt: int):
    result = db.search(habit["Id de habito"] == habit_idt)
    if result:
     return result[0] 
    else:
       print("No hay habitos disponibles")

def list_habits():
   return db.all()

def update_habit_status_t(habit_idt: int, New_statut: str):
   db.update({"Estado": New_statut},habit["Id de habito"] == habit_idt)