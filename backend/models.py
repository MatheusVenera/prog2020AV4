from config import db, db_file, path, remove

class Car(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  car_type = db.Column(db.String)
  brand = db.Column(db.String)
  model = db.Column(db.String)


  def __str__(self):
    return f'{self.id}. {self.model}, {self.car_type} - {self.brand}'


  def json(self):
    return {
      "id": self.id,
      "car_type": self.car_type,
      "brand": self.brand,
      "model": self.model
    }


if __name__ == "__main__":
  print(db_file)
  if path.exists(db_file):
    remove(db_file)

  db.create_all()

  car1 = Car(model="Pampa", car_type="Funcional", brand="Ford")
  car2 = Car(model="Fusca", car_type="Popular", brand="Volkswagen")

  db.session.add(car1)
  db.session.add(car2)

  db.session.commit()

  print(car1)
  print(car1.json())
