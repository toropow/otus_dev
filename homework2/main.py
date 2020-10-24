from homework2.water_transport import Yacht
from homework2.railways_transport import Locomotive

if __name__ == '__main__':
    yacht = Yacht('John', 30, 10, 5000, False, True)
    print(yacht)
    loco = Locomotive(name="Tommy", age=25, experience=2, salary=10000, personal_car=False, fuel_level=10)
    print(loco)
