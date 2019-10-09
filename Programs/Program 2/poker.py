# defining possible poker hands (flush, 2 of a kind, or 3 of a kind)
def three_of_a_kind(hand_as_list, output):
    if hand_as_list[0][0] == hand_as_list[1][0] == hand_as_list[2][0]:
        output.write("THREE OF A KIND\n")
    else:
        return "false"

def flush(hand_as_list, output):
    if hand_as_list[0][1] == hand_as_list[1][1] == hand_as_list[2][1]:
        output.write("FLUSH\n")
    else:
        return "false"

def two_of_a_kind(hand_as_list, output):
    if (hand_as_list[0][0] == hand_as_list[1][0] or
          hand_as_list[0][0] == hand_as_list[2][0] or
          hand_as_list[1][0] == hand_as_list[2][0]):
        output.write("TWO OF A KIND\n")
    else:
        return "false"

# prints the cards received from the input file        
def print_hand(hand_as_list, poker_output):
    poker_output.write("Poker Hand\n")
    poker_output.write("----------\n")
    number = 0
    for card in hand_as_list:
        number += 1
        poker_output.write("Card " + str(number) + ": " +
                           str(hand_as_list[(number - 1)][0].capitalize()) +
                           " of " + str(hand_as_list[(number - 1)][1].capitalize()) + "\n")
    poker_output.write("\n")

# uses functions defined earlier to evaluate outcome of the hand and write it to output file
def evaluate(hand_as_list, poker_output):
    poker_output.write("Poker Hand Evaluation: ")
    if flush(hand_as_list, poker_output) == "false":
        if three_of_a_kind(hand_as_list, poker_output) == "false":
            if two_of_a_kind(hand_as_list, poker_output) == "false":
                poker_output.write("NOTHING\n")
    poker_output.write("\n")


# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def main(poker_input, poker_output, cards_in_hand):    

    for hand in poker_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0], hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list, poker_output)
        evaluate(hand_as_list, poker_output)
        
# --------------------------------------

poker_input = open("poker.in", "r")
poker_output = open("poker.out", "w")

main(poker_input, poker_output, 3)

poker_input.close()
poker_output.close()
