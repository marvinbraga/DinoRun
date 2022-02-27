from core.scene import Scene


class Game(Scene):

    def __init__(self):
        super().__init__()
        self.is_finished = False
