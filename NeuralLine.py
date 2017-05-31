# Setting up in this section.
import random

done = "holder"

# In the long run, it's pretty unimportant how these weights are set up,
# As long as a) they're equal and b) they don't get much closer to 0.
# I haven't tested it out, but if that was changed it'd probably get weird as weights go negative.
we1=1
we2=1
we3=1
we4=1
we5=1

# This generates a new set of preset values for each neuron.
# These influence how the neurons act, and since it is randomized at the beginning,
# It's different each new run.
pre1=random.uniform(0.5,1.5)
pre2=random.uniform(0.5,1.5)
pre3=random.uniform(0.5,1.5)
pre4=random.uniform(0.5,1.5)
pre5=random.uniform(0.5,1.5)

# Due to how the "axons" go I needed two kinds of neurons.
def Neuron1(InValue,Preset):
    OutValue = InValue * Preset
    return OutValue
def Neuron2(InValue1,InValue2,InValue3,Weight1,Weight2,Weight3,Preset):
    # Basically just the math of using weights in averaging.
    OutValue = (InValue1 * Weight1) + (InValue2 * Weight2) + (InValue3 * Weight3)
    OutValue /= (Weight1 + Weight2 + Weight3)
    OutValue *= Preset
    return OutValue
    # Just to save a bit of space, and clean the code a bit, I functionized this.
def GiveResults(Intro,Outro):
    print("Input: " + str(Intro))
    print("Output: " + str(Outro))
    # Need to find a better way to express this section but it works.
def WeightMod(choice,w1,w2,w3,w4,w5):
    if choice == "add":
        # This is if it does okay - small, random variation in the weights.
        w1 += random.uniform(-0.1,0.1)
        w2 += random.uniform(-0.1,0.1)
        w3 += random.uniform(-0.1,0.1)
        w4 += random.uniform(-0.1,0.1)
        w5 += random.uniform(-0.1,0.1)
    elif choice == "mult":
        # If it does well, it reinforces the entire section.
        # Since it's multiplication, future additions/subractions have less effect.
        w1 *= 1.1
        w2 *= 1.1
        w3 *= 1.1
        w4 *= 1.1
        w5 *= 1.1
    else:
        # The first one, but potentially more extreme.
        w1 += random.uniform(-0.2,0.2)
        w2 += random.uniform(-0.2,0.2)
        w3 += random.uniform(-0.2,0.2)
        w4 += random.uniform(-0.2,0.2)
        w5 += random.uniform(-0.2,0.2)
    return w1, w2, w3, w4, w5

while done != "done":
    # This is so that it gets a new seed on each iteration,
    # So the random.uniform() in WeightMod varies each time it's called.
    random.seed()
    # I decided to limit the range of values it'd receive from 1 to 10, in integers.
    InputValue = random.randint(1,10)
    # The neurons actually working.
    OutA = Neuron1(InputValue,pre1)
    OutB = Neuron1(InputValue,pre2)
    OutC = Neuron1(InputValue,pre3)
    OutD = Neuron2(OutA,OutB,OutC,we1,we2,we3,pre4)
    OutE = Neuron2(OutA,OutB,OutC,we1,we2,we3,pre5)
    # Averaging and weighting the results of neurons D and E.
    OutputValue = (OutD * we4) + (OutE * we5)
    OutputValue /= (we4 + we5)
    # Figuring out how it did, telling you how it did, and adjusting itself accordingly.
    if (InputValue - 1) <= OutputValue <= (InputValue + 1):
        GiveResults(InputValue,OutputValue)
        print("I did well!")
        we1, we2, we3, we4, we5 = WeightMod("mult",we1,we2,we3,we4,we5)
    elif (InputValue - 2) <= OutputValue <= (InputValue + 2):
        GiveResults(InputValue,OutputValue)
        print("I did okay.")
        we1, we2, we3, we4, we5 = WeightMod("add",we1,we2,we3,we4,we5)
    else:
        GiveResults(InputValue,OutputValue)
        print("I did bad :(")
        we1, we2, we3, we4, we5 = WeightMod("addbig",we1,we2,we3,we4,we5)
    # To end, or not end, the program.
    # Just pressing and holding the enter key can give you a thousand iterations in about a minute.
    print("Do you with to be done?")
    done=input()
