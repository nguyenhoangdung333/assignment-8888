class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Invalid floor.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        print(f"\n--- Operating Elevator {elevator_number} ---")
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n--- FIRE ALARM! Returning all elevators to bottom floor ---")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i}:")
            elevator.go_to_floor(self.bottom_floor)


# Main program for Elevator/Building
plaza = Building(1, 10, 3)
plaza.run_elevator(0, 5)
plaza.run_elevator(1, 8)
plaza.fire_alarm()


import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = max(0, min(self.max_speed, self.current_speed + change))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\nStatus for {self.name}:")
        print(f"{'Reg No.':<10} | {'Max Spd':<8} | {'Cur Spd':<8} | {'Distance':<10}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.max_speed:<8} | "
                  f"{car.current_speed:<8} | {car.travelled_distance:<10}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


# Main program for the Race
cars_list = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
derby = Race("Grand Demolition Derby", 8000, cars_list)

hours_elapsed = 0
while not derby.race_finished():
    derby.hour_passes()
    hours_elapsed += 1
    
    # Print status every 10 hours
    if hours_elapsed % 10 == 0:
        print(f"\n--- Hour {hours_elapsed} ---")
        derby.print_status()

# Final result
print(f"\n--- Final Result (Total hours: {hours_elapsed}) ---")
derby.print_status()