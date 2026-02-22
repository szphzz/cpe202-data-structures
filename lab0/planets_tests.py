import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    def test_01(self): #ALL test function names must begin with "test..."
        sys.stdin = io.StringIO("136") #This simulates the user typing 136 as input
        sys.stdout = student_output = io.StringIO()   
        #The following lines show what the output should look like. Note carefully the newlines and spacing.
        expected_out = "What do you weigh on earth? \n"\
                       "On Mars you would weigh 51.68 pounds.\n"\
                       "On Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip()) #Uncomment this line to see your output from the test.
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        sys.stdin = io.StringIO("155.5") #This simulates the user typing 155.5 as input
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \n"\
                       "On Mars you would weigh 59.09 pounds.\n"\
                       "On Jupiter you would weigh 363.87 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip()) #Uncomment this line to see your output from the test.
        self.assertEqual(expected_out, student_output.getvalue().strip())


if __name__ == "__main__":
        unittest.main()
