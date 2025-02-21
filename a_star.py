def a_star(start_state, max_crossings):
    open_dict = {start_state: start_state._f}  # Χρησιμοποιούμε το hash του αντικειμένου ως κλειδί.
    closed_set = set()

    while open_dict:
        # Βρίσκουμε την κατάσταση με το ελάχιστο f.
        current = min(open_dict, key=open_dict.get)
        
        # Δια σχιση καταστα σεων απο  την Α* 
        
        # left_m = current.left_missionaries
        # left_c = current.left_cannibals
        # right_m = current.N - current.left_missionaries
        # right_c = current.N - current.left_cannibals
        # boat_left = current.boat_left
        # if current._g >= 1:
        #     f_left_m = current._father.left_missionaries
        #     f_left_c = current._father.left_cannibals
        #     f_right_m = current.N - current._father.left_missionaries
        #     f_right_c = current.N - current._father.left_cannibals
        
        #     if boat_left :
        #         print("g:", current._g,"m_r", right_m , "c_r", right_c, "m_b:", abs(f_right_m - right_m), " c_b:", abs(f_right_c - right_c), "h:", current._h)
        #     else:
        #         print("g:", current._g,"m_l", left_m, "c_l", left_c, " m_b:", abs(f_left_m - left_m), " c_b:", abs(f_left_c - left_c), "h:", current._h)


        del open_dict[current]  # Αφαιρούμε την κατάσταση από το open_dict.

        if current.is_final():
            return current  # Λύση βρέθηκε.

        if current._g >= max_crossings:
            print("Δεν βρέθηκε λύση εντός του περιορισμένου αριθμού διασχίσεων.")
            return None

        closed_set.add(current)  # Προσθέτουμε την κατάσταση στο closed_set.

        for child in current.get_children():
            if child not in closed_set and child not in open_dict:
                # Προσθέτουμε την κατάσταση στο open_dict με το αντίστοιχο f.
                open_dict[child] = child._f
            elif child in open_dict:
                # Αν βρούμε καλύτερο μονοπάτι, ενημερώνουμε το f.
                if child._f < open_dict[child]:
                    open_dict[child] = child._f

    return None # Δεν υπάρχει τελική κατάσταση.
