# Rodrigo Serdotte Freitas

with open("hr_system.txt") as hr_files:
    for line in hr_files:
        data_lines = line.split(" ")
        #print(data_lines)
                   
        name = data_lines[0]
        id_number = int(data_lines[1])
        job_title = data_lines[2]
        salary = int(data_lines[3])
        
        print(f"Name: {name}, Title: {job_title}")    
        
    # After printing all lines in the above format, restart the file to the beginning
    hr_files.seek(0)    
    print()    
    for line in hr_files:
        data_lines = line.split(" ")
                   
        name = data_lines[0]
        id_number = int(data_lines[1])
        job_title = data_lines[2]
        salary = int(data_lines[3])
        
        # Print in format "{name} (ID: {id_number}), {job_title} - ${salary}"
        print(f"{name} (ID: {id_number}), {job_title} - ${salary:.2f}")    
    print()
    
    # After printing all lines in the above format, restart the file to the beginning
    hr_files.seek(0)    
    print()    
    for line in hr_files:
        data_lines = line.split(" ")
                   
        name = data_lines[0]
        id_number = int(data_lines[1])
        job_title = data_lines[2]
        salary = float(data_lines[3]) / 24
        
        if job_title == "Engineer":
            salary = (float(data_lines[3]) / 24) + 1000
        
        # Print in format "{name} (ID: {id_number}), {job_title} - ${salary}"
        print(f"{name} (ID: {id_number}), {job_title} - ${salary:.2f}")   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
