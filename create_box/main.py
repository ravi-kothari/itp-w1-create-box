"""This is the entry point of the program."""


def create_box(height, width, character):
    if character == '*':
        x = ""
        for i in range(height):
            x = x + ('*' * width) + "\n"
        return x
            
            
    elif character == '@':
        x = ""
        for i in range(height):
            x = x + ('@' * width)+ "\n"
        return x 
        
    else:
        return ("go home")


if __name__ == '__main__':
    create_box(3, 4, '*')
