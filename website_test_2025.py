# website_test_2025
# Spencer Perkins

import streamlit as st
import random
import string
import numpy as np
import pandas as pd

# Creates grid for word search
def create_grid(size):
    return [["" for _ in range(size)] for _ in range(size)]

# Puts a given word onto the grid at random
def place_word(grid, word):
    size = len(grid)
    word = word.upper()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1)]
    # In order: right, down, left, up, diagonal down, diagonal up

    # Randomly places words down iteratively
    random.shuffle(directions)
    for dx, dy in directions:
        for x in range(size):
            for y in range(size):
                if can_place_word(grid, word, x, y, dx, dy):
                    for i in range(len(word)):
                        grid[x + i * dx][y + i * dy] = word[i]
                    return True
    return False

# Checks if word can fit on the grid
def can_place_word(grid, word, x, y, dx, dy):
    size = len(grid)
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= size or ny >= size:
            return False
        if grid[nx][ny] not in ("", word[i]):
            return False
    return True

# Randomly fill rest of spaces on grid
def fill_grid(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == "":
                grid[i][j] = random.choice(string.ascii_uppercase)
    return grid

# Main content of app
st.title("Spcer's Word Search Generation Website")
st.header("IDK this is the first thing I could think of")

# User input
words_input = st.text_area("Enter words as comma separated list")
words = [w.strip() for w in words_input.split(",")]

# Choose grid size
grid_size = st.slider("Grid size:", 8, 20, 12)

# Button to generate, creates word search
if st.button("Generate Word Search"):
    grid = create_grid(grid_size)
    failed = []
    for word in words:
        if place_word(grid, word) == False:
            failed.append(word)
    grid = fill_grid(grid)

    df = pd.DataFrame(grid)
    st.dataframe(df.style.set_properties(**{
        'text-align': 'center',
        'font-weight': 'bold'
    }))

    if failed:
        st.warning(f"Can't fit: {', '.join(failed)}")

    st.success("Word list: " + ", ".join(words))
