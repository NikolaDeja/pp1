def	hotel_list(hotels):
    l=[]
    i=0
    while i<len(hotels):
        hotel=hotels[i]
        l.append(hotel["name"])
        i+=1
    return l

def avg_price(hotels):
    i=0
    sum=0
    while i<len(hotels):
        hotel=hotels[i]
        sum+=hotel["price"]
        i+=1

    avg=sum/len(hotels)
    return avg

Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
print("Hotels in Krakow: ")
print(hotel_list(Hotels_in_Krakow))
print(f"Avreage hotel price Krakow: {avg_price(Hotels_in_Krakow)}")
print("Hotels in Sopot: ")
print(hotel_list(hotels_in_Sopot))
print(f"Avreage hotel price Sopot: {avg_price(hotels_in_Sopot)}")
if avg_price(Hotels_in_Krakow)<avg_price(hotels_in_Sopot):
    print("Cheaper hotels in Krakow")
else:
    print("Cheaper hotels in Sopot")