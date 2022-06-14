import streamlit as st



def main(parse_table,non_terminals,terminals):
    
    st.set_page_config(page_title="Parser Project")
    st.title("Parser Project")

    st.metric(label="Kata Terdaftar", value=10, delta_color="off")

    sentence = st.text_input('masukan kalimat : ')

    st.write('KATA YANG TERSEDIA')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Subject")
        for i in range(2):
            st.write(terminals[i])

    with col2:
        st.header("Predikat")
        for i in range(3):
            st.write(terminals[i+7])  

    with col3:
        st.header("Object")
        for i in range(5):
            st.write(terminals[i+2])

    tokens = sentence.lower().split()
    
    for i in range(len(tokens)):
        valid = parser(tokens[i], terminals)
        st.write(tokens[i], valid)

    item = searchtoken(tokens,terminals)

    if item == False:
        st.write("kata '",sentence, "' atau kalimat tidak sesuai")

    else:
        chekers = cheker(sentence,tokens,item,parse_table,non_terminals,terminals)
        if chekers == True:
            st.write('STRING', sentence, 'DITERIMA')
        elif chekers == False and len(tokens) != 1:
            st.write('ERROR! :', sentence, ' TIDAK SESUAI DENGAN GRAMMAR')

def searchtoken(tokens,terminals) :
    for count in tokens :
        if count not in terminals :
            return False
    return True

def parser(tokens,terminals) :
    for i in range(len(terminals)) :
        if tokens in terminals :
            str = "IS VALID"
            return str
        else :
            str ="ISN'T VALID"
            return str
            
def cheker(sentence,tokens,item,parse_table,non_terminals,terminals):

    while tokens != 'exit' and item == True:  
        
        tokens.append('EOS')
        stack = ['#','S']
        indext = 0
        symbol = tokens[0]

        while (len(stack) > 0):
            top = stack[len(stack)-1]
            if top in terminals:
                if top == symbol:
                    stack.pop()
                    indext += 1
                    symbol = tokens[indext]
                    if symbol == 'EOS':
                        stack.pop()
                else:
                    break
            elif top in non_terminals:
                if parse_table[(top, symbol)][0] != 'error':
                    stack.pop()
                    symbols_to_be_pushed = parse_table[(top, symbol)]
                    for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                        stack.append(symbols_to_be_pushed[i])
                else:
                    break
            else:
                break

        if symbol == 'EOS' and len(stack) == 0:
            return True
        else:
            return False
