import streamlit as st
import random
import requests
from PIL import Image, ImageOps
from io import BytesIO
import base64

# Function to set background
def set_background(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        img_data = base64.b64encode(response.content).decode()
        bg_image = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_data}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .title {{
            color: lightblue;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        }}
        </style>
        """
        st.markdown(bg_image, unsafe_allow_html=True)

# Set the background image
set_background("https://wallpapercave.com/wp/wp1880497.jpg")

# Display the title
st.markdown("<h1 class='title'>Mystic Marc's Tarot Telling</h1>", unsafe_allow_html=True)

# Checkbox for including the Suit of Weird
include_suit_of_weird = st.checkbox("Include the Suit of Weird")

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
            "upright": f"{name}: This card represents an eerie encounter with the unknown. It suggests that something beyond understanding is influencing the situation.\n\nIt may indicate an opportunity to embrace absurdity and the inexplicable, or it could serve as a warning that reality is shifting in ways that defy logic.",
            "reversed": f"{name} (Reversed): This card warns against obsession with the unknowable. The querent may be seeking answers in places where none exist.\n\nAlternatively, the reversed meaning can indicate clinging to rationality in a situation that demands a leap of intuition or surrender to chaos."
        }

# Base URL for Tarot images from Sacred Texts and Suit of Weird placeholders
image_base_url = "https://www.sacred-texts.com/tarot/pkt/img/"
weird_image_base_url = "https://github.com/user/weird_tarot_images/"

def get_card_image(card_name, reversed):
    """Fetch the Tarot card image and rotate if reversed."""
    words = card_name.split()
    if "Weird" in words:
        image_url = f"{weird_image_base_url}{card_name.replace(' ', '_').lower()}.jpg"
    else:
        if "The" in words or card_name in ["Justice", "Strength", "Judgement", "Death", "Temperance", "The Tower", "The Star", "The Moon", "The Sun", "The World"]:
            card_number = str(list(tarot_meanings.keys()).index(card_name)).zfill(2)
            image_url = f"{image_base_url}ar{card_number}.jpg"
        elif len(words) == 3 and words[1] == "of":  # Minor Arcana
            suit = suits.get(words[2], "")
            value = values.get(words[0], "")
            if suit and value:
                image_url = f"{image_base_url}{suit}{value}.jpg"
            else:
                return None
        else:
            return None
    
    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        if reversed:
            img = ImageOps.flip(img)  # Flip image upside down
        return img
    
    return None

spread_explanations = {
    "One Card Draw": ["This single card represents the most significant energy or theme influencing your life right now."],
    "Past-Present-Future": [
        "**Past:** This card represents the experiences and influences that have shaped the current situation.",
        "**Present:** This card highlights the current state of affairs, providing clarity on what is happening now.",
        "**Future:** This card suggests the likely direction based on present actions and circumstances."
    ],
    "Celtic Cross": [
        "**Present Situation:** The heart of the matter—what is happening right now.",
        "**Challenge:** The primary obstacle or difficulty facing the querent.",
        "**Past Influences:** Events and circumstances leading up to this moment.",
        "**Future Outlook:** A glimpse into what is likely to come if current energies continue.",
        "**Conscious Goals:** The querent’s desires, hopes, and conscious intentions.",
        "**Subconscious Influences:** Hidden factors, fears, or motivations affecting the situation.",
        "**Advice:** The best course of action to take given the current circumstances.",
        "**External Influences:** People, events, or forces beyond the querent’s control.",
        "**Hopes & Fears:** What the querent longs for and what they fear may happen.",
        "**Final Outcome:** The projected result based on the present trajectory."
    ],
    "Yes/No Spread": [
        "**Answer:** A single card drawn to provide insight into a yes-or-no question. Upright cards generally indicate 'Yes,' while reversed cards suggest 'No.' Additional nuances depend on the card's meaning and position."
    ]
}
