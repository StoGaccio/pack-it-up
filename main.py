#importo le librerie
import streamlit as st  #streamlit
from plurali import plul_calz, plul_mut, plul_pant, plurale_magliett, plul_fel #funzioni per il plurale

if __name__ == '__main__':
    
#ottenimento dati
    g = st.number_input('Inserisci il numero di giorni di viaggio:', min_value=1, step=1)   #numero giorni

    cf = g*2   #numero di cotton fioc

    if g > 7:   #presenza di lavatrice
        vl = st.radio('Avrai a disposizione una lavatrice?', ('Y', 'N'))
        if vl.lower() == 'y':
            g = 7

    ma = st.radio('In questa vacanza avrai bisogno di un costume?', ('Y', 'N')) #costume
    co = ma.lower() == 'y'

    m = g + 1   #numero magliette

    p = g//2    #numero pantaloni
    if p < 1:
        p = 1
    
    f = p-1 #numero felpe
    if f < 1:
        f = 1
    
    mu = g + 1  #numero mutande

    c = g + 1   #numero calze

    vcs = st.radio('Crema solare?', ('Y', 'N')) #crema solare
    cs = False
    if vcs.lower() == 'y':
        cs = True


#stampa lista
    st.write('Eccoti la lista delle cose da mettere in valigia:\n')
    st.write('- ' + str(m) + ' ' + plurale_magliett(m)) #magliette
    st.write('- ' + str(p) + ' ' + plul_pant(p)) #pantaloni
    st.write('- ' + str(c) + ' ' + plul_calz(c)) #calze
    st.write('- ' + str(mu) + ' ' + plul_mut(mu)) #mutande
    st.write('- ' + str(f) + ' ' + plul_fel(f)) #felpe
    st.write('- Beauty case:\n   - Spazzolino\n   - Dentifricio\n   - Shampoo\n   - Bagnoschiuma\n   - '+str(cf)+' Cotton fioc\n   - Deodorante\n   - Pettine\n   - Lametta\n   - Saponetta\n   - Polvere per capelli\n   - Schiuma da barba')
    #beauty case
    st.write('- Caricabatterie\n   - Trasformatore\n  - Cavi per i tuoi dispositivi, non li so')    #cavetteria
    st.write('- Cuffie')    #cuffie e cuffiette
    st.write('- Cuffiette')
    st.write('- Powerbank') #powerbank
    st.write('- Portafoglio')   #portafoglio
    st.write('- Libri/Kindle')  #roba da leggere
    st.write('- K-way')   #kway
    st.write('- Pigiama')   #pigiama
    if cs == True:  #crema solare
        st.write('- Crema solare')

    st.write('\nBUON VIAGGIO!') #saluti
