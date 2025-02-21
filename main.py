import time
from state import State
from a_star import a_star

# Παράδειγμα κλήσης με N, M και K
N = 3   # Αριθμός ιεραποστόλων και κανίβαλων.
M = 2   # Χωρητικότητα της βάρκας.
K = 100 # Μέγιστος αριθμός διασχίσεων.

initial_state = State(N,N,N, boat_capacity=M)

# Έναρξη μέτρησης χρόνου.
start_time = time.time()

solution = a_star(initial_state, max_crossings=K)

# Τέλος μέτρησης χρόνου.
end_time = time.time()
total_time = end_time - start_time

if solution:
    print("Λύση βρέθηκε:")
    path = []
    while solution:
        path.append(solution)
        solution = solution._father
    path.reverse()
    for step in path:
        step.print_state()

    # Εμφάνιση του συνολικού αριθμού μετακινήσεων.
    print(f"Συνολικές μετακινήσεις: {len(path) - 1}")
else:
    print("Δεν βρέθηκε λύση.")

print(f"Συνολικός χρόνος ολοκλήρωσης: {total_time:.4f} δευτερόλεπτα")