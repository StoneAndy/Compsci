import webbrowser as wb
import pyautogui as pg
import time as t

points = 0
show = pg.prompt ("What is your favorite show?")

if show == "the office":
    wb.open("https://www.youtube.com/watch?v=rtDzFmJNvG0")
    t.sleep(15)
    pg.alert ("That is the best show around")
    points += 20   
elif show == "parks and rec":
    wb.open("https://www.youtube.com/watch?v=SrLZgP-OR6s")
    t.sleep(15)
    pg.alert ("I think the office is better but parks and rec is a good choice")
    points += 10
elif show == "modern family":
    wb.open("https://www.youtube.com/watch?v=HbUup-3s2sM")
    t.sleep(15)
    pg.alert ("Phil is the best one on the the show")
    points += 10
elif show == "friends":
    wb.open("https://www.youtube.com/watch?v=P5TMcx0ofEc")
    t.sleep(15)
    pg.alert ("That is my brothers favorite show")
elif show == "Alf":
    wb.open("https://www.youtube.com/watch?v=MaydcVBdesU")
    t.sleep(15)
    pg.alert ("That stands for Alien Life Form")
elif show == "Gilligans Island":
    t.sleep(15)
    wb.open("https://www.youtube.com/watch?v=MaydcVBdesU")
    pg.alert ("Well gilligan, you did it again")
    points += 100
    t.sleep(15)
else:
    pg.alert ("Your favorite show is " + str(show))

    
sport = pg.prompt ("What is your favorite sport?")

if sport == "lacrosse":
    wb.open ("https://www.youtube.com/watch?v=S0TZdYqjDSg")
    t.sleep(15)
    pg.alert("you are not Paul Rabbil")
    points += 50
elif sport == "soccer":
    wb.open ("https://www.youtube.com/watch?v=K-U1ZgrsGGg")
    t.sleep(15)
    pg.alert ("Messi is bad")
    points += 10
elif sport == "hockey":
    wb.open ("https://www.youtube.com/watch?v=PT6kvPl0qEA")
    t.sleep(15)
    pg.alert ("cricket is better")
    points += 20
elif sport == "cricket":
    wb.open ("https://www.youtube.com/watch?v=DUuTU1MwAEU")
    t.sleep(15)
    pg.alert ("you should go pro")
    points += 100
elif sport == "dancing":
    wb.open ("https://www.youtube.com/watch?v=SV-eOBr6VC4")
    t.sleep(15)
    pg.alert ("That is not a sport")
elif sport == "swimming":
    wb.open ("https://www.youtube.com/watch?v=UmIYanq5gH8")
    t.sleep(15)
    pg.alert ("Michael Phelps is the fastest")
else:
    pg.alert ("Your favorite sport is " + str(sport))


animal = pg.prompt ("What is your favorite animal?")

if animal == "dog":
    wb.open ("https://www.youtube.com/watch?v=vvppaufeD3Q")
    t.sleep(15)
    pg.alert ("cool, I have 4 dogs")
    points += 40
elif animal == "cat":
    wb.open ("https://www.marthastewart.com/915432/international-cat-show-new-york-city")
    t.sleep(15)
    pg.alert ("cats are weird")
    points -= 20
elif animal == "bunny":
    wb.open ("https://www.youtube.com/watch?v=7JUEbHSmDqg")
    t.sleep(15)
    pg.alert ("they tast good")
    points += 5
elif animal == "birds":
    wb.open ("https://www.youtube.com/watch?v=OvCZDEPIco0")
    t.sleep(15)
    pg.alert ("they are basicly flying rats")
    points += 10
elif animal == "bigfoot":
    wb.open ("https://www.youtube.com/watch?v=kmzfdjJRotU")
    t.sleep(15)
    pg.alert ("That is not a animal")
    points += 200
elif animal == "chicken":
    wb.open ("https://www.youtube.com/watch?v=08wUT1ruaYU")
    t.sleep(15)
    pg.alert ("I dont like chikens, they are bad pets")
else:
    pg.alert ("Your favorite animal is " + str(animal))

   
food = pg.prompt ("What is your favorite food?")

if food == "chicken":
    wb.open ("https://www.allrecipes.com/video/851/juicy-roasted-chicken/?internalSource=picture_play&referringId=83557&referringContentType=Recipe")
    t.sleep(15)
    pg.alert ("I had chicken last night.")
    points += 10
elif food== "hamburgers":
    wb.open ("https://www.youtube.com/watch?v=Tqx5W9li6WQ")
    t.sleep(15)
    pg.alert ("I love hamburgers!")
    points += 50
elif food== "steak":
    wb.open ("https://www.youtube.com/watch?v=AmC9SmCBUj4")
    t.sleep(15)
    pg.alert ("steak is the best!")
    points += 100
elif food== "cerial":
    wb.open ("https://www.youtube.com/watch?v=uAmn1-Zn7dc")
    t.sleep(15)
    pg.alert ("its the most important meal of the day!")
elif food== "beef wellington":
    wb.open ("https://www.youtube.com/watch?v=TE2omM_NoXU")
    t.sleep(15)
    pg.alert ("Arbys, we have the meats!")
    Points += 300
elif food== "pasta":
    wb.open ("https://www.youtube.com/watch?v=UYhKDweME3A")
    t.sleep(15)
    pg.alert ("Im gluten free")
else:
    pg.alert ("Your favorite food is" + str(food))


    
MovieChar = pg.prompt ("What is your favorite MovieChar?")

if MovieChar == "Rick":
    wb.open ("https://www.youtube.com/watch?v=tZp8sY06Qoc")
    t.sleep(15)
    pg.alert ("A pickle Rick!")
    points-= 10
elif MovieChar== "Jason Borne":
    wb.open ("https://www.youtube.com/watch?v=xYG89rB6c5k")
    t.sleep(15)
    pg.alert ("its jason borne")
    points += 10
elif MovieChar== "billy madison":
    wb.open ("https://www.youtube.com/watch?v=G1PllrfeiVw")
    t.sleep(15)
    pg.alert ("stop looking at me swan")
    points += 50
elif MovieChar== "Tony Stark":
    wb.open ("https://www.youtube.com/watch?v=7H0yo-lDuk0")
    t.sleep(15)
    pg.alert ("look its iron man")
    points += 20
elif MovieChar== "buddy the elf":
    wb.open ("https://www.youtube.com/watch?v=cbQZ8GK2usU")
    t.sleep(15)
    pg.alert ("Snow ball fight!!!")
    points += 100
elif MovieChar== "Flash":
    wb.open ("https://www.youtube.com/watch?v=AXW9Hfoneuk")
    t.sleep(15)
    pg.alert ("he is fast.")
else:
    pg.alert ("Your favorite MovieChar is" + str(MovieChar))

    
pg.alert("you scored: " + str(points))
