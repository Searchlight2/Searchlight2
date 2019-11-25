
def get_r_string_sample_groups_by_SS_column(order_list,sample_groups_by_column):

    sample_groups_by_column_ordered = []
    for column_dict in sample_groups_by_column:
        column_list = []
        for sample_group in order_list:
            if sample_group in column_dict:
                column_list.append(sample_group)
        sample_groups_by_column_ordered.append("c(\"" + "\",\"".join(column_list) + "\")")

    sample_groups_by_column_ordered_r_string = "list(" + ",".join(sample_groups_by_column_ordered) + ")"

    return sample_groups_by_column_ordered_r_string





