import codecs
import os
import shutil
class Car(object):

    def __init__(self, num, name, year, fuel, volume, power, transmission, drive, wheel, color, run, lights, doors):
        self.num = num
        self.name = name
        self.year = year
        self.fuel = fuel
        self.volume = volume
        self.power = power
        self.transmission = transmission
        self.drive = drive
        self.wheel = wheel
        self.color = color
        self.run = run
        self.lights = lights
        self.doors = doors

    def show(self,p_type):
        if p_type == 'Название':
            print(self.name)
        elif p_type == 'Год выпуска':
            print(self.year)
        elif p_type == 'Тип используемого топлива':
            print(self.fuel)
        elif p_type == 'Объём двигателя':
            print(self.volume)
        elif p_type == 'Мощность двигателя':
            print(self.power)
        elif p_type == 'Тип коробки передач':
            print(self.transmission)
        elif p_type == 'Тип привода':
            print(self.drive)
        elif p_type == 'Расположение руля':
            print(self.wheel)
        elif p_type == 'Цвет':
            print(self.color)
        elif p_type == 'Пробег':
            print(self.run)
        elif p_type == 'Состояние фар':
            print(self.lights)
        elif p_type == 'Состояние дверей':
            print(self.doors)

    def change(self,p_type,text):
        with codecs.open('cars\car'+str(self.num)+'.txt', encoding = 'utf-8') as car_file:
            params_arr = list(car_file.readlines())
        params_arr_edited = []
        for word in params_arr:
            if '\r\n' in word:
                word = word.replace('\r\n','',1)
            if '\n' in word:
                word = word.replace('\n','',1)
            params_arr_edited.append(word)
        if p_type == 'Название':
            if len(text) > 50:
                return 'Название слишком длинное'
            if car_search(text) != None:
                return 'Машина с таким названием уже существует, введите другое название'
            if text == 'Выйти':
                return 'Название машины не может быть "Выйти"'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(params_arr_edited[11])
                self.name = text
        elif p_type == 'Год выпуска':
            if int(text) > 2022 or int(text) < 1800:
                return 'Год указан некорректно'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(params_arr_edited[11])
                self.year = text
        elif p_type == 'Тип используемого топлива':
            energy_source_array = ['Бензин','Дизель','Газ','Электричество','Гибрид','Водород']
            if not text in energy_source_array:
                return 'Неверно указан тип топлива. Доступные типы: "Бензин", "Дизель", "Газ", "Электричество", "Гибрид", "Водород"'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(params_arr_edited[11])
                self.fuel = text
        elif p_type == 'Объём двигателя':
            if not is_number(text):
                return 'Объём двигателя должен быть числом'
            elif is_number(text):
                if float(text) <= 0:
                    return 'Объём двигателя не может быть нулём или отрицательным числом'
                else:
                    params_arr_to_write = []
                    params_arr_to_write.append(params_arr_edited[0])
                    params_arr_to_write.append(params_arr_edited[1])
                    params_arr_to_write.append(params_arr_edited[2])
                    params_arr_to_write.append(text)
                    params_arr_to_write.append(params_arr_edited[4])
                    params_arr_to_write.append(params_arr_edited[5])
                    params_arr_to_write.append(params_arr_edited[6])
                    params_arr_to_write.append(params_arr_edited[7])
                    params_arr_to_write.append(params_arr_edited[8])
                    params_arr_to_write.append(params_arr_edited[9])
                    params_arr_to_write.append(params_arr_edited[10])
                    params_arr_to_write.append(params_arr_edited[11])
                    self.volume = text
        elif p_type == 'Мощность двигателя':
            if not text.isdigit():
                return 'Мощность двигателя должна быть числом'
            elif text.isdigit():
                if int(text) <= 0:
                    return 'Мощность двигателя не может быть нулём или отрицательным числом'
                else:
                    params_arr_to_write = []
                    params_arr_to_write.append(params_arr_edited[0])
                    params_arr_to_write.append(params_arr_edited[1])
                    params_arr_to_write.append(params_arr_edited[2])
                    params_arr_to_write.append(params_arr_edited[3])
                    params_arr_to_write.append(text)
                    params_arr_to_write.append(params_arr_edited[5])
                    params_arr_to_write.append(params_arr_edited[6])
                    params_arr_to_write.append(params_arr_edited[7])
                    params_arr_to_write.append(params_arr_edited[8])
                    params_arr_to_write.append(params_arr_edited[9])
                    params_arr_to_write.append(params_arr_edited[10])
                    params_arr_to_write.append(params_arr_edited[11])
                    self.power = text
        elif p_type == 'Тип коробки передач':
            transmission_array = ['Механика','Автомат','Вариатор','Робот']
            if not text in transmission_array:
                return 'Неверно указан тип коробки передач. Доступные типы: "Механика", "Автомат", "Вариатор", "Робот"'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(params_arr_edited[11])
                self.transmission = text
        elif p_type == 'Тип привода':
            drive_array = ['Передний','Задний','Полный']
            if not text in drive_array:
                return 'Неверно указан тип привода. Доступные типы: "Передний", "Задний", "Полный"'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(params_arr_edited[11])
                self.drive = text
        elif p_type == 'Расположение руля':
            wheel_array = ['Правый','Левый']
            if not text in wheel_array:
                return 'Неверно указано расположение руля. Доступные типы: "Правый", "Левый"'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(params_arr_edited[11])
                self.wheel = text
        elif p_type == 'Цвет':
            if not text.isalpha():
                return 'Цвет не может быть числом'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(params_arr_edited[11])
                self.color = text
        elif p_type == 'Пробег':
            if not text.isdigit():
                return 'Пробег должен быть числом'
            elif text.isdigit():
                if int(text) < 0:
                    return 'Пробег не должен быть отрицательным'
                else:
                    params_arr_to_write = []
                    params_arr_to_write.append(params_arr_edited[0])
                    params_arr_to_write.append(params_arr_edited[1])
                    params_arr_to_write.append(params_arr_edited[2])
                    params_arr_to_write.append(params_arr_edited[3])
                    params_arr_to_write.append(params_arr_edited[4])
                    params_arr_to_write.append(params_arr_edited[5])
                    params_arr_to_write.append(params_arr_edited[6])
                    params_arr_to_write.append(params_arr_edited[7])
                    params_arr_to_write.append(params_arr_edited[8])
                    params_arr_to_write.append(text)
                    params_arr_to_write.append(params_arr_edited[10])
                    params_arr_to_write.append(params_arr_edited[11])
                    self.run = text
        elif p_type == 'Состояние фар':
            lights_array = ['Включены','Выключены']
            if not text in lights_array:
                return 'Неверно указано состояние фар. Доступные состояния: "Включены", "Выключены"'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(text)
                params_arr_to_write.append(params_arr_edited[11])
                self.lights = text
        elif p_type == 'Состояние дверей':
            doors_array = ['Открыты','Закрыты']
            if not text in doors_array:
                return 'Неверно указано состояние дверей. Доступные состояния: "Открыты", "Закрыты"'
            else:
                params_arr_to_write = []
                params_arr_to_write.append(params_arr_edited[0])
                params_arr_to_write.append(params_arr_edited[1])
                params_arr_to_write.append(params_arr_edited[2])
                params_arr_to_write.append(params_arr_edited[3])
                params_arr_to_write.append(params_arr_edited[4])
                params_arr_to_write.append(params_arr_edited[5])
                params_arr_to_write.append(params_arr_edited[6])
                params_arr_to_write.append(params_arr_edited[7])
                params_arr_to_write.append(params_arr_edited[8])
                params_arr_to_write.append(params_arr_edited[9])
                params_arr_to_write.append(params_arr_edited[10])
                params_arr_to_write.append(text)
                self.doors = text
        try:
            with codecs.open('cars\car'+str(self.num)+'.txt', 'w+', encoding = 'utf-8') as car_file:
                for line in params_arr_to_write:
                    car_file.write(line + '\n')
            return 'Параметр изменён'
        except:
            pass

    def param_delete(self,p_type):
        with codecs.open('cars\car'+str(self.num)+'.txt', encoding = 'utf-8') as car_file:
            params_arr = list(car_file.readlines())
        params_arr_edited = []
        for word in params_arr:
            if '\r\n' in word:
                word = word.replace('\r\n','',1)
            if '\n' in word:
                word = word.replace('\n','',1)
            params_arr_edited.append(word)
        if p_type == 'Название':
            return 'Название машины нельзя удалить'
        elif p_type == 'Год выпуска':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.year = 'None'
        elif p_type == 'Тип используемого топлива':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.fuel = 'None'
        elif p_type == 'Объём двигателя':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.volume = 'None'
        elif p_type == 'Мощность двигателя':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.power = 'None'
        elif p_type == 'Тип коробки передач':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.transmission = 'None'
        elif p_type == 'Тип привода':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.drive = 'None'
        elif p_type == 'Расположение руля':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.wheel = 'None'
        elif p_type == 'Цвет':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.color = 'None'
        elif p_type == 'Пробег':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append(params_arr_edited[11])
            self.run = 'None'
        elif p_type == 'Состояние фар':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append('None')
            params_arr_to_write.append(params_arr_edited[11])
            self.lights = 'None'
        elif p_type == 'Состояние дверей':
            params_arr_to_write = []
            params_arr_to_write.append(params_arr_edited[0])
            params_arr_to_write.append(params_arr_edited[1])
            params_arr_to_write.append(params_arr_edited[2])
            params_arr_to_write.append(params_arr_edited[3])
            params_arr_to_write.append(params_arr_edited[4])
            params_arr_to_write.append(params_arr_edited[5])
            params_arr_to_write.append(params_arr_edited[6])
            params_arr_to_write.append(params_arr_edited[7])
            params_arr_to_write.append(params_arr_edited[8])
            params_arr_to_write.append(params_arr_edited[9])
            params_arr_to_write.append(params_arr_edited[10])
            params_arr_to_write.append('None')
            self.doors = 'None'
        try:
            with codecs.open('cars\car'+str(self.num)+'.txt', 'w+', encoding = 'utf-8') as car_file:
                for line in params_arr_to_write:
                    car_file.write(line + '\n')
            return 'Параметр удалён'
        except:
            pass

def car_add(name):
    global car_count
    lines = [name, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
    new_car_file = codecs.open('cars\car'+str(car_count)+'.txt','w+',encoding = 'utf-8')
    for line in lines:
        new_car_file.write(line + '\n')
    new_car_file.close()
    print('Создана новая машина')
    car_count += 1

def delete(num):
    os.remove('cars\car'+str(num)+'.txt')

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def chosen_car_debug():
    global chosen_car
    chosen_car = car.name

def params_check(name):
    params_array = ['Название','Год выпуска','Тип используемого топлива','Объём двигателя','Мощность двигателя','Тип коробки передач','Тип привода','Расположение руля','Цвет','Пробег','Состояние фар','Состояние дверей']
    if name in params_array:
        return name
    else:
        return False

def car_search(name):
    global chosen_car
    car_number = 0
    while True:
        try:
            with codecs.open('cars\car'+str(car_number)+'.txt', encoding = 'utf-8') as f:
                text = list(f.readlines())
            text1 = []
            for word in text:
                if '\r\n' in word:
                    word = word.replace('\r\n','',1)
                if '\n' in word:
                    word = word.replace('\n','',1)
                text1.append(word)
            if name == text1[0]:
                chosen_car = name
                return car_number
                break
        except FileNotFoundError:
            break
            print('Машины с таким названием не существует')
        car_number += 1

def create(num):
    global car
    with codecs.open('cars\car'+str(num)+'.txt', encoding = 'utf-8') as f:
        text = list(f.readlines())
    text1 = []
    for word in text:
        if '\r\n' in word:
            word = word.replace('\r\n','',1)
        if '\n' in word:
            word = word.replace('\n','',1)
        text1.append(word)
    name = text1[0]
    year = text1[1]
    fuel = text1[2]
    volume = text1[3]
    power = text1[4]
    transmission = text1[5]
    drive = text1[6]
    wheel = text1[7]
    color = text1[8]
    run = text1[9]
    lights = text1[10]
    doors = text1[11]
    car = Car(num, name, year, fuel, volume, power, transmission, drive, wheel, color, run, lights, doors)

running = True
car_count = 0
car_num = None
chosen_car = None

def delete_all_cars():
    shutil.rmtree('cars', ignore_errors = True)
    os.mkdir('cars')
while True:
    try:
        f = open('cars\car'+str(car_count)+'.txt')
        car_count += 1
        f.close()
    except FileNotFoundError:
        break
while running:
    if car_count == 0:
        print('Для начала работы необходимо создать новую машину')
        print('Введите название первой машины или введите "Выйти" для выхода из программы')
        message = input()
        while len(message) > 50 and not message == 'Выйти':
            print('Длина названия не может быть больше 50 символов')
            message = input()
        if not message == 'Выйти':
            car_add(message)
        if message == 'Выйти':
            running = False
    else:
        if car_num == None:
            print('Количество машин:',str(car_count)+',','введите название машины, чтобы изменить её параметры')
            print('Если вы хотите создать новую машину, введите команду "Создать" и нажмите Enter, затем введите название новой машины')
            print('Если вы хотите выйти из программы, введите "Выйти"')
            print('Если вы хотите удалить все машины, введите "Удалить все машины"')
            message = input()
            if message == 'Создать':
                print('Введите название для новой машины')
                message = input()
                while message == 'Создать':
                    print('Недопустимое название машины. Введите другое название')
                    message = input()
                existing_car_number = None
                existing_car_number = car_search(message)
                while not existing_car_number == None:
                    print('Машина с таким названием уже существует, введите другое название')
                    message = input()
                    existing_car_number = car_search(message)
                car_add(message)
            elif message == 'Выйти':
                running = False
            elif message == 'Удалить все машины':
                delete_all_cars()
                print('Все машины удалены')
                car_count = 0

            else:
                car_num = car_search(message)
                while car_num == None:
                    print('Машина с таким названием не найдена, введите другое название машины')
                    message = input()
                    while message == 'Создать':
                        print('Недопустимое название машины. Введите другое название')
                        message = input()
                    car_num = car_search(message)
        if car_num != None:
            try:
                del car
            except:
                pass
            create(car_num)
            chosen_car_debug()
            print('Выбрана машина под номером:',str(car_num)+',','название:',chosen_car)
            print('Если вы хотите выйти из режима редактирования параметров машины, введите "Выйти"')
            print('Если вы хотите удалить эту машину, введите "Удалить"')
            print('Чтобы просмотреть или изменить параметры машины, введите название параметра')
            print('Параметры для просмотра или изменения: Название, Год выпуска, Тип используемого топлива, Объём двигателя, Мощность двигателя, Тип коробки передач, Тип привода, Расположение руля, Цвет, Пробег, Состояние фар, Состояние дверей')
            message = input()
            if message == 'Выйти':
                print('Вы вышли из режима редактирования параметров')
                car_num = None
            elif message == 'Удалить':
                delete(car_num)
                car_count -= 1
                car_num = None
                chosen_car = None
                i = 0
                search_errors = 0
                folder = []
                while True:
                    try:
                        f = codecs.open('cars\car'+str(i)+'.txt', 'r', encoding = 'utf-8')
                        f.close()
                        fname = 'car'+str(i)+'.txt'
                        folder.append(fname)
                    except:
                        search_errors += 1
                    i += 1
                    if search_errors >= 3:
                        break
                for i in range(0, len(folder)):
                    try:
                        os.rename('cars\\'+folder[i], 'cars\car'+str(i)+'.txt')
                    except:
                        pass
                print('Машина удалена')
            else:
                print('Вы вошли в режим редактирования параметров, чтобы выйти из него, введите "Выйти"')
                params_exit = False
                while not params_exit:
                    params_function_result = params_check(message)
                    while not bool(params_function_result):
                        print('Такого параметра не существует, введите другой')
                        message = input()
                        if message != 'Выйти':
                            params_function_result = params_check(message)
                        else:
                            params_exit = True
                            print('Вы вышли из режима редактирования параметров')
                    if not params_exit:
                        print('Выбран параметр:',str(message)+',','введите "Просмотр", чтобы просмотреть значение параметра, "Замена", чтобы изменить параметр или "Удалить", чтобы удалить параметр')
                        print('Если вы хотите выбрать другой параметр, введите "Выбор другого параметра", если хотите выйти из режима редактирования параметров, введите "Выйти"')
                        message = input()
                        while not (message == 'Просмотр' or message == 'Замена' or message == 'Выбор другого параметра' or message == 'Удалить' or message == 'Выйти'):
                            print('Команда указана некорректно. Необходимо ввести "Просмотр", "Замена", "Удалить", "Выбор другого параметра" или "Выйти"')
                            message = input()
                        if message == 'Просмотр':
                            car.show(params_function_result)
                            print('Если вы хотите поменять этот параметр, введите "Замена", если хотите удалить, введите "Удалить", если хотите выбрать другой параметр, введите "Выбор другого параметра", если хотите выйти, введите "Выйти"')
                            message = input()
                            while not (message == 'Замена' or message == 'Удалить' or message == 'Выбор другого параметра' or message == 'Выйти'):
                                print('Команда указана некорректно. Необходимо ввести "Замена", "Удалить", "Выбор другого параметра" или "Выйти"')
                                message = input()
                            if message == 'Выйти':
                                params_exit = True
                                print('Вы вышли из режима редактирования параметров')
                            else:
                                if message == 'Замена':
                                    print('Введите новое значение')
                                    message = input()
                                    while not params_exit and params_function_result == 'Год выпуска' and not message.isdigit():
                                        print('Год выпуска может быть только числом')
                                        message = input()
                                        if message == 'Выйти':
                                            params_exit = True
                                            print('Вы вышли из режима редактирования параметров')
                                    if not message == 'Выйти':
                                        output = car.change(params_function_result,message)
                                        if output == 'Параметр изменён':
                                            print(output)
                                    while not output == 'Параметр изменён' and not params_exit:
                                        if message == 'Выйти':
                                            params_exit = True
                                            print('Вы вышли из режима редактирования параметров')
                                        elif not message == 'Выйти' and not params_exit:
                                            output = car.change(params_function_result,message)
                                            if output == 'Параметр изменён':
                                                print(output)
                                                params_exit = True
                                            else:
                                                print(output)
                                                print('Попробуйте ещё раз или введите "Выйти", чтобы покинуть режим изменения этого параметра')
                                                message = input()
                                        chosen_car_debug()
                                    params_exit = True
                                if message == 'Выбор другого параметра':
                                    print('Введите название другого параметра')
                                    message = input()
                                if message == 'Удалить':
                                    print(car.param_delete(params_function_result))
                                    params_exit = True
                        elif message == 'Замена':
                            print('Введите новое значение')
                            message = input()
                            while not params_exit and params_function_result == 'Год выпуска' and not message.isdigit():
                                print('Год выпуска может быть только числом')
                                message = input()
                                if message == 'Выйти':
                                    params_exit = True
                                    print('Вы вышли из режима редактирования параметров')
                            if not message == 'Выйти':
                                output = car.change(params_function_result,message)
                                if output == 'Параметр изменён':
                                    print(output)
                            while not output == 'Параметр изменён' and not params_exit:
                                if message == 'Выйти':
                                    params_exit = True
                                    print('Вы вышли из режима редактирования параметров')
                                elif not message == 'Выйти' and not params_exit:
                                    output = car.change(params_function_result,message)
                                    if output == 'Параметр изменён':
                                        print(output)
                                        params_exit = True
                                    else:
                                        print(output)
                                        print('Попробуйте ещё раз или введите "Выйти", чтобы покинуть режим изменения этого параметра')
                                        message = input()
                                chosen_car_debug()
                            params_exit = True
                            if message == 'Выбор другого параметра':
                                print('Введите название другого параметра')
                                message = input()
                            if message == 'Удалить':
                                print(car.param_delete(params_function_result))
                                params_exit = True
                        elif message == 'Удалить':
                            print(car.param_delete(params_function_result))
                            params_exit = True
                        elif message == 'Выбор другого параметра':
                            print('Введите название другого параметра')
                            message = input()
                        elif message == 'Выйти':
                            params_exit = True
                            print('Вы вышли из режима редактирования параметров')
