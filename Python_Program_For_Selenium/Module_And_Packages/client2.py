# Approach 1
# import sys
# sys.path.append("C:/Users/05444/PycharmProjects/Selenium/Python_Program_For_Selenium/Module_And_Packages/importing_modules_from_2_different_packages")
# sys.path.append("C:/Users/05444/PycharmProjects/Selenium/Python_Program_For_Selenium/Module_And_Packages/pack2")
# import module1
# import module2
#
# module1.display()
# module2.show()
#========================

# Approach 2
import sys
sys.path.append("C:/Users/05444/PycharmProjects/Selenium/Python_Program_For_Selenium/Module_And_Packages/importing_modules_from_2_different_packages")
sys.path.append("C:/Users/05444/PycharmProjects/Selenium/Python_Program_For_Selenium/Module_And_Packages/pack2")

from module1 import *
from module2 import *

display()
show()