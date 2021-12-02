import pprint

jojo = "Joseph Joestar"  # -------- global level access

class Student:
    jojo_name = "Josuke"  # ---- class level access

    def __init__(self, jojo_name, jojo_age, stand):
        self.jojo_name = jojo_name  # self.student_name already exists, so the class level student_name will be overwritten
        self.jojo_age = jojo_age    #  These variables do not exist yet in the class level, so they
        self.stand = stand                # will be created in the class level and assigned our method's parameters.  --FOR THIS INSTANCE


best_jojo = Student("Jotaro Kujo", 18, "Star Platinum")
print(best_jojo.jojo_name)
pprint.pprint(vars(best_jojo))
