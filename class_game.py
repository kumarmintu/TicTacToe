import numpy as np
class Game:
    def __init__(self, size , win_number , mode):
        self.size = size
        self.win_number = win_number
        self.mode = mode
        self.result = -1
        self.now = 0
        self.field = np.zeros(shape=(size,size))
    def print_field(self):
        for i in range(self.field.shape[0]):
            for j in range(self.field.shape[0]):
                if(self.field[i , j] == 0):
                    print('.' , end = '')
                if(self.field[i , j] == 1):
                    print('o' , end = '')
                if(self.field[i , j] == 2):
                    print('x' , end = '')
            print()
    def check_win(self):
        size_field = self.field.shape[0]
        for i in range(0 , size_field - self.win_number + 1):
            for j in range(0 , size_field - self.win_number + 1):
                part_field = self.field[i:i+self.win_number,j:j+self.win_number] #отрезаем часть поля k * k от исходного поля 
                for line in range(self.win_number):
                    if(part_field[part_field[line] == 1].shape[0] == self.win_number):#проверка строк на победу ноликов
                        return 1 #победа ноликов
                    if(part_field[part_field[line] == 2].shape[0] == self.win_number):#проверка строк на победу крестиков
                        return 2 #победа крестиков
                    if(part_field[part_field[: , line] == 1].shape[0] == self.win_number):#проверка столбцов на победу ноликов
                        return 1
                    if(part_field[part_field[: , line] == 2].shape[0] == self.win_number):#проверка столбцов на победу крестиков
                        return 2
                if(part_field[np.diagonal(part_field) == 1].shape[0] == self.win_number):#проверка главной диагонали на победу ноликов
                    return 1
                if(part_field[:, ::-1][np.diagonal(part_field[:, ::-1]) == 1].shape[0] == self.win_number):#проверка побочной диагонали на победу ноликов
                    return 1
                if(part_field[np.diagonal(part_field) == 2].shape[0] == self.win_number):#проверка главной диагонали на победу крестиков
                    return 2
                if(part_field[:, ::-1][np.diagonal(part_field[:, ::-1]) == 2].shape[0] == self.win_number):#проверка побочной диагонали на победу крестиков
                    return 2
        if(self.field[self.field == 0].shape[0] > 0):
            return -1 #игра не закончена
        return 0 #ничья
    def move(self):
        if(self.mode == 1 or (self.mode == 2 and self.now == 0)):
            data = list(map(int , input('Введите координаты клетки: x , y; где x - номер строки, y - номер столбца (1 <= x,y <= n): ').split()))
            self.field[data[0] - 1][data[1] - 1] = self.now + 1
            self.now = (self.now + 1) % 2
        self.print_field()
        self.result = self.check_win()
        if(self.result != -1):
            return self.result
