#####----- High/Low start -----#####
def highLow(maximum):
  import random

  maximum = int(maximum)
  number = random.randrange(0, maximum)
  guessCount = 0
  guessCheck = 0
  prevError = False
  guess = ""
  
  # Starts out with empty guess variable. Breaks loop once a valid guess is inputted. This is so the error handling works as intended
  while guess == "":
    try:
      guess = int(input("Please enter your guess: "))
      if guess < 0 or guess > maximum:
        print("Error: Guess outside of range!\n\n")
        guess = ""
    except:
      print("\nError: Invalid input!\n\n")

  while guess != number:
    try:
      if guess < 0 or guess > maximum:
        print("Error: Guess outside of range!\n\n")
        prevError = True
        guess = guessCheck
        if guessCount >= 0:
          guessCount -= 1
      if guess < number:
        if prevError == True:
          print("Your previous valid guess, " + str(guess) + ", was too low")
          prevError = False
        else:
          print("Your guess is too low, try again")
      else:
          if prevError == True:
            print("Your previous valid guess, " + str(guess) + ", was too high")
            prevError = False
          else:
            print("Your guess is too high, try again")
      guessCount += 1
      guessCheck = guess
      print("Number of guesses: " + str(guessCount) + "\n")
      guess = int(input("Please enter your guess: "))
      if guess == number:
        print("Hit!")
        print("It took you " + str(guessCount) + " guesses")
        break
    except:
      print("Error: Invalid input!\n\n")
      prevError = True
      if guessCount >= 0:
        guessCount -= 1
#####----- High/Low end -----#####

#####----- Mad Lib start -----#####
def madLib():
  words = [input("Input a noun: "), input("Input an adjective: "), input("Input a material: "), input("Input a body part: "), input("Input an adjective: "), input("Input a noun: "), input("Input a noun: "), input("Input an adjective: "), input("Input a noun: "), input("Input a verb: ")]
 
  print ("\nThe " + words[0] + " is a family of " + words[1] + " instruments usually made of " + words[2] + " and played with a single-reed " + words[3] + " piece. Although most " + words[0] + " are made from " + words[2] + ", they are categorized as " + words[1] + " instruments, because sound is produced by an " + words[2] + " reed rather than " + words[3] + " vibrating in a " + words[3] + "piece cup as with the " + words[2] + " instrument family. As with the other woodwind instruments, the " + words[4] + " of the note being played is controlled by covering holes in the body " + words[5] + " to control the resonant " + words[6] + " of the air column by changing the effective " + words[7] + " of the " + words[5] + ". The " + words[8] + " covers or uncovers the holes by " + words[9] + " keys.")
#####----- Mad Lib end -----#####

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

#####----- Python Who start -----#####
def pythonWho():
# An original Doctor Who adventure with the user as the Doctor's companion! Features the 11th Doctor after the series 6 finale, "The Wedding of River Song." Originally was going to take place after the the series 7 mid-series special, "The Snowmen," but tweed jacket > eggplant jacket
# Note that in this, if the user's input isn't one of the available options, it will (typically, there's some cases where the opposite is true) select the last option.
  options = ["1", "2", "3"]

  def beginning():
    print("It is a damp, foggy day. You're walking down an alleyway between two tall buildings. A wheezing wind starts to race past you, a rat scurries across the alley a few meters ahead. \nYou look up, the distant exit seems to shimmer and fade. \n\n[1] Turn back \n[2] Continue forward")
    choice = input("\n> ")
    print(".\n.\n.\n")
    if choice == options[0]:
      turnBack()
    else:
      continueForward()

  # Beginning choice 1 "Turn back"
  def turnBack():
    print("\nYou watch as a blue shape seems to push itself onto reality, and decide that this is too weird. You turn around and walk back the way you came. The wind howls. There's a loud bang joined by a church bell. The wind has stopped. There's a wooden squeak, then a young man's voice. \n\"You there! Hello!\" the voice calls. \n\n[1] Face the man \n[2] Ignore him")
    choice = input("\n> ")
    print(".\n.\n.\n")
    if choice == options[0]:
      faceTheMan()
    else:
      print("\nYou pick up your pace and race out of the alleyway, leaving the man and whatever magic he practices behind.")
      theEnd()

  # Turn back choice 1 "Face the man"
  def faceTheMan():
    print("\nYou stop. Whatever weirdness is going on here can be figured out later. You turn around, there's a bow tie-wearing man in a tweed overcoat standing in front of a large, blue box labelled \'Police PUBLIC CALL Box\' above the doors. The man lights up as you stare blankly at him. He grabs his bow tie with both hands and adjusts it. Once he considers it sufficiently adjusted, he raises a finger and points directly at you. You wince. \n\n\"Yeah! You! Come here! I need a hand.\"\n\nYou consider turning back and making a run for it, but, you've already tried that, and ended up changing your mind. You've decided this, and there's no going back.\n\n[1] Run \n[2] Walk up to the man \n\n> 2\n.\n.\n.\n")
    altWalkUpToHim()

  # Beginning choice 2 "Continue forward"
  def continueForward():
    print("\nThe weirdness doesn't bother you, so you try to continue your walk. You\'re forced to stop, as a blue box begins to form in the space in front of you. The wind howls. The howling gets louder and louder as the box seems to force itself into reality. A light on top of the box flashes in rhythm with the howling. With the distant clang of a church bell, the howling stops. Before you, a large wooden box labelled \'Police PUBLIC CALL Box\' stands tall. \n\nOne of the doors is pulled open from the inside and a bulky, young man with a large quiff of hair and a brown tweed jacket steps out. The door closes behind him. He spins around and faces the box. \n\"An alleyway? Why do you keep landing in alleyways?\" he scolds the box.")
    print("\nThe words you overhear him saying you find strange, but, not quite stranger than the box. You walk up to him and tap him on the shoulder. He spins around.\n\n\"What do you--! Oh! Wait! Could you help me? I need some help fixing things around my TARDIS.\" \n\nYou give him your best confused look. \n\n\"My box? The one I just stepped out of?\" He grumbles, \"Sometimes I wonder why I\'m fond of you guys.\"")
    thingsThatNeedFixing()

  # Alt. scene walking up to the Doctor if "turn back" was chosen
  def altWalkUpToHim():
    print("\nYou walk up to him. \"Yes! Thank you. My TARDIS needs some fixing.\"\n You give him your best confused look. \n\"My box? The one I just stepped out of?\" He grumbles, \"Sometimes I wonder why I\'m fond of you guys.\"")
    thingsThatNeedFixing()

  # Scene where the player decides what to fix
  def thingsThatNeedFixing():
    print("\n\"Anyways, despite your inability to understand the whole of time and space, you can still help. Come on in!\" He turns around and puts a key into the keyhole in the door. He pushes it open and you peek inside.")
    print("\n(Press enter to continue.)")
    choice = input("\n> ")
    print("\nIt's impossible.\n\nInside the box is an impossibly large room consisting mostly of orange and yellow hues. There's hallways twisting and turning around the edges of the room and a short staircase leading to a central console. The console is made of a large, bulbous block covered in buttons, levers and fidget toys. In the middle of the console, there's a large glass column leading to the ceiling. \nYou didn't even notice that you walked inside until you hear the man walk in behind you. \n\"I'm going to leave the door open, it\'s a bit stuffy in here.\" He takes off his coat and throws it onto a coat tree to the left of the door.\nHe runs up to the console and goes around it, flipping a lever there and pressing a button here. \n\"Making sure she's parked properly! Don\'t want to drift off into the vortex while you're helping me.\"\n\nOnce he was done, he walks up to the top of the staircase and looks down at you. \"Right! Well, now that she's anchored down, what would you like to fix?\" He then lists a bunch of various, sci-fi sounding items. \n\nThe only ones you make out are \'wibbly handler,\' \'temporal stabilizer,\' and \'telepathic circuit.\'\n\n[1] Wibbly handler \n[2] Temporal stabilizer \n[3] Telepathic circuit")
    choice = input("\n> ")
    print(".\n.\n.\n")
    if choice == options[0]:
      wobblyHandler()
    elif choice == options[1]:
      temporalStabilizer()
    else:
      telepathicCircuit()

  # Doctor asks for player's name
  def whatsYourName():
    print("\nHe urges you up to the console. \"I'm the Doctor, by the way. What's your name?\"")
    global name
    name = input("\n> ")
    print("\n\"Oh, " + name + "! That's a great name.\"\n")

  ##### Wobbly handler start #####
  ## A 98% original story as "wobbly handlers" don't exist in Doctor Who :D
  # Intro to wobbly
  def wobblyHandler():
    print("\n\"W-wobbly handler...\" you squeak out. Wobbly handler? Really? \n\"Wobbly handler! Great choice!\" The man exclaims. \nIt seems like something called the \'wobbly handler\' also exists.")
    whatsYourName()
    print("\"Come along, " + name + "! I'll show you where the wobbly handler is, and how to fix it.\"\nThe Doctor bounds over to a section of the console opposite to the staircase, you trail after him. You find him crouched down, poking at some wires on the underside of the console. As you get closer, he stands up and looks at you. He flicks his head to the side, throwing his hair out of his face. \n\n\"These wires. I need you to reconnect them. I've removed all the broken ones, so don't worry about that.\" He gestures to a pile of frayed wires on the glass floor. \nYou crouch down and look at the wires still in the console. There's 6. 3 different colours; red, yellow and blue. You reach out to connect the red wires back together. \n\n\"Stop!\" the Doctor yells. You freeze. \"What do you think you're doing?\"")
    print("\n(Press enter to continue.)")
    choice = input("\n> ")
    print("\nYou look up at him, confused. \n\n\"Red doesn't go to red! It goes to yellow. Think! It makes orange. Orange is the universal colour for... uhh,\" He pauses. \"I forget, actually. Point is, red doesn't connect to red. You need to make orange, purple and green--\" There's a distant clang of a church bell. The Doctor's face controrts into a panicked expression, \"Ohh! That w--\" He looks down at you, \"Doesn't matter! It's urgent! I think you can figure the wobbly handler out.\"\n\nHe then promptly takes off down one of the many winding halls, disappearing deeper into the TARDIS, chasing after the sound of the church bells.")
    wobblyHandlerGame()
  # Wobbly minigame
  def wobblyHandlerGame():
    def wobblyEnd():
      print("\nThere's a large spark from deep in the console and, rather suddenly, you find yourself outside in the alleyway where this all started. You hear the wind start to howl. You look over and see the box disappearing. You can hear the Doctor yelling from deep within the box. \nAfter a few seconds, the box is gone, and the wind calms down. \n\nYou rub your head. What just happened..? Hm... Oh well. You got places to be. \nYou continue down the alleyway.")
      theEnd()
    print("\n\n\nWhat did he say about the wires, again? Red doesn't connect to red? Weird. \nYou grab the top red wire and connect it to... \n\n[1] The bottom blue wire \n[2] The bottom red wire \n[3] The bottom yellow wire")
    choice = input("\n> ")
    print(".\n.\n.\n")
    if choice == options[2]:
      print("\nYou connect the top red wire to the bottom yellow wire. You hear a chirp from the console.\n")
      print("\nYou grab the top blue wire and connect it to... \n\n[1] The bottom red wire \n[2] The bottom blue wire")
      choice = input("\n> ")
      print(".\n.\n.\n")
      if choice == options[0]:
        print("\nYou connect the top blue wire to the bottom red wire. You hear another chirp from the console.\n\nOnly the top yellow wire and the bottom blue wire remain. You connect them together. The console chirps a third time.\n\nIt seems you are successful.")
        wobblyFinish()
      else:
        wobblyEnd()
    else:
      wobblyEnd()
  # Successful wobbly end
  def wobblyFinish():
    print("\n\n\nYou hear footsteps beind you. You turn around to see the Doctor walking back up the console from one of the halls. He's covered in soot.\n\"Pipes!\" He exclaims, \"Filty! Clogged! Needed a good clean.\"\nHe looks up that the glass column in the middle of the console while cleaning his hands off with a rag, \"Could've told me about me about them! No need to throw fits.\"\n\nHe looks at you while tossing the dirty rag to the side. \n\"Done with the wires, I see?\" He crouches down to examine your work, \"Good! Clean! All seems in order here. I think that's enough work for today.\"\n\nHe takes a long pause. \n\"Been a while since I had someone to travel with.\" He shifts his feet, \"All of time and the whole of space. Ready to be explored.\" He looks at you hopefully.\n\nThis \'Doctor\' is mad, you think. You knit your eyebrows. Come to think of it, everything around you right now is mad. \n\nThe Doctor softly claps, \"I'm asking if you would like to join me.\"\n\nJoin the Doctor? \n\n[1] Yes\n[2] No")
    choice = input("\n> ")
    print(".\n.\n.\n")
    if choice == options[0]:
      runWithTheDoctor()
      theEnd()
    else:
      dontRunWithTheDoctor()
      theEnd()
  ##### Wobbly handler end #####

  ##### Temporal stabilizer start #####
  ## I love the idea of 11 being dumb keeping the door open. The Weeping Angels are always after the TARDIS, so that would be a prime opportunity for them to try and steal it.
  def temporalStabilizer():
    print("\n\"T-temporal stabilizer...\" you squeak out. You recognise the word \'temporal,\' something to do with time? Hopefully it will be something that you can somewhat understand.")
    whatsYourName()
    print("\"Come along, " + name + "! I'll show you where the temporal stabilizers' pipes are, and how to fix them.\"\nHe bounds down the steps and over to a space on the wall beside the coat tree. After a quick dance of his fingers, a hexagonal panel on the wall pops open. Inside, wires and pipes glow a golden yellow. The Doctor fishes a roll of tape out from the pockets of his pants. How said roll fitted in there, you will never know.\n\n\"Here. Patch up those pipes, the temporal radiation that leaks from them makes her all grouchy and attracts all sorts of... statues. When you're done that...\" He pauses to grab a wrench from his other pocket, \"Tighten the seals a bit. While you do that, I'm going to work on the console. Yell when you're done. Make sure you yell. Can't hear you, otherwise. Head's too noisy.\"\nThe Doctor walks away and soon you hear him tinkering away at the console behind you.")
    print("\n(Press enter to continue.)")
    choice = input("\n> ")
    weepingAngels()

# The meat of this route
  def weepingAngels():
    print("\nYou look at the pipes and notice some of the \'temporal radiation\' that the Doctor mentioned. It glitters like gold and seems to fluctuate in how fast it moves. You look at the tape roll that the Doctor gave you, it's rubberized. It's Flex Tape... you think. Despite you knowing you'll most likely need scizzors, you try to tear it. \n\nIt tears with ease. You try to tear the piece you just made, and just end up sticking it to itself. You sigh in frustration, and tear another piece off of the roll. You try not to think about how weird the tape is as you patch up all the leaks you can find.\n\n\nAfter a while of patchwork, you hear a flap of wings from outside as you reach for the  wrench. You look over and see a stone statue of an angel. It has its face buried in its palms.\n\n[1] Ignore it \n[2] Approach it \n[3] Tell the Doctor")
    choice = input("\n> ")
    print(".\n.\n.\n")
    if choice == options[0]:
      print("You look away from it. It's weird, yes, but everything around you right now is weird. You lift up the wrench. It looks like a normal wrench, but after the tape ordeal, you don't trust anything that seems to be normal. You bring the wrench to the top of one of the pipes. There's a breeze behind you. You roll your eyes and turn around. The statue you saw earlier is standing in front of you, its arm outstretched, touching you on the shoulder. You hear the Doctor call out for you, but he's so far away.\n.\n.\n.\n\n")
      temporalEnd()
    elif choice == options[1]:
      print("You put the tape roll and wrench down before approaching the statue. You reach the door and look closely at the statue. It's stone.\n\nYou blink.\n\nSuddenly, the angel's hand is on your shoulder.\n.\n.\n.\n\n")
      temporalEnd()
    else:
      print("You yell at the Doctor. He doesn't hear you, so you yell louder. He finally hears you. You tell him that there's a statue outside. He leaps down the stairs and looks at the angel outside. Its arm is outstretched, reaching inside the TARDIS. Its face displays nothing but rage, its mouth is open wide, revealing a set of fangs. Despite its eyes being nothing but blank balls of stone, you can feel its gaze burning into you. No, not in to you, through you. It's staring hungrily at the pipes for the temporal stabilizer. \n\n\"A weeping angel...--\" the Doctor whispers, then looks at you. His face is full of panic. \n\n\"" + name + ", whatever you do. Do not look away from that statue! Don't even blink!\" He yells before running back up to the console. You hear him prancing around it, the clack of buttons and levers squeaking. Your eyes start to sting and water, but you can't let yourself blink. \nYou're frozen in fear, unable to do anything but follow the Doctor's instruction: Do not look away from that statue.")
      print("\n(Press enter to continue.)")
      choice = input("\n> ")
      print("\nThe TARDIS's doors try to close, but they hit the statue's arm. You hear the Doctor yell in frustration.\n\"She can\'t fly with the doors open! I need to disable her safety measures! " + name + ", hold on! Just a bit longer! Do not blink!\"\n\nYou hear the console crackle and pop. The distant bells clang urgently. The engines let out a warbling screech. Finally, you see the angel and the world around it start to fade. The engines stop warbling and start to make their now-comforting, groaning wheeze. You can see the outside world be replaced by a swirling storm of clouds before the doors slam shut.\n\n\"You can blink now, " + name + ". The angel is gone and- Oh!\" The Doctor is interupted by something heavy falling to the floor. Your eyes snap shut and let them rehydrate for a few seconds. You rub them open and see the Doctor crouched by the door. He\'s examining a stone arm.")
      print("\n(Press enter to continue.)")
      choice = input("\n> ")
      print("\n\"Tough ol\' girl, the TARDIS. She managed to break off the angel\'s arm.\" He picks it up and shows you it. You recoil. \"It's alright... I think. Never seen an angel have part of its body broken off. That one must've been starved. Still going to get rid of it. Sorry, " + name + ". No souvenirs. Maybe next time.\"\n\nYou don't complain. Even if the Doctor let you have the arm, you don't want it. He sets the arm down beside the door then walks back up to the console. He flicks a few levers, presses some buttons. There\'s a clang and the TARDIS goes silent.")
      print("\n\"Jumped a few minutes into the future. The angel should be long gone.\" The Doctor explains. He looks at you, his eyes twinkle in the TARDIS\' lights. You hear the doors creak open, outside is the alleyway. \"I\'ve been travelling alone for a while now, and, " + name + ", I might not have been here if it weren't for you. You were amazing keeping that weeping angel at bay. So, I need to ask. Would you join me? Here? In the TARDIS? The whole of space and time, just a button and lever or two away.\"\n\nJoin the Doctor? \n\n[1] Yes\n[2] No")
      choice = input("\n> ")
      print(".\n.\n.\n")
      if choice == options[0]:
        runWithTheDoctor()
        theEnd()
      else:
        dontRunWithTheDoctor()
        theEnd()

  # If the user gets touched by the weeping angel
  def temporalEnd():
    print("You wake up. You didn\'t even realize you passed out, what happened? You rub your head and look around. Looming over you are two red brick buildings with white trim. You\'re in an alleyway. You don\'t remember being in this specific alleyway, but, you also don\'t remember passing out. \n\nYou start to remember a bit of what happened. A man with a box, a weird box, asked for your help. Pipes. He wanted you to patch up some pipes in his box. There was this statue. A statue of an angel. It moved, but you never saw it move. It touched you on your shoulder, and you woke up here.\n\nYou shrug. It was probably just a dream. How you fell asleep in an alleyway? You try not to think much about it. You look up, admiring the old-timey houses beside you. You see something in one of the balconies. A statue. An angel statue. It has its head buried in his hands, but, through its fingers, you could swear it was smiling.")
    theEnd()
  ##### Temporal stabilizer end #####

  ##### Telepathic circuit start #####
  ## Originally this story was going to have the user and the Doctor face off against a Silent (the grey alien described later on), but, anyone who isn't very familiar with the show really wouldn't understand it (Silents are "memory proof" and can't be remembered.) Still like this one. I like to think that a Silent snuck into the TARDIS and she's trying to warn the user and the Doctor about it. Take this story as you will.
  def telepathicCircuit():
    print("\n\"T-telepathic circuit...\" you squeak out. You know what telepathy is, maybe even had an interest in it. Maybe this is finally your time to try and see if you have telepathic powers?\n\"Telepathic circuit!\" The man exclaims.")
    whatsYourName()
    print("\"Come along, " + name + "! I'll show you where the telepathic controller circuit is, and how to fix it.\"")
    print("The Doctor leads you up to the console and to a section of it that has two, hand-shaped indents.\n\n\"She needs a bit of callibrating! I'd do it myself, but, we\'re not on the best of terms. Too many dangerous trips.\" he pats the edge of the console, \"How good is your geography and history?\"\n\n[1] Good\n[2] Bad")
    choice = input("\n> ")
    print(".\n.\n.\n")
    print("He ignores your answer.\n\n\"Doesn't matter! Because that\'s not how TARDIS callibration works. It just needs pure and intent-full thoughts. You want to fix it, so you got your intent down. Now you just need to purify these thoughts. Put your hands on those controllers there.\" He gestures to the hand-shaped indents. You rest one hand on each of them. Your hands fit perfectly.\n\n\"Right! Now! Think about her. Especially her being repaired. Maybe throw in some sci-fi stories you know of to keep her on her toes.\" You hear the Doctor\'s voice fade away as you focus on the TARDIS.\n\nIt\'s calming, being telepathically connected with the TARDIS. Despite her being a machine, you can feel her emotions. She\'s happy, annoyed at the amount of disrepair, but happy. You can feel how much she cares for the Doctor. You feel her poking through your mind, looking through your past. As she went, you see images of yourself, but older. She\'s giving you glimpses into your future. \n\nSuddenly, she screams. Fear. That\'s all you feel. Fear. There\'s an image. A tall, grey alien with no eyes or mouth, wearing a black suit. The alien lets out an echoing warble. You jolt awake.\n\n\"What is it? What happened? Is she being rude? Did you kick them out?\" The Doctor yells at the TARDIS.\n\nTell the Doctor about the alien?\n\n[1] Yes \n[2] No")
    choice = input("\n> ")
    print(".\n.\n.\n")
    if choice == options[0]:
      print("You describe what you saw to the Doctor. He looks at you, confused.\n\n\"That\'s odd. Her memory banks must\'ve leaked. Don\'t worry about it, " + name + ", it\'s probably nothing.\" He looks at you, \"How do you feel about coming with me? All of time and space, ready to be explored. Exciting, yes, even more exciting when with company. We could figure out what you saw, you could continue helping me fix this old girl up. What do you say?\"\n\nJoin the Doctor? \n\n[1] Yes \n[2] No")
      choice = input("\n> ")
      print(".\n.\n.\n")
      if choice == options[0]:
        runWithTheDoctor()
        theEnd()
      else:
        dontRunWithTheDoctor()
        theEnd()
    else:
      print("You stay quiet about the alien. The Doctor looks grumpily at the glass column in the middle of the console, \"I don\'t think she likes you. Last time she didn\'t like someone, it didn\'t go well when they stuck around. I think it\'d be best if you left.\" He gestures towards the door.\n\nYou walk slowly towards the doors and exit the box. You walk a few paces away from it and turn around. It is, indeed, smaller on the outside. The doors slam shut, and the wind starts to howl. The light atop of the box pulses in rhythm with the wheeze of the engines. The howling fades as the box disappears.\n\nYou continue down the alley, walking through where the TARDIS once stood.")
      theEnd()
  ##### Telepathic circuit end #####

  # The end
  def theEnd():
    print("\nThe End \nTry again? \n\n[1] Yes \n[2] No")
    choice = input("\n> ")
    if choice == options[1]:
      print("\n\n\n.\n.\n.\n")
      start()
    else:
      print(".\n.\n.\n.\n.\n\n")
      beginning()

  # If player ever chooses to travel with the Doctor:
  def runWithTheDoctor():
    print("You shake your head \'yes.\' A smile grows on the Doctor\'s face before be begins to run and dance around the console, twisting and pressing things as he went. The doors slam shut.\n\n\"All of time!\" The Doctor yells from the other side of the console, \"All of... space!\" he says as he runs by you.\n\"I would ask \'Where to, " + name + "?\' but, as you might've figured out already...\" He stops beside you and rests a hand on a big lever on the console, \"There isn't much say in where we go. The TARDIS goes where the TARDIS wants. All I do is make sure she doesn't explode.\"\nHe smiles as he dramatically slams down the lever. A piece of glass inside the glass tube starts to slowly, carefully, float up and down in rhythm with the distant howling of the engines. \n\nThe Doctor's eyes grow wide as he almost whispers, \"Geronimo.\"")

  # If the player ever chooses to not travel with the Doctor:
  def dontRunWithTheDoctor():
    print("You shake your head \'no.\' The Doctor frowns and huffs. \n\"Well, " + name + ", the door is already open. Thank you for your help.\" \nYou nod and head for the door, which closes behind you as you step out of the box. Behind you, the wind began to howl-- no, the TARDIS' engines, began to howl. The howling fades as the box disappears.\n\nYou continue down the alley, walking through where the TARDIS once stood.")

  ### Setup end
  beginning()
  ### Start program

#####----- Python Who end -----#####

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

#####-----~@~-----#####
def start():
  print("Welcome to Error's Python Collection. \nPlease select a mini program. \n\n[1] High/Low Guessing Game \n[2] Mad Lib  \n[3] Simple Calculator \n[4] Python Who: Choose Your Own Adventure\n[5] Unknown Mass Calculator\n\nTo quit, type \"quit\"")

  selOptions = ["quit", "1", "2", "3", "4", "5"]
  sel = [input("\n> ")]
  selQuit = False

  while True:
    if sel[0] in selOptions:
      if sel[0] == selOptions[1]:
        print("\nYou have selected High/Low Guessing Game \n\nWhat would you like the maximum number to be?")
        try:
          maxHigh = input("\n> ")
          print("\n\nStarting High/Low with a maximum of " + maxHigh + "\n.\n.\n.\n")
          highLow(maxHigh)
          print("\n\n\n.\n.\n.\n")
          start()
        except:
          print("Invalid input!")
      elif sel[0] == selOptions[2]:
        print("\nYou have selected Mad Lib \n.\n.\n.\n")
        madLib()
        print("\n\n\n.\n.\n.\n")
        start()
      elif sel[0] == selOptions[3]:
        print("\nYou have selected Simple Calculator\n.\n.\n.\n")
        simpleCalc()
        print("\n\n\n.\n.\n.\n")
        start()
      elif sel[0] == selOptions[4]:
        print("\nYou have selected Python Who: Choose Your Own Adventure\n.\n.\n.\n")
        pythonWho()
        print("\n\n\n.\n.\n.\n")
        start()
      elif sel[0] == selOptions[5]:
        print("\nYou have selected Unknown Mass Calculator\n.\n.\n.\n")
        massCalc()
        print("\n\n\n.\n.\n.\n")
        start()
      else:
        print("Are you sure you want to quit? Y/N")
        selQuit = input("\n> ")
        if selQuit == "Y" or selQuit == "y":
          quit()
        else:
          print("\n\n\n")
          start()
    if sel[0] not in selOptions:
      print("\nThat is not a valid option! Try again")
      sel = [input("\n> ")]
#####-----~@~-----#####

start()
