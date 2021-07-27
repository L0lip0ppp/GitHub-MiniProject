import sys
def mainMenu():
    while True:
        print('''        ### MAIN MENU ###
        
        Select a number for the action you would like to do:
        
        1. View shop items
        2. Check shopping cart
        3. Add item to shopping cart
        4. Remove item from shopping cart
        5. How many items in shopping cart
        6. Clear shopping cart
        7. Check out/Place order
        8. Exit
        ''')

        selection = int(input('Make your selection:'))
        if selection == 1:
            displayCart()
        elif selection == 2:
            checkCart()
        elif selection == 3:
            addItem()
        elif selection == 4:
            removeItem()
        elif selection == 5:
            listLength()
        elif selection == 6:
            clearList()
        elif selection == 7:
            checkOut()
        elif selection == 8:
            sys.exit()

shopping_cart = {}

item_price = {'apple macbook air': 1439.15, 'asus s533eq 15.6': 1549.36, 'lenovo ip 3': 1399.56, 'samsung 64gb galaxy tab': 398.04, 'apple 10.2-inch ipad': 487.92, 'huawei hw-bah3 lte': 398.04, 'nintendo switch console': 488.99, 'sony playstation 5': 599.20, 'microsoft xbox console': 698.71}



def displayCart():
    display = input('Would you like to view the items in Categories, Alphabetically or in Ascending price?: ')
    if display == 'categories':
        print('''
          LAPTOPS                  *  PRICE EXCLUSIVE GST  *    GST 7%    *   OFFER   *
        - Apple Macbook Air        *       $1,345.00       *    $94.15    *    Yes    *
        - Asus S533EQ 15. 6        *       $1,448.00       *    $101.36   *    No     *
        - Lenovo IP 3              *       $1,308.00       *    $91.56    *    No     *
                                   *                       *              *           *
          TABLETS                  *                       *              *           *
        - Samsung 64GB Galaxy Tab  *       $372.00         *    $26.04    *    No     *
        - Apple 10.2-Inch Ipad     *       $456.00         *    $31.92    *    Yes    *
        - Huawei HW-BAH3 LTE       *       $372.00         *    $26.04    *    Yes    *
                                   *                       *              *           *
          GAME CONSOLE             *                       *              *           *
        - Nintendo Switch Console  *       $457.00         *    $31.99    *    Yes    *
        - Sony Playstation 5       *       $560.00         *    $39.20    *    No     *
        - Microsoft Xbox console   *       $653.00         *    $45.71    *    Yes    *''')
    elif display == 'alphabetically':
        print('''
                ITEMS              *   PRICE EXCLUSIVE GST  *    GST 7%    *   OFFER   *
        - Apple Macbook Air        *        $1,345.00       *    $94.15    *    Yes    *
        - Asus S533EQ 15. 6        *        $1,448.00       *    $101.36   *    No     *
        - Apple 10.2-Inch Ipad     *        $456.00         *    $31.92    *    Yes    *
        - Huawei HW-BAH3 LTE       *        $372.00         *    $26.04    *    Yes    *
        - Lenovo IP 3              *        $1,308.00       *    $91.56    *    No     *
        - Microsoft Xbox console   *        $653.00         *    $45.71    *    Yes    *
        - Nintendo Switch Console  *        $457.00         *    $31.99    *    Yes    *
        - Samsung 64GB Galaxy Tab  *        $372.00         *    $26.04    *    No     *
        - Sony Playstation 5       *        $560.00         *    $39.20    *    No     *''')
    elif display == 'ascending price':
        print('''
                ITEMS              *   PRICE EXCLUSIVE GST  *    GST 7%    *   OFFER   *
        - Asus S533EQ 15. 6        *        $1,448.00       *    $101.36   *    No     *
        - Apple Macbook Air        *        $1,345.00       *    $94.15    *    Yes    *
        - Lenovo IP 3              *        $1,308.00       *    $91.56    *    No     *
        - Microsoft Xbox console   *        $653.00         *    $45.71    *    Yes    *
        - Sony Playstation 5       *        $560.00         *    $39.20    *    No     *
        - Nintendo Switch Console  *        $457.00         *    $31.99    *    Yes    *
        - Apple 10.2-Inch Ipad     *        $456.00         *    $31.92    *    Yes    *
        - Huawei HW-BAH3 LTE       *        $372.00         *    $26.04    *    Yes    *
        - Samsung 64GB Galaxy Tab  *        $372.00         *    $26.04    *    No     *''')
    else:
        print('You have input an invalid statement')

def checkCart():
    print(shopping_cart)

def addItem():
    item = input('Enter the item you wish to add to cart:')
    if item in shopping_cart:
        print('Item is already in shopping cart')
        qnty = int(input('Enter the quantity:'))
        shopping_cart[item] = shopping_cart[item] + qnty
        for item in shopping_cart:
                print(item,':',shopping_cart[item])
    else:
        if item == 'apple macbook air':
            print('Apple Macbook Air        *        $1,345.00       *    $94.15    *    Yes    *')
        elif item == 'asus s533eq 15.6':
            print('Asus S533EQ 15.6        *        $1,448.00       *    $101.36   *    No     *')
        elif item == 'lenovo ip 3':
            print('Lenovo IP 3              *        $1,308.00       *    $91.56    *    No     *')
        elif item == 'samsung 64gb galaxy tab':
            print('Samsung 64GB Galaxy Tab  *        $372.00         *    $26.04    *    No     *')
        elif item == 'apple 10.2-inch ipad':
            print('Apple 10.2-Inch Ipad     *        $456.00         *    $31.92    *    Yes    *')
        elif item == 'huawei hw-bah3 lte':
            print('Huawei HW-BAH3 LTE       *        $372.00         *    $26.04    *    Yes    *')
        elif item == 'nintendo switch console':
            print('Nintendo Switch Console  *        $457.00         *    $31.99    *    Yes    *')
        elif item == 'sony playstation 5':
            print('Sony Playstation 5       *        $560.00         *    $39.20    *    No     *')
        elif item == 'microsoft xbox console':
            print('Microsoft Xbox console   *        $653.00         *    $45.71    *    Yes    *')
        confrm = input('Do you want to add ' + item + ' into your cart?, y/n :')
        if confrm == 'y':
            qnty = int(input('Enter the quantity:'))
            shopping_cart[item] = qnty
        elif confrm == 'n':
            print(item + ' will not be added into your cart')
        for item in shopping_cart:
            print(item,':',shopping_cart[item])

def removeItem():
    item = input('What item would you like to remove:')
    if item in shopping_cart:
        qnty = int(input('Enter quantity of ' + item + ' you want to remove:'))
        shopping_cart[item] = shopping_cart[item] - qnty
    else:
        print('Item is not in cart')
    for item in shopping_cart:
            print(item,':',shopping_cart[item])

def listLength():
    print('There are', len(shopping_cart), 'items in your cart')

def clearList():
    shopping_cart.clear()
    print('Your cart is now empty')

def checkOut():
    discount = input('Do you have a Membership discount? y/n :')
    







mainMenu()
