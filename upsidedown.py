def upsidedown(text):

    '''The function takes a string with ASCII characters 
    as an argument and returns the upside down version 
    of that string.'''
    
    for sign in text:
        if sign == 'a':
            text = text[:text.index(sign)] + '\u0250' \
                   + text[text.index(sign)+1:]
        elif sign == 'b':
            text = text[:text.index(sign)] + '\u0070' \
                   + text[(text.index(sign)+1):]
        elif sign == 'C':
            text = text[:text.index(sign)] + '\u0186' \
                   + text[text.index(sign)+1:]
        elif sign == 'c':
            text = text[:text.index(sign)] + '\u0254' \
                   + text[text.index(sign)+1:]
        elif sign == 'd':
            text = text[:text.index(sign)] + '\u0071' \
                   + text[text.index(sign)+1:]
        elif sign == 'E':
            text = text[:text.index(sign)] + '\u018E' \
                   + text[text.index(sign)+1:]
        elif sign == 'e':
            text = text[:text.index(sign)] + '\u01DD' \
                   + text[text.index(sign)+1:]
        elif sign == 'f':
            text = text[:text.index(sign)] + '\u025F' \
                   + text[text.index(sign)+1:]
        elif sign == 'h':
            text = text[:text.index(sign)] + '\u0265' \
                   + text[text.index(sign)+1:]
        elif sign == 'k':
            text = text[:text.index(sign)] + '\u029E' \
                   + text[text.index(sign)+1:]
        elif sign == 'm':
            text = text[:text.index(sign)] + '\u026F' \
                   + text[text.index(sign)+1:]
        elif sign == 'N':
            text = text[:text.index(sign)] + '\u0376' \
                   + text[text.index(sign)+1:]
        elif sign == 'n':
            text = text[:text.index(sign)] + '\u0075' \
                   + text[text.index(sign)+1:]
        elif sign == 'p':
            text = text[:text.index(sign)] + '\u0062' \
                   + text[text.index(sign)+1:]
        elif sign == 'q':
            text = text[:text.index(sign)] + '\u0064' \
                   + text[text.index(sign)+1:]
        elif sign == 'R':
            text = text[:text.index(sign)] + '\u0281' \
                   + text[text.index(sign)+1:]
        elif sign == 'r':
            text = text[:text.index(sign)] + '\u0279' \
                   + text[text.index(sign)+1:]
        elif sign == 'S':
            text = text[:text.index(sign)] + '\u01A7' \
                   + text[text.index(sign)+1:]
        elif sign == 's':
            text = text[:text.index(sign)] + '\u01A8' \
                   + text[text.index(sign)+1:]
        elif sign == 't':
            text = text[:text.index(sign)] + '\u0287' \
                   + text[text.index(sign)+1:]
        elif sign == 'u':
            text = text[:text.index(sign)] + '\u006E' \
                   + text[text.index(sign)+1:]
        elif sign == 'V':
            text = text[:text.index(sign)] + '\u0245' \
                   + text[text.index(sign)+1:]
        elif sign == 'v':
            text = text[:text.index(sign)] + '\u028C' \
                   + text[text.index(sign)+1:]
        elif sign == 'w':
            text = text[:text.index(sign)] + '\u028D' \
                   + text[text.index(sign)+1:]
        elif sign == 'y':
            text = text[:text.index(sign)] + '\u028E' \
                   + text[text.index(sign)+1:]
                   
    print(text)
