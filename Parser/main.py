import parse as par

non_terminals = ['S', 'NN', 'VB']
terminals = ['vader','moeder','mango','wortel','binden','boek','vest','eten','wassen','lezen']

parse_table = {}
parse_table[('S', 'vader')] = ['NN', 'VB', 'NN']  #1s
parse_table[('S', 'moeder')] = ['NN', 'VB', 'NN']   #1s
parse_table[('S', 'mango')] = ['NN', 'VB','NN']   #3o
parse_table[('S', 'wortel')] = ['NN', 'VB','NN'] #3o
parse_table[('S', 'binden')] = ['NN', 'VB','NN']    #3o
parse_table[('S', 'boek')] = ['NN', 'VB','NN']    #3o
parse_table[('S', 'vest')] = ['NN', 'VB','NN'] #3o
parse_table[('S', 'eten')] = ['error'] #2p
parse_table[('S', 'wassen')] = ['error']  #2p
parse_table[('S', 'lezen')] = ['error']   #2p
parse_table[('S', 'EOS')] = ['error']    #2p
parse_table[('NN', 'vader')] = ['vader']
parse_table[('NN', 'moeder')] = ['moeder']
parse_table[('NN', 'mango')] = ['mango']
parse_table[('NN', 'wortel')] = ['wortel']
parse_table[('NN', 'binden')] = ['binden']
parse_table[('NN', 'boek')] = ['boek']
parse_table[('NN', 'vest')] = ['vest']
parse_table[('NN', 'eten')] = ['error']
parse_table[('NN', 'wassen')] = ['error']
parse_table[('NN', 'lezen')] = ['error']
parse_table[('NN', 'EOS')] = ['error']
parse_table[('VB', 'vader')] = ['error']
parse_table[('VB', 'moeder')] = ['error']
parse_table[('VB', 'mango')] = ['error']
parse_table[('VB', 'wortel')] = ['error']
parse_table[('VB', 'binden')] = ['error']
parse_table[('VB', 'boek')] = ['error']
parse_table[('VB', 'vest')] = ['error']
parse_table[('VB', 'eten')] = ['eten']
parse_table[('VB', 'wassen')] = ['wassen']
parse_table[('VB', 'lezen')] = ['lezen']
parse_table[('VB', 'EOS')] = ['error']

par.main(parse_table, non_terminals, terminals)




    




