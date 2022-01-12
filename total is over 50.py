# #hi! My name is: Mohamed Abdulsalam..
#practice cource..
# #challeange (5.1)
"""
Set the total to 0 to start with.
While the total is 50 or less,
ask the user to input a number.
Add that number to the total and print the message “The total is… [total]”.
Stop the loop when the total is over 50. Upload program to GitHub and past the link.

"""
total = 0

while total<=50:
    num=int(input("Enter number:"))
    total+=num
    print("The total is", total)