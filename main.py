import streamlit as st
from plurali import plul_calz, plul_mut, plul_pant, plurale_magliett, plul_fel

if __name__ == '__main__':
    g = st.number_input('Inserisci il numero di giorni di viaggio:', min_value=1, step=1)
    cf = g*2
    if g > 7:
        vl = st.radio('Avrai a disposizione una lavatrice?', ('Y', 'N'))
        if vl.lower() == 'y':
            g = 7
    ma = st.radio('In questa vacanza avrai bisogno di un costume?', ('Y', 'N'))
    co = ma.lower() == 'y'
    m = g + 1
    p = g//2
    if p < 1:
        p = 1
    f = p-1
    if f < 1:
        f = 1
    mu = g + 1
    c = g + 1
    vcs = st.radio('Crema solare?', ('Y', 'N'))
    cs = vcs.lower() == 'y'

    st.write('Eccoti la lista delle cose da mettere in valigia:\n')
    st.write('- ' + str(m) + ' ' + plurale_magliett(m)) #magliette
    st.write('- ' + str(p) + ' ' + plul_pant(p)) #pantaloni
    st.write('- ' + str(c) + ' ' + plul_calz(c)) #calze
    st.write('- ' + str(mu) + ' ' + plul_mut(mu)) #mutande
    st.write('- ' + str(f) + ' ' + plul_fel(f)) #felpe
    st.write('- Beauty case:\n   - Spazzolino\n   - Dentifricio\n   - Shampoo\n   - Bagnoschiuma\n   - '+str(cf)+' Cotton fioc\n   - Deodorante\n   - Pettine\n   - Lametta\n   - Saponetta\n   - Polvere per capelli\n   - Schiuma da barba')