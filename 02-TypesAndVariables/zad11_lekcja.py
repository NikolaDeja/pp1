father=int(input("Enter father's income: "))
mother=int(input("Enter mother's income: "))
fam_memb=int(input("Enter number of people in family: "))

total=father+mother
person_in= total/fam_memb

print(f"Total income: {total}")
print(f"Income per person {person_in}")