def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#TO DO
def dollars_to_float(d):
    f = float(d.strip().replace("$", ""))
    return f

#TO DO
def percent_to_float(p):
    f = float(p.strip().replace("%", "")) / 100.0
    return f


main()