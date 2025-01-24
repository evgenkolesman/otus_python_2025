"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions_dir import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo = 0, max_cargo = 40):
        super().__init__()
        self._cargo = cargo
        self._max_cargo = max_cargo

    def load_cargo(self, cargo_additional):
        if self._cargo + cargo_additional <= self._max_cargo:
            self._cargo += cargo_additional
        else:
           raise CargoOverload(f'Cargo overload: {self._cargo} + {cargo_additional} > {self._max_cargo}')

    def __str__(self):
        return f'Plane: cargo = {self._cargo}, max_ cargo = {self._max_cargo}'

