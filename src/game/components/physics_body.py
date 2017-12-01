from pymunk import Body

class PhysicsBody:
    def __init__(self, shape, body=Body(body_type=Body.KINEMATIC)):
        self.body = body
        self.shape = shape
