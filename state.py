import math

class State:
    def __init__(self, numder, left_missionaries, left_cannibals, boat_left=True, father=None, g=0, boat_capacity=2):
        self.N = numder
        self.left_missionaries = left_missionaries
        self.left_cannibals = left_cannibals
        self.boat_left = boat_left
        self._father = father
        self._g = g  # κόστος που έχει διανυθεί
        self.boat_capacity = boat_capacity
        self._h = self.heuristic()  # εκτιμώμενο υπόλοιπο κόστος
        self._f = self._g + self._h  # συνολικό κόστος

    def heuristic(self):
        people_left = self.left_missionaries + self.left_cannibals

        if people_left == 0:
            return 0

        trips = math.ceil((people_left) / (self.boat_capacity - 1))
        penalty = 0 # Αύξηση του κόστους σε μη έγκυρες καταστάσεις

        if ((self.left_cannibals > self.left_missionaries > 0) or
                ((self.N - self.left_cannibals) > (self.N - self.left_missionaries) > 0)):
            penalty += 2

        if self.boat_left:
            # Υπολογισμός για την περίπτωση που η βάρκα είναι στην αριστερή όχθη
            if people_left <= self.boat_capacity:
                return 1
            else:
                return 2 * trips + 1 + penalty
        else:
            # Υπολογισμός για την περίπτωση που η βάρκα είναι στη δεξιά όχθη
            return 2 * trips + penalty

    def is_valid(self):
        # Αρνητικοί αριθμοί δεν επιτρέπονται
        if self.left_missionaries < 0 or self.left_cannibals < 0:
            return False

        # Υπολογισμός ατόμων στη δεξιά όχθη
        right_missionaries = self.N - self.left_missionaries
        right_cannibals = self.N - self.left_cannibals

        # Δεν επιτρέπεται να υπάρχουν περισσότεροι από το συνολικό αριθμό (N)
        if self.left_missionaries > self.N or self.left_cannibals > self.N:
            return False
        if right_missionaries > self.N or right_cannibals > self.N:
            return False

        # Έλεγχος ισορροπίας στις δύο όχθες
        if self.left_missionaries > 0 and self.left_missionaries < self.left_cannibals:
            return False
        if right_missionaries > 0 and right_missionaries < right_cannibals:
            return False

        return True

    def is_final(self):
        # Όλοι έχουν φτάσει στη δεξιά όχθη
        return self.left_missionaries == 0 and self.left_cannibals == 0 and not self.boat_left

    def get_children(self):
        # Δημιουργία νέων καταστάσεων για κάθε πιθανή μεταφορά
        moves = [(m, c) for m in range(self.boat_capacity + 1) for c in range(self.boat_capacity + 1)
                 if 1 <= m + c <= self.boat_capacity and (m == 0 or m >= c)]
        children = []

        for missionaries, cannibals in moves:
            if self.boat_left:
                new_state = State(self.N,
                    self.left_missionaries - missionaries,
                    self.left_cannibals - cannibals,
                    not self.boat_left,
                    father=self,
                    g=self._g + 1,
                    boat_capacity=self.boat_capacity
                )
            else:
                new_state = State(self.N,
                    self.left_missionaries + missionaries,
                    self.left_cannibals + cannibals,
                    not self.boat_left,
                    father=self,
                    g=self._g + 1,
                    boat_capacity=self.boat_capacity
                )

            if new_state.is_valid():
                children.append(new_state)

        return children

    def __hash__(self):
        return hash((self.left_missionaries, self.left_cannibals, self.boat_left))

    def __eq__(self, other):
        return (self.left_missionaries == other.left_missionaries
                and self.left_cannibals == other.left_cannibals
                and self.boat_left == other.boat_left)

    def __lt__(self, other):
        return self._f < other._f

    def print_state(self):
        # Υπολογισμός των ιεραποστόλων και κανίβαλων στη δεξιά και αριστερή όχθη
        right_missionaries = self.N - self.left_missionaries
        right_cannibals = self.N - self.left_cannibals

        if right_missionaries + right_cannibals != 0:
            father_right_missionaries = self.N - self._father.left_missionaries
            father_right_cannibals = self.N - self._father.left_cannibals

        # Υπολογισμός των ιεραποστόλων και κανίβαλων στη βάρκα
            if self.boat_left:
                boat_missionaries = abs(right_missionaries - father_right_missionaries)
                boat_cannibals = abs(right_cannibals - father_right_cannibals)
            else:
                boat_missionaries = abs(self.left_missionaries - self._father.left_missionaries)
                boat_cannibals = abs(self.left_cannibals - self._father.left_cannibals)

        # Εκτύπωση κατάστασης
            print(f"Βάρκα είναι στην {'αριστερή όχθη' if not self.boat_left else 'δεξιά όχθη'} "
                  f"και οι επιβάτες είναι -> Ιεραπόστολοι: {boat_missionaries}, Κανίβαλοι: {boat_cannibals}")
            print(f"Βάρκα έφτασε στην {'αριστερή όχθη.' if self.boat_left else 'δεξιά όχθη.'}")
        print(f"Αριστερή όχθη -> Ιεραπόστολοι: {self.left_missionaries}, Κανίβαλοι: {self.left_cannibals}", "||",
              f"Δεξιά όχθη -> Ιεραπόστολοι: {right_missionaries}, Κανίβαλοι: {right_cannibals}")
        print("-----")