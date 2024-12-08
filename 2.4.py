from datetime import datetime
class Evento:
    total_eventos=0
    
    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        
        Evento.total_eventos += 1
        
    def __str__(self):
        return f"Evento:{self.titulo}, Data: {self.data_hora}, Descrição:{self.descricao}, Concluido:{self.is_concluido}"

evento1 = Evento("Reunião", datetime(2024, 12, 10, 15, 30), "Reunião de planejamento")
evento2 = Evento("Almoço", datetime(2024, 12, 8, 12, 0), "Almoço de negócios")
print(f"Total de eventos: {Evento.total_eventos}")
print(f"Evento 1: {evento1}")
print(f"Evento 2: {evento2}")

class Evento:
    total_eventos = 0
    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1

    def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(nome,data_hora,descricao):
        if isinstance(nome, str) and isinstance(data_hora, datetime) and isinstance(descricao, str):
            return True
        return False

    def __str__(self):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descrição: {self.descricao}, Concluido: {self.is_concluido}"

evento1 = Evento("Reunião", datetime(2024, 12, 10, 15, 30), "Reunião de planejamento")
evento2 = Evento("Almoço", datetime(2024, 12, 8, 12, 0), "Almoço de negócios")
evento2.isConcluido()

print(f"Evento 2 concluído: {evento2.is_concluido}")
print(f"Total de eventos: {Evento.num_eventos()}")
print(Evento.valida_evento("Reunião", datetime(2024, 12, 10, 15, 30), "Reunião de planejamento"))
print(Evento.valida_evento("Reunião", "data inválida", "Reunião de planejamento"))

class Evento:
    total_eventos = 0
    
    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        
        Evento.total_eventos += 1

    def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(nome, data_hora, descricao):
        if isinstance(nome, str) and isinstance(data_hora, datetime) and isinstance(descricao, str):
            return True
        return False

    def __str__(self):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descrição: {self.descricao}, Concluido: {self.is_concluido}"

    def __eq__(self, other):
        return self.data_hora == other.data_hora

    def __ne__(self, other):
        return self.data_hora != other.data_hora

    def __lt__(self, other):
        return self.data_hora < other.data_hora

    def __le__(self, other):
        return self.data_hora <= other.data_hora

    def __gt__(self, other):
        return self.data_hora > other.data_hora

    def __ge__(self, other):
        return self.data_hora >= other.data_hora

evento1 = Evento("Reunião", datetime(2024, 12, 10, 15, 30), "Reunião de planejamento")
evento2 = Evento("Almoço", datetime(2024, 12, 8, 12, 0), "Almoço de negócios")

print(evento1)
print(evento2)
print(f"Evento 1 == Evento 2: {evento1 == evento2}")
print(f"Evento 1 != Evento 2: {evento1 != evento2}")
print(f"Evento 1 < Evento 2: {evento1 < evento2}")
print(f"Evento 1 <= Evento 2: {evento1 <= evento2}")
print(f"Evento 1 > Evento 2: {evento1 > evento2}")
print(f"Evento 1 >= Evento 2: {evento1 >= evento2}")
