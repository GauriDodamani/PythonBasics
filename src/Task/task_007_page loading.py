# You want to check whether a web page loads within 3 seconds (performance test condition).
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time=float(input("Enter the load time :").strip())

if load_time<3:
#    print(f"Web page loads with in {load_time} seconds")
    print("Web page loads with in 3 seconds")
else:
    print(f"⚠️ Page load too slow: {load_time} seconds")

# string format is used for printing the negative value withe f{variable_name}