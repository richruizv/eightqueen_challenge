import db

from sqlalchemy import Column, Integer, String


class Solution(db.Base):
    __tablename__ = 'solution'
    solution_id = Column(Integer, primary_key=True)
    board_size = Column(Integer, nullable=False)
    array_solution = Column(String, nullable=False)

    def __init__(self, board_size, array_solution):
        self.board_size = board_size
        self.array_solution = array_solution

    def __str__(self):
        return self.board_size