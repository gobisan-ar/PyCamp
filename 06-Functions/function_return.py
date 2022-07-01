# Single Return
def format_name_v1(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name_v1("GaRY", "OLdMan"))


# Multiple Return
def format_name_v2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


print(format_name_v2("", "OLdMan"))