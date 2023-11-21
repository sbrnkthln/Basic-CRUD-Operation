from prettytable import PrettyTable 

products = [{'Product Name' : 'Joy', 'Category' : 'Body Cream', 'Fragnance': 'Vanila Liquer', 'Product ID': 'A145', 'Price' : 120000, 'Stock' : 6},
            {'Product Name' : 'Pure Wonder', 'Category' : 'Body Cream', 'Fragnance': 'Iced Rose', 'Product ID': 'B390', 'Price' : 250000, 'Stock' : 5},
            {'Product Name' : 'Poppy', 'Category' : 'Body Mist', 'Fragnance': 'Fresh Woods', 'Product ID': 'M823', 'Price' : 200000, 'Stock' : 5},
            {'Product Name' : 'Peace', 'Category' : 'Shower Gel', 'Fragnance': 'Citrus', 'Product ID': 'C354', 'Price' : 125000, 'Stock' : 3},
            {'Product Name' : 'Dahlia', 'Category' : 'Body Mist', 'Fragnance': 'Dahlia Petals', 'Product ID': 'C267', 'Price' : 200000, 'Stock' : 5},
            {'Product Name' : 'Starlight', 'Category' : 'Shower Gel', 'Fragnance': 'Sunkissed Aple', 'Product ID': 'B678', 'Price' : 300000, 'Stock' : 7},
            {'Product Name' : 'Fairytale', 'Category' : 'Body Mist', 'Fragnance': 'Rose', 'Product ID': 'C950', 'Price' : 300000, 'Stock' : 9}]


products_tagging = [{'Product Name' : 'A Wishes', 'Product ID': 'A145', 'Tags' : {'title': '', 'description': '', 'keywords': ''}},
                    {'Product Name' : 'Pure Wonder', 'Product ID': 'B390', 'Tags' : {'title': '', 'description': '', 'keywords': ''}},
                    {'Product Name' : 'Dark Kiss', 'Product ID': 'M823', 'Tags' : {'title': '', 'description': '', 'keywords': ''}},
                    {'Product Name' : 'Peace', 'Product ID': 'C354', 'Tags' : {'title': '', 'description': '', 'keywords': ''}},
                    {'Product Name' : 'Dahlia', 'Product ID': 'C267', 'Tags' : {'title': '', 'description': '', 'keywords': ''}},
                    {'Product Name' : 'Starlight', 'Product ID': 'B678', 'Tags' : {'title': '', 'description': '', 'keywords': ''}},
                    {'Product Name' : 'Fairytale', 'Product ID': 'C950', 'Tags' : {'title': '', 'description': '', 'keywords': ''}}]

storage = []
tagging_bag = []

# sub-function
def display_product_list(products):
    x = PrettyTable()
    print('\n\033[1mProduct List\033[0m')
    x.field_names = ['Product Name', 'Category', 'Fragnance', 'ID', 'Price', 'Stock']
    for i in products:
        x.add_row([i['Product Name'], i['Category'], i['Fragnance'], i['Product ID'], i['Price'], i['Stock']])
    print(x)

# sub-function
def search_category(products):
    x = PrettyTable()
    print('\n\033[1mProducts Category: \033[0m\n• Body Cream\n• Body Mist\n• Shower Gel')
    input_category = input('\nWhat category do you want to search: ').lower()
    found_cat = [item for item in products if item['Category'].lower() == input_category]

    if found_cat:
        x.field_names = ['Product Name', 'Category', 'Fragnance', 'ID', 'Price', 'Stock']
        text = (f'{input_category}')
        text = text.capitalize()
        print(f'\n\033[1m{text}\033[0m')
        for i in found_cat:
            x.add_row([i['Product Name'], i['Category'], i['Fragnance'], i['Product ID'], i['Price'], i['Stock']])
        print(x)
    else:
        print('\n\033[1m[No such category found]\033[0m')

# main-function (READ)
def display_product():
    while True:
        print('\n\033[1mDisplay Product Menu\033[0m')
        print('a. Product List\nb. Search Based on Category\nc. Back to Home Page')

        user_input = input('\nChoose the menu option based on the letter: ').lower()
        if user_input == 'a':
            display_product_list(products)
        elif user_input == 'b':
            search_category(products)
        elif user_input == 'c':
            home_page()
        else:
            print('\n\033[1m[Invalid Option]\033[0m')

# main-function (CREATE)
def store_data():
    while True:
        print('\n\033[1mStore New Product Data Menu\033[0m')
        print('a. New data\nb. Back to Home Page')

        user_input = input('\nChoose the menu option based on the letter: ').lower()

        if user_input == 'a':
            print('\n\033[1mInput Product Information\033[0m')
            input_product_name = input('a. Product name      : ').capitalize()
            input_product_category = input('b. Product category  : ').capitalize()
            input_product_frag = input('c. Product fragnance : ').capitalize()

            while True:
                input_product_id = input('d. Product ID        : ').upper()
                if any(i['Product ID'] == input_product_id for i in products):
                    print('\n\033[1mProduct ID already exist!\033[0m\n')
                else:
                    break

            while True:
                try:
                    input_product_price = int(input('e. Product price (number) : '))
                    if input_product_price <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('\n\033[1m[Price must be greater than 0!]\033[0m\n')
            
            while True:
                try:
                    input_product_stock = int(input('f. Product stock (number) : '))
                    if input_product_stock <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('\n\033[1m[Stock must be greater than 0!]\033[0m\n')
                       
            yes_no_store = input('\nYou sure you want to add it to database (yes/no)? ').lower()
            if yes_no_store == 'yes':
                new_product = {
                    'Product Name' : input_product_name,
                    'Category' : input_product_category,
                    'Fragnance' : input_product_frag,
                    'Product ID' : input_product_id,
                    'Price' : input_product_price,
                    'Stock' : input_product_stock}
                products.append(new_product)
                display_product_list(products)
                print('\nSuccessfully added to database!')
            elif yes_no_store == 'no':
                store_data()
            else:
                print('\n\033[1m[Invalid Option]\033[0m')

        elif user_input == 'b':
            home_page()
        else:
            print('\n\033[1m[Invalid Option]\033[0m')
    
# main-function (UPDATE)
def update_data():
    while True:
        print('\n\033[1mUpdate Data Menu\033[0m')
        print('a. Update Data\nb. Back to Home Page')

        user_input = input('\nChoose the menu option based on the letter: ').lower()

        if user_input == 'a':
            display_product_list(products)
            input_id = input(f'\nEnter the product\'s ID you want to update: ').strip()
            input_id = input_id.upper()

            found_id = None
            for i in range(len(products)):
                if products[i]['Product ID'] == input_id:
                    found_id = i
                    break

            if found_id is not None:
                print(f'\n\033[1mProduct Information for ID: {input_id}\033[0m ')
                print(f"a. Product Name : {products[found_id]['Product Name']}")
                print(f"b. Category     : {products[found_id]['Category']}")
                print(f"c. Fragnance    : {products[found_id]['Fragnance']}")
                print(f"d. Price        : {products[found_id]['Price']}")
                print(f"e. Stock        : {products[found_id]['Stock']}")

                index_column = input('\nEnter the letter of the column you want to update: ')
                new_data = input('\nEnter new data: ')

                if index_column == 'a':
                    products[found_id]['Product Name'] = new_data.capitalize()
                elif index_column == 'b':
                    products[found_id]['Category'] = new_data.capitalize()
                elif index_column == 'c':
                    products[found_id]['Fragnance'] = new_data.capitalize()
                elif index_column == 'd':
                    try:
                        products[found_id]['Price'] = int(new_data)
                    except ValueError:
                        print('\n\033[1m[Number Only]\033[0m\n')
                elif index_column == 'e':
                    try:
                        products[found_id]['Stock'] = int(new_data)
                    except ValueError:
                        print('\n\033[1m[Number Only]\033[0m\n')
                else:
                    print('\n\033[1m[Invalid Option]\033[0m')

                yes_no_update = input('\nYou sure you want to update the data (yes/no): ')
                if yes_no_update == 'yes':
                    display_product_list(products)
                    print('\nData succesfully updated!')
                elif yes_no_update == 'no':
                    update_data()
                else:
                    print(f'\n\033[1m[Invalid Option]\033[0m')

            else:
                print('\n\033[1m[No such ID found]\033[0m\n') 

        elif user_input == 'b':
            home_page()
        else:
            print('\n\033[1m[Invalid Option]\033[0m')
                    
# main-function (DELETE)
def remove_data():
    while True:
        print('\n\033[1mRemove Item Menu\033[0m')
        print('a. Remove Data\nb. Back to Home Page')

        user_input = input('\nChoose the menu option based on the letter: ').lower()

        if user_input == 'a':
            while True:
                try:
                    display_product_list(products)
                    del_product_id = input("\nEnter the product's ID for the item you want to remove: ").strip()
                    del_product_id = del_product_id.upper()
                    if all(i['Product ID'] != del_product_id for i in products):
                        raise ValueError
                    break
                except ValueError:
                    print('\n\033[1m[No such ID found]\033[0m')
                    remove_data()

            yes_no_remove = input('\nYou sure you want to remove the item from database (yes/no)? ').lower()
            if yes_no_remove == 'yes':
                found_id = None
                for i in products:
                    if i['Product ID'] == del_product_id:
                        found_id = i
                        break     
                if found_id is not None:
                    storage.append(found_id)
                    products.remove(found_id)  
                    display_product_list(products)
                    print(f"\nItem \"{found_id['Product Name']}\" with Product ID \"{found_id['Product ID']}\" has been succesfully removed from the database!")
                    remove_data()
            elif yes_no_remove == 'no':
                remove_data()
            else:
                print('\n\033[1m[Invalid Option]\033[0m')
            
        elif user_input == 'b':
            home_page()
        else:
            print('\n\033[1m[Invalid Option]\033[0m')
            
# sub_function
def show_deleted_data(storage): 
    x = PrettyTable()
    print('\n\033[1mDeleted Data 𖤘 :\033[0m')
    x.field_names = ['Product Name', 'Category', 'Fragnance', 'ID', 'Price', 'Stock'] 
    for i in storage:
        x.add_row([i['Product Name'], i['Category'], i['Fragnance'], i['Product ID'], i['Price'], i['Stock']])
    print(x)

# main-function (RESTORE DATA)
def restored_data():
    while True:
        print('\n\033[1mRestored Deleted Data\033[0m')
        print('a. Restored data\nb. Back to Home Page')
    
        user_input = input('\nChoose the menu option based on the letter: ').lower()

        if user_input == 'a':
            if not storage:
                print("\nNo data has been deleted yet")
                restored_data()

            while True:
                try:
                    show_deleted_data(storage)
                    returned_product_id = input("\nEnter the product's ID for the item you want to return: ").strip()
                    returned_product_id = returned_product_id.upper()
                    if any(i['Product ID'] != returned_product_id for i in storage):
                        raise ValueError
                    break
                except ValueError:
                    print('\n\033[1m[No such ID found]\033[0m')
                    restored_data()
                    
            yes_no_returned = input('\nYou sure you want to return the item to the database (yes/no)? ').lower()
            if yes_no_returned == 'yes':
                found_id = None
                for i in storage:
                    if i['Product ID'] == returned_product_id:
                        found_id = i
                        break
                if found_id is not None:
                    storage.remove(found_id)
                    products.append(found_id)
                    display_product_list(products)
                    print(f"\nItem \"{found_id['Product Name']}\" with Product ID \"{found_id['Product ID']}\" has been succesfully restored to the database!")
                    restored_data()
            elif yes_no_returned == 'no':
                restored_data()
            else:
                print('\n\033[1m[Invalid Option]\033[0m')

        elif user_input == 'b':
            home_page()
        else:
            print(f'\n\033[1m[Invalid Option]\033[0m')

# sub-function
def display_product_tags(input):
    print('\n============================ \033[1mProduct Tags\033[0m =============================')
    print('--------------------------------------------------------------------')  
    for i in range(len(tagging_bag)):
        print(f"\n{'Product Name  : '}{input[i]['Product Name']}")
        print(f"{'Product ID    : '}{input[i]['Product ID']}")
        print(f"{'Title         : '}{input[i]['Title']}")
        print(f"{'Description   : '}{input[i]['Description']}")
        print(f"{'Keywords      : '}{input[i]['Keywords']}")
    
# sub-function
def input_id(product_id):
    for i in products_tagging:
        if i['Product ID'] == product_id:
            print(f'\n\033[1mAdd tags for product:\033[0m')
            i['Product Name'].title()
            i['Product ID'].upper()
            i['Tags']['title'] =        input('• Enter title: ').title()
            i['Tags']['description'] =  input('• Enter description: ').capitalize()
            i['Tags']['keywords'] =     input('• Enter keywords: ').capitalize()

            tagging_bag.append({
                'Product Name': i['Product Name'],
                'Product ID': i['Product ID'],
                'Title': i['Tags']['title'],
                'Description': i['Tags']['description'],
                'Keywords': i['Tags']['keywords']})
            
            display_product_tags(tagging_bag)
            print('\nTags has been updated!')
            return
    if i['Product ID'] != product_id:
        print('\n\033[1m[No such ID found]\033[0m')
            
# main-function (PRODUCT TAGGING)
def tagging():
    while True:
        print('\n\033[1mProduct Tagging\033[0m')
        print('a. View Product Tags\nb. Add Tags\nc. Back to Home Page')
    
        user_input = input('\nChoose the menu option based on the letter: ').lower()

        if user_input == 'a':
            if not tagging_bag:
                print('\n\033[1m[No product tags has been made]\033[0m')
                tagging()
            else:
                display_product_tags(tagging_bag)
        elif user_input == 'b':
            display_product_list(products)
            tagging_id = input("\nEnter product's ID you want to add product tags: ").strip()
            tagging_id = tagging_id.upper()
            input_id(tagging_id)
        elif user_input == 'c':
            home_page()
        else:
            warning1 = '[Invalid Option]'
            print(f'\n\033[1m{warning1}\033[0m')

# main MENU
def home_page():
    while True:
        print(f'''
--------------------------------
         \033[1m"Poppy Bloom"\033[0m
     \033[1mStore Data Management\033[0m
--------------------------------
a. Display Product Data
b. Store New Product Data
c. Update Product Data
d. Remove Product Data
e. Restored Deleted Product Data
f. Add Product Tags
g. Exit From Menu
''')
        
        user = input('Choose the menu option based on letter: ').lower()
        if user == 'a':
            display_product()
        elif user == 'b':
            store_data()
        elif user == 'c':
            update_data()
        elif user == 'd':
            remove_data()
        elif user == 'e':
            restored_data()
        elif user == 'f':
            tagging()
        elif user == 'g':
            print('\nYou Have Left the System\n')
            quit()
        else:
            print('\n\033[1m[Invalid Option]\033[0m')

home_page()