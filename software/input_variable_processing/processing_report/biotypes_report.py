

def biotypes_report(global_variables):

    biotypes_dict = global_variables["biotypes_dict"]

    print("detected " + str(len(biotypes_dict.keys())) + " biotypes in the background file.")

    if len(biotypes_dict.keys()) > 5:
        print("note: detected more than 5 biotypes, each biotype doubles the initial runtime. See the manual for details.")
        print("note: you can reduce the number of biotypes by setting unwanted biotypes to \"other\" in the background file.")

    print()

