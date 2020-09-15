import time as t


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                t.sleep(7)
            elif i == 1:
                t.sleep(2)
            elif i == 2:
                t.sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
