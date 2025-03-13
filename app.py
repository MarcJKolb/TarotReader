import streamlit as st
import random
import matplotlib.pyplot as plt
from PIL import Image
import requests
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

# Base URL for Tarot images from the Rider-Waite deck
image_base_url = "https://www.sacred-texts.com/tarot/xr/i"

def get_card_image(card_name):
    """Fetch the Tarot card image from the online source."""
    image_filename = card_name.lower().replace(" ", "") + ".jpg"
    image_url = f"{image_base_url}/{image_filename}"
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
    except Exception as e:
        return None
    return None

# Available spreads with positions
spreads = {
    "One Card Draw": {
        "positions": ["Insight"],
        "layout": [(0.5, 0.5)]
    },
    "Past-Present-Future": {
        "positions": ["Past", "Present", "Future"],
        "layout": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)]
    },
    "Celtic Cross": {
        "positions": [
            "Present Situation", "Challenge", "Past Influences", "Future Outlook", "Conscious Goals", "Subconscious Influences",
            "Advice", "External Influences", "Hopes & Fears", "Final Outcome"
        ],
        "layout": [
            (0.5, 0.5), (0.6, 0.5), (0.4, 0.5), (0.7, 0.5), (0.5, 0.7), (0.5, 0.3),
            (0.8, 0.8), (0.8, 0.6), (0.8, 0.4), (0.8, 0.2)
        ]
    }
}

st.title("Tarot Reading App")

# Dropdown for spread selection
spread_choice = st.selectbox("Choose a Tarot Spread", list(spreads.keys()))

if st.button("Draw Cards"):
    spread = spreads[spread_choice]
    drawn_cards = random.sample(list(tarot_meanings.keys()), len(spread["positions"]))
    
    st.subheader("Your Reading:")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    
    for i, (card, pos) in enumerate(zip(drawn_cards, spread["layout"])):
        x, y = pos
        card_image = get_card_image(card)
        
        if card_image:
            st.image(card_image, caption=f"{spread['positions'][i]}: {card}", use_column_width=True)
        else:
            ax.text(x, y, f"{spread['positions'][i]}\n{card}", ha='center', va='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        st.write(f"**{spread['positions'][i]}: {card}**")
        st.write(f"_Meaning_: {tarot_meanings[card]}")
        st.write("---")
    
    st.pyplot(fig)
