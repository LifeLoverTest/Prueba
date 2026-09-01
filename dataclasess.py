from dataclasses import dataclass

@dataclass
class Mascota: 
  nombre: str
  especie: str
  edad: int 
  vacunado: bool = False 
  
  def __post_init__(self):
    if not self.nombre.strip():
      raise ValueError("No es posible dejar el nombre en blanco")

"""mascota1 = Mascota("Pedro", "Perro", 12, True)"""
mascota2 = Mascota("", "Gato", 0)

print(mascota1)