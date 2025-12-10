from abc import *

# Class for the cost of insurance
class Assurable(ABC):
    @abstractmethod
    def calculer_prime_assurance(self):
        return 10