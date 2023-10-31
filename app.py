import random
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_solver import genetic_tsp
from utils import read_input

st.set_page_config(layout="wide")


page_element="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://cdn.wallpapersafari.com/88/75/cLUQqJ.jpg");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}

[data-testid="stSidebar"]> div:first-child{
background-image: url("https://mcdn.wallpapersafari.com/medium/89/87/X7GDE5.jpg");
background-size: cover;
}
</style>

"""
st.markdown(page_element, unsafe_allow_html=True)

"""
# Genetic Algorithm for Travelling Salesman Problem

The Traveling Salesman Problem (TSP) is a well-known combinatorial optimization problem in which a salesman is tasked with finding the shortest possible route that visits a set of cities exactly once and returns to the starting city.

Feel free to play adjust the parameters in the sidebar and explore the procedure in a visual manner.

"""

with st.sidebar:
    select_dataset = st.selectbox(
        label="Select a dataset",
        options=("p01.in", "dj15.in", "dj38.in", "att48.in", "qa194.in"),
    )

    num_generations = st.number_input(
        "Number of generations", min_value=10, max_value=5000, step=10
    )

    population_size = st.number_input(
        "Population size", min_value=10, max_value=5000, step=10
    )

    mutation_prob = st.number_input(
        "Mutation probability", min_value=0.0, max_value=1.0, value=0.1
    )

    random_seed_checkbox = st.checkbox("Set a random seed?")

    if random_seed_checkbox:
        random_seed = st.number_input("Random seed", min_value=0, step=1, value=42)
        random.seed(random_seed)
        np.random.seed(random_seed)

col1, col2 = st.columns(2)

col1.header("Optimal Solution")
progress_bar = st.empty()
current_distance = st.empty()
plot = col1.empty()
done = st.empty()
final_distance = st.empty()

optimal_distances = {
    "p01.in": 284,
    "dj15.in": 3172,
    "dj38.in": 6656,
    "att48.in": 33523,
    "qa194.in": 9352,
}
optimal_distance = st.write(
    f"**Optimal Distance:** {optimal_distances[select_dataset]}"
)

col2.header("Distance over time")
df = pd.DataFrame({"Distance": []})
chart = col2.empty()


## Genetic Algorithm
best_solution, best_distance = genetic_tsp(
    select_dataset,
    num_generations,
    population_size,
    mutation_prob,
    chart,
    plot,
    progress_bar,
    current_distance,
)

progress_bar.empty()
current_distance.empty()

cities = read_input(f"data/{select_dataset}")


done.write("**Done**!")
final_distance.write(f"**Final Distance:** {best_distance}")
