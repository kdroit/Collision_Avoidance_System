import math
import random
from Car import Car
import Object

MILES_TO_KILO = 1.609344
FEET_TO_PIXELS = 10
DECELERATION_RATE = 6.096  # meters per second^2
ACCELERATION_RATE = 3  # meters per second^2
METER_FOOT_CONVERSION = 0.3048
MAX_SPEED_LIMIT = 55


_speed_limit = 25
_running = False
_resumeable = True
_traction_coefficient = 0.3

_road = {
    "Forward Center": None,
    "Sim Car": None,
    "Left Parallel": None,
    "Left Aft": None,
    "Right Parallel": None,
    "Right Aft": None
}


# Action Class
class Action:
    _time_req = 0
    _adjustments = {"target speed": 0, "steering angle": 0}

    def __init__(self, time_req, target_speed=0, angle=0):
        self._time_req = time_req
        self._adjustments.update({"target speed": target_speed})
        self._adjustments.update({"steering angle": angle})

    def get_time_req(self):
        return self._time_req

    def get_adjustments(self):
        return self._adjustments

# End Action Class


# Conversion functions
def mph_to_meters_per_second(current_velocity):
    return current_velocity * 0.44704

def mph_to_kph(current_velocity):
    return MILES_TO_KILO * current_velocity

def meters_to_feet(meters):
    return meters / METER_FOOT_CONVERSION


def feet_to_meters(feet):
    return feet * METER_FOOT_CONVERSION


def calculate_action(velocity, scaler, distance, target_lane):
    target_speed = velocity * scaler
    lane_change_time = time_to_change_lane(target_speed, distance)
    lane_change_distance = distance_to_change(target_speed, lane_change_time)
    time_req = lane_change_time + time_to_change_speed(velocity, target_speed)
    target_steering_angle = steering_angle(target_lane, lane_change_distance)
    return Action(time_req, target_speed, target_steering_angle)


# Distance and Lane change Calculations
def minimum_breaking_distance(current_velocity):
    # The AASHTO formula for minimum breaking distance is in metric
    # d = (0.278 * reaction_time * velocity) + (velocity**2/(254 *(friction_coefficient + slope)))
    # velocity = mph_to_meters_per_second(current_velocity)
    velocity = mph_to_kph(current_velocity)
    meters = (0.278 * 1 * velocity) + (pow(velocity, 2) / (254 * 0.3))
    return meters_to_feet(meters)

def distance_to_change(speed, time_constraint):
    return speed * time_constraint


def steering_angle(target_lane, forward_travel):
    lane_distance = 12
    if target_lane == "left":
        lane_distance *= -1
    radian_change = math.atan2(lane_distance, forward_travel)
    return math.degrees(radian_change)


# Velocity Calculations
def delta_speed(object_speed, vehicle_speed):
    return object_speed - vehicle_speed


def calculate_speed_scaler(horizontal_position):
    scaler = 1
    if horizontal_position < 120:
        # The right lane drives faster, 110% of speed limit
        scaler = 1.1
    if horizontal_position > 240:
        # The left lane drives slower, 90% of speed limit
        scaler = .9
    return scaler


# Time Calculations
def time_to_change_lane(speed, delta_distance):
    max_time = 4
    mps = mph_to_meters_per_second(speed)
    collision_time = delta_distance / meters_to_feet(mps)
    return min(max_time, collision_time)


def time_to_change_speed(current_velocity, target_speed):
    current_metric = mph_to_meters_per_second(current_velocity)
    target_metric = mph_to_meters_per_second(target_speed)
    delta_speed = target_metric - current_metric
    if delta_speed > 0:
        rate = ACCELERATION_RATE
    else:
        rate = DECELERATION_RATE
    return delta_speed / rate


# Display Calculations
def calculate_vertical_pixel_change(delta_time, car_speed, obj_speed):
    car_speed = mph_to_meters_per_second(car_speed)
    obj_speed = mph_to_meters_per_second(obj_speed)
    fixed_pixel_shift = meters_to_feet(car_speed) * FEET_TO_PIXELS * delta_time
    obj_pix_speed = meters_to_feet(obj_speed) * FEET_TO_PIXELS * delta_time
    delta_pixel = obj_pix_speed - fixed_pixel_shift
    return delta_pixel


def horizontal_shift_calculation(delta_time, total_time):
    return (delta_time * 120) / total_time


# Update Speed
def set_speed_limit(speed):
    if speed < 0:
        print("Speed limit must be positive")
    if speed > MAX_SPEED_LIMIT:
        print(f"The max Speed Limit is {MAX_SPEED_LIMIT}")
    _speed_limit = speed
    update_traffic_speed()


def get_speed_limit():
    return _speed_limit


def update_traffic_speed():
    for key, value in _road:
        if isinstance(value, Car):
            value.set_speed(_speed_limit)


# Add Cars and Objects
def add_sim_car():
    _road.update({"Center Lane": Car(_speed_limit)})


def add_car(position):
    sim_car = _road.get("Sim Car")
    if ('Right' in position):
        horizontal_position = round(sim_car.x()) + 120
    if ('Left' in position):
        horizontal_position = round(sim_car.x()) - 120
    if ('Aft' in position):
        vertical_position = round(sim_car.y()) + 200
    else:
        vertical_position = round(sim_car.y())
    
    new_car = Car(_speed_limit, horizontal_position, vertical_position, sim_car)
    _road.update({position: new_car})

    return new_car



def add_object():
    sim_car = _road.get("Center Lane")
    horizontal_position = 0
    vertical_position = sim_car.get_minimum_stopping_distance() * 10
    velocity = random.randint(0, MAX_SPEED_LIMIT)
    obj = Object(horizontal_position, vertical_position, velocity, sim_car)
    #self._road.update({"Forward Center": obj})
    #if (self._running):
    #    obj.start()


# Simulation Controls
def pause():
    for key, value in _road:
        if value is not None:
            value.pause()


def stop():
    pause()
    _resumeable = False


def resume():
    if _resumeable:
        for key, value in _road:
            if value is not None:
                value.resume()


def reset():
    for key, value in _road:
        _road.update({key: None})
        if key == "Center Lane":
            add_sim_car()
    _resumeable = True


def start():
    _running = True
    for key, value in _road:
        if value is not None:
            value.start()


def get_location_data():
    return _road