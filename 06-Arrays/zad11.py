
def month(n):
    arr= ["January", "February","March","April","May","June",
      "July","August","September","October","November","December"]
    return arr[n-1]

n=int(input("Enter month number: "))

print(f"Month name: {month(n)}")