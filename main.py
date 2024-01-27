import data


# TODO: Determine the best coins combination to pay the product and return the
#  money with best combination of coins, as well.


def greeting():
    """Shows a greeting to the user"""
    print("\n************************************************\n"
          "Hello, Welcome to your favorite Coffee Machine!!\n"
          "************************************************")


def report():
    """Prints/exposes the current resources"""
    resources = data.resources
    print(f'\nResources:\n\t"Water": {resources["water"]},\n\t"Milk":'
          f' {resources["milk"]},\n\t"Coffee": {resources["coffee"]},\n'
          f'\n\t"Money": {data.profit}')


def change_machine_resources(new_resources):
    """receives a dictionary with resources as keys and quantity to operate
    as value. The quantity can be positive or negative"""
    resources = data.resources

    print()
    for key in new_resources:
        # new_value = resources[key] + new_resources[key]
        # print(f"Old {key} = {resources[key]}, new {key} = {new_value}")
        # resources[key] = new_value
        resources[key] = resources[key] + new_resources[key]
    # print(data.resources)


def recharge():
    """When operated by a qualified professional by providing a password,
    changes the quantity of the resources.
    The password is static and defined in data.py for practical purposes"""

    # changeMachineResorces()
    def authentication():
        """Checks if the provided password is correct or wrong"""
        password = input("\nPlease, enter password:-->")
        if password == data.password:
            print("\nVerification successful")
            return 1
        else:
            print("\nWrong Password")
            return 0

    if authentication():
        new_resources = {}
        print("\nEnter resources change:")
        resources = data.resources
        for keys in resources:
            new_resources[keys] = float(input(f"\tEnter amount "
                                              f"for {keys}:-->"))
        change_machine_resources(new_resources)


def reduce_resources(ingredient_amounts):
    """Reduces the quantity of the resources by the giving amount. The input
    should be a dictionary regarding the 'resources' variable from data.py"""
    # changeMachineResources()
    new_resources_change = {}
    for key in ingredient_amounts:
        new_resources_change[key] = -ingredient_amounts[key]
    change_machine_resources(new_resources_change)


def count_coins(money_received):
    """Returns the sum of the value of all coins entered by the user"""
    return sum(money_received.values())


def return_money(payed_money, cost):
    print(f"Your return is: {round(payed_money - cost, 2)}")


def receive_money(cost):
    """Receives the coins and checks if the total value is enough for
    buying the product.
    The operation can be canceled at any point while entering the amount per
    coin.
    Returns the extra money"""
    # TODO: Cancel Operation
    money_received = {}
    coin_types_and_price = data.coin_types_and_price

    for coin_type in coin_types_and_price:
        user_input = input("Enter amount of {} coins: (type c to "
                           "cancel)-->".format(coin_type)).lower()
        if not (user_input == 'c'):
            price = coin_types_and_price[coin_type]
            money_received[coin_type] = int(user_input) * price
        else:
            return 2

    total_value = count_coins(money_received)
    print("\nTotal money received: " + str(total_value))

    if round(total_value - cost, 2) >= 0:
        data.profit += cost
        if total_value > cost:
            return_money(total_value, cost)
        return 1
    else:
        return 0


def are_ingredients_enough(product_ingredients):
    resources = data.resources
    for key in product_ingredients:
        if resources[key] < product_ingredients[key]:
            return False
    return True


def make_product(product_key: str):
    """Checks the type of product, receives the money and states if is
    enough to buy the product. If yes, subtracts the right amount to each
    resource and shows a message to the user to enjoy its coffee"""

    product = data.MENU[product_key]

    if are_ingredients_enough(product["ingredients"]):

        cost = product["cost"]
        print("The cost for {} is: {} $".format(product["name"], cost))

        is_money_right = receive_money(cost)
        if is_money_right == 1:
            reduce_resources(product["ingredients"])
        elif is_money_right == 2:
            print("Operation canceled.")
        else:
            print("Not enough money. Sorry. Money refunded")
    else:
        print("\nThere are not enough resources. Sorry 😣")


def execute_command(user_input: str):
    """Checks the commands submitted by the user and returns the ID of the
    command"""
    if user_input == 'e' or user_input == 'l' or user_input == 'c':
        make_product(user_input)
    elif user_input == 'r':
        report()
    elif user_input == 'f':
        recharge()
    else:
        print("Wrong Input. Enter a valid option.")


def main():
    is_machine_on = True

    while is_machine_on:
        greeting()
        # report = r, recharge = f, off = turn off machine
        user_input = input("What would you like? (expresso(e)/latte("
                           "l)/cappuccino(c))").lower()
        if user_input == 'off':
            is_machine_on = False
        else:
            execute_command(user_input)

    print("Maintenance Process...")


main()
