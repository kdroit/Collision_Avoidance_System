import time
from PyQt6.QtCore import QSequentialAnimationGroup
from PyQt6.QtWidgets import QGraphicsWidget
from PyQt6.QtGui import QColor, QPalette
import Simulation_Logic as sim_logic # should use meaningful names


FORWARD_SENSOR = "Forward Sensor"
LEFT_PARALLEL = "Left Parallel"
RIGHT_PARALLEL = "Right Parallel"
LEFT_AFT = "Left Aft"
RIGHT_AFT = "Right Aft"


class Car(QGraphicsWidget):

    _sensors = {
        FORWARD_SENSOR: None,
        LEFT_PARALLEL: None,
        LEFT_AFT: None,
        RIGHT_PARALLEL: None,
        RIGHT_AFT: None,
    }

    _evasive_actions = {
        "stop": None,
        "accelerate left": None,
        "left": None,
        "break left": None,
        "accelerate right": None,
        "right": None,
        "break right": None
    }

    # Car constructor
    def __init__(self, speed, loc_x, loc_y, simulated_car = None):
        # Constructor for the other cars that exist
        super().__init__()
        self.loc_x = loc_x
        self.loc_y = loc_y
        if (simulated_car is not None):
            self._simulated_car = simulated_car
            self.color = "blue"
            self.setObjectName("Other Car") # sets the Object name
        else:
            self._simulated_car = True
            self.color = "#CC0000" # red
            self.setObjectName("Test Car") # sets the Object name
        self.anim_group = QSequentialAnimationGroup()
        self.width = 60
        self.length = 150
        self.resize(self.width, self.length) # set the size of the car
        self.setPos(self.loc_x, self.loc_y) # set the location of the car
        self.set_speed(speed, loc_x)
        self.setAutoFillBackground(True) # sets an important property
        # set up the color of the car
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(self.color))
        self.setPalette(palette)

    # Getters, Setters, and Updaters
    def get_current_velocity(self):
        return self._current_velocity

    def get_horizontal_position(self):
        return self._horizontal_position

    def get_vertical_position(self):
        return self._vertical_position

    def get_tire_angle(self):
        return self._tire_angle

    def get_minimum_stopping_distance(self):
        return self._minimum_stopping_distance

    def set_speed(self, speed, loc_x = None):
        scaler = sim_logic.calculate_speed_scaler(round(loc_x))
        self._target_speed = speed * scaler

    def set_sensor(self, sensor_name, object):
        self._sensors.update({sensor_name: object})
        self._determine_collision_alert(sensor_name, object)
        if self._collision_alert:
            self._evade_collision()

    def set_current_velocity(self, velocity=None):
        if velocity is None:
            self._accelerate(self._target_speed)
        elif velocity < self._current_velocity:
            self._accelerate(velocity)
        else:
            self._decelerate(velocity)

    def update_position(self):
        delta_time = time.time() - self._time_now
        self._time_now = time.time()
        self._update_vertical_position(delta_time)
        self._update_horizontal_position(delta_time)

    # Simulation Control Functions
    def pause(self):
        self.update_position()

    def resume(self):
        self._time_now = time.time()

    def start(self):
        self._time_now = time.time()

    # Pixel Change Calculations
    def _update_vertical_position(self, delta_time):
        if isinstance(self._simulated_car, Car):
            obj_speed = self._current_velocity
            car_speed = self._simulated_car.get_current_velocity()
            delta_pixel = sim_logic.calculate_vertical_pixel_change(delta_time, car_speed, obj_speed)
            self._vertical_position += delta_pixel

    def _update_horizontal_position(self, delta_time):
        horizontal_shift = self._tire_angle
        delta_time = delta_time / self._lane_change_time
        if horizontal_shift != 0:
            shift = sim_logic.horizontal_shift_calculation(delta_time, self._lane_change_time)
            if horizontal_shift < 0:
                self._horizontal_position -= shift
            else:
                self._horizontal_position += shift

    # Speed and Steering Functions
    def _accelerate(self, target_speed):
        while self._current_velocity != target_speed:
            self._current_velocity += 1

    def _decelerate(self, target_speed):
        while self._current_velocity != target_speed:
            self._current_velocity -= 1

    def _turn_left(self, target_angle):
        while self._tire_angle != target_angle:
            self._tire_angle -= 0.1

    def _turn_right(self, target_angle):
        while self._tire_angle != target_angle:
            self._tire_angle += 0.1

    # Sensor Functions
    def _determine_collision_alert(self, sensor_name, object):
        if sensor_name == FORWARD_SENSOR:
            if sim_logic.delta_speed(object.get_velocity(), self._current_velocity) < 0:
                self._collision_alert = True

    def _adjust_sensors(self):
        # Resets the sensors after a lane change
        position = self._horizontal_position
        if position < 0:
            new_fwd = self._sensors.get(RIGHT_PARALLEL)
        else:
            new_fwd = self._sensors.get(LEFT_PARALLEL)
        self._sensors.update({FORWARD_SENSOR: new_fwd})
        self._sensors.update({LEFT_AFT: None})
        self._sensors.update({RIGHT_AFT: None})
        self._sensors.update({RIGHT_PARALLEL: None})
        self._sensors.update({LEFT_PARALLEL: None})

    # Collision Avoidance Decision Functions
    def _evade_collision(self):
        while self._collision_alert:
            self._build_evasive_options()
            adjustments = self._determine_best_course_of_action()
            self._perform_action(adjustments)
            if abs(self._horizontal_position) == 120:
                self._adjust_sensors()
                self._correct_course()

    def _build_evasive_options(self):
        # Accelerate to 130% need 20 feet lead of car lane change takes max 3 seconds
        left_call = 0
        right_call = 0
        obj = self._sensors.get(FORWARD_SENSOR)
        collision_distance = obj.get_distance_in_ft()
        velocity = self._current_velocity

        # Set stop first then remove if possible
        time_to_stop = sim_logic.time_to_change_speed(velocity, 0)
        self._evasive_actions.update({"stop": sim_logic.Action(time_to_stop)})

        for key, value in self._sensors:
            if value is None:
                self._evasive_actions.update({"stop": None})
                # Do not want the car to stop on the road as much as possible
                if key == LEFT_PARALLEL:
                    left_call += 1
                    action_variables = sim_logic.calculate_action(velocity, 1.3, collision_distance, "left")
                    self._evasive_actions.update({"accelerate left": action_variables})
                elif key == LEFT_AFT:
                    left_call += 1
                    action_variables = sim_logic.calculate_action(velocity, 0.9, collision_distance, "left")
                    self._evasive_actions.update({"break left": action_variables})
                if key == RIGHT_PARALLEL:
                    right_call += 1
                    action_variables = sim_logic.calculate_action(velocity, 1.3, collision_distance, "right")
                    self._evasive_actions.update({"accelerate right": action_variables})
                elif key == RIGHT_AFT:
                    right_call += 1
                    action_variables = sim_logic.calculate_action(velocity, 0.7, collision_distance, "right")
                    self._evasive_actions.update({"break right": action_variables})

        # If nothing sits in the left or right lane
        if left_call == 2:
            action_variables = sim_logic.calculate_action(velocity, 1, collision_distance, "left")
            self._evasive_actions.update({"left": action_variables})
        if right_call == 2:
            action_variables = sim_logic.calculate_action(velocity, 1, collision_distance, "right")
            self._evasive_actions.update({"right": action_variables})

    def _determine_best_course_of_action(self):
        adjustments = None
        time = 0

        for key, value in self._evasive_actions:
            if value is not None:
                action_time = value.get_time_req()
                if (time == 0) or (action_time < time):
                    time = action_time
                    adjustments = value.get_adjustments()
        return adjustments

    # Collision Avoidance Performance Functions
    def _perform_action(self, adjustments):
        change_speed = adjustments.get("target speed")
        change_lane = adjustments.get("steering angle")
        obj_distance = self._sensors.get(FORWARD_SENSOR).get_distance_in_ft()
        obj_distance = sim_logic.feet_to_meters(obj_distance)
        if change_speed > self._current_velocity:
            self._accelerate(change_speed)
        if change_speed < self._current_velocity:
            self._decelerate(change_speed)
        self._lane_change_time = sim_logic.time_to_change_lane(change_speed, obj_distance)
        if change_lane < 0:
            self._turn_left(change_lane)
        if change_lane > 0:
            self._turn_right(change_lane)

    def _correct_course(self):
        # Resets the steering to 0 and adjusts the speed to the appropriate level
        velocity = self._current_velocity
        scaler = sim_logic.calculate_speed_scaler(self._horizontal_position)
        target_velocity = self._target_speed * scaler

        if self._horizontal_position < 0:
            self._turn_right(0)
        else:
            self._turn_left(0)

        if velocity < target_velocity:
            self._accelerate(target_velocity)
        else:
            self._decelerate(target_velocity)