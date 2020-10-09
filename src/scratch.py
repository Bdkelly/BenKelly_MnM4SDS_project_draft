newval = input("Change Value")
if newval.upper() == "Y":
    if new_value(low,high) is not None:
        high,low = new_value(high,low)
    else:
        pass
    
def new_value(high,low):
    val_c = input("Would you like to change a high or low value")
    try:
        if val_c.upper().rstrip() == "HIGH":
            let_c = input("What Letter would you like to change? ")
            new_value = input("Please enter your new value -> ")
            high[let_c] = new_value
            return high,low
        else:
            let_c = input("What Letter would you like to change? ")
            new_value = input("Please enter your new value -> ")
            low[let_c] = new_value
            return high,low
    except:
        ends = input("Something went wrong would you like to try? ")
        if ends.upper().rstrip() == "YES":
            main(low,high)
        else:
            return  