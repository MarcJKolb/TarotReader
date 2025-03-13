import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

# Expanded Tarot card meanings including Major and Minor Arcana
tarot_meanings = {
    "The Fool": "A journey of new beginnings, spontaneity, and trust in the universe. Encourages stepping into the unknown with curiosity and optimism. The Fool represents pure potential and the willingness to embrace the unknown. It signifies a moment of spontaneity, where one must trust in the path ahead despite uncertainty. This card often suggests that taking a leap of faith will lead to exciting discoveries and personal growth.\n\nAt its core, The Fool embodies an adventurous spirit, free from fear or doubt. It advises embracing change with an open heart, knowing that missteps are part of the journey. Whether starting a new project, relationship, or chapter in life, The Fool encourages an enthusiastic and lighthearted approach.",
    "The Magician": "Symbolizes skill, resourcefulness, and manifestation. Represents the power to create your reality through focused will and action. The Magician harnesses the energy of the universe to manifest intentions into reality. It highlights the importance of confidence, knowledge, and the ability to take decisive action. This card suggests that all the necessary tools for success are already at hand.\n\nBeyond mere capability, The Magician represents mastery and the alignment of thoughts, words, and deeds. It is a reminder that disciplined focus and intention-setting will bring desired outcomes. In readings, this card urges the querent to take control of their destiny through self-empowerment and strategic planning.",
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
        tarot_meanings[f"{value} of {suit}"] = (
            f"The {value} of {suit} represents the energy and essence of this suit in a specific context. It carries unique lessons and insights relevant to personal and external circumstances.\n\n"
            f"When drawn, the {value} of {suit} invites reflection on how its theme influences the current situation. It serves as a reminder to be mindful of the interplay between emotions, actions, thoughts, and material aspects of life."
        )

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

spread_explanations = {
    "One Card Draw": "This single card represents the most significant energy or theme influencing your life right now. It provides insight into your current situation and serves as guidance for how to proceed. Pay attention to the imagery, meaning, and personal resonance of the card as it relates to your question or concern.",
    "Past-Present-Future": (
        "1. **Past**: This card represents the experiences and influences that have shaped the current situation. It reveals past lessons, patterns, and decisions that continue to impact the present.\n\n"
        "2. **Present**: This card highlights the current state of affairs, providing clarity on what is happening now. It reflects emotions, challenges, and opportunities that require attention.\n\n"
        "3. **Future**: This card suggests the likely direction based on present actions and circumstances. While not set in stone, it provides guidance on what to expect and how to influence the outcome."
    ),
    "Celtic Cross": (
        "1. **Present Situation**: The heart of the matter—what is happening right now.\n\n"
        "2. **Challenge**: The primary obstacle or difficulty facing the querent.\n\n"
        "3. **Past Influences**: Events and circumstances leading up to this moment.\n\n"
        "4. **Future Outlook**: A glimpse into what is likely to come if current energies continue.\n\n"
        "5. **Conscious Goals**: The querent’s desires, hopes, and conscious intentions.\n\n"
        "6. **Subconscious Influences**: Hidden factors, fears, or motivations affecting the situation.\n\n"
        "7. **Advice**: The best course of action to take given the current circumstances.\n\n"
        "8. **External Influences**: People, events, or forces beyond the querent’s control.\n\n"
        "9. **Hopes & Fears**: What the querent longs for and what they fear may happen.\n\n"
        "10. **Final Outcome**: The projected result based on the present trajectory."
    )
}

st.title("Tarot Reading App")
spread_choice = st.selectbox("Choose a Tarot Spread", list(spread_explanations.keys()))
st.write(spread_explanations[spread_choice])
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
            st.write(tarot_meanings[card])
        st.write("---")
