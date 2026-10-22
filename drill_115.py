coding_club = {"Aman", "Riya", "Karan", "Neha", "Dev"}
robotics_club = {"Riya", "Karan", "Priya", "Dev", "Raj"}
design_club = {"Neha", "Dev", "Priya", "Isha"}

c_r = coding_club.intersection(robotics_club)
c_r_not_d = c_r.difference(design_club)

print(c_r_not_d)