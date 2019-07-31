from pymoo.algorithms.moead import moead
from pymoo.factory import get_problem, get_visualization
from pymoo.optimize import minimize
from pymoo.util.reference_direction import UniformReferenceDirectionFactory

# create the optimization problem
ref_dirs = UniformReferenceDirectionFactory(3, n_points=100).do()

method = moead(
    ref_dirs=ref_dirs,
    n_neighbors=15,
    decomposition="pbi",
    prob_neighbor_mating=0.7
)

res = minimize(get_problem("dtlz2"),
               method,
               termination=('n_gen', 200)
               )

get_visualization("scatter", angle=(45, 45)).add(res.F).show()