# environment.py
class Environment:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height

    def limit_position(self, agent):
        # Wrap around if the agent goes out of bounds (optional challenge)
        if agent.x < 0:
            agent.x = self.width
        elif agent.x > self.width:
            agent.x = 0
        if agent.y < 0:
            agent.y = self.height
        elif agent.y > self.height:
            agent.y = 0
