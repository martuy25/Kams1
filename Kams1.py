class Test(unittest.TestCase):

 

    def test_normal(self):

        test = "Machine name=GARY1;Datetime=20210729120005;Status=OK;Pct=0.05"

        expected = ["GARY1", "2021-07-29", "12:00:05" , "OK",  "0.05"]

        generated = update(STATUS_TEST=test, testing=True)

        self.assertEqual(expected, generated)

 

    def test_no_update(self):

        test = ""

        expected = "FAILURE"

        generated = update(STATUS_TEST=test)

        self.assertEqual(expected, generated)

 

    def test_iterations(self):

        test = "Machine name=GARY1;Datetime=2021074120005;Status=OK;Pct=0.25" 

        expected = [25, 50, 75, 100]

        generated = update(STATUS_TEST=test, pct=True)

 

 

 

 

 

 

 

 

 

 

 

 

 

from typing import Text