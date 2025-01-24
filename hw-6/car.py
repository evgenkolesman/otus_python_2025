"""
создайте класс `Car`, наследник `Vehicle`
"""
from engine import Engine

class Car(Engine):

    def __init__(self, volume, pistons, engine: Engine ):
        super().__init__(volume, pistons)
        self._engine = engine

    @property
    def engine(self):
        return self.engine

    @engine.setter
    def engine(self, engine_new: Engine):
        self._engine = engine_new