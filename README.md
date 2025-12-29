# Navigating-the-Knight
A Python program to determine whether a knight can move between two squares on a chessboard in one or two legal moves.

♞ Knight Reachability in Two Moves
This repository contains a Python program that determines whether a knight on a standard 8×8 chessboard can move from a given starting square to a target square in one or two legal moves.

🧠 Problem Statement
Given:
an initial position (x, y)
a final destination (xf, yf)
(where coordinates range from 1 to 8),
the program checks:
if the knight can reach the destination in one move
otherwise, if it is reachable in two moves
otherwise, reports that it is not possible in two moves
All moves follow standard chess rules for a knight.

⚙️ Approach
A helper function GenMoves(x, y) generates all legal knight moves from a given square, ensuring the knight remains within the board boundaries.
First, the program checks whether the destination is reachable in one move.
If not, it generates all possible intermediate positions from the starting square and checks whether the destination is reachable from any of those positions in two moves.
This layered approach mirrors the actual movement constraints of a knight without unnecessary computation.

🧪 Edge Cases Considered
Moves near the edges and corners of the board
Destinations reachable in one move vs two moves
Positions that are unreachable within two moves

🛠️ Possible Improvements
Extending the solution to check reachability in N moves
Refactoring move generation to avoid in-place list modification
Representing the board as a graph and applying BFS

📚 Language Used
Python
