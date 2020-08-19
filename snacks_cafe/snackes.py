def main():
    print("***************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To quit at any time, type 'quit' **")
    print("***************************************")

    menu = [
        {
            "name": "Appetizers",
            "types": [
                "Wings",
                "Cookies",
                "Spring Rolls",
            ],
        },
        {
            "name": "Entrees",
            "types": [
                "Salmon",
                "Steak",
                "Meat Tornado",
                "A Literal Garden",
            ],
        },
         {
            "name": "Desserts",
            "types": [
                "Ice Cream",
                "Cake",
                "Pie",
            ],
        }, 
        {
            "name": "Drinks",
            "types": [
                "Coffee",
                "Tea",
                "Unicorn Tears",
            ],
        },
    ]
    i=0
    lst = ["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]

    for x in range(4):
        print(menu[x]["name"])
        print("----------")
        for y in range(len(menu[x]["types"])):
            print(menu[x]["types"][y])
        print("  ")
    
    print("****************************************")
    print("** What would you like to order? **")
    print("****************************************")
    
    orders = []
    entering = input()
    while entering != 'quit':
        if entering in lst:
            orders.append(entering)
            occurance=orders.count(entering)
            print("** %d order of %s have been added to your meal **" %(occurance,entering))
        else:
                print('please order from the menu')
    
        entering = input()

if __name__ == '__main__':
    main()