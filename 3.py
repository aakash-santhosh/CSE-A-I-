t=int(input("enter temperature in celsius"))
v=int(input("enter wind speed in km"))
windspeedindex=13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
print("wind speed index",windspeedindex)
