#class function
class shopListMe:
    #initializer method (accept 2 parameters)
    def __init__(self, FoodName, FoodAmount): #2 parameters (other than self) : NameCA, and AmountCA
        self.__FoodName = FoodName #attributes 1
        self.__FoodAmount = FoodAmount #attributes 2
        self.__FoodPrice = self.__priceList() #attributes 3 - using private method (self.__variablename)
        self.__calculator = self.countshopList() #attributes 4 - using public method (self.variablename)
    
    #private method to store the list
    def __priceList(self):
        #using if and elif 
        if self.__FoodName == 'Dry Cured Iberian Ham' :
            self.__FoodPrice = 117.80
        elif self.__FoodName == 'Wagyu Steaks' :
            self.__FoodPrice = 450.00
        elif self.__FoodName == 'Matsutake Mushrooms' :
            self.__FoodPrice = 272.00
        elif self.__FoodName == 'Kopi Luwak Cofee' :
            self.__FoodPrice = 306.50
        elif self.__FoodName == 'Moose Cheese' :
            self.__FoodPrice = 487.20
        elif self.__FoodName == 'White Truffles' :
            self.__FoodPrice = 3600.00
        elif self.__FoodName == 'Blue Fin Tuna' :
            self.__FoodPrice = 3603.30
        elif self.__FoodName == 'Le Bonnotte Potatoes' :
            self.__FoodPrice = 270.81
        else :
            self.__FoodPrice = 0.00   
        
        return self.__FoodPrice
    
    #public method to calculate
    def countshopList(self):
        self.__calculator = self.__FoodAmount * self.__FoodPrice
        return (self.__calculator)
    
    #accessors
    def getNameCA(self):
        return self.__FoodName
    
    def getAmountCA(self):
        return self.__FoodAmount
    
    def getPriceCA(self):
        return self.__FoodPrice
    
    def getcountCA(self):
        return self.__calculator