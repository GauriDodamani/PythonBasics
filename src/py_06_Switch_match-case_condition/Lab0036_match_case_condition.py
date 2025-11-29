from unittest import case

print("Enter the type of test you want ")

test_type=input("The type of tests are : API, UI, Selenium, Performance, Sanity, Security : ")

match test_type:
    case "API":      # if string need to be in quotes "API"
        print("You executed : API")
    case "UI":
        print("You executed : UI")
    case "Selenium":
        print("You executed : Selenium")
    case "Performance":
        print("You executed : Performance")
    case "Sanity":
        print("You executed : Sanity")
    case "Security":
        print("You executed : Security")
    case _:
        print("Invalid")