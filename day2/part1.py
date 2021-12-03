class Submarine:
    def __init__(self):
        self.aim = 0
        self.horizontal_position = 0
        self.depth = 0

    def change_horizontal_position(self, amount):
        self.horizontal_position += amount
    
    def change_depth(self, amount):
        self.depth += amount

    def follow_course(self, course):
        commands = {
            "forward": lambda amount: self.change_horizontal_position(amount),
            "up": lambda amount: self.change_depth(-amount),
            "down": lambda amount: self.change_depth(amount)
        }

        for command in course:
            commands[command[0]](int(command[1])) 

commands = list(map(lambda command: command.split(), list(open("input.txt", "r").read().splitlines())))

submarine = Submarine()
submarine.follow_course(commands)

print(submarine.horizontal_position*submarine.depth)
