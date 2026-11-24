class Microwave: 
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand=brand
        self.power_rating=power_rating

    def turn_on(self) -> None: 
        if self.turn_on: 
            print(f'Microwave ({self.brand}) is already turned on.')
        else: 
            self.turn_on=True
            print(f'Microwave ({self.brand}) is now turned on.')

    def turn_off(self) -> None: 
        if self.turn_on: 
            self.turn_on=False
            print(f'Microwave ({self.brand}) is now turned off.')
        else:
            print(f'Microwace ({self.brand}) is already turned off.')

    def run(self, seconds: int) -> None: 
        if self.turn_on: 
            print(f'Running ({self.brand}) for {seconds} seconds.')
        else:
            print(f'A mystical force whispers: "Turn on your microwave first..."')

    def __str__(self) -> str: 
        return f'{self.brand} (Rating: {self.power_rating})'

    def __repr__(self) -> str: 
        return f'Microwave: (brand: {self.brand} and power_rating: {self.power_rating})'



smeg: Microwave=Microwave('Smeg', 'B')
bosch: Microwave=Microwave(
    'Bosch',
    'C'
)


print(str(smeg))

print(str(bosch))

print(repr(bosch))

print(repr(smeg))

bosch.turn_on()
# bosch.turn_off()
bosch.run(20)


# bosch.turn_off()
bosch.turn_on()
bosch.run(30)
