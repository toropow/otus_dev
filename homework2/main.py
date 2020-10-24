from homework2.water_transport import Yacht
from homework2.railways_transport import Locomotive

if __name__ == '__main__':
    yacht = Yacht('John', 30, 10, 5000, False, True)
    print(yacht)
    loco = Locomotive(name="Tommy", age=25, experience=2, salary=10000, personal_car=False, fuel_level=10)
    print(loco)

#Example work
# This is Yacht
# Color: White
# Weight: 1000
# Consumption per 100 km: 100
# Type of engine: diesel
# Capitan name: John
# Capitan age:  30
# Capitan experience 10,
# Capitan star career at: 20
#
#
# This is Locomotive
# Color: Green
# Weight: 2000
# Consumption per 100 km: 300
# Capacity of tank: 20000
# Rain train sound: ChuhChuh... ToooTooo
# Train manager name: Tommy
# Train manager age:  25
# Train manager experience 2,
# Train manager star career at: 23
