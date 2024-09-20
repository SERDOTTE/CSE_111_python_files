# Adventure Game - Rodrigo Serdotte. This game has a history that user will respond the questions choosing alternatives that will change 
# the plot of the story
# This history has many options, each choose he made, the history will change
#The main purpose of this project is to practice the if, elif and else functions


print()
print('\033[93m***********************************************************************************************************')
print('Indiana Jones, the famous archaeologist and adventurer, found himself in a dense tropical forest')
print('in search of a legendary treasure: the Serpent Necklace, a mystical artifact said to have the')
print('power to control snakes. At every step, he faced choices that would shape his journey.')
print('Indiana Jones is faced with three options: follow the shining PATH, explore the dark CAVES, consult the MAP.')
print('**************************************************************************************************************\033[m')  
print()

while True:
    first_choice = input('Enter the name of the desired option, chose only one: 1.PATH  2.CAVE  3.MAP: ')
           
    if first_choice.upper() in ['PATH', 'CAVE', 'MAP']:
        break
    else:
        print()
        print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: PATH, CAVE or MAP.\033[m')
        print()
        
if first_choice.upper() == 'PATH':
    print()
    print('\033[93m***********************************************************************************************************')
    print('\033[93m1. Jones decides to follow an old paved PATH, a sign of a lost civilization.\033[m')
    print('\033[93mAlong the illuminated path which of the following should Indiana Jones do: EXPLORE the ruins, \nFollow \
        the ancient INSCRIPTIONS or look for TRAPS.\033[m')
    print('**************************************************************************************************************\033[m')  
    print()
    
    while True:
        second_choice_path = input('Enter the nome of next decision, chose only one: 1.EXPLORE   2.INSCRIPTIONS   3.TRAPS: ')
             
        if second_choice_path.upper() in ['EXPLORE', 'INSCRIPTIONS', 'TRAPS']:
            break
        else:
            print()
            print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: EXPLORE, INSCRIPTIONS or TRAP.\033[m')
            print()
    if second_choice_path.upper() == 'EXPLORE':
        print()
        print('\033[93m***********************************************************************************************************')
        print('\033[93m1.1. He decides to explore the ancient ruins he found along the way.\033[m')
        print('\033[93mExploring the Indiana ruins he came across some ancient artifacts and a wall full of paintings.\n \
              Despite the beauty of the place, Indiana was afraid whether he should stop at the ruins or continue the search\n \
              for the necklace.He must choose one of the following options:: INVESTIGATE ARTIFACTS, studdy mural PAINTINGS or IGNORE ruins:\033[m')
        print('**************************************************************************************************************\033[m')  
        while True:
            third_choice_path = input('Enter the nome of next decision, chose only one: 1.INVESIGATE   2.PAINTINGS   3.IGNORE: ')
             
            if third_choice_path.upper() in ['INVESTIGATE', 'PAINTINGS', 'IGNORE']:
                break
            else:
                print()
                print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: INVESIGATE, PAINTINGS or IGNORE.\033[m')
                print()
        print('\033[93m***********************************************************************************************************')
        if third_choice_path.upper() == 'INVESTIGATE':
            print('1.1.1. When investigating the artifacts, he realized that they would do little to help him find the necklace.')
        elif third_choice_path.upper() == 'PAINTINGS':
            print('1.1.2. He chooses to study the mural paintings, seeking information about local history. ')
        elif third_choice_path.upper() == 'IGNORE':
            print('1.1.3. Suspicious, he chooses not to stop at the ruins and continue the search for the Necklace. ')
        print('**************************************************************************************************************\033[m')  
        
    elif second_choice_path.upper() == 'INSCRIPTIONS':
        print('\033[93m***********************************************************************************************************')
        print('1.2. Following the ancient inscriptions, Indiana has to choose between deciphering them, ignoring \n them or using \
            them to mark the path.: 1. DECIPHER   2. UNFOLLOW   3. MARK the path')
        print('**************************************************************************************************************\033[m')  
        while True:
            third_choice_path = input('Enter the nome of next decision, chose only one: 1. DECIPHER   2. UNFOLLOW   3. MARK the path: ')
             
            if third_choice_path.upper() in ['DECIPHER', 'UNFOLLOW','MARK']:
                break
            else:
                print()
                print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: DECIPHER, UNFOLLOW or MARK.\033[m')
                print()
        print('\033[93m***********************************************************************************************************')
        if third_choice_path.upper() == 'DECIPHER':
            print('1.2.1. He decides to spend time deciphering the inscriptions to obtain valuable information.')
        elif third_choice_path.upper() == 'UNFOLLOW': 
            print('1.2.2. Choose to ignore the inscriptions and trust your instinct to find your way.')
        elif third_choice_path.upper() == 'MARK':
            print('1.2.3. Jones decides to mark the walls so he doesn´t get lost while exploring.')  
        print('**************************************************************************************************************\033[m') 
      
    elif second_choice_path.upper() == 'TRAPS':
        print('\033[93m***********************************************************************************************************')
        print('1.3. Suspicious, he decides to look for traps before proceeding and to do so he must decide to use \n special \
              equipment to detect traps, trust his intuition to avoid traps or bypass them at the risk of encountering \n other \
              obstacles.Olhar por armagilhas: 1. Use ESPCIAL EQUIPAMENT     2. Trust in your INTUITION      3. get AROUND the traps.')
        print('**************************************************************************************************************\033[m')
        while True:
            third_choice_path = input('Enter the nome of next decision, chose only one: 1. ESPECIAL EQUIPAMENT   2. INTUITION   3. AROUND: ')
             
            if third_choice_path.upper() in ['ESPECIAL EQUIPAMENT', 'INTUITION', 'AROUND']:
                break
            else:
                print()
                print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: ESPECIAL EQUIPAMENT, INTUITION or AROUND.\033[m')
                print()
        print('\033[93m***********************************************************************************************************')
        if third_choice_path.upper() == 'ESPECIAL EQUIPAMENT':
            print('1.3.1. Jones chooses to use special equipment to detect traps. ')
        elif third_choice_path.upper() == 'INTUITION': 
            print('1.3.2. Decide to trust your intuition to avoid possible pitfalls. ')
        elif third_choice_path.upper() == 'AROUND':
            print('1.3.3. He decides to try to get around the traps, risking encountering other obstacles. ')    
        print('**************************************************************************************************************\033[m')
               
            
                    
elif first_choice.upper() == 'CAVE':
    print()
    print('\033[93m***********************************************************************************************************')
    print('2. Inside the dark CAVES, Indiana a notices that a mysterious glow is coming from one direction \nand thinks about \
    using torches to light the way, when she realizes that there are sounds in another part of the cave. \nJones is faced \
    with three decisions to choose from: Follow the Mysterious GLOW, Use TORCHES or Hear Distant SOUNDS')
    print('**************************************************************************************************************\033[m')
    
    while True:
        second_choice_cave = input('Enter the nome of next decision, chose only one: 1.GLOW   2.TORCHES   3.SOUNDS: ')
             
        if second_choice_cave.upper() in ['GLOW', 'TORCHES', 'SOUNDS']:
            break
        else:
            print()
            print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: GLOW, TORCHES or SOUNDS.\033[m')
            print()
    if second_choice_cave.upper() == 'GLOW':
        
        print()
        print('\033[93m***********************************************************************************************************')
        print('2.1 He chooses to follow a mysterious light that seems to lead him deeper into the caves.')
        print('Now he has to decide: Follow a mysterious glow, investigate the source of a light coming from the cave, \
              \n prepare for a possible attack or avoid the approaching light.')
        print('**************************************************************************************************************\033[m')
        while True:
            third_choice_cave = input('Enter the nome of next decision, chose only one: 1.LIGHT SOURCE   2.ATTACK   3.AVOID light: ')
             
            if third_choice_cave.upper() in ['LIGHT SOURCE', 'ATTACK', 'AVOID']:
                break
            else:
                print()
                print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: LIGHT SOURCE, ATTACK, AVOID.\033[m')
                print()
        print('\033[93m***********************************************************************************************************')
        if third_choice_cave.upper() == 'LIGHT SOURCE':
            print('2.1.1. Jones decides to investigate the source of the light to understand if it is friendly or hostile. ')
        elif third_choice_cave.upper() == 'ATTACK':
            print('2.1.2. Realizing a possible danger, he decides to prepare for a possible attack.')
        elif third_choice_cave.upper() == 'AVOID':
            print('2.1.3. Suspicious, he chooses to avoid the light, choosing darker paths.')
        print('**************************************************************************************************************\033[m')
        
        
    elif second_choice_cave.upper() == 'TORCHES':
        print('\033[93m***********************************************************************************************************')
        print('2.2. Indiana Jones decides to light torches to light the way, but to do so he must choose whether \nto look for \
            resources to keep the torch lit, whether to extinguish the torch or throw torches to illuminate specific areas.')
        print('**************************************************************************************************************\033[m')
        while True:
            third_choice_cave = input('Enter the nome of next decision, chose only one: 1.search for RESOURCES   2.PUT OUT the torch   3.THROW the torch away: ')
             
            if third_choice_cave.upper() in ['RESOURCES', 'PUT OUT', 'THROW']:
                break
            else:
                print()
                print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: RESOURCES, PUT OUT or THROW.\033[m')
                print()
        print('\033[93m***********************************************************************************************************')
        if third_choice_cave.upper() == 'RESOURCES':
            print('2.2.1. He decides to look for resources to replenish his torches while exploring. ')
        elif third_choice_cave.upper() == 'PUT OUT':
            print('2.2.2. He chooses to put out the torches, trying to camouflage himself in the darkness. ')
        elif third_choice_cave.upper() == 'THROW':
            print('2.2.3. Jones decides to throw a torch from a distance to illuminate specific areas. ')
        print('**************************************************************************************************************\033[m')
        
        
        
    elif second_choice_cave.upper() == 'SOUNDS':
        print('\033[93m***********************************************************************************************************')
        print('2.3. In another part of the cave he notices sounds coming constantly, Indiana Jonas must decide whether \nto identify \
            the sounds heard, ignore them and continue his search or try to contact the source of that sound in the hope of finding someone.')
        print('**************************************************************************************************************\033[m') 
        while True:
            third_choice_cave = input('Enter the nome of next decision, chose only one: 1.IDENTIFY the sounds   2.do NOT CARE about the sounds   3.search for COMPANY: ')
             
            if third_choice_cave.upper() in ['IDENTIFY', 'NOT CARE', 'COMPANY']:
                break
            else:
                print()
                print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: IDENTIFY, NOT CARE or COMPANY.\033[m')
                print()
        print('\033[93m***********************************************************************************************************')
        if third_choice_cave.upper() == 'IDENTIFY':
            print('2.3.1. He decides to identify the sounds to determine if they are imminent threats. ')
        elif third_choice_cave.upper() == 'NOT CARE':
            print('2.3.2. Choose to ignore the sounds and trust your instincts. ')
        elif third_choice_cave.upper() == 'COMPANY':
            print('2.3.3. Jones decides to look for company to face possible threats together. ')
        print('**************************************************************************************************************\033[m') 
        
elif first_choice.upper() == 'MAP':
    print()
    print('\033[93m***********************************************************************************************************')
    print('\033[93m3. When studying the MAP, Indiana Jones faces three choices. \nChoose only one: \
        lok for the SHORTEST PATH, Analyze Forgotten SYMBOLS or Search for LANDMARKS.')
    print('**************************************************************************************************************\033[m') 
    
    while True:
        second_choice_map = input('Enter the nome of next decision, chose only one: 1.SHORTEST PATH   2.SYMBOLS   3.LANDMARKS: ')
             
        if second_choice_map.upper() in ['SHORTEST PATH', 'SYMBOLS', 'LANDMARKS']:
            break
        else:
            print()
            print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: SHORTEST PATH, SYMBOLS or LANDMARKS.\033[m')
            print()
    if second_choice_map.upper() == 'SHORTEST PATH':
        print()
        print('\033[93m***********************************************************************************************************')
        print('3.1 He chooses to follow the shortest route indicated on the map.')
        print('Who has to make one of the following decisions: SPEED up the pace, STUDY the terrain or look for SHORTCUTS')
        print('**************************************************************************************************************\033[m') 
        while True:
            third_choice_map = input('Enter the nome of next decision, chose only one: 1.SPEED up the pace   2.STUDY the terrain   3.search for SHORTCUTS: ')
             
            if third_choice_map.upper() in ['SPEED', 'STUDY', 'SHORTCUTS']:
                break
            else:
                print()
                print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: SPEED, STUDY or SHORTCUTS.\033[m')
                print()
        print('\033[93m***********************************************************************************************************')
        if third_choice_map.upper() == 'SPEED':
            print('3.1.1. Jones decides to quicken his pace to take the shortest route as quickly as possible. ')
        elif third_choice_map.upper() == 'STUDY':
            print('3.1.2. Choose to study the terrain while taking the shortest route. ')
        elif third_choice_map.upper() == 'SHORTCUTS':
            print('3.1.3. He decides to look for shortcuts that can shorten the path even further.')
        print('**************************************************************************************************************\033[m') 
        
        
    elif second_choice_map.upper() == 'SYMBOLS':
        print('\033[93m***********************************************************************************************************')
        print('3.2. Jones decides to analyze forgotten symbols on the map for additional clues.')
        print('So what should he do: look for HIDDEN meanings, COMPARE with the records he already has or ask for help from translation EXPERTS')
        print('**************************************************************************************************************\033[m') 
        while True:
                third_choice_map = input('Enter the nome of next decision, chose only one: 1.search for HIDDEN meanings   2.COMPARE with old records   3.ask for help from EXPERTS: ')
                
                if third_choice_map.upper() in ['HIDDEN', 'COMPARE', 'EXPERTS']:
                    break
                else:
                    print()
                    print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: HIDDEN, COMPARE or EXPERTS.\033[m')
                    print()
        print('\033[93m***********************************************************************************************************')            
        if third_choice_map.upper() == 'HIDDEN':
            print('3.2.1. He chooses to look for hidden meanings in symbols to better understand the region. ')
        elif third_choice_map.upper() == 'COMPARE':
            print('3.2.2. Jones decides to compare the symbols with ancient records to gain valuable insights. ')
        elif third_choice_map.upper() == 'EXPERTS':
            print('3.2.3. He decides to send images of the symbols for experts to decipher. ')
        print('**************************************************************************************************************\033[m')
    
    
    elif second_choice_map.upper() == 'LANDMARKS':
        print('\033[93m***********************************************************************************************************') 
        print('3.3. He chooses to look for landmarks in the forest before deciding on the path. To do this, what \n \
            he must do: CLIMB trees, follow animal TRAILS or observe the CONSTELLATION.')  
        print('**************************************************************************************************************\033[m')
        while True:
                third_choice_map = input('Enter the nome of next decision, chose only one: 1.CLIMB the trees   2.follow animal TRAILS   3.observe the CONSTELLATION: ')
                
                if third_choice_map.upper() in ['CLIMB', 'TRAILS', 'CONSTELLATION']:
                    break
                else:
                    print()
                    print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: CLIMB, TRACKS or CONSTELLATION.\033[m')
                    print()
        print('\033[93m***********************************************************************************************************') 
        if third_choice_map.upper() == 'CLIMB':
            print('3.3.1. Jones decides to climb trees to get a broader view of the area and find references. ')
        elif third_choice_map.upper() == 'TRAILS':
            print('3.3.2. Choose to follow animal tracks, trusting that they can take you to important locations. ')
        elif third_choice_map.upper() == 'CONSTELLATION':
            print('3.3.3. He decides to observe the constellation in the sky to find a safe direction. ')  
        print('**************************************************************************************************************\033[m') 
print()               
print('.... to be continue....')            
