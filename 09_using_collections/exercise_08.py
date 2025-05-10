# Explain why the code below prints different values on lines 3 and 4.

# text = "It's probably pining for the fjords!"

# print(text[21:35].rfind('f'))     # 8
# print(text.rfind('f', 21, 35))    # 29

Line 3 slices the string and the substring starts at index 0. For line 4 it starts at index 21 but index 0 doesn't change.