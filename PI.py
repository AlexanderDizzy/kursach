class PI:
    def __init__(self):
        self.Error1 = 0
        self.Up2 = 0
        self.Up = 0
        self.Ui2 = 0
        self.Ui = 0
        self.Ui20 = 0
        self.Ui0 = 0
        self.Out1 = 0

        self.Kp1 = 4
        self.Ki1 = 2.65

    def run(self, h1, x1, X):
        self.Error1 = X - x1
        self.Up = self.Kp1 * self.Error1
        self.Ui = self.Ui0 + self.Ki1 * h1 * self.Error1

        #охроничение
        if self.Ui > 20:
            self.Ui = 20
            self.Ui0 = self.Ui
        elif self.Ui < -20:
            self.Ui = -20
            self.Ui0 = self.Ui
        self.Ui0 = self.Ui

        self.Out1 = self.Up + self.Ui
        return self.Out1