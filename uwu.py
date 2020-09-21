# Function to convert into UwU text
def generateUwU(input_text):
    # the length of the input text
    length = len(input_text)

    # variable declaration for the output text
    output_text = ''

    # check the cases for every individual character
    for i in range(length):

        # initialize the variables
        current_char = input_text[i]
        previous_char = '&# 092;&# 048;'

        # assign the value of previous_char
        if i > 0:
            previous_char = input_text[i - 1]

            # change 'L' and 'R' to 'W'
        if current_char == 'L' or current_char == 'R':
            output_text += 'W'

        # change 'l' and 'r' to 'w'
        elif current_char == 'l' or current_char == 'r':
            output_text += 'w'

        # if the current character is 'o' or 'O'
        # also check the previous charatcer
        elif current_char == 'O' or current_char == 'o':
            if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm':
                output_text += "yo"
            else:
                output_text += current_char

                # if no case match, write it as it is
        else:
            output_text += current_char

    return output_text