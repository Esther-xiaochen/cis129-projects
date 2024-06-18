# cis129_lab03_coffeeShop.py
# Author: [Xiaochen Zhang]

def main():
    print("***************************************")
    print("My Coffee and Muffin Shop")
    num_coffees = int(input("Number of coffees bought?\n"))
    num_muffins = int(input("Number of muffins bought?\n"))
    num_teas = int(input("Number of teas bought?\n"))
    num_cookies = int(input("Number of cookies bought?\n"))
    print("***************************************\n")
    
    # Prices - 价格
    price_coffee = 5.00
    price_muffin = 4.00
    price_tea = 3.00
    price_cookie = 2.50

    # Calculate costs - 计算费用
    subtotal = (num_coffees * price_coffee) + (num_muffins * price_muffin) + (num_teas * price_tea) + (num_cookies * price_cookie)
    tax = subtotal * 0.06
    total = subtotal + tax

    # Print receipt - 打印收据
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{num_coffees} Coffee at $5 each: $ {num_coffees * price_coffee:.2f}")
    print(f"{num_muffins} Muffins at $4 each: $ {num_muffins * price_muffin:.2f}")
    print(f"{num_teas} Tea at $3 each: $ {num_teas * price_tea:.2f}")
    print(f"{num_cookies} Cookies at $2.5 each: $ {num_cookies * price_cookie:.2f}")
    print(f"6% tax: $ {tax:.2f}")
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************")
    print("Thank you for visiting My Coffee and Muffin Shop!\nPlease come again!")
    # 感谢光临我的咖啡和松饼店！欢迎再次光临！

if __name__ == "__main__":
    main()
