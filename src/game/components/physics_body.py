from pymunk import Body

class PhysicsBody:
    def __init__(self, shape, body=Body(body_type=Body.STATIC)):
        self.body = body
        self.shape = shape
