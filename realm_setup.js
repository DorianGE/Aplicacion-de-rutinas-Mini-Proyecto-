const Realm = require("realm");

const HabitSchema = {
  name: "Habito",
  properties: {
    _id: "int",
    nombre: "string",
    frecuencia: "string",
    Estatus: "string"
  },
  primaryKey: "_id"
};

async function archivo() {
  const realm = await Realm.open({
    path: "Realm-data/habits.realm",
    schema: [HabitSchema]
  });

  realm.write(() => {
    realm.create("Habito", {
      _id: 1,
      nombre: "Beber agua",
      frecuencia: "Diario",
      Estatus: "pendiente"
    });
  });

  console.log("✅ Archivo generado correctamente");
  realm.close();
}

archivo();
