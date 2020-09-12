import os
import csv


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError:
            print('ValueError')

    def get_photo_file_ext(self):
        ext_dict = ['.jpg', '.jpeg', '.png', '.gif']
        ext = str(os.path.splitext(self.photo_file_name)[1])
        if ext in ext_dict:
            return ext
        else:
            print('Wrong Extension')


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            print('Value Error')


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

        try:
            length, width, height = (float(c) for c in body_whl.split('x'))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra  # дополнительное описание машины


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            #print(row)
            car = None
            ext_dict = ['.jpg', '.jpeg', '.png', '.gif']
            if len(row) != 7:
                continue
            #print(row)
            elif str(os.path.splitext(row[3])[1]) == '':
                continue
            elif str(os.path.splitext(row[3])[1]) not in ext_dict:
                continue
            elif row[0] == '' or row[1] == '' or row[3] == '' or row[5] == '':
                continue
            elif row[0] == Car.car_type:
                if row[2] == '':
                    continue
                car = Car(row[1], row[3], row[5], row[2])
                car_list.append(car)
            elif row[0] == Truck.car_type:
                car = Truck(row[1], row[3], row[5], row[4])
                car_list.append(car)
            elif row[0] == SpecMachine.car_type:
                if row[6] == '':
                    continue
                car = SpecMachine(row[1], row[3], row[5], row[6])
                car_list.append(car)


            #car_list.append(car)

            print(car_list)

        return car_list

#csv_ = '/Users/elizabethlorelei/Documents/Programming/Test/Python3/rus_cources/coursera_week3_cars.csv'

#get_car_list(csv_)


#print(str(os.path.splitext('f30.jpeg.txt')))
