# Naruszenie zasady DIP

class SwitchableDevice:

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SwitchableDevice):
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class Fan(SwitchableDevice):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan is stopped")


class Button:
    def __init__(self, device: SwitchableDevice):
        self._device = device

    def press(self):
        self._device.turn_on()


# Usage
light = Light()
light_button = Button(light)

fan = Fan()
fan_button = Button(fan)

light_button.press()
fan_button.press()
