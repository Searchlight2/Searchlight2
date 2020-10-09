import sys

from misc.is_sample_group import is_sample_group
from misc.is_number import is_number


# validates the mde workflow parameters
def mde_validation(mde_workflow_parameters, sample_groups, de_parameters):

    # gets the names of the des
    de_keys = {}
    for de_parameter in de_parameters:
        de_keys[de_parameter["de_ID"]] = True

    mde_names = {}

    for mde_parameter in mde_workflow_parameters:


        # required inputs
        mde_name = None

        # gets the sub-parameters
        sub_params_list = mde_parameter.split(",")

        #number of des
        de_count = 0

        # checks the sub params
        for sub_param in sub_params_list:

            # Tests the name sub-parameter
            if sub_param.upper().startswith("name=".upper()):

                if len(sub_param.split("=")) != 2:
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format."
                    sys.exit(1)

                mde_name = sub_param.split("=")[1]

                if mde_name.upper() in mde_names:
                    print >> sys.stderr, "Error: the Mde name " + mde_name + " is used more than once."
                    sys.exit(1)
                mde_names[mde_name] = True


            # Tests the order sub-parameter
            if sub_param.upper().startswith("order=".upper()):
                if len(sub_param.split("=")) != 2:
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (order=)."
                    sys.exit(1)

                order = sub_param.split("=")[1].split("+")

                if len(order) < 2:
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (> 2 sample groups in order=)"
                    sys.exit(1)

                for sample_group in order:
                    if not is_sample_group(sample_group.upper(), sample_groups):
                        print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (order sample group missing from sample sheet"
                        sys.exit(1)

            # Tests the de sub-parameters
            if sub_param.upper().startswith("numerator=".upper()):
                if len(sub_param.split("*")) != 2:
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (numerator=)."
                    sys.exit(1)

                numerator_string,denominator_string = sub_param.split("*")

                if len(numerator_string.split("=")) != 2:
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (numerator=x*deonminator=y)."
                    sys.exit(1)
                if not denominator_string.upper().startswith("denominator=".upper()):
                    print >> sys.stderr, "Error: the Mde parameter " + mde_parameter + " is not in the correct format (denominator=)."
                    sys.exit(1)
                if len(denominator_string.split("=")) != 2:
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (denominator=)."
                    sys.exit(1)

                numerator = numerator_string.split("=")[1]
                denominator = denominator_string.split("=")[1]

                if not is_sample_group(numerator.upper(), sample_groups):
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (numerator sample group missing from sample sheet)."
                    sys.exit(1)
                if not is_sample_group(denominator.upper(), sample_groups):
                    print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (denominator sample group missing from sample sheet)."
                    sys.exit(1)

                de_ID = numerator.upper() + " vs " + denominator.upper()
                if de_ID not in de_keys:
                    print >> sys.stderr, "Error: the Mde parameter " + mde_parameter + " is not in the correct format (no de parameter of same name): " + de_ID
                    sys.exit(1)

                de_count += 1


            # Tests the correlation cut-off sub-parameter
            if sub_param.upper().startswith("scc=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print >> sys.stderr, "Error: the Mde parameter " + mde_parameter + " is not in the correct format (scc is not a number)"
                    sys.exit(1)





        # tests if the required inputs have been supplied
        if de_count < 2:
            print >> sys.stderr, "Error: the Mde parameter " + mde_parameter + " has fewer than 2 des."
            sys.exit(1)

        if mde_name == None:
            print >> sys.stderr, "Error: the Mde parameter: " + mde_parameter + " is not in the correct format (missing name=)."
            sys.exit(1)


        print "validated the mde parameter: " + mde_parameter














