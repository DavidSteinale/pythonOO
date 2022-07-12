import datetime

class Data:
    def datanow(self):
        self.agora = datetime.date.today()
        print('Data atual:', self.agora.strftime(" %d/%m/%Y "))