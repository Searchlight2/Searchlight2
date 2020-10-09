from misc.is_number import is_number

# Parses the de workflow parameters into a usable format
def de_parsing(de_workflow_parameters, global_variables):

    parsed_de_parameters = []
    for de_parameter in de_workflow_parameters:

        # default sub-parameters
        de_file_path = None
        numerator_group = None
        denominator_group = None
        p_threshold = 0.05
        fold_threshold = 1
        order_list = None
        gl_file_path = None

        # gets the sub-parameters
        sub_params_list = de_parameter.split(",")
        for sub_param in sub_params_list:
            if sub_param.upper().startswith("file=".upper()):
                de_file_path = sub_param.split("=")[1]
            if sub_param.upper().startswith("numerator=".upper()):
                numerator_group = sub_param.split("=")[1].upper()
            if sub_param.upper().startswith("denominator=".upper()):
                denominator_group = sub_param.split("=")[1].upper()
            if sub_param.upper().startswith("p.adj=".upper()):
                p_threshold = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("log2fold=".upper()):
                fold_threshold = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("order=".upper()):
                order_list = sub_param.split("=")[1].split("+")
                order_list = [x.upper() for x in order_list]
            if sub_param.upper().startswith("gl=".upper()):
                gl_file_path = sub_param.split("=")[1]


        # Parses the gl if supplied
        if gl_file_path == None:
            gl_dict = None
        else:
            gl_dict = {}
            gl_file = open(gl_file_path).readlines()
            for line in gl_file:
                gl_dict[line.rstrip().upper()] = True


        # Parses the de file:
        de_file = open(de_file_path).readlines()
        de_dict = {}
        header = True

        for line in de_file:

            if header:
                header = False
            else:
                gene,log2fold,p,padj = line.rstrip().split("\t")
                gene = gene.upper()
                sig = False

                if is_number(log2fold):
                    log2fold_valid = True
                    log2fold = round(float(log2fold),2)
                else:
                    log2fold_valid = False
                if is_number(p):
                    p_valid = True
                    p = float(p)
                else:
                    p_valid = False
                if is_number(padj):
                    padj_valid = True
                    padj = float(padj)
                else:
                    padj_valid = False

                if log2fold_valid and p_valid and padj_valid:
                    valid = True

                    if padj < p_threshold and abs(log2fold) > fold_threshold:
                        sig = True
                    else:
                        sig = False
                else:
                    valid = False

                in_gl = True
                if gl_dict != None:
                    if gene not in gl_dict:
                        in_gl = False

                # Stores the parsed gene
                de_dict[gene] = {"sig" : sig, "log2fold" : log2fold, "p" : p, "p.adj" : padj, "valid" : valid, "log2fold_valid" : log2fold_valid, "p_valid" : p_valid, "p.adj_valid" : padj_valid, "in_gl" : in_gl}


        # sets the order to the default (numerator+denominator) if unsupplied
        if order_list == None:
            order_list = [denominator_group,numerator_group]


        # Stores the parsed parameter:
        de_parameter_dict = {}
        de_parameter_dict["de_dict"] = de_dict
        de_parameter_dict["numerator_group"] = numerator_group
        de_parameter_dict["denominator_group"] = denominator_group
        de_parameter_dict["p_threshold"] = p_threshold
        de_parameter_dict["fold_threshold"] = fold_threshold
        de_parameter_dict["order_list"] = order_list
        de_parameter_dict["gl_dict"] = gl_dict
        de_parameter_dict["de_ID"] = numerator_group + " vs " + denominator_group
        de_parameter_dict["de_file_path"] = de_file_path

        parsed_de_parameters.append(de_parameter_dict)
        print "parsed the de parameter: " + de_parameter


    global_variables["de_parameters"] = parsed_de_parameters

    return global_variables



