from unittest import TestCase
from main import NQueens


def check_solution_if_exists(correct_solution,available_solution):
    for solution in available_solution:
        if solution == correct_solution:
            return True
    return False

class QueenTesting(TestCase):
    def test_check_solutions_from_specific_board(self):
        """
        We are checking that our Class return the correct number of solutions based of the N-Queen Challenge on internet
        https://en.wikipedia.org/wiki/Eight_queens_puzzle#:~:text=The%20problem%20of%20finding%20all,board%2C%20but%20only%2092%20solutions.
        """

        queen = NQueens(8,0)
        self.assertEqual(queen.solutions, 92)

        queen = NQueens(1,0)
        self.assertEqual(queen.solutions, 1)
        
        queen = NQueens(2,0)
        self.assertEqual(queen.solutions, 0)

        queen = NQueens(3,0)
        self.assertEqual(queen.solutions, 0)

        queen = NQueens(4,0)
        self.assertEqual(queen.solutions, 2)

        queen = NQueens(5,0)
        self.assertEqual(queen.solutions, 10)

        queen = NQueens(6,0)
        self.assertEqual(queen.solutions, 4)

    def test_check_queen_not_touching(self):
        """
        We are testing function "check_place" correctly validates that queen are not under queens attack
        - positions are the current solution status with the placed queen 
        - occupied_rows is the row that we are about to populate
        - column is the pivot that we are evaluating
        """
        queen = NQueens(1,0)

        self.assertTrue(queen.check_place(positions=[-1,-1,-1,-1] ,ocuppied_rows=0 ,column=1))
        self.assertTrue(queen.check_place(positions=[0,2,-1,-1] ,ocuppied_rows=1 ,column=3))
        self.assertTrue(queen.check_place(positions=[2,0,3,-1] ,ocuppied_rows=3 ,column=1))
        
        self.assertFalse(queen.check_place(positions=[1,3,-1,2] ,ocuppied_rows=2 ,column=2))


    def test_check_correct_solution_from_differents_board(self):
        """
        We pick 3 NxN boards and checking that at least three correct solutions are on the given results
        """

        solutions_queen_5 = [[2,0,3,1,4],[2,4,1,3,0],[3,0,2,4,1]]
        queen = NQueens(5,0)

        for correct_solution in solutions_queen_5:
            solutions_is_founded = check_solution_if_exists(correct_solution,queen.possible_solutions)
            
            self.assertTrue(solutions_is_founded, f"The solution {correct_solution} was not found")

        
        solutions_queen_8 = [[1,5,0,6,3,7,2,4],[4,0,7,3,1,6,2,5],[6,2,0,5,7,4,1,3]]
        
        queen = NQueens(8,0)

        for correct_solution in solutions_queen_8:
            solutions_is_founded = check_solution_if_exists(correct_solution,queen.possible_solutions)
            
            self.assertTrue(solutions_is_founded, f"The solution {correct_solution} was not found")

        solutions_queen_9 = [[1,3,8,6,2,0,5,7,4],[3,6,4,1,8,0,2,7,5],[8,5,7,1,3,0,6,4,2]]

        queen = NQueens(9,0)

        for correct_solution in solutions_queen_9:
            solutions_is_founded = check_solution_if_exists(correct_solution,queen.possible_solutions)
            
            self.assertTrue(solutions_is_founded, f"The solution {correct_solution} was not found")