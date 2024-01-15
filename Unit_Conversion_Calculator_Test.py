"""
Project Name: Unit Conversion Calculator Test
Date: 1/9/2023
Author: Liam Cassell
All Rights Reserved 
Revision #: 0
"""

import Unit_Conversion_Calculator as UCS #Imports file to test
from unittest.mock import patch #Import the patch function to test the print()
import unittest.mock as mock
#import sys #Import sys to print out statments

#UCS.main()




@patch('builtins.print')
def test(mock_print):
    print('Here')
    # The actual test
    testValue = 2
    testUnitIn = 'METER'
    testUnitOut = 'FOOT'

    testUnitMap1, testUnitMap2 = UCS.unitMapReturn(testUnitIn, testUnitOut, testValue) #Get the dictionarys that hold the conversion data
    UCS.unitLogic(testUnitMap1[testUnitIn], testUnitMap2 [testUnitOut]) #Logic to determine which type of conversion will take place, return to main if types are not compatible
    worked = mock_print.assert_called_with('The result is: 6.561683333333334 ft') #Checks the last call and returns a assertion error if print out is not correct
    print(bool(worked))
    
    # Showing what is in mock
   
    #sys.stdout.write(str( mock_print.call_args ) + '\n') #Prints the arguments for the mock call to the terminal
    #sys.stdout.write(str( mock_print.call_args_list ) + '\n')

test()


"""
import Unit_Conversion_Calculator as UCS #Imports file to test
import unittest
from unittest.mock import patch

class testLengthM2I(unittest.TestCase):

    inputTestList = [1, 'meter', 'foot'] #Inputs to test with list

    @patch('builtins.input', return_value = inputTestList)
    def test_sum_string_of_ints(self, mock_input):
        result = UCS.main()
        self.assertEqual(result, 'The result is: 6.561683333333334 ft')

"""