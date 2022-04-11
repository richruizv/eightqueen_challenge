import time

import db
from models import Solution

"""The n queens puzzle."""
class NQueens:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self, size,print_options):
        # Store the puzzle (problem) size and the number of valid solutions
        self.size = size
        self.print_options = print_options
        self.solutions = 0
        self.possible_solutions = []
        
        self.solve()

    def solve(self):
        """Solve the n queens puzzle and print the number of solutions"""

        start_time = time.time()        
        
        if self.print_options != 4: #if the solutions are already saving in the db, we proceed to directly showing 
            positions = [-1] * self.size
            self.put_queen(positions, 0)
        else:
            self.read_from_database()

        self.total_time = round((time.time() - start_time),2)
        
        if self.print_options == 3 and self.solutions > 0: #we save the data into the database if the system ask to
            self.saving_in_database()

        print(f"\nFound  {self.solutions} solutions. Time taken: {self.total_time}")

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            
            self.possible_solutions.append([i for i in positions]) #collecting all the solutions on this array, and with list comprehension because we want to save the values of the list

            if self.print_options == 1:
                self.show_short_board(positions)
            elif self.print_options == 2:
                self.show_full_board(positions)
            
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):  
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
                return False
        return True

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("")

    def show_short_board(self, positions):
        """
        Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the corresponding row.
        """ 
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

    def saving_in_database(self):
        db.session.query(Solution).filter(Solution.board_size==8).delete()

        for solution in self.possible_solutions:
            str_solution = str(solution)
            str_solution = str_solution[1:len(str_solution)-1]
            solution = Solution(self.size,str_solution)
            db.session.add(solution)
        
        db.session.commit()
    
    def read_from_database(self):
        for row in db.session.query(Solution).filter(Solution.board_size == self.size).all():
            solution = [int(i) for i in row.array_solution.split(",")] #Converting the string in a list of integers
            self.show_short_board(solution)
            self.solutions += 1

        if self.solutions == 0 and self.size > 4:
            print("We couldn't find anything in the dabatase, you should pick the option 3 if you want to store the solutions")




def main():
    """Initialize and solve the n queens puzzle"""
    try:
        print("""
_____ _       _     _                                 _            _           _ _                       
|  ___(_)     | |   | |                               ( )          | |         | | |                      
| |__  _  __ _| |__ | |_    __ _ _   _  ___  ___ _ __ |/ ___    ___| |__   __ _| | | ___ _ __   __ _  ___ 
|  __|| |/ _` | '_ \| __|  / _` | | | |/ _ \/ _ \ '_ \  / __|  / __| '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \\
| |___| | (_| | | | | |_  | (_| | |_| |  __/  __/ | | | \__ \ | (__| | | | (_| | | |  __/ | | | (_| |  __/
\____/|_|\__, |_| |_|\__|  \__, |\__,_|\___|\___|_| |_| |___/  \___|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|
          __/ |               | |                                                               __/ |     
         |___/                |_|                                                              |___/

The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

In this project, you can decide any board size you want!!!

        """
        )
        board_size = int(input("please, put the board size: "))
        print("""
Select a way you want to show the results
    1: Show Simple board (positions of each array)
    2: Show Full board ( an ASCII representation of the chess board)
    3: Store in Database (Saving into a Postgress database)
    4: Check Solutions from Database ( Read the information from the last saving)
    0: Check only the final amount of solutions
        """)

        print_options = int(input("please, pick one of the print options: "))

        if print_options not in [0,1,2,3,4]:
            return print("You should pick one of the given option")
        else:
            NQueens(board_size,print_options)
    except ValueError as e:
        print("You should put integer values")


if __name__ == "__main__":
    # execute only if run as a script
    main()
