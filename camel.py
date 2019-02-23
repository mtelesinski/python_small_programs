def camel(ccs, separator='_'):

    '''take a CamelCasedString as an argument and transform it 
    into a snake_cased_string. A different separator can be given 
    as the second argument.'''
    
    for i in ccs:
        if i != i.lower():
            if ccs.index(i) == 0:
                ccs = i.lower()+ccs[(ccs.index(i)+1):]
            else:
                ccs = ccs[:(ccs.index(i))]+separator+i.lower() \
                      +ccs[(ccs.index(i)+1):]
    print(ccs)
