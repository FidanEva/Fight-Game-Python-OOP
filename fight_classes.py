# Modulların ıazəm olan funksiyalarını import edirik.
from sys import exit
from random import randint
from time import sleep
from os import system

class Gamer:
    # İlk metodda nümunə atributlarını tanıdırıq. Default dəyərlər mənimsədirik.
    def __init__(self, name, energy = 100,life = 3):
        self.name = name
        self.energy = energy
        self.life = life
        self.coup = 0

    # Oyunçular haqqında məlumatları ekrana yazdırmaq üçün funksiya yaradırıq
    def showthesituation(self):
        print("{}'s energy is {}, life is {}".format(self.name, self.energy, self.life))
        return self

    # Parametr olaraq bhücum olunan obyekti göndərəcəyimiz strike metodunu yaradırıq. Sadəcə class içində istifadə ediləcəyi üçün gizli metod kimi qeyd edirik.
    def __strike(self,gamer):
        # Həmin obyektin  hər hücumda aldğı zərbə sayı artır
        gamer.coup += 1
        # Enerjisi azalır
        gamer.energy -= 10

        # Aldığı hər 3 zərbədə bir can itirməsi üçün şərt qoyuruq.
        if gamer.coup % 3 == 0:
            print("{} got coup 3 times. He lost a life".format(gamer.name))
            gamer.life -= 1

        # Enerjisi 0-a bərabər olub ondan kiçildikdə isə mənfi qiymət almaması üçün 0-a bərabərləşdiririk. Və yenə bir can azalır.
        if gamer.energy <= 0:
            print("All {}'s energy is gone, He lost a life".format(gamer.name))
            gamer.energy = 0
            gamer.life -= 1

        # Canı 0-a düşdükdə isə enerji sıfırlanır oyun bitir və oyundan çıxılır.
        if gamer.life < 1:
            gamer.energy = 0
            print("""
            {} lose :(
            {} win. Congrats :)
            """.format(gamer.name, self.name))
            exit()

    # Hücum əməliyyatını yerinə yetirən metod. Parametr olaraq rəqib oyunçunu alır
    def attack(self,opponent):
        print("""
        Attacking...
        Please wait..
        """)

        # Yüuklənmə effekti yaratmaq üçün hər 0.3 saniyədə ekrana ardıcıl noqtələr yazdırırıq
        for i in range(0,7):
            sleep(0.3)
            print(".",end="",flush=True)

        # Random olaraq 0-1-2 alan dəyişəni resulta mənimsədirik.
        result = randint(0,2)
        # 0 seçilərsə heç-heçə sayılır
        if result == 0:
            print("\nDraw!")
            # Bu zaman hər iki oyunçunun enerjisi azalır
            self.energy -= 5
            opponent.energy -= 5
            # Yenə hər ikisinin enerjisini mənfi olmaması üçün 0-a çatıb azaldıqda 0-a bərabərləşdiririk.
            if self.energy <= 0 or opponent.energy <= 0:
                self.energy = 0
                opponent.energy = 0

        # Nəticə 1 olarsa seçilmiş obyekt hücum etmiş sayılır
        elif result == 1:
            print("\nYou successfully attacked.")
            # Strike metodu ilə rəqibə hücum əməliyyatını aparırıq.
            self.__strike(opponent)

        # Nəticə 2 olarsa zərbə almış sayılırıq
        else:
            print("\nYou got coup.")
            # Və hücumu öz üzərimizə yerinə yetiririk
            self.__strike(self)

        return self

    # Oyundan çıxmaq üçün quit funksiyasından istifadə edirik
    def quit(self):
         quit()

# Classa aid iki obyekt yaradırıq.
g1 = Gamer("Avatar")
g2 = Gamer("Batman")

# Əsas işləri yerinə yetiən main funksiyası yaradırıq.
def main():
    i = 1
    # Sonsuz sayda dövr edə bilməsi üçün ühile operatoruna True şərtini veririk.
    while i:
        system("cls")
        print()
        print("{} ROUND".format(i))
        i += 1
        print()
        # İstifadəçidən roundu oynamaq istəyib istəmədğini soruşuruq.
        ch = input("Are you ready for the round? Y/N\t")
        # Cavabı hə idisə yaratdığımız birinci obyektin ikinciyə hücumu reaallaşır. Və nəticələr ekrana yazdırılır
        if ch == "y" or ch == "Y":
            # Burada chaining metodundan istifadə edərək g1 obyektindən çağırılan metodlar eyni sətrdə çağırılır.

            g1.attack(g2).showthesituation()
            g2.showthesituation()
            print()
            print("=" * 60)
            print()
            # Ekranın birdən-birə deyil də istifadəçi entere basdıqdan sonra təmizlənməsi üçün boş input tələb edirik.
            input("Pres to back to menu")


        # Əgər istifadəçi yox cavabınmı verirsə hər birinin son vəziyyəti göstərilir və oyundan çıxılır.
        elif ch == "n" or ch == "N":
            print("Final situation:")
            g1.showthesituation()
            # Burada da chaining metodundan istifadə olunur
            g2.showthesituation().quit()
            print()
            # Ekranın birdən-birə deyil də istifadəçi entere basdıqdan sonra təmizlənməsi üçün boş input tələb edirik.
            input("Pres to back to menu")


        # Səhv input daxil etdikdə ekrana bildiriş gəlir.
        else:
            print("""
            Wrong input.
            Please, try again.
            """)

# Prosesləri yerinə yetirən hissə
# Sonsuz sayda dövr edə bilməsi üçün ühile operatoruna True şərtini veririk.
while True:
    # H'r dövrdə ekranın təmizlənməsi üçün (terminalda) os modulunun sys funksiyasına "cls" əmrini veririk.
    system("cls")
    print("""
    For Fight - F
    For quit - Q
    """)

    # Print etdiyimiz seçimlərdən birini seçməsi üçün istifadəçidən sorğu aparrıq
    choose = input("Make a choice: ")
    # Döyüşmək istəyirsə bayaq yaratdığımız main funksiyasını çağırırıq.
    if choose == "f" or choose == " F":
        while True:
            # Hər dövrdə ekranın təmizlənməsi üçün (terminalda) os modulunun sys funksiyasına "cls" əmrini veririk.
            system("cls")

            main()
            # Ekranın birdən-birə deyil də istifadəçi entere basdıqdan sonra təmizlənməsi üçün boş input tələb edirik.
            input("Pres to back to menu")


    # Oyundan çıxmaq istəyirsə obyekt üzərindən quit metodunu çaöırırıq.
    elif choose == "q" or choose == "Q":
        g1.quit()

    # Əks halda yalnış input daxil etdiyinə görə bildiriş göndəririk.
    else:
        print("""
    Wrong input.
    Please, try again.
    """)
