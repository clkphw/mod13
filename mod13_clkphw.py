import unittest
from .StockApiDone import *

class Test(unittest.TestCase):

    def setUp(self):
        self.symbol = getStockName()
        self.chartType = getChartType()
        self.timeSeriesType = getTimeSeries()
        #Both start and end date
        self.date = getDate()

    def test_symbol(self):
        if(self.symbol.isalpha() == True):
            if(len(self.symbol) <= 7 & len(self.symbol) >= 1):
                self.assertTrue(self.symbol.isupper())
                self.assertFalse(self.symbol.isupper(), "Stock symbol is not all upper case")
            else:
                self.assertFalse(False, "Stock symbol not correct length")
        else:
            self.assertFalse(False, "Stock symbol is not all alpha characters")
    
    def test_chartType(self):
        if(self.chartType == 1 | self.chartType == 2):
            self.assertTrue(True)
        else:
            self.assertFalse(False, "Chart value must be 1 or 2")
    
    def test_timeSeriesType(self):
        if(self.timeSeriesType == 1 | self.timeSeriesType == 2 | self.timeSeriesType == 3 | self.timeSeriesType == 4):
            self.assertTrue(True)
        else: 
            self.assertFalse(False, "Times Series value must be 1, 2, 3, or 4")

    def test_date(self):

        try:
            dateObject = datetime.datetime.strptime(self.date, '%Y-%m-%d')
            print(dateObject)
        except ValueError:
            self.assertFalse(False, "Date should be in format YYYY-MM-DD")


if __name__ == '__main__':
    unittest.main()