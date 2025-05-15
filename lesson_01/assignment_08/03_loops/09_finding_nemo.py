# Loop over the elements of the fish_list list below, logging each one. Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)         # moved to top of block to satisfy "logging each" req
    if fish == 'Nemo':  # changed from is to ==
        break           # removed print(fish) preceding this line