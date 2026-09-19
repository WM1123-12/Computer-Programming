# William Meares
# Computer Programming
# Period 4
# 9/18/2026

flight_log = [600, 950, 1300, 1520, 1700, 1800, 1880, 1950]
print(f"Initial logs: {flight_log}")
flight_log.append(2050)
print(f"Logs after fist new measurment: {flight_log}")
flight_log.append(2120)
print(f"Logs after second new measurment{flight_log}")
flight_log.pop(0)
print(f"Logs after first data removal: {flight_log}")
flight_log.pop(0)
print(f"Logs after second data removal: {flight_log}")
flight_log.insert(1, 1400)
print(f"Resulting flight log: {flight_log}")
