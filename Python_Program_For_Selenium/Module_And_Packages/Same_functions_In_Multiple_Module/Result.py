#
#
# # Call the same function from different modules
# Approach 1
# import animal
# import bird
# import human
#
# animal.fly()
# animal.talk()
# animal.walk()
#
# bird.walk()
# bird.fly()
# bird.talk()
#
# human.talk()
# human.fly()
# human.walk()

# Approach 2

from bird import *

fly()
walk()
talk()

from animal import *

fly()
walk()
talk()

from human import  *
fly()
walk()
talk()
