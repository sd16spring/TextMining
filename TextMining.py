# HEADER
# Author: Cedric Kim
# League of Legends Chat Log Analysis
# This program looks at the chat log during a game and shows the most toxic person based off their language
# we can see if the most toxic person in the game was the person who was banned (reported multiple times)
# run in terminal, cntrl + b does not work (subl does not like input)
import random
import webbrowser
import math
import time
from Info import champions, champion_side, word_dictionary

def create_readable_list(text_file):     ## returns a list of readable strings
    """ creates splits between '},{'
        >>> create_readable_list('this},{will},{be},{split')
        ['this', 'will', 'be', 'split']
    """
    message_list = text_file.split("},{")
    return message_list
#print create_readable_list(raw_data)

def create_single_message_list(string_in_list): ## first index of the list is the champion, second is the team, after third, the comments.
    """ doctests here are incredibly hard
    """
    single_message_list = []
    for champion in champions:
        if string_in_list.find(''':"'''+ champion) != -1:         ##if the champion is found, add it first
            single_message_list.append(champion)
    for side in champion_side:                          ## if the side is found, add it next
        if string_in_list.find(side) != -1:
            single_message_list.append(side[1:-1])
    if string_in_list.find("""message":""") != -1:      ## if message is found, add it next
        message_index_start = string_in_list.find("""message":""") + 10
        message_index_end = string_in_list.find(""","association""") -1
        single_message_list.append(string_in_list[message_index_start: message_index_end])
    return single_message_list

def create_message_list(raw_data):
    """ doctests here are also incredibly hard
    """
    raw_list = create_readable_list(raw_data)
    message_list = []           ##output list, of lists
    for raw_string in raw_list:
        checked = False
        single_message = create_single_message_list(raw_string)## creates single_message_list
        if(len(message_list) == 0):                             ## if there is nothing in the output list
            message_list.append(single_message)                 ## add it
        else:                                                   ## if there is something
            for i in range(len(message_list)):                 ## we need to check if the message is the same champion
                if(len(single_message) > 0):
                    if message_list[i][0] == single_message[0]:     ## if the champion is the same,
                        message_list[i].extend(single_message[2:])  ## add the message to the same list as the champion
                        checked = True
                    if (i == len(message_list) -1 and checked != True):     ## if no list was added, and champion is not the same,
                        message_list.append(single_message)          ## add the list to the end
    return message_list

def return_raw_champion_list(raw_data):
    """ doctests here are also incredibly hard
    """
    message_list = create_message_list(raw_data)
    raw_champion_list = []
    for raw_champion_string in message_list[:][:]:
        raw_champion_list.append(raw_champion_string)
    return raw_champion_list

def return_toxicity_level(champion_string, word_dict):        ## inputs the string of the champion, and the dictionary
    """
        >>> return_toxicity_level(['noob', 'idiot'], word_dictionary)
        11
    """
    level = 0   
    for key in word_dict.keys():            # for every key that exists
        for word in word_dict[key]:         # we take each word in the dict
            for string in (name.lower() for name in champion_string):   #for every string in the champion list                     
                if word in string:              # if the string exists
                    level += key               #we add the toxicity value to the level
    return level

def return_champion_toxicity(raw_data, word_dict):          #returns a list with the champion and toxicity level
    champion_toxicity_list = []
    raw_champion_list = return_raw_champion_list(raw_data)  #we get each individual message file
    for i in range(len(raw_champion_list)-1):              # for however long the message is,
        champion_toxicity_list.append(raw_champion_list[i][0:2])    # we add the champion and relation to offender,
        toxicity_level = return_toxicity_level(raw_champion_list[i][2:], word_dict)  
        champion_toxicity_list.append(toxicity_level)               #and add the toxicity level for each one
    return champion_toxicity_list

def return_champion_toxicity_ratios(raw_data, word_dict):
    champion_toxicity_list = return_champion_toxicity(raw_data, word_dict)
    sum = 0.0
    for element in champion_toxicity_list:              #for each element
        if isinstance(element, int):                    # find the toxicity values
            sum += element                              #add to the sum
    for i in range(len(champion_toxicity_list)-1):      #for each index
        if isinstance(champion_toxicity_list[i], int):  #if the element is an integer
            if sum != 0:
                champion_toxicity_list[i] = float("{0:.3f}".format(champion_toxicity_list[i] * 1.0/ sum))   #turn the toxicity into a ratio and cut off all values except 2 decimals
    return champion_toxicity_list

def highest_toxicity(champion_toxicity_list_ratio):          #returns the champion and toxicity
    toxicity_order = []
    highest_toxicity_champion = ''
    highest_toxicity = 0
    for i in range(len(champion_toxicity_list_ratio)-1):              #for each element
        if isinstance(champion_toxicity_list_ratio[i], float):          # if we find the toxicity level
            if highest_toxicity < champion_toxicity_list_ratio[i]:     # if its the highest we've seen
                highest_toxicity_champion = champion_toxicity_list_ratio[i-1][0]      #store it the champion
                highest_toxicity = champion_toxicity_list_ratio[i]
    return [highest_toxicity_champion, highest_toxicity]

def is_offender(champion_toxicity_list_ratio):           #returns true if the most toxic was the offender
    toxicity_order = []
    check_offender_list = []
    highest_toxicity_champion = ''
    highest_toxicity = 0
    for i in range(len(champion_toxicity_list_ratio)-1):              #for each element
        if isinstance(champion_toxicity_list_ratio[i], float):          # if we find the toxicity level
            if highest_toxicity < champion_toxicity_list_ratio[i]:     # if its the highest we've seen
                highest_toxicity_champion = champion_toxicity_list_ratio[i-1][0]      #store it the champion
                highest_toxicity = champion_toxicity_list_ratio[i]
    check_offender_list.append(highest_toxicity_champion)       #create a list we can compare too
    check_offender_list.append('offender')
    return check_offender_list in champion_toxicity_list_ratio

def ratio_of_accurate_analysis(word_dictionary, case_start, case_end):      #treturns the ratio of number of correct
    number_correct = 0
    for i in range(case_start, case_end):
        if i > 0:
            file = open("./cases/" + str(i) + ".txt")
            raw_data = file.read()
            if is_offender(return_champion_toxicity_ratios(raw_data, word_dictionary)):
                number_correct += 1
    return 1.0*number_correct / (case_end - case_start)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #print ratio_of_accurate_analysis(word_dictionary, 8000, 8800)
    #^^^ un-comment if you want to see how many cases are accurate choose start and end case between 1-10000
    while  True:
        case_string = raw_input("Enter new League case number(1- 10000):")
        print(chr(27) + "[2J")                                      ##clears screen
        case_number = int(case_string)
        if case_number > 0 and case_number < 10001:
            print 'case_number:                  ' + case_string
            file = open("./cases/" + str(case_number) + ".txt")
            raw_data = file.read()
            toxic_info = highest_toxicity(return_champion_toxicity_ratios(raw_data, word_dictionary))
            print "Highest toxicity percentage:  " + str(100*toxic_info[1]) + ' %'
            print "champion:                     " + str(toxic_info[0])
            print "Is offender:                  " + str(is_offender(return_champion_toxicity_ratios(raw_data, word_dictionary)))
            decision = raw_input("Show Other Toxic Ratios? (Y/N):")
            if 'y' == decision.lower():
                print return_champion_toxicity_ratios(raw_data, word_dictionary)
            decision = raw_input("Open up case in browser? (Y/N):")
            if 'y' == decision.lower():
                print('\n')
                webbrowser.open('https://tribunal.ga/case/' + str(case_number))
                time.sleep(1)
        else:
            print 'Please enter case number between 1 and 10000'