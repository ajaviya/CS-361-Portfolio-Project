# Name: Anthony Javiya
# Course: 361 - Intro to Software Engineering I
# Date: 07/16/2023
# Description:: This program contains my Willamette Fish Facts App which satisfies the requirements for Milestone #1.
#               Note it currently has the fish data hardcoded within functions in order to display interactivity. This
#               data will later be stored in my partner's code as a microservice which this program calls upon to get
#               the results for.

import sys
from PIL import Image
import random


def mainmenu():

    while True:
        print("\n-----------------------------------------------")
        print('\nW I L L A M E T T E   F I S H  F A C T S')
        print('\nWelcome! Explore the local fish of the Willamette River by selecting one of the options below: ')
        print('1. Search by name')
        print('2. Advanced search')
        print('3. Generate information for a random fish')
        print('4. Other information')
        print ('Q. Quit')
        print("\n-----------------------------------------------")
        option = input ('\nSelect an option: ')
        if option.lower () == 'q':
            sys.exit()
        elif option == '1':
            searchByNameMenu()
        elif option == "2":
            advancedSearchMenu()
        elif option == "3":
            randomFishGen()
        elif option == "4":
            return otherInfo()
        else:
            print ('Invalid selection!')


def searchByNameMenu():

    while True:
        print("\n-----------------------------------------------")
        print('\nSEARCH BY NAME')
        print("\nPlease enter the name of a fish you want information on: ")
        print('L. See list of fish names')
        print('B. Back to Main Menu')
        print('Q. Quit')
        print("\nNeed help picking a fish name? Enter L instead of a fish name to see a list of fish")
        print("\n-----------------------------------------------")
        option = input('\nFish name: ')
        if option.lower() == 'q':
            sys.exit()
        elif option.lower() == 'b':

            return mainmenu()
        elif option.lower() == 'l':
            fishList()

        elif option.lower() == 'channel catfish':
            channel_catfish()

        elif option.lower() == 'yellow perch':
            yellow_perch()

        elif option.lower() == 'reticulate sculpin':
            reticulate_sculpin()

        elif option.lower() == "starry flounder":
            starry_flounder()

        elif option.lower() == "white sturgeon":
            white_sturgeon()

        elif option.lower() == "smallmouth bass":
            smallmouth_bass()

        elif option.lower() == "northern pikeminnow":
            northern_pikeminnow()

        elif option.lower() == "bluegill":
            bluegill()

        elif option.lower() == "black crappie":
            black_crappie()

        elif option.lower() == "common carp":
            common_carp()

        elif option.lower() == "chinook salmon":
            chinook_salmon()
        else:
            print('Invalid selection!')


def fishList():
        print("\n-----------------------------------------------")
        print("\nList of Fish found in Willamette River:")
        print("\nYellow Perch")
        print("Channel Catfish")
        print("Reticulate Sculpin")
        print("Starry Flounder")
        print("White Sturgeon")
        option2 = input("\nEnter Y to load more or N to return to the Search By Fish Name menu: ")
        if option2.lower() == "n":
            return searchByNameMenu()

        elif option2.lower() == "y":
            print("\nSmallmouth Bass")
            print("Northern Pikeminnow")
            print("Bluegill")
            print("Black Crappie")
            print("Common Carp")
            print("Chinook Salmon")
            print("\n-----------------------------------------------")
        else:
            print("Invalid entry. Please try again")
            return fishList()


def advancedSearchMenu():
    print("\n-----------------------------------------------")
    print("\nAdvanced Search")
    print("1. Search by Attribute")
    print("B. Return to main menu")
    print("\n-----------------------------------------------")
    option = input("Please select an option: ")
    if option.lower() == "b":
        return mainmenu()
    elif option == "1":
        return searchByAttributeMenu()
    else:
        print("Invalid selection. Please try again.")
        return advancedSearchMenu()

def searchByAttributeMenu():
    print("\n-----------------------------------------------")
    print("\nSearch By Attribute")
    print("\nPlease enter an attribute to filter fish results by")
    print("Eligible attributes include: Native/Invasive, Game Fish, and Commonly Eaten")
    print("N. Native")
    print("I. Invasive")
    print("G. Game Fish")
    print("C. Commonly Eaten")
    print("B. Back to main menu")
    print("\n-----------------------------------------------")
    option = input("Enter an attribute: ")
    if option.lower() == "b":
        return mainmenu()
    elif option.lower() == "n":
        response = proceed_check()
        if response == 1:
            yellow_perch()
            reticulate_sculpin()
            starry_flounder()
            white_sturgeon()
            northern_pikeminnow()
            chinook_salmon()
        elif response == 2:
            searchByAttributeMenu()

    elif option.lower() == "i":
        response = proceed_check()
        if response == 1:
            channel_catfish()
            smallmouth_bass()
            black_crappie()
            common_carp()
        elif response == 2:
            searchByAttributeMenu()

    elif option.lower() == "g":
        response = proceed_check()
        if response == 1:
            yellow_perch()
            channel_catfish()
            smallmouth_bass()
            black_crappie()
            chinook_salmon()
            white_sturgeon()
        elif response == 2:
            searchByAttributeMenu()

    elif option.lower() == "c":
        response = proceed_check()
        if response == 1:
            yellow_perch()
            channel_catfish()
            smallmouth_bass()
            chinook_salmon()
        elif response == 2:
            searchByAttributeMenu()

    else:
        print("Invalid selection. Please try again")
        return searchByAttributeMenu()


def randomFishGen():
    num = random.randint(1, 10)
    if num == 1:
        yellow_perch()
    if num == 2:
        channel_catfish()
    if num == 3:
        reticulate_sculpin()
    if num == 5:
        starry_flounder()

    if num == 5:
        white_sturgeon()

    if num == 6:
        smallmouth_bass()

    if num == 7:
        northern_pikeminnow()

    if num == 8:
        black_crappie()

    if num == 9:
        common_carp()

    if num == 10:
        chinook_salmon()

def otherInfo():
    print("\n-----------------------------------------------")
    print("\nOther Information")
    print("1. Freshwater Conservation Efforts in Oregon")
    print("2. Oregon Fishing License")
    print("B. Return to main menu")
    print("\n-----------------------------------------------")
    option = input("Please select an option: ")
    if option.lower() == "b":
        return mainmenu()
    elif option == "1":
        return conservationmenu()
    elif option == "2":
        return fishingmenu()
    else:
        print("Invalid selection. Please try again.")
        return advancedSearchMenu()

def conservationmenu():
    print("\n-----------------------------------------------")
    print("\nFreshwater Conservation Efforts in Oregon")
    print("See this link for more info:  https://www.oregonconservationstrategy.org/overview/")
    print("B. Return to main menu")
    print("\n-----------------------------------------------")
    option = input("Please select an option: ")
    if option.lower() == "b":
        return mainmenu()
    else:
        print("Invalid selection. Please try again.")
        return conservationmenu()

def fishingmenu():
    print("\n-----------------------------------------------")
    print("\nState of Oregon Fishing License Information")
    print("See this link for more info:  https://myodfw.com/fishing/licensing-info")
    print("B. Return to main menu")
    print("\n-----------------------------------------------")
    option = input("Please select an option: ")
    if option.lower() == "b":
        return mainmenu()
    else:
        print("Invalid selection. Please try again.")
        return fishingmenu()


def proceed_check():
    print("\n-----------------------------------------------")
    print("\nThis search will present information and photos for all fish which match the chosen attribute. Are you sure you want to proceed? Enter Y to continue, or N to return back to the Search by Attribute Menu. ")
    print("\n")
    option = input("Continue?: ")
    if option.lower() == "y":
        return 1
    elif option.lower() == "n":
        return 2
    else:
        print("Invalid selection, please try again.")
        proceed_check()
def channel_catfish():
    print("\n-----------------------------------------------")
    print("\nC H A N N E L  C A T F I S H (Ictalurus punctatus)")
    print("\nNative?: No")
    print("\nHabitat: ")
    print(
        "They usually prefer freshwater habitats. You can find them in lakes, ponds, streams, creeks, reservoirs, and more. They prefer deeper habitats and water bodies with currents.")
    print("\nDiet: ")
    print(
        "Adult channel catfish, over 45 cm (17.7 in), consume fishes such as yellow perch and sunfish. The diet of adults consists of snails, clams,[12] crustaceans (such as crayfish[12]), snakes, frogs, small fish, insects, aquatic plants, algae, seeds, grains, nuts, and even small birds and small mammals occasionally. Younger channel catfish are more consistently omnivorous, eating a large variety of plants and animals.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\channel catfish.jpg")
    im.show()


def yellow_perch():
    print("\n-----------------------------------------------")
    print("\nY E L L O W  P E R C H (Perca flavescens)")
    print("\nNative?: Yes")
    print("\nHabitat: ")
    print(
        "Yellow perch are commonly found in the littoral zones of both large and small lakes, but also inhabit slow-moving rivers and streams, brackish waters, and ponds. Due to human intervention, they are currently found in many man-made lakes, reservoirs, and river impoundments. The perch are most abundant in lakes that may be warm or cool and are extremely productive in smaller lakes where they can dominate unless controlled by predation.")
    print("\nDiet: ")
    print(
        "Primarily, age and body size determine the diets of yellow perch. Zooplankton is the primary food source for young and larval perch. By age one, they shift to macroinvertebrates, such as midges and mosquitos. Large adult perch feed on invertebrates, fish eggs, crayfish, mysid shrimp, and juvenile fish. They have been known to be predominantly piscivorous and even cannibalistic in some cases. About 20% of the diet of a yellow perch over 32 g (1.1 oz) in weight consists of small fish. Maximum feeding occurs just before dark, with typical consumption averaging 1.4% of their body weight.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\yellow perch.jpg")
    im.show()


def reticulate_sculpin():
    print("\n-----------------------------------------------")
    print("\nR E T I C U L A T E  S C U L P I N (Cottus perplexus)")
    print("\nNative?: Yes")
    print("\nHabitat: ")
    print("Usually inhabits rubble and gravel-bottomed pools and riffles of headwaters, creeks and small rivers, but can shift to other habitats depending on the environmental conditions and composition of fish communities. ")
    print("\nDiet: ")
    print("The diet of Reticulate Sculpins is made up of mostly aquatic invertebrates such as mayflies, stoneflies, beetles, caddisflies, and chironomid midges.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\reticulate sculpin.jpg")
    im.show()

def starry_flounder():
    print("\n-----------------------------------------------")
    print("\nS T A R R Y  F L O U N D E R (Platichthys stellatus)")
    print("\nNative?: Yes")
    print("\nHabitat: ")
    print("The primary habitat for this species is within mud, sand, or gravel bottoms from 0–375 m (1230 ft), but most commonly above 146 m (479 ft). They are usually found near shore and often enter brackish or even fresh water on occasion. Highly salinated water is something this fish stays away from because of its inability to keep its cells from becoming hypersalinated.")
    print("\nDiet: ")
    print("The starry flounder before metamorphosis is dependent upon planktonic organisms as a food source during its younger stage of life. Feeding is usually done by waiting for the prey to settle to the floor or around eye level of the flounder and then make a quick lunge at the food drawing a mouthful of water also to help pull the prey in. As the fish develops more, they are able to feed upon small clams, some larger fish, invertebrates and also worms. When the starry flounder reaches adulthood the primary stomach contents that has been found are clams. Clams that are too large for ingestion often have their siphons eaten.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\starry flounder.jpg")
    im.show()

def white_sturgeon():
    print("\n-----------------------------------------------")
    print("\nW H I T E  S T U R G E O N (Acipenser transmontanus)")
    print("\nNative?: Yes")
    print("\nHabitat: ")
    print("White sturgeon are primarily found in large freshwater streams and estuaries along the Pacific coast, but will occasionally undertake extensive ocean travels inside the 50-fathom line.")
    print("\nDiet: ")
    print("Juveniles less than 600 mm (2.0 ft) TL are known to feed on tube-dwelling amphipods, mysids, isopods, (Corophium) spp, and other benthic invertebrates, as well as on the eggs and fry of other fish species. Adults greater than 600 mm (2.0 ft) consume a variety prey species, adjusting to a piscivorous diet of herring, shad, starry flounder, goby, smelt, anchovy, lamprey, and salmon, as well as benthic items such as invasive overbite clam. With feeding movements influenced due to tidal cycles, studies show more active movement at night, hinting that white sturgeon may be nocturnal foragers.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\white sturgeon.jpg")
    im.show()

def smallmouth_bass():
    print("\n-----------------------------------------------")
    print("\nS M A L L M O U T H  B A S S (Micropterus dolomieu)")
    print("\nNative?: No")
    print("\nHabitat: ")
    print("The smallmouth bass is found in clearer water than the largemouth, especially streams, rivers, and the rocky areas and stumps and also sandy bottoms of lakes and reservoirs. It can also survive in a stronger current than other black bass. The smallmouth prefers cooler water temperatures than its cousin the largemouth bass, and as a result will often seek out deeper, faster moving water during the hot summer months.")
    print("\nDiet: ")
    print("Carnivorous, its diet comprises crayfish, amphibians, insects, and smaller fish, while the larvae feed on various zooplankton and insect larvae. Adults also cannibalize young of other parents.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\smallmouth bass.jpg")
    im.show()


def northern_pikeminnow():
    print("\n-----------------------------------------------")
    print("\nN O R T H E N  P I K E M I N N O W (Ptychocheilus oregonensis)")
    print("\nNative?: Yes")
    print("\nHabitat: ")
    print("Common in the main river channel and in sloughs, tributaries, and seasonal watercourses")
    print("\nDiet: ")
    print("Omnivorous, but prey upon invertebrates when young and feed more on fish as they grow larger")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\northern pikeminnow.jpg")
    im.show()


def bluegill():
    print("\n-----------------------------------------------")
    print("\nS M A L L M O U T H  B A S S (Lepomis macrochirus)")
    print("\nNative?: No")
    print("\nHabitat: ")
    print("Common in sloughs, tributaries, and seasonal watercourses")
    print("\nDiet: ")
    print("Terrestrial and aquatic insects along with small fish, other small animals, and some plants")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\bluegill.jpg")
    im.show()


def black_crappie():
    print("\n-----------------------------------------------")
    print("\nB L A C K  C R A P P I E (Pomoxis nigromaculatus)")
    print("\nNative?: No")
    print("\nHabitat: ")
    print("Occasionally found in sloughs, tributaries, and seasonal watercourses")
    print("\nDiet: ")
    print("Juveniles eat small insects, plants, and animals. Adults tend to eat more fish.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\black crappie.jpg")
    im.show()


def common_carp():
    print("\n-----------------------------------------------")
    print("\nC O M M O N  C A R P (Cyprinus carpio)")
    print("\nNative?: No")
    print("\nHabitat: ")
    print("Common throughout the main river channel and in sloughs and tributaries. Occasionally found in seasonal watercourses. ")
    print("\nDiet: ")
    print("Usually feed on the bottom. Eat plants, insects, worms, and other small animals including fish. During summer, they also feed on berries and seeds that fall into the water.")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\common carp.jpg")
    im.show()


def chinook_salmon():
    print("\n-----------------------------------------------")
    print("\nC H I N O O K  S A L M O N (Oncorhynchus tshawytscha)")
    print("\nNative?: Yes")
    print("\nHabitat: ")
    print("Juveniles are common in the main river channel and in sloughs, tributaries, and seasonal watercourses, but seldom far from permanent waters.")
    print("\nDiet: ")
    print("Aquatic and terrestrial insects; crustaceans and other invertebrates")
    print("\n-----------------------------------------------")
    im = Image.open("C:\\Users\\tonyj\\CS-361-Projects\\milestone_1\\chinook salmon.jpg")
    im.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainmenu()


