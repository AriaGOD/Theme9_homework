import re


def validate_vehicle_number(number: str):
    pattern = r'^[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}$'

    if re.match(pattern, number):
        vehicle_number = number[:6]
        region = number[6:]

        return vehicle_number, region
    else:
        return None


# Input from user
vehicle_number = input("Введите номер транспортного средства: ")

# Validate the number
result = validate_vehicle_number(vehicle_number)

if result:
    print(f"Номер валиден: {result[0]}, Регион: {result[1]}")
else:
    print("Номер не валиден")
