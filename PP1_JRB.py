"""
Created on Wed Apr 10 10:18:02 2024

@author: jbeason
"""

import streamlit as st
import numpy as np

def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        st.write(" | ".join(row))
        if row != board[-1]:
            st.write("-" * 9)

def check_winner(board):
    """Checks if there's a winner or if it's a tie."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # Check for tie
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "tie"
    return None

def main():
    """Main function to play Tic Tac Toe."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Start the game loop
    current_player = "X"
    st.title("Tic Tac Toe")
    st.write("Player X starts the game!")
    while True:
        print_board(board)
        st.write(f"Player {current_player}'s turn")
        # Get player input
        row = st.selectbox("Select row (0-2):", range(3), key= 'select_row')
        col = st.selectbox("Select column (0-2):", range(3), key= 'select_col')
        if board[row][col] == " ":
            # Update the board
            board[row][col] = current_player
            # Check for winner or tie
            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "tie":
                    st.write("It's a tie!")
                else:
                    st.write(f"Player {winner} wins!")
                break
            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            st.write("That position is already taken. Try again.")

if __name__ == "__main__":
    main()