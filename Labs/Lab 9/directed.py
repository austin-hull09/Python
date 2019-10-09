

stranger_things = {}
stranger_things["The Vanishing of Will Byers"] = "The Duffer Brothers"
stranger_things["The Weirdo on Maple Street"] = "The Duffer Brothers"
stranger_things["Holly, Jolly"] = "Shawn Levy"
stranger_things["The Body"] = "Shawn Levy"
stranger_things["The Flea and the Acrobat"] = "The Duffer Brothers"
stranger_things["The Monster"] = "The Duffer Brothers"
stranger_things["The Bathtub"] = "The Duffer Brothers"
stranger_things["The Upside Down"] = "The Duffer Brothers"

def episodes_directed(dictionary, director):
    count = 0
    for i in dictionary:
        if dictionary[i] == director:
            count += 1
    print(str(director) + " directed " + str(count) + " episodes")
    
episodes_directed(stranger_things, "The Duffer Brothers")
episodes_directed(stranger_things, "Shawn Levy")
episodes_directed(stranger_things, "Kerri Cobb")
