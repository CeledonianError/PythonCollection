#####----- Simple Calculator start -----#####
def simpleCalc():
  while True:
    try:
      print("Please input 2 numbers")
      inputNums = [int(input("\n> ")), int(input("> "))]
      options = ["A", "S", "D", "M", "E"]
      optionsLow = ["a", "s", "d", "m", "e"]
      prevError = False

      if prevError == True:
        print("\nHow would you like to manipulate the numbers " + str(inputNums[0]) + " and " + str(inputNums[1]) + "? \n[A]dd \n[S]ubtract \n[D]ivide \n[M]ultiply \n[E]xponent \nTo quit, type \"quit\"")
        prevError = False
      else:
        print("\nHow would you like to manipulate these numbers? \n[A]dd \n[S]ubtract \n[D]ivide \n[M]ultiply \n[E]xponent \nTo quit, type \"quit\"")

      selOp = input("\n> ")

      if selOp == "quit":
        break
        # Addtion
      if selOp == options[0] or selOp == optionsLow[0]:
        print("\n" + str(inputNums[0]) + " + " + str(inputNums[1]) + " = " + str(inputNums[0] + inputNums[1]) + "\n")
        # Subtraction
      elif selOp == options[1] or selOp == optionsLow[1]:
        print("\n" + str(inputNums[0]) + " - " + str(inputNums[1]) + " = " + str(inputNums[0] - inputNums[1]) + "\n")
        # Division
      elif selOp == options[2] or selOp == optionsLow[2]:
        print("\n" + str(inputNums[0]) + " / " + str(inputNums[1]) + " = " + str(inputNums[0] / inputNums[1]) + "\n")
        # Multiplication
      elif selOp == options[3] or selOp == optionsLow[3]:
        print("\n" + str(inputNums[0]) + " * " + str(inputNums[1]) + " = " + str(inputNums[0] * inputNums[1]) + "\n")
        # Exponent
      elif selOp == options[4] or selOp == optionsLow[4]:
        print("\n" + str(inputNums[0]) + "^" + str(inputNums[1]) + " = " + str(inputNums[0] ** inputNums[1]) + "\n")
      else:
        print("\"" + selOp + "\" is not an option!\n")
        prevError = True
    except:
      print("Invalid Input! Whole numbers only")
#####----- Simple Calculator end -----#####