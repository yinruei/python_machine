# class Ball:
#     def __init__(self, radius):
#         self.radius = radius
# ball=Ball(1.23)
# print(ball.radius)
# ball.radius=2.32
# print(ball.radius)

# -----------------------------------------------------------
# class Ball:
#     def __init__(self, radius):
#         if radius <= 0:
#             raise ValueError('必須是正數')
#         self.__radius = radius
    
#     def getRadius(self):
#         return self.__radius

#     def setRadius(self, radius):
#         if radius <= 0:
#             raise ValueError('必須是正數')
#         self.__radius = radius

# ball = Ball(1.23)
# print(ball.getRadius())
# ball.setRadius(2.31)

# -----------------------------------------------------------

# class Ball:
#     def __init__(self, radius):
#         if radius <= 0:
#             raise ValueError('必須是正數')
#         self.__radius = radius
    
#     def getRadius(self):
#         return self.__radius
        
#     def setRadius(self, radius):
#         self.__radius = radius
        
#     def delRadius(self):
#         del self.__radius
        
#     radius = property(getRadius, setRadius, delRadius, 'radius 特性說明')

# ball = Ball(1.23)
# print(ball.radius)
# ball.radius = 2.31

# -----------------------------------------------------------

import math
class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def volumn(self):
        print("st.q")
        return 4.0 / 3.0 * math.pi * self.__radius ** 3
    
    @volumn.setter
    def volumn(self, volumn):
        if volumn <= 0:
            raise ValueError('必須是正數')
        print("nd.q")
        self.__radius = ((3.0 * volumn) / (4.0 * math.pi)) ** (1.0 / 3.0)
        
ball = Ball(10.0)
print(ball.volumn)
ball.volumn = 5000
print(ball.radius)