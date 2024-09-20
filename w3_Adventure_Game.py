print('Indiana Jones, the famous archaeologist and adventurer, found himself in a dense tropical forest')
print('in search of a legendary treasure: the Serpent Necklace, a mystical artifact said to have the')
print('power to control snakes. At every step, he faced choices that would shape his journey.')
print('Indiana Jones is faced with three options: follow the shining path, explore the dark caves, consult the map.')
print('Choose one of the options below:')
print('1. PATH')  
print('2. CAVE')
print('3. MAP')


first_choice = None
valid_first_choice = ['PATH', 'CAVE', 'MAP']

while True:
    first_choice = input('Enter the name of the desired option PATH, CAVE or MAP: ')
    # Get user input for first choice
    
    #if first_choice.upper() in valid_first_choice:
        #break
        
    # Check user choice and provide corresponding output
    if first_choice.upper() == "PATH":
        print('1. Jones decides to follow an old paved path, a sign of a lost civilization.')
        print('Along the illuminated path which of the following should Indiana Jones do: Explore the ruins, Follow the ancient inscriptions or look for traps.')
        print('Choose one of the options below:')
        print('1.1 EXPLORE')  
        print('1.2 INSCRIPTIONS')
        print('1.3. TRAPS')
        
        second_choice = None
        while second_choice not in ['EXPLORE', 'INSCRIPTIONS', 'TRAPS']:
        
            second_choice = input('Enter the name of the desired options EXPLORE, INSCRIPTIONS or TRAPS: ')
            
            if second_choice.upper() == 'EXPLORE':
                print('1.1 He decides to EXPLORE the ancient ruins he found along the way, which of the following should Indiana Jones do: Investigate Artifacts, Study Mural Paintings or Skip the Ruins?')
                print('Choose one of the options below:')
                print('1.1.1 INVESTIGATE')  
                print('1.1.2. MURAL PAINTINGS')
                print('1.1.3. SKIP')
                
                third_choice = None
                valid_choices = ['INVESTIGATE', 'MURAL PAINTINGS', 'SKIP']
                
                while third_choice not in ['INVESTIGATE', 'MURAL PAINTINGS', 'SKIP']:
                    
                    user_input = input('Enter the name of the desired option - INVESTIGATE, MURAL PAINTINGS or SKIP: ')
                    third_choice = user_input.upper()
                    
                    if third_choice == 'INVESTIGATE':
                        print()
                        print('1.1.1 Indiana Jones decides to INVESTIGATE specific artifacts in the ruins for clues.')
                                
                    elif third_choice == 'MURAL PAINTINGS':
                        print()
                        print('1.1.2 He chooses to study the MURAL PAINTINGS, seeking information about local history.')
                        
                    elif third_choice == 'SKIP':
                        print()
                        print('1.1.3 Suspicious, he chooses not to stop at the ruins and continue the search for the Necklace.')
                    else:
                        print()
                        print('Chose just one of the options: INVESTIGATE, MURAL PAINTINGS or SKIP.')
            
            elif second_choice.upper() == 'INSCRIPTIONS':
                print('1.2 Indiana chooses to follow enigmatic INSCRIPTION on the walls that seem to point to a hidden temple.')
                print('At this moment he is faced with three options, which one should he follow?\
                    Decipher the transcripts, ignore the transcripts or Mark the Path?')
                print('1.2.1. DECIPHER')  
                print('1.2.2. IGNORE')
                print('1.2.3. MARK')
                
                                             
            elif second_choice.upper() == 'TRAPS':
                print('1.2.3 You chose TRAPS.')
            else: 
                print('Chose just one of the options: EXPLORE, INSCRIPTIONS or TRAPS.')
            
    elif first_choice.upper() == "CAVE":
        print('2. Inside the dark CAVES, Indiana Jones is faced with three decisionsto choose from: Follow the Mysterious Glow,\
            Use Torches or Hear Distant Sounds')
        print('2.1. GLOW')  
        print('2.2. TORCHES')
        print('2.3. SOUNDS')
        
        second_choice_cave = None
        
        while second_choice_cave not in ['GLOW', 'TORCHES', 'SOUNDS']:
            second_choice_cave = input('Enter the name of the desired option - GLOW, TORCHES or SOUNDS: ') 
            
            if second_choice_cave.upper() == 'GLOW':
                print('2.1 You chose to follow the MYSTERIOUS GLOW. This part of the story is under construction.')
            # You might want to add more details or options for the user here.
            
            elif second_choice_cave.upper() == 'TORCHES':
                print('2.2 You chose TORCHES. This part of the story is under construction.')
            # You might want to add more details or options for the user here.

            elif second_choice_cave.upper() == 'SOUNDS':
                print('2.3 You chose to HEAR DISTANT SOUNDS. This part of the story is under construction.')
            # You might want to add more details or options for the user here.

            else:
                print('Invalid choice. Please type the word corresponding to one of the options: GLOW, TORCHES, or SOUNDS.')

        
    elif first_choice.upper() == "MAP":
        print("3. When studying the MAP, Indiana Jones faces three choices: \nChoose the Shortest Path, Analyze Forgotten Symbols or Search for Landmarks ")
         
        
        while True:
            
            second_choice_map = input('Enter the name of the desired option \n3.1 SHORTEST PATH \n3.2 SYMBOLS \n3.3 LANDMARKS: ') 
            if second_choice_map.upper() in ['SHORTEST PATH', 'SYMBOLS', 'LANDMARKS']:
                break
            else:
                print('\033[0;31mInvalid choice. Please type one of the options - SHORTEST PATH, SYMBOLS or LADMARKS only.\033[m') 
            # if second_choice_map.upper() in valid_map_choices:
            #    break
            #else:
            #    print('Invalid choice. Please type one of the options above.')
                
                
            if second_choice_map.upper() == 'SHORTEST PATH':
                print('3.1 You chose the SHORTEST PATH. This part of the story is under construction.')
                # You might want to add more details or options for the user here.
                
            elif second_choice_map.upper() == 'SYMBOLS':
                print('3.2 You chose to ANALYZE FORGOTTEN SYMBOLS. This part of the story is under construction.')
                # You might want to add more details or options for the user here.

            elif second_choice_map.upper() == 'LANDMARKS':
                print('3.3 You chose to SEARCH FOR LANDMARKS. This part of the story is under construction.')
                # You might want to add more details or options for the user here.
            
            #else: 
                #print('Invalid choice. Please type one of the options - SHORTEST PATH, SYMBOLS or LADMARKS only.')
  
    else:
        print()
        print('\033[0;31mInvalid choice. Please type the word corresponding to one of the options: PATH, CAVE or MAP.\033[m')

