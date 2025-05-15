# Loop over the elements of the fish_list list below, logging each one. Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    if fish is 'Nemo':
        print(fish)
        break
    print(fish)