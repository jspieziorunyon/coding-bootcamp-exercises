"""
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

A list of the same messages but with all instances of the word dang removed.
A list containing the number of dang words that were removed from each message at that particular index.
Here are some examples:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]

Here are the steps for you to follow. There are a LOT of steps! It won't be easy, but if you follow the steps exactly, you will pass this assignment:

Create the 2 empty lists that you'll return at the end:
One for the filtered messages with "dang" removed.
And one for the counts of dangs removed from those messages.
Loop over the list of messages. For each message:
Split the message string into a list of words using the .split() string method.
Create an empty list for all the good words in this message.
Create another empty list for all the dangs in this message.
For each word in the message:
If the word is "dang", add it to the list of dangs.
If it is not "dang", add it to the list of good words.
Join the list of good words into a single string using the .join() method.
Append the new filtered message to the list of filtered messages.
Count the dangs by getting the length of the list of dangs.
Append the count of dangs to the list of counts of dangs.
After looping over the list of messages, return the list of filtered messages first, then the list of counts of dangs.
"""

def filter_messages(messages):
    filtered = []
    filtered_count = []
    good_words = []
    bad_words = []
    all_words = []
    

    for message in messages:
        all_words = message.split()
    
        for word in all_words:
            if word == "dang":
                bad_words.append(word)
            else:
                good_words.append(word)
    
        filtered.append(" ".join(good_words))
        filtered_count.append(len(bad_words))
        good_words = []
        bad_words = []
                

    return filtered, filtered_count
