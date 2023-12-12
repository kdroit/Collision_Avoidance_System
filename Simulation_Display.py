###############################################################################
#                  Revision History Table
###############################################################################
#    DATE    #    AUTHOR   #    WHAT
# 11/26/2023 # Keith Droit # Created initial Simulation_Display.py
# 11/27/2023 # Keith Droit # Found a way to add the road lines and 
#            #             #   animate the lines.
# 11/28/2023 # Keith Droit # Added grass image as the background,
#            #             # Added the code for displaying message.
# 11/29/2023 # Keith Droit # Imported Input and added John's control panel.
# 11/30/2023 # Keith Droit # Added function to set the animation duration.
# 12/03/2023 # Keith Droit # Testing QGraphicsWidget - but not working for Car.
# 12/04/2023 # Keith Droit # Now addCar is working. Added code for moveCar.
#            #             # Cars need their own sequential animation group,
#            #             # which will be placed into the parallel anim group.
# 12/05/2023 # Keith Droit # Added addObject() method.
# 12/05/2023 # Keith Droit # Added code for when the speed is changed.
# 12/05/2023 # Keith Droit # Added code for the resetSimulation() method.
###############################################################################

from PyQt6.QtCore import ( QSize, Qt, QPoint, QPropertyAnimation, QTimer,
                          QParallelAnimationGroup, QSequentialAnimationGroup)
from PyQt6.QtWidgets import (QMainWindow, QGraphicsTextItem,
                             QGraphicsScene, QGraphicsWidget, QGraphicsView)
from PyQt6.QtGui import QColor, QPalette
from Input import Input
import Simulation_Logic
from Car import Car
from Object import Object

DEFAULT_SPEED = 25

class Simulation_Display(QMainWindow):
    """This displays the simulation window and 
        animates the widgets.
    """
    cur_speed = DEFAULT_SPEED
    speed_limit = 55
    lane_count = 3
    lane_width = 120 # pixels, 12 feet
    road_height = 1500
    _line_length = 100 # pixels, 10 ft
    _min_size = QSize(1000,900)
    _right_margin = 20
    _space_between_lines = 300
    _animation_length = _line_length + _space_between_lines
    _anim_group = QParallelAnimationGroup()
    alert = None

    _stylesheet = """
        Simulation_Display {
            background: url("grass.jpg") repeat;
        }
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Collision Avoidance System")
        self.setObjectName("Simulation Window")
        self.setStyleSheet(self._stylesheet)
        self.setMinimumSize(self._min_size)
        self.addControlPanel() # add Control Panel
        self.addLane(self.lane_count) # add the Road
        self.addRoadLines(self.lane_count, self.road, self.setDuration())
        self.alert = self.messageBox()
        self.startup()

    def addLane(self, laneCount):
        roadWidth = laneCount * self.lane_width
        xpos = self.width() - roadWidth - self._right_margin
        road = QGraphicsScene(0, 0, roadWidth, self.road_height, self)
        road.setObjectName("Roadway")
        # set road color
        color = QColor(0,0,0)
        color.setNamedColor("#130A06")
        road.setBackgroundBrush(color)
        self.road = road
        # Create the QGraphicsView
        self.view = QGraphicsView(self.road)
        self.view.setParent(self)
        self.view.setGeometry(xpos, 0, roadWidth, self.road_height)
        # turn off the vertical scrollbar
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def addRoadLines(self, laneCount, parent: QGraphicsScene, duration):
        """Adds lane markers to the road"""
        length = self._line_length # length of the line
        width = 5    # width of the line, 6 inches
        
        self.anim_lines = []
        index = 0
        for lane in range(1,laneCount):
            for ypos in range(-100, self.road_height, 
                              self._space_between_lines + length):
                xpos = lane * self.lane_width
                line = QGraphicsWidget()
                line.resize(width, length)
                line.setPos(xpos, ypos)
                line.setAutoFillBackground(True)
                # yposa = ending ypos of line for animation
                yposa = ypos + length + self._space_between_lines
                animation = QPropertyAnimation(line, b"pos")
                animation.setEndValue(QPoint(xpos, yposa))
                animation.setDuration(duration)
                animation.setLoopCount(-1)
                animation.setObjectName("roadline")
                self.anim_lines.append( animation )
                self._anim_group.addAnimation(self.anim_lines[index])
                index = index + 1
                parent.addItem(line)

    def addControlPanel(self):
        """Add the Control Panel"""
        self.control_panel = Input(Simulation_Logic, self)

    def messageBox(self):
        """Set up the container for messages"""
        displayBox = QGraphicsWidget()
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('white'))
        displayBox.setAutoFillBackground(True)
        displayBox.setPalette(palette)
        #displayBox.setPos(120,100)
        displayBox.setGeometry(125,100,100,50)
        return displayBox

    def errorMsg(self, message):
        """Display the message"""
        text = QGraphicsTextItem(message)
        text.setParentItem(self.alert)
        text.setX(5)
        text.setY(5)
        text.adjustSize()
        self.alert.resize(text.textWidth() + 10, 40)
        self.road.addItem(self.alert)
        timer = QTimer(self.alert)
        timer.timeout.connect(self.closeMsg)
        timer.start(2500)
        
    def closeMsg(self):
        """Remove the message"""
        if (self._alert.findChild(QGraphicsTextItem)):
            self._alert.children().remove(QGraphicsTextItem)
        for child in (self._alert.children()):
            self._alert.children().remove(child)
        self.alert.hide()
    
    def startAnimation(self):
        """Start the simulation's animation"""
        self._anim_group.setLoopCount(-1)
        self._anim_group.start()
    
    def stopAnimation(self):
        """Stop the animation"""
        self._anim_group.stop()
    
    def pauseAnimation(self):
        """Pause the simulation"""
        self._anim_group.pause()
    
    def resetSimulation(self):
        """Reset the Simulation"""
        self._anim_group.clear() # clear animations
        self.road.clear() # clear items from road
        self.cur_speed = DEFAULT_SPEED # reset speed to the default
        # rebuild the roadlines and their animation
        self.addRoadLines(self.lane_count, self.road, self.setDuration())
        self.startup()
   
    def addObject(self, object: QGraphicsWidget):
        """Add the Object to the road"""
        object.setParent(self.road)
        self.road.addItem(object)
        # The object appears stationary in the road
        # but must be animated to move down the road
        distance = 1500 - object.loc_y
        location = QPoint(object.loc_x, 1500)
        duration = self.setDuration(distance, self.cur_speed)
        self.moveObject(object, location, duration)

    def moveObject(self, object, location: QPoint, duration):
        """Allow the stationary object to move down the road"""
        animation = QPropertyAnimation(object, b"pos")
        animation.setEndValue(location)
        animation.setDuration(duration)
        animation.setObjectName("object")
        animation.object = object # set a reference to the object
        object.anim_group.addAnimation( animation )
        self._anim_group.addAnimation(object.anim_group)

    def addCar(self, car: QGraphicsWidget):
        """Add the Car to the road"""
        car.setParent(self.road)
        self.road.addItem(car)
        if (car._target_speed != self.cur_speed):
            if (car._target_speed < self.cur_speed):
                # slow car will disappear off the bottom
                location = QPoint(car.loc_x, 1500)
                distance = 1500 - car.loc_y
                speed = self.cur_speed - car._target_speed
            else:
                # fast car will disappear off the top
                location = QPoint(car.loc_x, -200)
                distance = car.loc_y + 200
                speed = car._target_speed - self.cur_speed
            duration = self.setDuration(distance, speed)
            self.moveCar(car, location, duration)
    
    def moveCar(self, car, location: QPoint, duration):
        """Move the Car to the target location"""
        animation = QPropertyAnimation(car, b"pos")
        animation.setEndValue(location)
        animation.setDuration(duration)
        if (car._simulated_car):
            animation.setObjectName("simulated_car")
        else:
            animation.setObjectName("other_car")
        animation.car = car # set a reference to the car
        car.anim_group.addAnimation( animation )
        self._anim_group.addAnimation(car.anim_group)
    
    def setDuration(self, distance=_animation_length, speed=cur_speed):
        """Calcuate the duration for the animation in milliseconds"""
        pxft = 10 # pixels per foot
        ftsec = 1.4667 # feet per second per mile
        ms = round(distance / pxft / ftsec / speed * 1000)
        #print("duration:", ms, "ms")
        return ms
    
    def set_cur_speed(self, speed: int):
        """Set the current speed"""
        #Check speed is type of integer
        if (isinstance(speed, int)):
            # Check speed limit
            if (speed <= self.speed_limit):
                self.cur_speed = speed
                duration = self.setDuration(speed=speed)
                for prop in (self._anim_group.children()):
                    if (prop.objectName() == "roadline"):
                        prop.setDuration(duration)
                    if (isinstance(prop, QSequentialAnimationGroup)):
                        for child in (prop.children()):
                            if (child.objectName() == "object"):
                                cur_y = child.object.y()
                                end_y = child.endValue().y()
                                distance = end_y - cur_y
                                child.setDuration(
                                    self.setDuration(distance, speed))
                            else:
                                if (child.objectName() == "simulated_car"):
                                    # normally, it stays in place
                                    pass
                                elif (child.objectName() == "other_car"):
                                    # other cars stay at the same speed
                                    # so need to adjust anim up or down
                                    # and possibly direction
                                    car = child.car
                                    cur_y = car.y()
                                    end_y = child.endValue().y()
                                    end_x = child.endValue().x()
                                    if (end_y > cur_y and 
                                        car._target_speed > speed):
                                        # car was going down, but now up
                                        end_y = -200
                                        end_point = QPoint(end_x, end_y)
                                        child.setEndValue(end_point)
                                        distance = cur_y - end_y
                                        speed_diff = car._target_speed - speed
                                    else:
                                        distance = end_y - cur_y
                                        speed_diff = speed - car._target_speed
                                    # set the new duration of the animation
                                    new_duration = self.setDuration(distance, 
                                                     speed_diff)
                                    child.setDuration(new_duration)

    def startup(self):
        """Start up routine"""
        win_height = self.height()
        init_y = win_height - 200
        car = Car(self.cur_speed, 150, init_y)
        self.addCar(car)
        center = round(win_height / 2)
        distance = car.loc_y - center
        speed = round(self.cur_speed * .25)
        duration = self.setDuration(distance, speed)
        self.moveCar(car, QPoint(car.loc_x, center), duration)
        Simulation_Logic._road.update({"Sim Car": car})

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    app = QApplication([])
    window = Simulation_Display()
    window.show()
    window.errorMsg("Simulation Started")
    app.exec()
