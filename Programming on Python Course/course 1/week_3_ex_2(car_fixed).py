import os.path
import csv


class CarBase:

    """
    базовый класс для транспортных средств
    """

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self.validate_input(brand)
        self.photo_file_name = self.validate_input(photo_file_name)
        try:
            self.carrying = float(self.validate_input(carrying))
        except ValueError:
            print('ValueError')

    def validate_input(self, value):

        """
        метод валидации данных, возвращает значение, если оно валидно,
        иначе выбрасывает исключение ValueError
        """

        if value == '':
            raise ValueError
        return value

    def get_photo_file_ext(self):
        ext_dict = ['.jpg', '.jpeg', '.png', '.gif']
        ext = str(os.path.splitext(self.photo_file_name)[1])
        self.validate_input(ext)
        if ext in ext_dict:
            return ext
        else:
            raise ValueError


class Car(CarBase):

    """
    класс описывающий автомобили для перевозок людей
    """

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(self.validate_input(passenger_seats_count))



class Truck(CarBase):

    """
    класс описывающий автомобили для перевозок грузов
    """

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = self.validate_input(body_whl)
        self.body_length, self.body_width, self.body_height = self.parse_whl(body_whl)

    def parse_whl(self, body_whl):
        """возвращает реальные размеры кузова length, width, height"""
        try:
            length, width, height = (float(c) for c in body_whl.split('x', 2))
        except Exception:
            length, width, height = 0.0, 0.0, 0.0

        return length, width, height


    def get_body_volume(self):
        """возвращает объем кузова"""
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):

    """
    класс описывающий спецтехнику
    """

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = self.validate_input(extra)  # дополнительное описание машины


def get_car_list(csv_filename):

    """возвращает список объектов, сохраненных в файле csv_filename"""

    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            #print(row)
            car = None
            if len(row) != 7:
                continue
            #print(row)

            elif row[0] == Car.car_type:
                car = Car(row[1], row[3], row[5], row[2])
                car_list.append(car)
            elif row[0] == Truck.car_type:
                car = Truck(row[1], row[3], row[5], row[4])
                car_list.append(car)
            elif row[0] == SpecMachine.car_type:
                car = SpecMachine(row[1], row[3], row[5], row[6])
                car_list.append(car)


            #car_list.append(car)

            print(car_list)

        return car_list

csv_ = '/Users/elizabethlorelei/Documents/Programming/Test/Python3/rus_cources/coursera_week3_cars.csv'

get_car_list(csv_)


#print(str(os.path.splitext('f30.jpeg.txt')))
