#Katelyn Alloway
#This program is going to be set up as a patient check-in file at a medical building.
print("Hello! Welcome to the Alloway Family Medical Center!")
print("My name is Katelyn Alloway, but I go by Katey and I will be your virtual assistant!")
print("If there are any questions or concerns, feel free to send an email to kmalloway0651@eagle.fgcu.edu")
print("Please answer the following questions:")
print("What is your name?")
name= ("Katey Alloway.")
print("My name is",name)
print("How old are you?")
age= (20-2)
#I used subtraction 20-2 to equal 18 because I'm 18 years old.
print("I am", age, "years old.")
print("What is your date of birth?")
print('I was born on 11','26', '2002',sep='-')
#With the help of POGIL and Brianna a team member of mine helped me to use sep. Sep uses the - to separate the dates.
print("How tall are you?")
heightFeet= (1+4)
#I used addition to equal 5 since I am 5 feet tall. 
heightInches= (2*3)
#I used multiplication 2 times 3 to equal 6 because I am 6 inches tall
print("I am", heightFeet, "feet", heightInches, "inches tall.")
#Brianna Berent helped me because I couldn't figure out how I should put the feet and inches after the numbers.
print("How much do you weigh?")
weight= (633/6)
#630/6 equals 105 so I kept guessing numbers a little higher divided by 6 until it equaled 105.5)
print("I weigh", weight, "pounds.")
print("Thank you for your information!" '\n' "What brings you in today?")
#the \n function moves the sentence onto the next line showing it is 2 separate thoughts.
daysInjured= 9%10
print("I have had a headache for the last", daysInjured, "days and it won't go away.")
#The % function gives the remainder of the function, I used it to explain that the patient has had a headache for long and it won't go away.
print("Oh no! On a scale from 1-10 how bad is your pain?")
pain= 2**3
print("I would say an", pain, "on a scale from 1-10.")
#The ** is an exponent, i did 2**3 to symbolize an 8 is how bad it hurts.
print("I am so sorry! About how many hours of sleep would you say you're getting a night?")
sleepingNights= 28//5
print("Around", sleepingNights, "hours a night.")
#the // function divides the numbers, but does the closest whole number with no remainder.
print("Okay. Only 5 hours a night? That could be a contributing factor to the headaches. Are you feeling any other symptoms?")
string1 = "A low grade fever"
string2 = " and a small stomach ache."
#had to add a space before the word and so it separates the 2 strings with a space. 
string_combined = string1+string2
print(string_combined)
print("Okay. I will add all of this to the file for your doctor that you will meet with shortly is aware.")
string3 = "Thank you!"
print(string3*2)
print("Of course! I hope you begin to feel better soon, Dr. Alloway will now see you.")
print("Okay! Thank you so much! Have a good day.")
print("You do the same.")
print("Hello", name, "I hear you've been feeling sick! Approximately how long has this been going on?")
count=+9
print("This has been going on for about", count, "days.")
print("Oh no! I'm sorry to hear that, that is not good! I am going to run a few tests on you to see if we can find out what is going on.")
print("Okay sounds good, thank you.")
print("First we are going to draw blood and take your blood levels to see if something is wrong there.")
print("Okay.")
#Now I am going to do the if statements to integrate them to see what is wrong with the patient.
blood=float(input("Enter blood levels of blood urea nitrogen (BUN): "))
if blood>=20:
      print("Infection! :0")
elif blood>=15:
    print("Normal!")
elif blood>=10:
    print("Okay!")
elif blood<=5:
    print("Malnutrition! :0")
else:
    print("Kidney failure! :(")
#The normal range of BUN levels in blood is between 6-20mg.
#I used "if" to show if the answer is higher than 20 than the program needs to tell the patient they have an infection.
#I used "elif" to show that any other answer needs to respond to the corresponding word that matches the amount
print("Let me run some more tests to see if anything else is going on.")
print("Okay.")
def main():
      first_test = int(input("What is your pain on a scale in your abdomin between 1 and 10: "))
      second_test = int(input("What is your pain scale in your head between 1 and 10: "))
      operator = input("Enter a '+' if your pain is getting worse or a '-' if it is getting better: ")

      if operator == '+':
            print("You are going to need to be admitted.")
      elif operator == '-':
            print("You are able to go home tonight, but we will need you to come visit again.")
      else:
            print("Unsuccessful results. Test again.")

main()
total = 0
for total_days_experienced in range(5):
      days_experienced=int(input("Enter a number for how long you have been experiencing this pain: "))
      total += days_experienced
      print("Okay,so you've been experiencing this for:", total, "days.")
total = 0
for total_days_experienced in range(5):
      days_experienced=int(input("Enter a number for how long you have been experiencing this pain: "))
      total -= days_experienced
      print("Okay,so you've been experiencing this for:", total, "days.")
print("So the amount of days is:", days_experienced, "correct?")
days_experienced = True
while days_experienced:
      day1 = int(input("What was your pain scale the first day?: "))
      day2 = int(input("What was your pain scale the second day?: "))
      day3 = int(input("What was your pain scale the third day?: "))
      day4 = int(input("What was your pain scale the fourth day?: "))
      maximum_of_days =  max(day1, day2, day3, day4)
      print("So on the:", maximum_of_days, "is the day you experienced the most pain.")
      other = input("Type 'yes' is that is correct.")
      if other != 'y':
            days_experienced = False
print("Alright, this is good information.")
      

