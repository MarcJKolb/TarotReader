import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

# Tarot card meanings (expanded)
tarot_meanings = {
    "The Fool": "A leap of faith, embracing the unknown, fresh starts, and limitless potential.",
    "The Magician": "Manifestation of goals, personal power, resourcefulness, and mastery.",
    "The High Priestess": "Hidden knowledge, intuition, spiritual wisdom, and the subconscious.",
    "The Empress": "Fertility, nurturing energy, abundance, creativity, and comfort.",
    "The Emperor": "Structure, authority, discipline, stability, and protection.",
    "The Hierophant": "Traditional wisdom, guidance, spiritual authority, and societal norms.",
    "The Lovers": "Deep relationships, moral dilemmas, choices guided by the heart, and harmony.",
    "The Chariot": "Victory through willpower, control over opposing forces, discipline, and ambition.",
    "Strength": "Inner courage, emotional mastery, patience, and overcoming adversity.",
    "The Hermit": "Seeking truth through solitude, introspection, wisdom, and guidance.",
    "Wheel of Fortune": "Cycles of change, fate, unexpected shifts, and turning points.",
    "Justice": "Balance, truth, accountability, fair decisions, and ethical clarity.",
    "The Hanged Man": "A shift in perspective, surrender, patience, and enlightenment through sacrifice.",
    "Death": "Transformation, the end of a phase, renewal, and necessary change.",
    "Temperance": "Balance, moderation, blending elements for harmony, and self-restraint.",
    "The Devil": "Bondage to materialism, addiction, toxic cycles, and illusions of control.",
    "The Tower": "Sudden upheaval, breaking false foundations, radical change, and revelation.",
    "The Star": "Hope, renewal, inspiration, and trusting in the universe’s guidance.",
    "The Moon": "Illusions, subconscious fears, uncertainty, and deep emotions.",
    "The Sun": "Joy, success, vitality, clarity, and celebration of life.",
    "Judgement": "A moment of reckoning, self-reflection, rebirth, and awakening.",
    "The World": "Completion, achieving goals, unity, wholeness, and fulfillment."
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
    "Temperance": "f/f8/RWS_Tarot_14_Temperance.jpg/300px-RWS_Tarot_14_Temperance.jpg",
    "The Devil": "5/55/RWS_Tarot_15_Devil.jpg/300px-RWS_Tarot_15_Devil.jpg",
    "The Tower": "5/53/RWS_Tarot_16_Tower.jpg/300px-RWS_Tarot_16_Tower.jpg",
    "The Star": "d/db/RWS_Tarot_17_Star.jpg/300px-RWS_Tarot_17_Star.jpg",
    "The Moon": "7/7f/RWS_Tarot_18_Moon.jpg/300px-RWS_Tarot_18_Moon.jpg",
    "The Sun": "1/17/RWS_Tarot_19_Sun.jpg/300px-RWS_Tarot_19_Sun.jpg",
    "Judgement": "d/dd/RWS_Tarot_20_Judgement.jpg/300px-RWS_Tarot_20_Judgement.jpg",
    "The World": "f/ff/RWS_Tarot_21_World.jpg/300px-RWS_Tarot_21_World.jpg"
}

st.title("Tarot Reading App")
spread_choice = st.selectbox("Choose a Tarot Spread", ["One Card Draw", "Past-Present-Future", "Celtic Cross"])
num_cards = 1 if spread_choice == "One Card Draw" else (3 if spread_choice == "Past-Present-Future" else 10)
if st.button("Draw Cards"):
    drawn_cards = random.sample(list(tarot_meanings.keys()), num_cards)
    for card in drawn_cards:
        image_url = image_base_url + image_paths.get(card, "")
        col1, col2 = st.columns([1, 2])
        with col1:
            if image_url:
                st.image(image_url, caption=card, use_container_width=True)
        with col2:
            st.write(f"**{card}**")
            st.write(f"_Meaning_: {tarot_meanings[card]}")
        st.write("---")
