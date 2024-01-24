""" 
Project Name: Unit Conversion Calculator
Date: 12/7/2023
Author: Liam Cassell
All Rights Reserved 
Revision #: 1 (Updated program as to provide campatiblity for testing, fixed imperial volume calculations)
"""

test = 'This is a test for PR'

def userInput(): #Function to get the users input numeric amount, input unit type, desired unit output.
    A = metricUnit
    B = imperialUnit
    
    print(f'This calculator only accepts the follow inputs.') #Print string to show user what options there are input
    print(f'Please enter from the following Metric selection: {A.inputStr}')
    print(f'Or from the following Imperial selection: {B.inputStr}') 

    numericInput = float(input('Please enter the amount of your input unit: ')) #gets the user inputs
    inputUnit = input('Enter your input unit type: ')
    outputUnit = input('Enter your desired output unit type: ')

    inputUnit = inputUnit.upper() #Converts data to upper case for data handling
    outputUnit = outputUnit.upper()

    return numericInput, inputUnit, outputUnit #Return Results

def unitMapReturn(inputUnit, outputUnit, numericInput): #Creates and input and output map(dictionary) with all needed data for the conversion
    A = metricUnit #Initialize  classes to inherit their properties
    B = imperialUnit
    D = systemUnitConversions

    unitMap = { # Unit nested dictionary to keep track unit type, system, abbrecation, and the base unit for calcaulation purposes
        'METER' : { 'TYPE' : 'LENGTH', 'SYSTEM' : 'METRIC', 'ABBREVIATED' : 'm', 'BASE UNIT' : A.ONE, 'CONVERSION RATIO' : D.lengthM2I}, #Metric units/Length
        'LITER' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'METRIC', 'ABBREVIATED' : 'l', 'BASE UNIT' : A.ONE, 'CONVERSION RATIO' : D.volumeM2I}, #Volume
        'GRAM' : { 'TYPE' : 'WEIGHT', 'SYSTEM' : 'METRIC', 'ABBREVIATED' : 'g', 'BASE UNIT' : A.ONE, 'CONVERSION RATIO' : D.weightM2I}, #Weight
        'CELSIUS' : { 'TYPE' : 'TEMPERATURE', 'SYSTEM' : 'METRIC', 'ABBREVIATED' : 'C', 'BASE UNIT' : A.C }, #Temp
        'KELVIN' : { 'TYPE' : 'TEMPERATURE', 'SYSTEM' : 'METRIC', 'ABBREVIATED' : 'K', 'BASE UNIT' : A.K },

        'INCH' : { 'TYPE' : 'LENGTH', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'in', 'BASE UNIT' : B.IN, 'CONVERSION RATIO' : D.lengthI2M}, #Imperial units/Length
        'FOOT':  { 'TYPE' : 'LENGTH', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'ft', 'BASE UNIT' : B.FT, 'CONVERSION RATIO' : D.lengthI2M},
        'MILE' : { 'TYPE' : 'LENGTH', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'mi', 'BASE UNIT' : B.MI, 'CONVERSION RATIO' : D.lengthI2M},

        'FLUID OUNCE' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'fl-oz', 'BASE UNIT' : B.FLOZ, 'CONVERSION RATIO' : D.volumeI2M}, #Volume
        'TABLESPOON' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'tbsp', 'BASE UNIT' : B.TBSP, 'CONVERSION RATIO' : D.volumeI2M},
        'TEASPOON' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'tsp', 'BASE UNIT' :  B.TSP, 'CONVERSION RATIO' : D.volumeI2M},
        'CUP' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'cu', 'BASE UNIT' :  B.CU, 'CONVERSION RATIO' : D.volumeI2M},
        'PINT' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'pt', 'BASE UNIT' :  B.PT, 'CONVERSION RATIO' : D.volumeI2M},
        'QUART' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'qt', 'BASE UNIT' :  B.QT, 'CONVERSION RATIO' : D.volumeI2M},
        'GALLON' : { 'TYPE' : 'VOLUME', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'gal', 'BASE UNIT' : B.GAL, 'CONVERSION RATIO' : D.volumeI2M},

        'OUNCE' : { 'TYPE' : 'WEIGHT', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'oz', 'BASE UNIT' :  B.OZ, 'CONVERSION RATIO' : D.weightI2M}, #Weight
        'POUND' : { 'TYPE' : 'WEIGHT', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'lb', 'BASE UNIT' : B.LB, 'CONVERSION RATIO' : D.weightI2M},
        'TON' : { 'TYPE' : 'WEIGHT', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 't', 'BASE UNIT' : B.T, 'CONVERSION RATIO' : D.weightI2M},

        'FAHRENHEIT' : { 'TYPE' : 'TEMPERATURE', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'F', 'BASE UNIT' : B.F}, #Temp
        'RANKINE' : { 'TYPE' : 'TEMPERATURE', 'SYSTEM' : 'IMPERIAL', 'ABBREVIATED' : 'R', 'BASE UNIT' : B.R}
    }

    inputUnitMap = {inputUnit : unitMap[inputUnit]} #Create new maps with the needed information based on the user input
    outputUnitMap =  {outputUnit : unitMap[outputUnit]}
    inputUnitMap[inputUnit]['INPUT VALUE'] = numericInput #Adds users numeric input to inputUnitMap under INPUT VALUE
  
    return inputUnitMap, outputUnitMap
    

def unitLogic(inputUnitMap, outputUnitMap): #Logic to determine which type of conversion will take place, return to main if types are not compatible
    if inputUnitMap['TYPE'] ==  outputUnitMap['TYPE']: #If equal then determine system type, checks to see if the unit types are compatible 
        if inputUnitMap['TYPE'] ==  'TEMPERATURE': #If tempature then start tempature conversion
            C = tempatureConversion(inputUnitMap, outputUnitMap) #Initialize the tempatureConversion class
            newBaseValue = C.beseUnitTempConversion(inputUnitMap['INPUT VALUE'], inputUnitMap['ABBREVIATED']) #Converts the input to the base unit of either C or F depending on the system, reutrns the result for more calcualtions
            newBase = C.tempatureLogic(newBaseValue) #Handles the logic of the tempature conversion and returns the result of the conversion
            prefix = '' #Sets prefix to nothing for these calcualtions
            newUnit = outputUnitMap['ABBREVIATED'] #Sets the output of the new unit to the abbrecaited version users desired output

        else: #Else calculate everything else
            newBase, newUnit, prefix = systemConversionType(inputUnitMap, outputUnitMap) #Determine the type of calculation that needs to be performed based on the system, then call the appropiate calculation for length, volume, or weight

    else: #Else restart program 
        print('The types are not compatible') 
        main() #Restart program
    
    newBase = round(newBase, 3) #Return only 3 decimal places
    return newBase, newUnit, prefix #Return all 


class tempatureConversion: #A class to organize temperature conversion logic, variables and calculations
    def __init__(self,inputUnitMap,outputUnitMap)-> None: #Initialize class varibles
        self.baseUnit = inputUnitMap['BASE UNIT']
        self.baseUnitNew = outputUnitMap['BASE UNIT']
        self.inputValue = inputUnitMap['INPUT VALUE']
        self.newUnit = outputUnitMap['ABBREVIATED']

        self.inputMap = inputUnitMap
        self.outputMap = outputUnitMap

        self.A = metricUnit
        self.B = imperialUnit
        self.D = systemUnitConversions

    def beseUnitTempConversion(self, funcInput, abrvValue): #Converts the input to the base unit of either C or F depending on the system, reutrns the result for more calcualtions
        newValue = self.rankine2BaseUnit(funcInput, abrvValue) #Converts from Rankine to Fahernheit if posible
        newValue = self.kelvin2BaseUnit(newValue, abrvValue) #Converts from Kelvin to Celcius if posible
        return newValue
             
    def tempatureLogic(self, newBaseValue):
        if (self.inputMap['SYSTEM'] == 'METRIC')  and (self.outputMap['SYSTEM'] == 'IMPERIAL'): # If metric to imperail conversion
            newValue = self.tempatureConversionM2I(newBaseValue) #Converts from Celcuis to Fahernheit
            newValue = self.beseUnitTempConversion(newValue, self.outputMap['ABBREVIATED']) #Converts input from Fahernheit to Rankine if needed

        elif (self.inputMap['SYSTEM'] == 'IMPERIAL')  and (self.outputMap['SYSTEM'] == 'IMPERIAL'): # If imperail to imperail conversion  
            newValue = self.tempatureConversionI2I(newBaseValue) #Converts input from Fahernheit to Rankine or Rankine to Fahernheit, return result

        elif (self.inputMap['SYSTEM'] == 'IMPERIAL')  and (self.outputMap['SYSTEM'] == 'METRIC'): # If imperail to metric conversion 
            newValue = self.tempatureConversionI2M(newBaseValue) #Converts from Fahernheit to Celcuis
            newValue = -newValue #Inverts value to work with baseUnitTempConversion computations
            newValue = self.beseUnitTempConversion(newValue, self.outputMap['ABBREVIATED']) #Converts input from Celcuis to Kelvin if needed
            newValue = -newValue #Invert solution after conversion
         
        elif (self.inputMap['SYSTEM'] == 'METRIC')  and (self.outputMap['SYSTEM'] == 'METRIC'): # If metric to metric conversion  
            newValue = self.tempatureConversionM2M(newBaseValue) #Converts input from Celsius to Kelvin or Kelvin to Clesius, return result
        return newValue
    
    def rankine2BaseUnit(self, newValue, abrvValue):# Converts Rankine to Fahrenheit, or does nothing returns result 
        if(self.inputMap['ABBREVIATED'] == 'R') and (abrvValue == 'R') and (self.outputMap['SYSTEM'] == 'METRIC'): #If statement to check handle case of the input is Rankine and need to convert to metric
            newValue = newValue - self.B.R #Inverted Rankine to Fahrenheit
        else:
            if (abrvValue == 'R'): #Rankine to Fahrenheit
                newValue = newValue + self.B.R
            else: #Else do nothing and pass the result back
                pass
        return newValue
    
    def kelvin2BaseUnit(self, newValue, abrvValue): #Converts Kelvin to Celcius, or does nothing returns result 
        if (abrvValue == 'K'): # Kelvin to Celcius
            newValue = newValue + self.A.K
        else: #Else do nothing and pass the result back
            pass
        return newValue

    def tempatureConversionI2I(self, newValue): #Converts input from Fahernheit to Rankine or Rankine to Fahernheit, return result
        if (self.inputMap['ABBREVIATED'] == 'F' )  and (self.outputMap['ABBREVIATED'] == 'R'): # Fahrenheit to Rankine
            newValue = newValue + self.B.R
        else: # Else Rankine to Fahrenheit conversion
            newValue = newValue - 2*self.B.R #Conversion constant x2 to undo baseUnitConversion()
        return newValue
    
    def tempatureConversionI2M(self, funcInput): #For Fahrenheit to Celcius conversion
        newValue = (funcInput - 32) * (5/9)
        return newValue

    def tempatureConversionM2M(self, newValue): #Converts input from Celsius to Kelvin or Kelvin to Clesius, return result
        if (self.inputMap['ABBREVIATED'] == 'C' )  and (self.outputMap['ABBREVIATED'] == 'K'): # Celsius to Kelvin
            newValue = self.inputValue - self.A.K
        else: # Else kelvin to Celsius conversion already took place
            pass
        return newValue

    def tempatureConversionM2I(self, funcInput): #For Celcius to Fahrenheit conversion
        newValue = (funcInput * 9/5) + 32
        return newValue
    
class systemUnitConversions():# Holds all the units for the converions between the metric and imperial system
    lengthM2I = 39.3701 #Metric to imperial: Meter to inch
    volumeM2I = 202.8841 #Liter to tsp
    weightM2I = 0.035274 #Gram to oz

    lengthI2M = 0.0254 #Metric to imperial: Inch to meter
    volumeI2M = 0.00492892 #tsp to liter
    weightI2M = 28.3495 #oz to gram

class metricUnit(): #Holds all the information needed for metric prefixes/scale
    GIGA, MEGA, KILO, ONE, CENTI, MILI, MICRO, NANO = 1000000000, 1000000, 1000, 1, 0.01, 0.001, 0.0000001, 0.000000001   #Metric Scale
    C, K = 1,-273.15    #Temp
    metricPrefixMap = {GIGA : 'G', MEGA : 'M', KILO : 'k', ONE : '', CENTI : 'c', MILI : 'm', MICRO : 'u', NANO : 'n' } #Metric Unit Map
    metricTempMap = {C: 'C', K : 'K'} #Metric tempature map
    inputStr = 'Gram, Meter, Liter, Celcius, Kelvin' #String for acceptible inputs

class imperialUnit(): #Holds data needed for imperial unit converion
    IN,  FT, MI = 1, 12, 63360 #Length
    TSP, TBSP, FLOZ, CU, PT, QT, GAL = 1, 3, 6, 48, 96, 192, 768 #Volume
    OZ, LB, T  = 1, 16, 32000 #Weight
    F, R =  1, 459.67  #Temp

    imperialPrefixMap = {IN : 'in', FT : 'ft', MI : 'mi', FLOZ : 'fl-oz', TBSP : 'tbsp', TSP : 'tsp', PT : 'pt', QT : 'qt'} #Imperial Unit Map
    imperialTempMap = {F :'F', R : 'R'} # Imperail Temp Map
    inputStr = 'Inch, Foot, Mile, Fluid Ounce, Tablespoon, Teaspoon, Cup, Pint, Quart, Gallon, Ounce, Pound, Ton, Fahrenheit, Rankine' #String for acceptible inputs


def systemConversionType(inputUnitMap, outputUnitMap): #Determine the type of calculation that needs to be performed based on the system, then call the appropiate calculation for length, volume, or weight
    A = metricUnit
    prefix = '' # sets prefix to nothing 
    
    if (inputUnitMap['SYSTEM'] == 'METRIC' )  and (outputUnitMap['SYSTEM'] == 'IMPERIAL'): #If Metric to Imperial then perform calculation
        newBaseUnit = systemConversion(inputUnitMap) #Converts from one system to another using conversions ratio and returns the result
        newUnitMap = inputUnitMap #To keep a pure unit map
        newUnitMap['INPUT VALUE'] = newBaseUnit #Assigns a new input value as to call the same function as before
        newUnit, newBase = imperialBaseUnitConversion(newUnitMap, outputUnitMap) #Uses information found an in unit map calcaulates the unit conversion ratio, returns resulting base and new unit type
        

    elif (inputUnitMap['SYSTEM'] == 'METRIC' )  and (outputUnitMap['SYSTEM'] == 'METRIC'): #If Metric to Metric then perform calculation
        base = metricBaseUnitConversion(inputUnitMap) #Fucntion to figure out the base prefix
        prefix = A.metricPrefixMap[base]
        newBase = inputUnitMap['INPUT VALUE'] / base
        newUnit = outputUnitMap['ABBREVIATED'] #Sets the output of the new unit to the abbrecaited version users desired output
       
    elif (inputUnitMap['SYSTEM'] == 'IMPERIAL' )  and (outputUnitMap['SYSTEM'] == 'METRIC'): #If Imperial to Metric then perform calculation
        newBaseUnit = systemConversion(inputUnitMap) #Converts from one system to another using conversions ratio and returns the result
        newUnitMap = inputUnitMap #To keep a pure unit map
        newUnitMap['INPUT VALUE'] = newBaseUnit #Assigns a new input value as to call the same function as before
        base = metricBaseUnitConversion(newUnitMap) #Fucntion to figure out the base prefix
        prefix = A.metricPrefixMap[base] #Get the metric prefix
        newBase = inputUnitMap['INPUT VALUE'] / base
        newUnit = outputUnitMap['ABBREVIATED'] #Sets the output of the new unit to the abbrecaited version users desired output
        
    elif (inputUnitMap['SYSTEM'] == 'IMPERIAL' )  and (outputUnitMap['SYSTEM'] == 'IMPERIAL'): #If Imperial to Imperial then perform calculation
        newUnit, newBase = imperialBaseUnitConversion(inputUnitMap, outputUnitMap) #Uses information found an in unit map calcaulates the unit conversion ratio, returns resulting base and new unit type

    return newBase, newUnit, prefix


def systemConversion(inputUnitMap): #Converts from one system to another using conversions ratio and returns the result
    baseUnit = inputUnitMap['BASE UNIT']
    conversionRatio = inputUnitMap['CONVERSION RATIO']
    inputValue = inputUnitMap['INPUT VALUE']

    baseUnitNew = baseUnit * inputValue * conversionRatio #Conversion ratio calculation
    return baseUnitNew

def metricBaseUnitConversion(inputUnitMap): #Determines how far away from the base unit the input was and assigns it an appropiate value to the nearest metric prefix, return result
    unitMap = inputUnitMap
    baseUnit = unitMap['BASE UNIT']
    a = unitMap['INPUT VALUE']
    A = metricUnit

    match a: #Case statement to determine the correct prefix range
        case _ if a >= A.GIGA:
                base = A.GIGA
        case _ if (a < A.GIGA) and (a >= A.MEGA):
                base = A.MEGA
        case _ if (a < A.MEGA) and (a >= A.KILO):
                base = A.KILO
        case _ if (a < A.KILO) and (a >= A.ONE):
                base = A.ONE
        case _ if (a < A.ONE) and (a >= A.CENTI):
                base = A.CENTI
        case _ if (a < A.CENTI) and (a >= A.MILI):
                base = A.MILI
        case _ if (a < A.MILI) and (a >= A.MICRO):
                base = A.MICRO
        case _ if a <= A.NANO:
                base = A.NANO
    return base

def imperialBaseUnitConversion(inputUnitMap, outputUnitMap): #Uses information found an in unit map calcaulates the unit conversion ratio, returns resulting base and new unit type
    baseUnit = inputUnitMap['BASE UNIT']
    baseUnitNew = outputUnitMap['BASE UNIT']
    inputValue = inputUnitMap['INPUT VALUE']
    newUnit = outputUnitMap['ABBREVIATED']
       
    #Perform unit conversion
    a = inputValue * baseUnit #Converts the user input to a base unit for calculations
    a = a / baseUnitNew #Converts unit into base unit 
    return newUnit, a


def main():# Main function
    numericInput, inputUnit, outputUnit = userInput() #Get user inputs
    inputUnitMap, outputUnitMap = unitMapReturn(inputUnit,outputUnit, numericInput) #Get the dictionarys that hold the conversion data
    newBase, newUnit, prefix = unitLogic(inputUnitMap[inputUnit], outputUnitMap [outputUnit]) #Logic to determine which type of conversion will take place, return to main if types are not compatible

    print(f'The result is: {newBase} {prefix}{newUnit}') #Print the result

if __name__ == '__main__':
    main()
