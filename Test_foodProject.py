import unittest
import foodProject

class TestFoodProject(unittest.TestCase):
    def test_foodProject(self):


        # the following few test will cover some edge cases for "bad"user input.
        self.assertEqual( "cookies",foodProject.proccessUserInput(""))
        self.assertEqual( "cookies",foodProject.proccessUserInput("lobst_er"))
        self.assertEqual( "cookies",foodProject.proccessUserInput("l0bster"))
        self.assertEqual( "cookies",foodProject.proccessUserInput("lobst_er1"))
        self.assertEqual("cookies",foodProject.proccessUserInput("l00000000"))
        self.assertEqual("cookies",foodProject.proccessUserInput("_)(&#^$"))


        # the follwoing test cases will cover some "good" user input
        # for our api request we must replaces the spaces with a "+"
        self.assertEqual( "lobster+and+steak",foodProject.proccessUserInput("lobster and steak"))
        self.assertEqual("lobster++steak",foodProject.proccessUserInput("lobster  steak"))
        self.assertEqual("+eggs+ham",foodProject.proccessUserInput(" eggs ham"))
        self.assertEqual( "++++++++++lobster",foodProject.proccessUserInput("          lobster"))


        #the following test will check that the "get" methods are returning the actual data

        # there is one problem with this unit test and that is that the api is constantly being updated
        # so we do not always get the same json file back. so since i have the values to be compared
        # hard coded sometimes the test return as false!
        self.assertEqual("Broiled Butter Lobster",foodProject.getRecipeName(foodProject.getAllReipe("lobster"),1))
        self.assertEqual("Extraordinary Chocolate Chip Cookies", foodProject.getRecipeName(foodProject.getAllReipe("cookies"), 4))
        self.assertEqual(100, foodProject.getRecipeCookTime(foodProject.getAllReipe("steak+and+cheese"), 4))
        self.assertEqual("http://www.lemonsforlulu.com/grilled-steak-with-roasted-tomatoes-and-blue-cheese/", foodProject.getRecipeLink(foodProject.getAllReipe("steak and cheese"), 3))



if __name__ == '__main__':
    unittest.main()