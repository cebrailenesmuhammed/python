
product_price_one =int (input ("birinci ürün"))
product_price_second = int(input(" ikinci ürünün : \n"))






def main(product_price_onee ,product_price_secondd):
 total= product_price_onee + product_price_secondd
 if total <= 200:
    print("price: ",total)

 elif total > 200:
   print ("price:",total/4)
main( product_price_second,product_price_one )
