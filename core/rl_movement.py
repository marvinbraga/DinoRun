from core.abstract_movement import AbstractMovement


class MovementRight2Left(AbstractMovement):

    def move(self):
        self.artefact.rect[0] -= self.speed
        if self.artefact.rect[0] <= self.final:
            self.artefact.kill()
