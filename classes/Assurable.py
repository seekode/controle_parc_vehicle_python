from abc import ABC, abstractmethod


class Assurable(ABC):
    @abstractmethod
    def calculer_prime_assurance(self):
        pass
