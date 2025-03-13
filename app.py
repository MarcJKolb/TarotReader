import streamlit as st
import random
import matplotlib.pyplot as plt
from PIL import Image
import os

# Load detailed Tarot meanings from a structured dataset
def load_tarot_meanings():
    return {
        "The Fool": "Represents new beginnings, spontaneity, and free spirit.",
        "The Magician": "Symbolizes power, resourcefulness, and inspired action.",
        "The High Priestess": "Encourages intuition, mystery, and inner wisdom.",
        "The Empress": "Represents nurturing, abundance, and femininity.",
        "The Emperor": "Stands for authority, structure, and stability.",
        "The Hierophant": "Symbolizes tradition, spiritual guidance, and wisdom.",
        "The Lovers": "Reflects choices, harmony, and relationships.",
        "The Chariot": "Signifies determination, control, and victory.",
        "Strength": "Embodies courage, patience, and inner strength.",
        "The Hermit": "Encourages soul-searching, introspection, and guidance.",
        "Wheel of Fortune": "Symbolizes fate, change, and life cycles.",
        "Justice": "Represents truth, fairness, and law.",
        "The Hanged Man": "Denotes letting go, new perspectives, and sacrifice.",
        "Death": "Symbolizes transformation, endings, and renewal.",
        "Temperance": "Stands for balance, patience, and purpose.",
        "The Devil": "Warns of addiction, materialism, and bondage.",
        "The Tower": "Denotes sudden upheaval, chaos, and revelation.",
        "The Star": "Represents hope, inspiration, and serenity.",
        "The Moon": "Symbolizes illusion, fear, and subconscious mind.",
        "The Sun": "Brings joy, success, and vitality.",
        "Judgement": "Calls for reflection, reckoning, and awakening.",
        "The World": "Marks completion, achievement, and travel."
    }

# Available spreads with detailed placements and explanations
spreads = {
    "One Card Draw": {
        "positions": ["Card 1"],
        "layout": [(0.5, 0.5)],
        "explanation": ["A single card insight into your situation."]
    },
    "Past-Present-Future": {
        "positions": ["Past", "Present", "Future"],
        "layout": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)],
        "explanation": [
            "Past: Influences shaping the current situation.",
            "Present: The present state and its challenges.",
            "Future: The likely outcome based on the current trajectory."
        ]
    },
    "Celtic Cross": {
        "positions": [
            "Present", "Challenge", "Past", "Future", "Above", "Below",
            "Advice", "External Influences", "Hopes & Fears", "Outcome"
        ],
        "layout": [
            (0.5, 0.5), (0.6, 0.5), (0.4, 0.5), (0.7, 0.5), (0.5, 0.7), (0.5, 0.3),
            (0.8, 0.8), (0.8, 0.6), (0.8, 0.4), (0.8, 0.2)
        ],
        "explanation": [
            "Present: Your current situation.",
            "Challenge: Main obstacle or issue at hand.",
            "Past: Key factors influencing the present.",
            "Future: Possible developments.",
            "Above: Conscious influences guiding you.",
            "Below: Subconscious factors affecting the situation.",
            "Advice: Suggested approach or wisdom.",
            "External Influences: Outside forces impacting you.",
            "Hopes & Fears: What you hope for or fear.",
            "Outcome: The likely result of the situation."
        ]
    }
}

def load_card_image(card_name):
    """Loads a Tarot card image if available."""
    filename = f"images/{card_name.replace(' ', '_')}.jpg"
    if os.path.exists(filename):
        return Image.open(filename)
    return None

st.title("Tarot Reading App")

# Dropdown for spread selection
spread_choice = st.selectbox("Choose a Tarot Spread", list(spreads.keys()))

tarot_meanings = load_tarot_meanings()

if st.button("Draw Cards"):
    spread = spreads[spread_choice]
    drawn_cards = random.sample(list(tarot_meanings.keys()), len(spread["positions"]))
    
    st.subheader("Your Reading:")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    
    for i, (card, pos, explanation) in enumerate(zip(drawn_cards, spread["layout"], spread["explanation"])):
        x, y = pos
        card_image = load_card_image(card)
        
        if card_image:
            st.image(card_image, caption=f"{spread['positions'][i]}: {card}", use_column_width=True)
        else:
            ax.text(x, y, f"{spread['positions'][i]}\n{card}", ha='center', va='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        st.write(f"**{spread['positions'][i]}: {card}**")
        st.write(f"_Meaning_: {tarot_meanings[card]}")
        st.write(f"_Role_: {explanation}")
        st.write("---")
    
    st.pyplot(fig)
