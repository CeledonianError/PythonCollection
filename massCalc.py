#####----- Mass Calculator start ----#####
def massCalc():
  print("\n\nPlease have the following ready:")
  print(" - Mass that you were given")
  print(" - Molar mass of the chemical that you know the mass of")
  print(" - Amount of moles of each chemical")
  print(" - Molar mass of the chemical that you need to know the mass of")

  givenMassSuccess = False
  givenMolarSuccess = False
  givenMolesSuccess = False
  unknownMolarSuccess = False
  unknownMolesSuccess = False

  while True:
    ## Ask for each value
    # Given/known mass (G)
    while givenMassSuccess == False:
      try:
        print("\n\nWhat is the mass you were given?")
        givenMass = float(input("\n> "))
        givenMassSuccess = True
        break
      except:
        print("Error: Invalid input! Please only input numbers!")

    # Given/known mass chemical molar mass (k)
    while givenMolarSuccess == False:
      try:
        print(".\n.\n.\n")
        print("What is the molar mass of the chemical that you know the mass of?")
        givenMolar = float(input("\n> "))
        givenMolarSuccess = True
        break
      except:
        print("Error: Invalid input! Please only input numbers!")

    # Given/known mass chemical moles (first n)
    while givenMolesSuccess == False:
      try:
        print(".\n.\n.\n")
        print("How many moles of the \'known mass\' chemical are there?")
        givenMoles = float(input("\n> "))
        givenMolesSuccess = True
        break
      except:
        print("Error: Invalid input! Please only input numbers!")
    
    # Unknown mass chemical molar mass (c)
    while unknownMolarSuccess == False:
      try:
        print(".\n.\n.\n")
        print("What is the molar mass of the chemical you wish to know the mass of?")
        unknownMolar = float(input("\n> "))
        unknownMolarSuccess = True
        break
      except:
        print("Error: Invalid input! Please only input numbers!")

    # Unknown mass chemical moles (second n)
    while unknownMolesSuccess == False:
      try:
        print(".\n.\n.\n")
        print("How many moles of the \'unknown mass\' chemical are there?")
        unknownMoles = float(input("\n> "))
        unknownMolesSuccess = True
        break
      except:
        print("Error: Invalid input! Please only input numbers!")

  # Display input to ensure that values are correct
    print(".\n.\n.\n")
    print("The numbers you have inputted are:\n")
    print("Given/known mass: " + str(givenMass))
    print("Molar mass of chemical with known mass: " + str(givenMolar))
    print("Moles of chemical with known mass: " + str(givenMoles))
    print("Molar mass of chemical with unknown mass: " + str(unknownMolar))
    print("Moles of chemical with unknown mass: " + str(unknownMoles))

    print("\nAre these values correct? \n\n[Y]es\n[N]o")
    select = input("\n> ")
    print(".\n.\n.\n")
    if select == "N" or select == "n":
      print("Which value is incorrect?")
      print("\n[1] Given/known mass\n\tCurrent value: " + str(givenMass))
      print("\n[2] Molar mass of chemical with known mass\n\tCurrent value: " + str(givenMolar))
      print("\n[3] Moles of chemical with known mass\n\tCurrent value: " + str(givenMoles))
      print("\n[4] Molar mass of chemical with unknown mass\n\tCurrent value: " + str(unknownMolar))
      print("\n[5] Moles of chemical with unknown mass\n\tCurrent value: " + str(unknownMoles))
      print("\nAccidentally went into this menu? Type \"back\" to go back.")

    # Resetting "success" variable(s) makes program go back and redo that part
      select = input("\n> ")
      if select == "1":
        givenMassSuccess = False
      elif select == "2":
        givenMolarSuccess = False
      elif select == "3":
        givenMolesSuccess = False
      elif select == "4":
        unknownMolarSuccess = False
      elif select == "5":
        unknownMolesSuccess = False
      elif select == "back" or select == "Back":
        print("----------")
      else:
        print("Error! " + select + " is not an option! Please only use numbers 1 - 5")
    else:
      # Do calculation (u = Gnc/nk) and display it
      ## I know that "n" shouldn't be used twice in the above equation but it makes it easier to remember :)
      unknownMass = ((givenMass * (unknownMolar * unknownMoles)) / (givenMoles * givenMolar))
      print("The unknown mass is " + str(unknownMass))
      print("\nPress enter key when ready to go to final menu.")
      select = input("\n> ")

      print("Do you have another chemical you need to find the mass of?\n\n[Y]es\n[N]o")

      select = input("\n> ")
      if select == "Y" or select == "y":
        print("\n\n\nRestarting...\n\n\n\n\n\n\n\n\n\n")
        # Reset - output most of starting txt and reset all variables
        print("Please have the following ready:")
        print(" - Mass that you were given")
        print(" - Molar mass of the chemical that you know the mass of")
        print(" - Amount of moles of each chemical")
        print(" - Molar mass of the chemical that you need to know the mass of")

        givenMassSuccess = False
        givenMolarSuccess = False
        givenMolesSuccess = False
        unknownMolarSuccess = False
        unknownMolesSuccess = False
      else:
        print("Thank you for using Error's Mass Calculator!\n\n\n")
        break
        
#####----- Mass Calculator end ----#####