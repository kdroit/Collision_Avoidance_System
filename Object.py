import time
import Simulation_Logic as sl


class Object:
    _horizontal_position = 0
    _vertical_position = 0
    _current_velocity = 0
    _distance = 0
    _time_now = 0
    _simulated_car = None

    def __init__(self, horizontal_position, vertical_position, current_velocity, sim_car):
        self._horizontal_position = horizontal_position
        self._vertical_position = vertical_position
        self._current_velocity = current_velocity
        self._simulated_car = sim_car
        self.set_distance(sim_car)

    def get_current_velocity(self):
        return self._current_velocity

    def get_horizontal_position(self):
        return self._horizontal_position

    def get_vertical_position(self):
        return self._vertical_position

    def get_distance_in_ft(self):
        return self._distance * 10

    def get_time(self):
        return self._time_now

    def set_distance(self, sim_car):
        self._distance = (self._vertical_position - sim_car.get_vertical_position())

    def update_vertical_position(self):
        delta_time = time.time() - self._time_now
        car_speed = self._simulated_car.get_current_velocity()
        delta_pixel = sl.calculate_vertical_pixel_change(delta_time, car_speed, self._current_velocity)
        self._distance += delta_pixel
        self._time_now = time.time()

    def pause(self):
        self.update_vertical_position()

    def resume(self):
        self._time_now = time.time()