movies={"barbie": "9am", "John Wick": "12pm", "Chosen":"3pm", "Dracula":"9pm"}

userchoice= input("What movie do you want to see?:")
showtime= movies.get(values)

if showtime== None:
    print()
else:
    print("Movie not showing today.")

