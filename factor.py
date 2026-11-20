name = str(input("Lotfan esm kharidar ra vared konid: "))
product_name = input("esm kalaye moshtari ra vared konid: ")
price_of_products = int(input("geymat kalaye moshtari ra vared konid: ").strip())
quaintity = int(input("tedad kalaye moshtari ra vared konid: "))
discount_status = str(input("in kala takhfif darad ? : bale/kheyr"))
if discount_status == "bale":
    discount = float(input("mgdar takhfif ra vared konid: ").strip())
else :
    discount = 0
shipping_cost = int(input("hazine ersal kalara vared konid: "))
javab_pardakht =input("pardakht shod? : bale/kheyr")

total_cost = price_of_products * quaintity
discount_amount = total_cost * discount / 100
final_cost = total_cost -discount_amount + shipping_cost

if price_of_products <= 0:
    print("khata :geymat nabayad kam tar ya mosavi sefr bashad")
elif discount < 0 or discount > 100:
    print("khata : megdar takhfif mojaz nist")
elif quaintity <= 0:
    print("khata : teddad nabayad kamtar mosavi sefr bashad")
elif shipping_cost < 0:
    print("khata : hazine ersal nemitvanad kamtar az sefr bashad")
elif discount_status != "bale" and discount_status != "kheyr":
    print("khata : fagat ba bale ya kheyr pasokh dahid")
elif javab_pardakht != "bale" and javab_pardakht != "kheyr":
    print("khata : fagat ba bale ya kheyr pasokh dahid")
elif javab_pardakht == "bale":
    print("\n --------factor--------")
    print("pardakht shode :)")
    print(f'agha/khanom : {name}')
    print(f' kala : {product_name}')
    print(f'geymat vahed : {price_of_products:,}'.strip())
    print(f'tedad kala : {quaintity}')
    print(f'takhfif : {discount:,}%')
    print(f'hazine ersal : {shipping_cost:,}')
    print(f'geymat nahayi : {final_cost:,}')
elif javab_pardakht == "kheyr":
    print("pardakht nashode :/")


