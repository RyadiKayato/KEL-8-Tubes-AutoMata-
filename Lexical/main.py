#================================ CARA PENGERJAAN ================================
# petunjuk menjalankan algoritma :
# masukan beberapa kata dalam bahasa belanda, dan setiap katanya diberi spasi.
# kata yang diterima :
# HIJ
# ZE
# LIEFDE
# KOPEN
# ETEN
# FILM
# SALADE
# SAP
# FRUIT
# TEKENING

import string
import streamlit as st
terminals = ['Vader','Moeder','Mango','Wortel','Binden','Boek','Vest','Eten','Wassen','Lezen']

st.header("Lexical analyzer")
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


sentence = st.text_input('Input words : ')
input_string = sentence.lower() + '#'

alphabet_list = list(string.ascii_lowercase)

state_list = [
    'q0',
    'q1',
    'q2',
    'q3',
    'q4',
    'q5',
    'q6',
    'q7',
    'q8',
    'q9',
    'q10',
    'q11',
    'q12',
    'q13',
    'q14',
    'q15',
    'q16',
    'q17',
    'q18',
    'q19',
    'q20',
    'q21',
    'q22',
    'q23',
    'q24',
    'q25',
    'q26',
    'q27',
    'q28',
    'q30',
    'q31',
    'q32',
    'q33',
    'q34',
    'q35',
    'q36',
    'q37',
    'q38',
    'q39',
    'q40',
    
]

transition_table = {}

for i in state_list:
    for alphabet in alphabet_list:
        transition_table[(i, alphabet)] = 'ERROR'
    transition_table[(i, '#')] = 'ERROR'
    transition_table[(i, ' ')] = 'ERROR'

#initial
transition_table[('q0', ' ')] = 'q0'
#finish_state
transition_table[('q0', 'b')] = 'q1'
transition_table[('q1', 'i')] = 'q2'
transition_table[('q2', 'n')] = 'q3'
transition_table[('q3', 'd')] = 'q4'
transition_table[('q4', 'e')] = 'q5'
transition_table[('q5', 'n')] = 'q39'
transition_table[('q39', ' ')] = 'q40'
transition_table[('q39', '#')] = 'ACCEPT'
transition_table[('q40', ' ')] = 'q40'
transition_table[('q40', '#')] = 'ACCEPT'

#BOEK
transition_table[('q0', 'b')] = 'q1'
transition_table[('q1', 'o')] = 'q7'
transition_table[('q7', 'e')] = 'q8'
transition_table[('q8', 'k')] = 'q39'

#ETEN
transition_table[('q0', 'e')] = 'q9'
transition_table[('q9', 't')] = 'q10'
transition_table[('q10', 'e')] = 'q11'
transition_table[('q11', 'n')] = 'q39'

#LEZEN
transition_table[('q0', 'l')] = 'q12'
transition_table[('q12', 'e')] = 'q13'
transition_table[('q13', 'z')] = 'q14'
transition_table[('q14', 'e')] = 'q15'
transition_table[('q15', 'n')] = 'q39'

#mango
transition_table[('q0', 'm')] = 'q16'
transition_table[('q16', 'a')] = 'q17'
transition_table[('q17', 'n')] = 'q18'
transition_table[('q18', 'g')] = 'q19'
transition_table[('q19', 'o')] = 'q39'

#MOEDER
transition_table[('q0', 'm')] = 'q16'
transition_table[('q16', 'o')] = 'q20'
transition_table[('q20', 'e')] = 'q21'
transition_table[('q21', 'd')] = 'q22'
transition_table[('q22', 'e')] = 'q23'
transition_table[('q23', 'r')] = 'q39'

#VADER
transition_table[('q0', 'v')] = 'q24'
transition_table[('q24', 'a')] = 'q25'
transition_table[('q25', 'd')] = 'q26'
transition_table[('q26', 'e')] = 'q27'
transition_table[('q27', 'r')] = 'q39'

#VEST
transition_table[('q0', 'v')] = 'q24'
transition_table[('q24', 'e')] = 'q28'
transition_table[('q28', 's')] = 'q29'
transition_table[('q29', 't')] = 'q39'

#WASSEN
transition_table[('q0', 'w')] = 'q30'
transition_table[('q30', 'a')] = 'q31'
transition_table[('q31', 's')] = 'q32'
transition_table[('q32', 's')] = 'q33'
transition_table[('q33', 'e')] = 'q34'
transition_table[('q34', 'n')] = 'q39'

#WORTEL
transition_table[('q0', 'w')] = 'q30'
transition_table[('q30', 'o')] = 'q35'
transition_table[('q35', 'r')] = 'q36'
transition_table[('q36', 't')] = 'q37'
transition_table[('q37', 'e')] = 'q38'
transition_table[('q38', 'l')] = 'q39'

#looping 
transition_table[("q40", "b")] = "q1"
transition_table[("q40", "e")] = "q9"
transition_table[("q40", "l")] = "q12"
transition_table[("q40", "m")] = "q16"
transition_table[("q40", "v")] = "q24"
transition_table[("q40", "w")] = "q30"



idx_char = 0
state = 'q0'
current_token = ''

while state != 'ACCEPT' and sentence != '':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state == 'q40':
        st.write('current token: ',current_token,'-> valid')
        current_token = ''

    if state == 'ERROR' and idx_char != 0:
        st.write(current_token,'error')
        break
    idx_char += 1

if state == 'ACCEPT':
    st.write('All tokens are entered: ',sentence,'-> valid')
elif state != 'ACCEPT' and idx_char != 0:
    st.write('All tokens are entered: ',sentence,'-> not valid')
 
