import streamlit as st
import random
import requests
from PIL import Image, ImageOps
from io import BytesIO

# Display the title
st.markdown("<h1 style='text-align: center; color: lightblue;'>Marc's Mystic Tarot Tellings</h1>", unsafe_allow_html=True)

# Checkbox for including the Suit of Weird
include_suit_of_weird = st.checkbox("Include the Suit of Weird")
use_reversals = st.checkbox("Include Reversed Cards")

# Dropdown for spread selection
spread_choice = st.selectbox("Choose a Tarot Spread", list(spread_explanations.keys()))
num_cards = len(spread_explanations[spread_choice])

if st.button("Draw Cards"):
    drawn_cards = [(card, random.choice([True, False]) if use_reversals else False) for card in random.sample(list(tarot_meanings.keys()), num_cards)]
    
    for i, (card, reversed) in enumerate(drawn_cards):
        image = get_card_image(card, reversed)
        col1, col2 = st.columns([1, 2])
        with col1:
            if isinstance(image, Image.Image):
                st.image(image, caption=f"{card} (Reversed)" if reversed else card, use_container_width=True)
            else:
                st.image(image_base_url + image, caption=f"{card} (Reversed)" if reversed else card, use_container_width=True)
        with col2:
            st.write(f"**{spread_explanations[spread_choice][i]}**")
            st.write(f"**{card}**")
            st.write(tarot_meanings[card]["reversed" if reversed else "upright"])
