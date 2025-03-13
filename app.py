import streamlit as st
import random
import requests
from PIL import Image, ImageOps
from io import BytesIO

# Expanded Tarot card meanings including Major and Minor Arcana
tarot_meanings = {
    "The Fool": {
        "upright": "A journey of new beginnings, spontaneity, and trust in the universe. Encourages stepping into the unknown with curiosity and optimism. The Fool represents pure potential and the willingness to embrace the unknown. It signifies a moment of spontaneity, where one must trust in the path ahead despite uncertainty. This card often suggests that taking a leap of faith will lead to exciting discoveries and personal growth.\n\nAt its core, The Fool embodies an adventurous spirit, free from fear or doubt. It advises embracing change with an open heart, knowing that missteps are part of the journey. Whether starting a new project, relationship, or chapter in life, The Fool encourages an enthusiastic and lighthearted approach.",
        "reversed": "A warning against recklessness and naivety. The reversed Fool suggests acting without thinking, which could lead to unnecessary risks and foolish mistakes. This card urges caution before taking leaps of faith.\n\nIt may also indicate hesitation or fear of stepping into the unknown. The reversed Fool can represent someone feeling stuck, afraid of making the wrong choice, or lacking confidence in their abilities."
    },
    "The Magician": {
        "upright": "Symbolizes skill, resourcefulness, and manifestation. Represents the power to create your reality through focused will and action. The Magician harnesses the energy of the universe to manifest intentions into reality. It highlights the importance of confidence, knowledge, and the ability to take decisive action. This card suggests that all the necessary tools for success are already at hand.\n\nBeyond mere capability, The Magician represents mastery and the alignment of thoughts, words, and deeds. It is a reminder that disciplined focus and intention-setting will bring desired outcomes. In readings, this card urges the querent to take control of their destiny through self-empowerment and strategic planning.",
        "reversed": "Indicates manipulation, illusion, or untapped potential. The reversed Magician suggests that someone may be using their skills dishonestly or that there is a lack of clarity in their goals.\n\nIt can also signal self-doubt, where the querent may have all the necessary tools but lacks confidence to use them. The reversed Magician warns against deception—whether from others or oneself—and urges reassessment of personal integrity and ambitions."
    }
}

# Minor Arcana (Suit of Wands, Cups, Swords, and Pentacles)
suits = {"Wands": "wa", "Cups": "cu", "Swords": "sw", "Pentacles": "pe"}
values = {
    "Ace": "ac", "Two": "02", "Three": "03", "Four": "04", "Five": "05",
    "Six": "06", "Seven": "07", "Eight": "08", "Nine": "09", "Ten": "10",
    "Page": "pa", "Knight": "kn", "Queen": "qu", "King": "ki"
}

# Add Minor Arcana to the dictionary
for suit in suits:
    for value in values:
        tarot_meanings[f"{value} of {suit}"] = {
            "upright": f"The {value} of {suit} represents the energy and essence of this suit in a specific context. It carries unique lessons and insights relevant to personal and external circumstances.\n\nWhen drawn, the {value} of {suit} invites reflection on how its theme influences the current situation. It serves as a reminder to be mindful of the interplay between emotions, actions, thoughts, and material aspects of life.",
            "reversed": f"The reversed {value} of {suit} represents blockages, delays, or misaligned energy in the suit's domain. It suggests resistance to lessons or challenges in emotional, mental, or material aspects of life.\n\nIt may indicate avoidance, denial, or an internal struggle with the themes of {suit}. This card urges awareness of where one’s energy is being restricted or misused."
        }

# Base URL for Tarot images from Sacred Texts
image_base_url = "https://www.sacred-texts.com/tarot/pkt/img/"

def get_card_image(card_name, reversed):
    """Fetch the Tarot card image from Sacred Texts using the specified filename structure and rotate if reversed."""
    words = card_name.split()
    if "The" in words or card_name in ["Justice", "Strength", "Judgement", "Death", "Temperance", "The Tower", "The Star", "The Moon", "The Sun", "The World"]:
        card_number = str(list(tarot_meanings.keys()).index(card_name)).zfill(2)
        image_filename = f"ar{card_number}.jpg"
    elif len(words) == 3 and words[1] == "of":  # Minor Arcana
        suit = suits.get(words[2], "")
        value = values.get(words[0], "")
        if suit and value:
            image_filename = f"{suit}{value}.jpg"
        else:
            return None  # Return None if suit or value is missing
    else:
        return None  # Return None if unrecognized format
    
    image_url = image_base_url + image_filename
    
    if reversed:
        response = requests.get(image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = ImageOps.flip(img)  # Flip image upside down
            return img
    
    return image_url

spread_explanations = {
    "One Card Draw": ["This single card represents the most significant energy or theme influencing your life right now. It provides insight into your current situation and serves as guidance for how to proceed."],
    "Past-Present-Future": [
        "**Past:** This card represents the experiences and influences that have shaped the current situation.",
        "**Present:** This card highlights the current state of affairs, providing clarity on what is happening now.",
        "**Future:** This card suggests the likely direction based on present actions and circumstances."
    ],
}

st.title("Tarot Reading App")
spread_choice = st.selectbox("Choose a Tarot Spread", list(spread_explanations.keys()))
st.write(spread_explanations[spread_choice])
num_cards = len(spread_explanations[spread_choice])

use_reversals = st.checkbox("Include Reversed Cards")

if st.button("Draw Cards"):
    drawn_cards = [(card, random.choice([True, False]) if use_reversals else False) for card in random.sample(list(tarot_meanings.keys()), num_cards)]
    
    for i, (card, reversed) in enumerate(drawn_cards):
        image = get_card_image(card, reversed)
        col1, col2 = st.columns([1, 2])
        with col1:
            if isinstance(image, Image.Image):
                st.image(image, caption=f"{card} (Reversed)" if reversed else card, use_column_width=True)
            else:
                st.image(image, caption=f"{card} (Reversed)" if reversed else card, use_column_width=True)
        with col2:
            meaning_key = "reversed" if reversed else "upright"
            st.write(f"**{spread_explanations[spread_choice][i]}**")
            st.write(f"**{card}**")
            st.write(tarot_meanings[card][meaning_key])
        st.write("---")
