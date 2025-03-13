import streamlit as st
import random
import matplotlib.pyplot as plt
from PIL import Image
import os

# Tarot deck including Major and Minor Arcana (simplified for now)
tarot_deck = {
    "The Fool": "New beginnings, optimism, trust in life.",
    "The Magician": "Action, the power to manifest.",
    "The High Priestess": "Inaction, going within, the mystical.",
    "The Empress": "Motherhood, fertility, nature.",
    "The Emperor": "Fatherhood, leadership, stability.",
    "The Hierophant": "Tradition, conformity, morality and ethics.",
    "The Lovers": "Love, union, relationships, values alignment.",
    "The Chariot": "Control, willpower, success, action, determination.",
    "Strength": "Courage, subtle power, compassion, persuasion.",
    "The Hermit": "Contemplation, search for truth, inner guidance.",
    "Wheel of Fortune": "Change, cycles, fate, decisive moments.",
    "Justice": "Fairness, truth, cause and effect, law.",
    "The Hanged Man": "Sacrifice, release, martyrdom.",
    "Death": "Endings, transformation, transition.",
    "Temperance": "Balance, moderation, being sensible.",
    "The Devil": "Destructive patterns, addiction, giving away power.",
    "The Tower": "Sudden upheaval, broken pride, disaster.",
    "The Star": "Hope, faith, rejuvenation.",
    "The Moon": "Mystery, the subconscious, dreams.",
    "The Sun": "Joy, success, celebration, positivity.",
    "Judgement": "Reflection, reckoning, awakening.",
    "The World": "Completion, wholeness, integration, travel."
}

# Add Minor Arcana
suits = ["Wands", "Cups", "Swords", "Pentacles"]
values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]
for suit in suits:
    for value in values:
        tarot_deck[f"{value} of {suit}"] = "A unique interpretation based on traditional meanings."

# Available spreads
spreads = {
    "One Card Draw": {"positions": ["Card 1"], "layout": [(0.5, 0.5)], "explanation": ["A single card insight into your situation."]},
    "Past-Present-Future": {
        "positions": ["Past", "Present", "Future"],
        "layout": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)],
        "explanation": [
            "Past: Influences that have shaped the situation.",
            "Present: The current state and challenges.",
            "Future: The direction in which things are headed."
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
            "Present: The current situation.",
            "Challenge: The main obstacle or issue.",
            "Past: Factors leading to the present.",
            "Future: Likely developments.",
            "Above: Conscious influences.",
            "Below: Subconscious influences.",
            "Advice: Guidance for action.",
            "External Influences: Factors beyond control.",
            "Hopes & Fears: Inner hopes or anxieties.",
            "Outcome: The likely result."
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

if st.button("Draw Cards"):
    spread = spreads[spread_choice]
    drawn_cards = random.sample(list(tarot_deck.keys()), len(spread["positions"]))
    
    st.subheader("Your Reading:")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    
    for i, (card, pos, explanation) in enumerate(zip(drawn_cards, spread["layout"], spread["explanation"])):
        x, y = pos
        ax.text(x, y, f"{spread['positions'][i]}\n{card}", ha='center', va='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        st.write(f"**{spread['positions'][i]}: {card}**")
        st.write(f"_Meaning_: {tarot_deck[card]}")
        st.write(f"_Role_: {explanation}")
        
        # Display card image if available
        card_image = load_card_image(card)
        if card_image:
            st.image(card_image, caption=card, use_column_width=True)
        
        st.write("---")
    
    st.pyplot(fig)
