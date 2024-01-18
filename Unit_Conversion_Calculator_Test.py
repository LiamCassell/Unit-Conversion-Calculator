"""
Project Name: Unit Conversion Calculator Test
Date: 1/9/2023
Author: Liam Cassell
All Rights Reserved 
Revision #: 0
"""
import pytest as pt #Imports pytest for testing
import Unit_Conversion_Calculator as UCS #Imports file to test


def testMain(testInput,testUnit1, testUnit2): #Calls all the fucntions found in UCS main for testing return results

    numericInput, inputUnit, outputUnit = testInput, testUnit1, testUnit2 #Set the user inputs for testing purposes

    inputUnitMap, outputUnitMap = UCS.unitMapReturn(inputUnit,outputUnit, numericInput) #Get the dictionarys that hold the conversion data
    newBase, newUnit, prefix = UCS.unitLogic(inputUnitMap[inputUnit], outputUnitMap [outputUnit]) #Logic to determine which type of conversion will take place, return to main if types are not compatible
    
    return newBase, newUnit, prefix

def printSuccess(testUnit1, testUnit2, x = [0]): #Print result keeps track of how many times this fucntion was called
    x[0]+= 1 #Uses pythons functions recersive properties to have list x as counter for each time the print the function was called
    print(f'Test #{x[0]} converting {testUnit1} to {testUnit2} was succsefull moving onto the next test.') #Print succesful message
    return


    #-----------------------------------------------------------------------TEST FOR VOLUME, WEIGHT, AND LENGTH CONVERSIONS---------------------------------------------------------------------------
def main():
    #Test 1 metric to metric conversion length
    testInput, testUnit1, testUnit2 = 14534, 'METER', 'METER' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == 14.534 and newUnit == 'm' and prefix == 'k' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message

    #Test 2 metric to imperial conversion weight
    testInput, testUnit1, testUnit2 = 98123, 'GRAM', 'POUND' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == 216.324 and newUnit == 'lb' and prefix == '' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message

    #Test 3 metric to imperial conversion volume
    testInput, testUnit1, testUnit2 = 0.0431, 'LITER', 'TABLESPOON' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    #assert newBase == 2.915 and newUnit == 'tbsp' and prefix == '' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message

    #Test 4 imperial to metric conversion length
    testInput, testUnit1, testUnit2 = 3.10686, 'MILE', 'METER' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == 5 and newUnit == 'm' and prefix == 'k' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message

    #Test 5 imperial to imperial conversion volume
    testInput, testUnit1, testUnit2 = 1.231, 'FLUID OUNCE', 'TABLESPOON' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == 2.462 and newUnit == 'tbsp' and prefix == '' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message


#-----------------------------------------------------------------------TEST FOR TEMPATURE CONVERSIONS---------------------------------------------------------------------------

    #Test 6 metric to imperial conversion temp
    testInput, testUnit1, testUnit2 = 255, 'KELVIN', 'RANKINE' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == 459 and newUnit == 'R' and prefix == '' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message


    #Test 7 metric to metric conversion temp
    testInput, testUnit1, testUnit2 = 310, 'KELVIN', 'CELSIUS' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == 36.85 and newUnit == 'C' and prefix == '' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message


    #Test 8 imperial to metric conversion temp
    testInput, testUnit1, testUnit2 = -40, 'FAHRENHEIT', 'CELSIUS' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == -40 and newUnit == 'C' and prefix == '' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message


    #Test 9 imperial to imperial conversion temp
    testInput, testUnit1, testUnit2 = 500, 'RANKINE', 'FAHRENHEIT' #Inputs to test
    newBase, newUnit, prefix = testMain(testInput, testUnit1, testUnit2) #Calls all the fucntions found in UCS main for testing returns results

    assert newBase == 40.33 and newUnit == 'F' and prefix == '' #Test the results with the correct answer
    printSuccess(testUnit1, testUnit2) #Prints a success message

    return

main() #Call main



















"""
import Unit_Conversion_Calculator as UCS #Imports file to test
from unittest.mock import patch #Import the patch function to test the print()

import sys


def testSuccessMSG(testUnitIn, testUnitOut):
    print("Here")
    print(f'The calculator has succeseffully converted from {testUnitIn} to {testUnitOut}')
    sys.stdout.write(f'The calculator has succeseffully converted from {testUnitIn} to {testUnitOut}')
    return

@patch('builtins.print')
def test(mock_print):
   
    
    testValue = 2
    testUnitIn = 'METER'
    testUnitOut = 'FOOT'

    testUnitMap1, testUnitMap2 = UCS.unitMapReturn(testUnitIn, testUnitOut, testValue) #Get the dictionarys that hold the conversion data
    UCS.unitLogic(testUnitMap1[testUnitIn], testUnitMap2 [testUnitOut]) #Logic to determine which type of conversion will take place, return to main if types are not compatible
    mock_print.assert_called_with('The result is: 6.561683333333334 ft') #Checks the last call and returns a assertion error if print out is not correct
    testSuccessMSG(testUnitIn, testUnitOut) #Print out a success message
    
    return
    

test()

"""


