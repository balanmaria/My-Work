def format_name(l_name, f_name):
    formated_l_name=l_name.title()
    formated_f_name = f_name.title()

    print(f"{formated_l_name} {formated_f_name}")

format_name("MaRiA", "BALAN")

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))