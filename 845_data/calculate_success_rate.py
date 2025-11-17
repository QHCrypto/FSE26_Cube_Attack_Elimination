import os

def analyze_files(folder_path):
    total_files = 0
    success_count = 0
    solving_times = []
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        
        # Ensure it is a file and not a subfolder
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r') as file:
                    content = file.read()
                    
                    # Analyze "Wether success:"
                    start_idx = content.find("Wether success:")
                    if start_idx != -1:
                        start_idx += len("Wether success:")
                        number_str = content[start_idx:].split()[0]
                        if number_str == '1':
                            success_count += 1
                    
                    # Analyze "Equation solving time is"
                    time_idx = content.find("Equation solving time is")
                    if time_idx != -1:
                        time_idx += len("Equation solving time is")
                        time_str = content[time_idx:].split()[0]
                        try:
                            solving_time = float(time_str)
                            solving_times.append(solving_time)
                        except ValueError:
                            print(f"Unable to parse time value in {filename}: {time_str}")
                    
                    total_files += 1
            except (IOError, UnicodeDecodeError):
                print(f"Unable to read file: {filename}")
                continue
    
    if total_files == 0:
        print("No readable files found in the folder")
        return
    
    # Calculate success rate
    success_ratio = success_count / total_files
    
    # Calculate statistics for solving times
    if solving_times:
        max_time = max(solving_times)
        avg_time = sum(solving_times) / len(solving_times)
    else:
        max_time = avg_time = 0.0
    
    # Output results
    print(f"Total files: {total_files}")
    print(f"Number of successes (count of 1s): {success_count}")
    print(f"Success ratio: {success_ratio:.2%}")
    print(f"Maximum solving time: {max_time:.4f}s")
    print(f"Average solving time: {avg_time:.4f}s")


folder_path = "/Practical_Trivium_attack_1/845_data/845_results"  
analyze_files(folder_path)