from functions.student_grades import main
from functions.mandelbrot_plot import draw_mandel
from functions.pagerank_algorithm import barabasi_albert_network, squirrel_edges

# Exercise 1
# Results are printed in the terminal
main()

# Exercise 2
# Parameters, such as max. iterations, x-range, and y-range are defined.
# Mandelbrot plot is in output.png
draw_mandel(200)

# Exercise 3.1
barabasi_albert_network(5, 400, 4)
squirrel_edges("squirrel_edges.csv")