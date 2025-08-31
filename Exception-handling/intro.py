def brewChai(type): 
    
    try:
        if(type == "unknown"):
            raise ValueError("Unknown not allowed")
    except ValueError as e:
        print("Error: ", e)

    else:
        print(type)
    finally:
        print("next customer ...")


brewChai("Ginger")
brewChai("unknown")
    