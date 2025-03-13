import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

# Expanded Tarot card meanings including Minor Arcana
tarot_meanings = {
    "The Fool": "A leap of faith, embracing the unknown, fresh starts, and limitless potential. Trust your instincts and take a bold step forward.",
    "The Magician": "Manifestation of goals, personal power, resourcefulness, and mastery. You have all the tools to create your desired reality.",
    "The High Priestess": "Hidden knowledge, intuition, spiritual wisdom, and the subconscious. Trust your inner voice and seek deeper truths.",
    "The Empress": "Fertility, nurturing energy, abundance, creativity, and comfort. Connect with nature and embrace self-care.",
    "The Emperor": "Structure, authority, discipline, stability, and protection. Take control of your circumstances and establish order.",
    "The Hierophant": "Traditional wisdom, guidance, spiritual authority, and societal norms. Learn from a mentor or follow conventional wisdom.",
    "The Lovers": "Deep relationships, moral dilemmas, choices guided by the heart, and harmony. A major decision about love or values is at hand.",
    "The Chariot": "Victory through willpower, control over opposing forces, discipline, and ambition. Stay focused and push forward with determination.",
    "Strength": "Inner courage, emotional mastery, patience, and overcoming adversity. True strength comes from inner peace and resilience.",
    "The Hermit": "Seeking truth through solitude, introspection, wisdom, and guidance. Take time alone to find answers within yourself.",
    "Wheel of Fortune": "Cycles of change, fate, unexpected shifts, and turning points. Life is in motion—embrace new opportunities.",
    "Justice": "Balance, truth, accountability, fair decisions, and ethical clarity. Seek honesty and fairness in all dealings.",
    "The Hanged Man": "A shift in perspective, surrender, patience, and enlightenment through sacrifice. Let go of control to gain insight.",
    "Death": "Transformation, the end of a phase, renewal, and necessary change. Embrace the new by releasing the old.",
    "Temperance": "Balance, moderation, blending elements for harmony, and self-restraint. Take a measured approach to life’s challenges.",
    "The Devil": "Bondage to materialism, addiction, toxic cycles, and illusions of control. Recognize and break free from negative patterns.",
    "The Tower": "Sudden upheaval, breaking false foundations, radical change, and revelation. Accept transformation even when it’s painful.",
    "The Star": "Hope, renewal, inspiration, and trusting in the universe’s guidance. Remain optimistic and have faith in your path.",
    "The Moon": "Illusions, subconscious fears, uncertainty, and deep emotions. Things are not as they seem—trust your intuition.",
    "The Sun": "Joy, success, vitality, clarity, and celebration of life. Happiness and clarity shine upon you.",
    "Judgement": "A moment of reckoning, self-reflection, rebirth, and awakening. Make peace with the past and move forward.",
    "The World": "Completion, achieving goals, unity, wholeness, and fulfillment. You have reached a significant milestone in your journey."
}

# Base URL for Tarot images from Wikimedia Commons
image_base_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/"
image_paths = {
    "The Fool": "d/d7/RWS_Tarot_00_Fool.jpg/300px-RWS_Tarot_00_Fool.jpg",
    "The Magician": "d/de/RWS_Tarot_01_Magician.jpg/300px-RWS_Tarot_01_Magician.jpg",
    "The High Priestess": "8/88/RWS_Tarot_02_High_Priestess.jpg/300px-RWS_Tarot_02_High_Priestess.jpg",
    "The Empress": "d/d2/RWS_Tarot_03_Empress.jpg/300px-RWS_Tarot_03_Empress.jpg",
    "The Emperor": "c/c3/RWS_Tarot_04_Emperor.jpg/300px-RWS_Tarot_04_Emperor.jpg",
    "The Hierophant": "8/8d/RWS_Tarot_05_Hierophant.jpg/300px-RWS_Tarot_05_Hierophant.jpg",
    "The Lovers": "3/3a/TheLovers.jpg/300px-TheLovers.jpg",
    "The Chariot": "9/9b/RWS_Tarot_07_Chariot.jpg/300px-RWS_Tarot_07_Chariot.jpg",
    "Strength": "f/f5/RWS_Tarot_08_Strength.jpg/300px-RWS_Tarot_08_Strength.jpg",
    "The Hermit": "4/4d/RWS_Tarot_09_Hermit.jpg/300px-RWS_Tarot_09_Hermit.jpg",
    "Wheel of Fortune": "3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg/300px-RWS_Tarot_10_Wheel_of_Fortune.jpg",
    "Justice": "e/e0/RWS_Tarot_11_Justice.jpg/300px-RWS_Tarot_11_Justice.jpg",
    "The Hanged Man": "2/2b/RWS_Tarot_12_Hanged_Man.jpg/300px-RWS_Tarot_12_Hanged_Man.jpg",
    "Death": "d/d7/RWS_Tarot_13_Death.jpg/300px-RWS_Tarot_13_Death.jpg",
    "The Star": "d/db/RWS_Tarot_17_Star.jpg/300px-RWS_Tarot_17_Star.jpg"
}

def get_card_image(card_name):
    """Fetch the Tarot card image from Wikimedia Commons."""
    if card_name in image_paths:
        return image_base_url + image_paths[card_name]
    return None

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
