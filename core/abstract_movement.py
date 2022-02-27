from abc import ABCMeta, abstractmethod


class AbstractMovement(metaclass=ABCMeta):

    def __init__(self, artefact, speed, final):
        self.final = final
        self.speed = speed
        self.artefact = artefact

    @abstractmethod
    def move(self):
        pass
