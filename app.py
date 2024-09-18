import streamlit as st

# Kontrollera om saldo redan finns, annars initiera det
if "saldo" not in st.session_state:
    st.session_state.saldo = 0  # Startsaldo på 0 kr

# Visa nuvarande saldo
st.write(f"Din nuvarande saldo är: {st.session_state.saldo} kr")

# Möjlighet att sätta in pengar på kontot
insättning = st.number_input("Hur mycket pengar vill du sätta in på ditt konto", min_value=0, value=0)

# Knapp för att sätta in pengar
if st.button("Sätt in pengar"):
    st.session_state.saldo += insättning
    st.success(f"Du har lagt in {insättning} kr. Ditt nya saldo är {st.session_state.saldo} kr.")

# Välj biljettpris och antal biljetter
biljettpris = 100  # Fast biljettpris per biljett (kan anpassas beroende på ålder)
antal_biljetter = st.number_input("Hur många biljetter vill du köpa?", min_value=1, value=1)

# Beräkna totalkostnaden för biljetter
totalpris = biljettpris * antal_biljetter
st.write(f"Totalpriset för {antal_biljetter} biljetter är: {totalpris} kr")

# Knapp för att köpa biljetter
if st.button("Köp biljetter"):
    if st.session_state.saldo >= totalpris:
        st.session_state.saldo -= totalpris
        st.success(f"Du har köpt {antal_biljetter} biljetter för {totalpris} kr!")
        st.write(f"Ditt nya saldo är: {st.session_state.saldo} kr")
    else:
        st.error(f"Du har inte tillräckligt med pengar på kontot. Du behöver {totalpris} kr men har bara {st.session_state.saldo} kr.")

# Datum
from datetime import datetime
dagens_datum = datetime.now().strftime("%Y-%m-%d")
st.header(f"Dagens datum: {dagens_datum}")
