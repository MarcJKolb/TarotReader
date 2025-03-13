import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

# Expanded Tarot card meanings including Major and Minor Arcana
tarot_meanings = {
    "The Fool": "A journey of new beginnings, spontaneity, and trust in the universe. Encourages stepping into the unknown with curiosity and optimism.",
    "The Magician": "Symbolizes skill, resourcefulness, and manifestation. Represents the power to create your reality through focused will and action.",
    "The High Priestess": "Encourages deep intuition, inner wisdom, and connection to the subconscious. Represents mystery and hidden knowledge.",
    "The Empress": "Represents fertility, nurturing energy, and abundance. Encourages creativity, growth, and connection to nature.",
    "The Emperor": "Symbolizes authority, discipline, and structure. Represents stability, leadership, and control over one's domain.",
    "The Hierophant": "Reflects tradition, conformity, and spiritual teachings. Encourages seeking guidance from established beliefs or mentors.",
    "The Lovers": "Represents love, deep relationships, and moral choices. Suggests harmony, commitment, and aligning values.",
    "The Chariot": "Symbolizes determination, victory, and control over opposing forces. Encourages focus and disciplined effort.",
    "Strength": "Represents inner resilience, patience, and emotional mastery. Encourages overcoming challenges through gentle power.",
    "The Hermit": "Encourages solitude, introspection, and self-discovery. Represents wisdom gained through inner reflection.",
    "Wheel of Fortune": "Symbolizes cycles of fate, change, and destiny. Encourages embracing life's ups and downs with acceptance.",
    "Justice": "Represents truth, fairness, and accountability. Encourages making ethical choices and seeking balance in life.",
    "The Hanged Man": "Encourages new perspectives, surrender, and patience. Represents personal growth through letting go.",
    "Death": "Symbolizes transformation, endings, and renewal. Encourages embracing change and personal evolution.",
    "Temperance": "Represents moderation, balance, and harmony. Encourages blending different aspects of life for stability.",
    "The Devil": "Symbolizes materialism, addiction, and destructive patterns. Encourages awareness and breaking free from unhealthy attachments.",
    "The Tower": "Represents upheaval, sudden change, and revelation. Encourages rebuilding after major transformations.",
    "The Star": "Symbolizes hope, renewal, and inspiration. Encourages faith in the future and trust in the universe.",
    "The Moon": "Represents illusions, intuition, and the subconscious. Encourages exploring hidden emotions and uncertainties.",
    "The Sun": "Symbolizes success, joy, and clarity. Encourages embracing positivity and achieving fulfillment.",
    "Judgement": "Represents awakening, reckoning, and self-evaluation. Encourages personal transformation and renewal.",
    "The World": "Symbolizes completion, achievement, and wholeness. Encourages recognizing accomplishments and entering a new cycle."
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
        tarot_meanings[f"{value} of {suit}"] = f"Represents the energy of {value} within the suit of {suit}. Interpretation varies based on position and surrounding cards."

# Base URL for Tarot images from Sacred Texts
image_base_url = "https://www.sacred-texts.com/tarot/pkt/img/"

def get_card_image(card_name):
    """Fetch the Tarot card image from Sacred Texts using the specified filename structure."""
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
    
    return image_base_url + image_filename

st.title("Tarot Reading App")
spread_choice = st.selectbox("Choose a Tarot Spread", ["One Card Draw", "Past-Present-Future", "Celtic Cross"])
num_cards = 1 if spread_choice == "One Card Draw" else (3 if spread_choice == "Past-Present-Future" else 10)
if st.button("Draw Cards"):
    drawn_cards = random.sample(list(tarot_meanings.keys()), num_cards)
    for card in drawn_cards:
        image_url = get_card_image(card)
        col1, col2 = st.columns([1, 2])
        with col1:
            if image_url:
                st.image(image_url, caption=card, use_container_width=True)
        with col2:
            st.write(f"**{card}**")
            st.write(f"_Meaning_: {tarot_meanings[card]}")
        st.write("---")
