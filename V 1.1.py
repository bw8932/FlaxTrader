__author__ = 'Jennifer'
print ("\n\nFlax Trader 1.1\n\n")
print ("\t\tBy Brady")
raw_input()

import random

monocle = 0
inventory = 0
location = 1

def price_change():
#PRICE CHANGE WHEN NEEDED
    global flax_price
    global oat_price
    global wheat_price
    global barley_price
    global coffee_price

    flax_price = random.randint(1,10)
    oat_price = random.randint(10,20)
    wheat_price = random.randint(20,40)
    barley_price = random.randint(50,100)
    coffee_price = random.randint(100,500)
price_change()

#set all cash and commodity inventories to start
def initial_inv():

    global flax_inv
    global oat_inv
    global wheat_inv
    global barley_inv
    global coffee_inv
    global cash

    flax_inv = 0
    oat_inv = 0
    wheat_inv = 0
    barley_inv = 0
    coffee_inv = 0
    cash = random.randint(20,100)
initial_inv()

cash = 10000

# space() for three enters
def space():
    print ("")
    print ("")
    print ("")


#Option 1: Look Around
def look_around():
    if location == 1:
        print ("You are in beautiful Toronto, Moose Capital of the world!")
    if location == 2:
        print ("The Chicago streets bustle with activity and sizzling sausage.")
    if location == 3:
        print ("London: A city under siege by ferocious be-hatted beefeaters.")
    if location == 4:
        print ("The air is rich with the smell of fresh-baked Parisian bread and fresher-baked Parisian ennui.")

    space()
    main_menu()


#Option 2:  Price Check
def price_check():
    print ("You check the latest prices off the ticker.")
    print ("\tFlax: \t\t$%s per bushel.") % (flax_price)
    print ("\tOats: \t\t$%s per bushel.") % (oat_price)
    print ("\tWheat: \t\t$%s per bushel.") % (wheat_price)
    print ("\tBarley: \t$%s per bushel.") % (barley_price)
    print ("\tCoffee: \t$%s per bushel.") % (coffee_price)
    print ("")

    space()
    main_menu()


#Option 3: Buy
def buy():

    # must get cash and flax_inv, global variables, into the function

    print ("""A sharply dressed man with a mustache greets you.  'So you want to buy some commodities, eh?
    Maybe some nice flax? Here's the price situation:""")

    print ("")
    print ("\t1. Flax: \t$%s per bushel.") % (flax_price)
    print ("\t2. Oats: \t$%s per bushel.") % (oat_price)
    print ("\t3. Wheat: \t$%s per bushel.") % (wheat_price)
    print ("\t4. Barley: \t$%s per bushel.") % (barley_price)
    print ("\t5. Coffee: \t$%s per bushel.") % (coffee_price)
    print ("")

    print ("You have $%s.") % (cash)

    buy_choice = int(raw_input("What would you like to buy?[1-5]"))
#flax buy
    if buy_choice == 1:
        flax_buy()
        main_menu()

#oat buy
    if buy_choice == 2:
        oat_buy()
        main_menu()

# wheat buy
    if buy_choice == 3:
        wheat_buy()
        main_menu()

#barley buy
    if buy_choice == 4:
        barley_buy()
        main_menu()

#coffee buy
    if buy_choice == 5:
        coffee_buy()
        main_menu()

    else:
        print ("That is not an option on offer.")
        buy()


#flax_buy function
def flax_buy():
    global cash
    global flax_inv
    global bought_flax
    possible_flax = (cash / flax_price)
    print ("You could buy a maximum of "), possible_flax, ("bushels of flax.")
    bought_flax = int(raw_input("How many bushels would you like to buy? "
                        ""
                        ""))
    if bought_flax <= possible_flax:
        print ("You bought %s bushels of flax.") % (bought_flax)
    if bought_flax > possible_flax:
        bought_flax = 0
        print ("You do not have enough money for that much flax. Too bad!")
        buy()
    flax_inv += bought_flax
    cash -= (bought_flax * flax_price)
    print ("You now have %s bushels of flax and $%s") % (flax_inv, cash)

#oat buy
def oat_buy():
    global cash
    global oat_inv
    global bought_oat
    possible_oat = (cash / oat_price)
    print ("You could buy a maximum of "), possible_oat, ("bushels of oats.")
    bought_oat = int(raw_input("How many bushels would you like to buy? "
                        ""
                        ""))
    if bought_oat <= possible_oat:
        print ("You bought %s bushels of oats") % (bought_oat)
    if bought_oat > possible_oat:
        bought_oat = 0
        print ("You do not have enough money for that much oats. Too bad!")
        buy()
    oat_inv += bought_oat
    cash -= (bought_oat * oat_price)
    print ("You now have %s bushels of oat and $%s") % (oat_inv, cash)

# wheat buy
def wheat_buy():
    global cash
    global wheat_inv
    global bought_wheat
    possible_wheat = (cash / wheat_price)
    print ("You could buy a maximum of "), possible_wheat, ("bushels of wheat.")
    bought_wheat = int(raw_input("How many bushels would you like to buy? "
                        ""
                        ""))
    if bought_wheat <= possible_wheat:
        print ("You bought %s bushels of wheat") % (bought_wheat)
    if bought_wheat > possible_wheat:
        bought_wheat = 0
        print ("You do not have enough money for that much wheat. Too bad!")
        buy()
    wheat_inv += bought_wheat
    cash -= (bought_wheat * wheat_price)
    print ("You now have %s bushels of wheat and $%s") % (wheat_inv, cash)


# barley buy
def barley_buy():
    global cash
    global barley_inv
    global bought_barley
    possible_barley = (cash / barley_price)
    print ("You could buy a maximum of "), possible_barley, ("bushels of barley.")
    bought_barley = int(raw_input("How many bushels would you like to buy? "
                        ""
                        ""))
    if bought_barley <= possible_barley:
        print ("You bought %s bushels of barley") % (bought_barley)
    if bought_barley > possible_barley:
        bought_barley = 0
        print ("You do not have enough money for that much barley. Too bad!")
        buy()
    barley_inv += bought_barley
    cash -= (bought_barley * barley_price)
    print ("You now have %s bushels of barley and $%s") % (barley_inv, cash)


# coffee buy
def coffee_buy():
    global cash
    global coffee_inv
    global bought_coffee
    possible_coffee = (cash / coffee_price)
    print ("You could buy a maximum of "), possible_coffee, ("bushels of coffee.")
    bought_coffee = int(raw_input("How many bushels would you like to buy? "
                        ""
                        ""))
    if bought_coffee <= possible_coffee:
        print ("You bought %s bushels of coffee") % (bought_coffee)
    if bought_coffee > possible_coffee:
        bought_coffee = 0
        print ("You do not have enough money for that much coffee. Too bad!")
        buy()
    coffee_inv += bought_coffee
    cash -= (bought_coffee * coffee_price)
    print ("You now have %s bushels of coffee and $%s") % (coffee_inv, cash)

#Option 4: Sell

def sell():

    # must get cash and flax_inv, global variables, into the function
    global cash
    global flax_inv
    global oat_inv
    global wheat_inv
    global barley_inv
    global coffee_inv

    print ("""A man with a mustache greets you. 'So you want to sell some commodities, eh?
    Wheat, perhaps? Here's the price situation:""")

    print ("")
    print ("\t1. Flax: \t$%s per bushel. You have %s bushels.") % (flax_price) (flax_inv)
    print ("\t2. Oats: \t$%s per bushel. You have %s bushels.") % (oat_price) (oat_inv)
    print ("\t3. Wheat: \t$%s per bushel. You have %s bushels.") % (wheat_price) (wheat_inv)
    print ("\t4. Barley: \t$%s per bushel. You have %s bushels.") % (barley_price) (barley_inv)
    print ("\t5. Coffee: \t$%s per bushel. You have %s bushels.") % (coffee_price) (coffee_inv)
    print ("")

    print ("You have $%s.") % (cash)

    sell_choice = int(raw_input("What would you like to sell? [1-5]"))

#flax sell
    if sell_choice == 1:
        flax_sell()
        main_menu()

#oat sell
    if sell_choice == 2:
        oat_sell()
        main_menu()

# wheat sell
    if sell_choice == 3:
        wheat_sell()
        main_menu()

#barley sell
    if sell_choice == 4:
        barley_sell()
        main_menu()

#coffee sell
    if sell_choice == 5:
        coffee_sell()
        main_menu()

    else:
        print ("That is not an option on offer.")
        sell()


# flax sell
def flax_sell():
    global cash
    global flax_inv
    global sold_flax
    print ("You have"), flax_inv, ("bushels of flax available to sell.")
    sold_flax = int(raw_input("How many bushels would you like to sell? "
                        ""
                        ""))

    if sold_flax <= flax_inv:
        flax_inv -= sold_flax
        cash += (sold_flax * flax_price)
        print ("After selling the flax, you are left with $%s and %s bushels of flax.") % (cash, flax_inv)


    else:
        print ("""Muddy Waters said, 'you can't lose what you never had.'
        Though in this case it's more like you can't sell what you never owned.""")
        flax_sell()


# oat sell
def oat_sell():
    global cash
    global oat_inv
    global sold_oat
    print ("You have"), oat_inv, ("bushels of oats available to sell.")
    sold_oat = int(raw_input("How many bushels would you like to sell? "
                        ""
                        ""))

    if sold_oat <= oat_inv:
        oat_inv -= sold_oat
        cash += (sold_oat * oat_price)
        print ("After selling the oats, you are left with $%s and %s bushels of oats.") % (cash, oat_inv)

    else:
        print ("""Muddy Waters said, 'you can't lose what you never had.'
        Though in this case it's more like you can't sell what you never owned.""")
        oat_sell()




# wheat sell
def wheat_sell():
    global cash
    global wheat_inv
    global sold_wheat
    print ("You have"), wheat_inv, ("bushels of wheat available to sell.")
    sold_wheat = int(raw_input("How many bushels would you like to sell? "
                        ""
                        ""))

    if sold_wheat <= wheat_inv:
        wheat_inv -= sold_wheat
        cash += (sold_wheat * wheat_price)
        print ("After selling the wheat, you are left with $%s and %s bushels of wheat.") % (cash, wheat_inv)

    else:
        print ("""Muddy Waters said, 'you can't lose what you never had.'
        Though in this case it's more like you can't sell what you never owned.""")
        wheat_sell()





# barley sell
def barley_sell():
    global cash
    global barley_inv
    global sold_barley
    print ("You have"), barley_inv, ("bushels of barley available to sell.")
    sold_barley = int(raw_input("How many bushels would you like to sell? "
                        ""
                        ""))

    if sold_barley <= barley_inv:
        barley_inv -= sold_barley
        cash += (sold_barley * barley_price)
        print ("After selling the barley, you are left with $%s and %s bushels of barley.") % (cash, barley_inv)


    else:
        print ("""Muddy Waters said, 'you can't lose what you never had.'
        Though in this case it's more like you can't sell what you never owned.""")
        barley_sell()



# coffee sell
def coffee_sell():
    global cash
    global coffee_inv
    global sold_coffee
    print ("You have"), coffee_inv, ("bushels of coffee available to sell.")
    sold_coffee = int(raw_input("How many bushels would you like to sell? "
                        ""
                        ""))

    if sold_coffee <= coffee_inv:
        coffee_inv -= sold_coffee
        cash += (sold_coffee * coffee_price)
        print ("After selling the coffee, you are left with $%s and %s bushels of coffee.") % (cash, coffee_inv)


    else:
        print ("""Muddy Waters said, 'you can't lose what you never had.'
        Though in this case it's more like you can't sell what you never owned.""")
        coffee_sell()













#Option 5: Check inventory
def check_inv():
    print ("Flax:"), flax_inv, ("bushels")
    print ("Oats:"), oat_inv, ("bushels")
    print ("Wheat:"), wheat_inv, ("bushels")
    print ("Barley:"), barley_inv, ("bushels")
    print ("Coffee:"), coffee_inv, ("bushels")
    print ("")
    print ("You currently have $"), cash,(".")
    space()
    main_menu()

#Option 6: Wait 24 hours
def wait():
    global flax_price
    global flax_inv
    global monocle
    print ("You decide to wait until tomorrow.")
    print ("You lay right down on the trading floor, pull out your emergency pillow, and drift off to sleep.")
    print ("...")
    raw_input()
    print ("ZZZZzzzzzz")
    raw_input()
    sleep_number = random.randint(1,10)
    if sleep_number < 3 and flax_inv > 1:
        print("""BUzzzzzZZZZzzzzzz
        You wake with a start. You have heard this sound before.
        It is the dreaded Lesser Flax Weevil! A whole swarm of them!
        They devour your flax in an instant, release a collective buggy belch,
        and depart.""")
        print ("""Combing through the slobbery remains in the morning,
               you find only a single bushel of flax intact.""")
        flax_inv = 1

    if sleep_number > 8:
        flax_inv += 5
        print ("""You wake in the night to the sight of several tiny men in pointed caps.
        They are singing a cheery tune to themselves and several of them appear to be climbing
         around on your flax wagon. You're about to hit them with your emergency pillow when you
         realize they aren't stealing your flax... they're adding to it! You want to watch the
         tiny little men work, but you're very sleepy.
         In the morning, you discover they added 5 bushels to your flax supply!""")
    elif cash > 500 and monocle == 0:
        print ("""Just before you drift off to sleep, a slender man with a tuxedo and monocle
        approaches you. 'Good to see a fellow richguy in the business,' he says approvingly.
        'I'd like to invite you to join the monocle club, where we trade in only the finest flax.'
        He hands you a beautiful black velvet box, and, when you look up from it, you see that he has disappeared.""")
        open_box1 = raw_input("Open velvet box? y/n")
        if open_box1 == "y" or open_box1 == "Y":
                print ("You pop open the box to reveal... a smaller mahogany case! So luxurious; his tree did not die in vain.")
                open_box2 = raw_input("Open mahogany case? y/n")
                if open_box2 == "y" or open_box2 == "Y":
                    print ("You unseal the mahogany case to reveal... a silvery bag. It shimmers in the light.")
                    open_box3 = raw_input("Open silver bag? y/n")
                    if open_box3 == "y" or open_box3 == "Y":
                        print ("You open the silvery bag to reveal... a monocle! On a golden chain.")
                        print ("It's a bit flashy, but when you pop it on, it fits just fine.")
                        monocle = 1
                    else:
                        print ("""It's a lovely shiny bag. No sense spoiling it by digging around inside with
                               your dirty hands.""")
                else:
                    print ("Best to leave that case safely closed.  It's prettier this way!")

        else:
                print ("You wisely elect to leave the box sealed. No telling what horrors lurk inside it.")


    else:
        print ("""You sleep through the night, and wake with a slightly sore back.
You reflect on the fact that sleeping on commodities exchange floors is not
recommended by most chiropracters.""")

#add in help guy if you have no money or flax
#add in the "tooth fairy" who offers to sell you teeth

#daily flax price adjustment
    flax_price = random.randint(1, 10)
    space()
    main_menu()

#option 7: Travel

def travel():

    global location
    global flax_price
    global cash

    print ("You head to the airport. FlaxAir is having a special sale, and all one-way tickets are currently 20 dollars!")
    print ("Available destinations are:")
    print ("1. Toronto")
    if location == 1:
        print ("\t[You are here]")
    print ("2. Chicago")
    if location == 2:
        print ("\t[You are here]")
    print ("3. London")
    if location == 3:
        print ("\t[You are here]")
    print ("4. Paris")
    if location == 4:
        print ("\t[You are here]")
    destination = int(raw_input("Where would you like to go? (1,2,3, or 4)"))

    if destination == location:
        print ("Wherever you go, there you are. But you are already there. So you cannot go there.")
        raw_input()
        travel()
    elif destination == 1 or destination == 2 or destination == 3 or destination == 4:
        print ("You pay the skycaptain your fare and board the plane.")
        print ("VROOOOOOOOM! It is a big noisy metal bird.")
        print ("...")
        raw_input()
        print ("...")
        location = destination
        print ("You arrive in sunny")
        if location == 1:
            print ("Toronto")
        if location == 2:
            print ("Chicago")
        if location == 3:
            print ("London")
        if location == 4:
            print ("Paris")

#change flax price on travel
        flax_price = random.randint(1, 10)
#charge 20 dollars
        cash -= 20


        space()
        main_menu()


    else:
        print ("That was not a number between 1 and 4. Try again.")
        raw_input()
        travel()




#main_menu will be basecamp

def main_menu():
    print ("MAIN MENU\n")
    print ("\t 1. Look Around")
    print ("\t 2. Check Price")
    print ("\t 3. Buy")
    print ("\t 4. Sell")
    print ("\t 5. Check inventory")
    print ("\t 6. Wait until tomorrow")
    print ("\t 7. Travel")
    press = raw_input("\nPlease press 1,2,3, 4, 5, or 6:  ")
    if press == "1":
        space()
        look_around()
    elif press == "2":
        space()
        price_check()
    elif press == "3":
        space()
        buy()
    elif press == "4":
        space()
        sell()
    elif press == "5":
        check_inv()
        space()
    elif press == "6":
        wait()
        space()
    elif press == "7":
        travel()
        space()

    else:
        print ("\nThat is not a number between 1 and 6. \n\nTry again.")
        space()
        main_menu()

main_menu()




