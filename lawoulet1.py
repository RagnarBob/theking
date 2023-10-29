from random import randrange
import pickle

computer = randrange(0,100)
print(computer)



name = input("antre nonw :")
while " " in name or name.islower() == False:
    name=input("antre yon non ki akseptab :")
    

try:
    with open("sko.pkl","rb") as sko_file:
         sko = pickle.load(sko_file)
except(FileNotFoundError,EOFError):
     sko={}

user_sko=sko.get(name,0)             
        
nbr_de_chans = 5

print(f"yes,yes, {name} !!! ou rete {nbr_de_chans} chans pouw jwenn nonb odinate an")
while True :
    while nbr_de_chans > 0:
        try :
                nbr_chwazi = int(input("antre yon nonb ant 0 et 200 :"))
                if 0<= nbr_chwazi<=200 :
                    nbr_de_chans -= 1
                    print(f"ou rete { nbr_de_chans} chans")
                    if nbr_chwazi == computer:
                        print("ou genyen")
                        print("nonb computer a te chwazi an se : ", computer)
                        user_sko += nbr_de_chans * 30  
                        print("bravo ou fe",user_sko,"pwen")
                        break
                    elif nbr_chwazi < computer:
                        print("nonb computer a pi gran")
                    else:
                        print("nonb computer an pi piti")
                else:
                  print("ou pa nan enteval lan") 
        except ValueError:
            print("saw antre an pa bon,antre yon nonb ant 0 et 100") 

    if nbr_de_chans == 0:
        print("ou pa gen chans anko. nonb computer an te chwazi an se:", computer) 

    sko[name] = user_sko   

    with open("sko.pkl","wb") as sko_file:
      pickle.dump(sko,sko_file)

    nbr_de_chans = 5
    rejwe = input("siw vle rejwe peze yon bouton sou klavye an, peze \"k\" pouw kite : ").strip().lower()
    if rejwe == "k" :
        break
    
print("mesi! sko final ou se",user_sko,"pwen")             


                         

                  



                 
      
