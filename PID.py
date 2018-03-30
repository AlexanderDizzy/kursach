class PID:
    def __init__(self):
        self.Error1 = 0
        self.Error_prew = 0
        self.Ud = 0
        self.Up = 0
        self.Ui = 0
        self.Ui0 = 0
        self.Out1 = 0

        self.Kp1 = 4
        self.Ki1 = 2.65
        self.Kd = 0.1

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

        self.Ud = self.Kd*(self.Error1-self.Error_prew)/h1
        self.Out1 = self.Up + self.Ui + self.Ud
        self.Error_prew = self.Error1
        self.Ui0 = self.Ui

        return self.Out1