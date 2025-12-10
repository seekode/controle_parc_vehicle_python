from abc import ABC, abstractmethod


class Insurable(ABC):
    @abstractmethod
    def calculate_insurance_prenium(self):
        pass
    