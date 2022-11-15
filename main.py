import pyautogui
import random
import time

class MouseStep:
    x:int = None
    y:int = None
    speed:float = None
    
    def __init__(self) -> None:
        if None in [self.x, self.y]:
            self.set_random_pos()
        if self.speed is None:
            self.speed = self.get_random_speed()
    

    def set_random_pos(self, co_x_y:tuple=None, overwrite:bool = False):
        """Sets the x and y coordinates 

        Args:
            co_x_y (tuple): usually from self.get_random_pos
        """
        if co_x_y is None: co_x_y = self.get_random_pos()
        self.x = co_x_y[0] if overwrite or self.x is None else self.x
        self.y = co_x_y[1] if overwrite or self.y is None else self.y
    
    def get_random_pos(self):
        """Gets the pos"""
        x = random.randint(0, 1900)
        y = random.randint(0, 1080)
        return (x, y)

    def get_random_speed(self):
        "Get speed"
        speed = random.random()
        if speed< 0.2: speed = 0.2 # Minimum speed
        return speed


def move_mouse(mouse_step:MouseStep=None):
    if mouse_step is None: mouse_step = MouseStep()
    pyautogui.moveTo(mouse_step.x, mouse_step.y, mouse_step.speed)
    
while True:
    move_mouse()
    time.sleep(1.5)
    