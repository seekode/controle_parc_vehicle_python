from abc import ABC, abstractmethod


class Insurable(ABC):

    @abstractmethod
    def calculate_insurance_premium(self):
        pass