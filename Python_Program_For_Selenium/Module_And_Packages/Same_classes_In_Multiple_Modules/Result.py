# # Approach 1
#
# import Animal
# import Bird
# import Human
#
# obj=Animal.animal()
# obj.fly()
# obj.walk()
# obj.talk()
#
# obj1=Bird.bird()
#
# obj1.fly()
# obj1.talk()
# obj1.walk()
#
#
# obj2=Human.human()
# obj2.walk()
# obj2.fly()
# obj2.talk()

# Approach 2

from Animal import animal


obj1=animal()
obj1.fly()
obj1.walk()
obj1.talk()

from Bird import bird
obj2=bird()
obj2.fly()
obj2.talk()
obj2.walk()