#di buat saat mati lampu
import time

susu = 0
botol = 0
bubuksusu = 0
type = 0

time.sleep(1)
print("Hello, name is sav")
time.sleep(0.5)
name = input("what is your name ? ")
time.sleep(0.5)
print("hello!",name, "what a cool name masyaallah")
time.sleep(3)
print("now im in boarding school and now mati lampu so i get bored and i try some code maybe")
time.sleep(4.5)
print("so..")
time.sleep(2)
ask = input("do you want to play or not? yes/no/curhatan? ")
if ask == "yes" :
    print("please follow the instruction!")
    time.sleep(2)
    bubuksusu = input("type bubuksusu bot")
    if bubuksusu == "bubuksusu" :
        print("Adding some bubuk to bottle...")
        time.sleep(1)
        print("Done!")
        botol = input("type botol ")
        if botol == "botol" :
            print("Adding bubuk susu and water to bottle...")
            time.sleep(1)
            print("Done!")
            susu = input("type susu ") 
            if susu == "susu" :
                print("mixing all ingredients...")
                time.sleep(1)
                print("mixing all ingredients..")
                time.sleep(1)
                print("mixing all ingredients...")
                time.sleep(1)
                print("Done!")
                time.sleep(1)
                print("Congrast you make a bottle of milk")
elif ask == "no" :
    print("ok thank you")
elif ask == "curhatan" :
    print("HAI jadi skrg mati lampu dan wifi mati blom nyala gua gatau mau ngapain akhirnya gua ngoding karena gua sebenarnya punya game candy crush saga tapi live gua abis akhirnya yaudah karena rata rata apk sekarang membutuhka wifi akhirnya pun gwejh membuka vsc / visual studio code yh gitu deh dan sy sgt bingung mau ngapain satu kelas stress semua kaga ada wifi gua juga gatau mau ngapain lagi oke trimakasih kwan!")
    time.sleep(3)
    print("terimakasih :D")

else : 
     print("sorry type yes/no/curahatan")

