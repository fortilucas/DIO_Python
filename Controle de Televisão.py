class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada=False
        else:
            self.ligada=True

    def aumenta_canal(selfs):
        self.canal += 1

    def diminui_canal(selfs):
        self.canal -= 1




televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)