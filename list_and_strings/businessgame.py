import time
lemonadestands=1
newspaperdeliveries=0
donutshops=0
banks=0
oilcompanies=0
lemonadestand_price=1
newspaperdelivery_price=5
donutshop_price=5000
bank_price=1000000
oilcompany_price=1000000000
money=0
income=1*lemonadestands+50*newspaperdeliveries+500*donutshops+10000*banks+1000000*oilcompanies
while True:
    price=0
    buy=input('Buy anything? ')
    if buy=='yes':
        print('Your money: ',money)
        print('lemonade stand costs ',lemonadestand_price)
        print('newspaper delivery costs ',newspaperdelivery_price)
        print('donut shop costs ',donutshop_price)
        print('bank costs ',bank_price)
        print('oil company costs',oilcompany_price)
        purchased=input('Input yes/no if you want to buy the business: ').split()
        if purchased[0]=='yes':
            price+=lemonadestand_price
        if purchased[1]=='yes':
            price+=newspaperdelivery_price
        if purchased[2]=='yes': 
            price+=donutshop_price
        if purchased[3]=='yes:':  
            price+=bank_price
        if purchased[4]=='yes':
            price+=oilcompany_price
        if price<=money:
            if purchased[0]=='yes':
                lemonadestands+=1
                lemonadestand_price*=1.05
            if purchased[1]=='yes':
                newspaperdeliveries+=1
                newspaperdelivery_price*=1.06
            if purchased[2]=='yes':
                donutshops+=1
                donutshop_price*=1.07
            if purchased[3]=='yes:':
                banks+=1
                bank_price*=1.08
            if purchased[4]=='yes':
                oilcompanies+=1
                oilcompany_price*=1.1
            money-=price
            time.sleep(30)
        else:
            print('Sorry, not enough money, buy next time :)')
            time.sleep(30)
            continue
    else:
        time.sleep(30)
        continue
    money+=income

