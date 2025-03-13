import streamlit as st
import random
import requests
from PIL import Image, ImageOps
from io import BytesIO

# Display the title
st.markdown("<h1 style='text-align: center; color: lightblue;'>Mystic Marc's Tarot Telling</h1>", unsafe_allow_html=True)

# Checkbox for including the Suit of Weird
include_suit_of_weird = st.checkbox("Include the Suit of Weird")
use_reversals = st.checkbox("Include Reversed Cards")

# Dropdown for spread selection
spread_choice = st.selectbox("Choose a Tarot Spread", [
    "One Card Draw", "Past-Present-Future", "Celtic Cross", "Yes/No Spread"
])

# Button to draw cards
if st.button("Draw Cards"):
    
    # Define number of cards per spread
    num_cards = {
        "One Card Draw": 1,
        "Past-Present-Future": 3,
        "Celtic Cross": 10,
        "Yes/No Spread": 1
    }[spread_choice]
    
    # Expanded Tarot card meanings including Major, Minor, and the Suit of Weird
    tarot_meanings = {
        "The Fool": {
            "upright": "A journey of new beginnings, spontaneity, and trust in the universe. Encourages stepping into the unknown with curiosity and optimism.",
            "reversed": "A warning against recklessness and naivety. Suggests hesitation or fear of stepping into the unknown."
        }
    }
    
    # Minor Arcana (Suit of Wands, Cups, Swords, and Pentacles)
    suits = {"Wands": "wa", "Cups": "cu", "Swords": "sw", "Pentacles": "pe"}
    values = {
        "Ace": "ac", "Two": "02", "Three": "03", "Four": "04", "Five": "05",
        "Six": "06", "Seven": "07", "Eight": "08", "Nine": "09", "Ten": "10",
        "Page": "pa", "Knight": "kn", "Queen": "qu", "King": "ki"
    }
    
    # The Suit of Weird
    if include_suit_of_weird:
        suits["Weird"] = "wd"
        weird_cards = {
            "Ace": "The Unfathomable",
            "Two": "The Doppelgänger",
            "Three": "The Laughing Void",
            "Four": "The Locked Room",
            "Five": "The Teeth Collector",
            "Six": "The Impossible Gift",
            "Seven": "The Unreadable Text",
            "Eight": "The Repeating Dream",
            "Nine": "The Silent Choir",
            "Ten": "The Collapse",
            "Page": "The Fool with Too Many Eyes",
            "Knight": "The Masked Wanderer",
            "Queen": "The Whispering Woman",
            "King": "The Architect of the Impossible"
        }
        for value, name in weird_cards.items():
            tarot_meanings[f"{value} of Weird"] = {
                "upright": f"{name}: This card represents an eerie encounter with the unknown. It suggests that something beyond understanding is influencing the situation.",
                "reversed": f"{name} (Reversed): This card warns against obsession with the unknowable. The querent may be seeking answers in places where none exist."
            }
    
    # Draw cards and determine if they are reversed
    drawn_cards = [(card, random.choice([True, False]) if use_reversals else False) for card in random.sample(list(tarot_meanings.keys()), num_cards)]
    
    # Display the drawn cards
    for card, reversed in drawn_cards:
        meaning_key = "reversed" if reversed else "upright"
        st.write(f"**{card} ({'Reversed' if reversed else 'Upright'})**")
        st.write(tarot_meanings[card][meaning_key])
        st.write("---")
