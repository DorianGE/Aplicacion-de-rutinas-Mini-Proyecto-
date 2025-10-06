import os
from redis_setup import save_habit, read_habit, update_habit_status
from tinydb_setup import save_habit_T, read_habit_t, update_habit_status_t, list_habits

def Crear_habito():
 Id_habit = int(input("Ingrese el numero de id del habito: "))
 Habit = input("Ingrese el habito: ")
 Frecuencia = input("Ingrese con la frecuencia que se hace(Diario/semanal/mensual): ")

 save_habit(habit_id= Id_habit,habit_name=Habit, frecuency=Frecuencia)
 save_habit_T(habit_idt=Id_habit, habit_namet=Habit, frecuencyt=Frecuencia)

def Actualizar_Estado():
  Id_Habit = int(input("Ingrese el Id de habito que desea modificar: "))
  Estatus_Nuevo = input("Ingrese el estado a actualizr(Pendiente/Completado): ")

  update_habit_status(habit_id=Id_Habit, New_status=Estatus_Nuevo)
  update_habit_status_t(habit_idt=Id_Habit,New_statut=Estatus_Nuevo)

  input("presione enter para continuar")
  limpiar_pantalla()

def Leer_Habito():
 Id_Habito = int(input("Ingrese el Id del habito que desea ver: "))

 Habito = read_habit(habit_id= Id_Habito)
 Habito_T = read_habit_t(habit_idt= Id_Habito)

 print("habito en Redist" + str(Habito))
 print("habito encontrado en tiny: "+ str(Habito_T))

 input("presione enter para continuar")
 limpiar_pantalla()

def limpiar_pantalla():
  os.system('cls' if os.name == 'nt' else 'clear')

while True:
 print("------MENU-----")
 print("1.-Crear un habito")
 print("2.-Leer el habito")
 print("3.-Actulizar estado de un habito")
 print("4.-Salir")

 opcion = input("Selecciona cual va usar:")
 limpiar_pantalla()

 if opcion == "1":
  Crear_habito()
  limpiar_pantalla()

 elif opcion == "2":
  Leer_Habito()

 elif opcion == "3":
   Actualizar_Estado()

 elif opcion == "4":
   print("Saliendo de la aplicacion . . .")
   break
 
 else:
  print("Eliga una opcion de las que se muestra en pantalla.")