import streamlit as st
import random

# Tarot deck (simplified, can be expanded)
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

# Available spreads
spreads = {
    "One Card Draw": 1,
    "Past-Present-Future": 3,
    "Celtic Cross": 10
}

st.title("Tarot Reading App")

# Dropdown for spread selection
spread_choice = st.selectbox("Choose a Tarot Spread", list(spreads.keys()))

if st.button("Draw Cards"):
    num_cards = spreads[spread_choice]
    drawn_cards = random.sample(list(tarot_deck.keys()), num_cards)
    
    st.subheader("Your Reading:")
    for i, card in enumerate(drawn_cards, 1):
        st.write(f"**Card {i}: {card}**")
        st.write(f"_Meaning_: {tarot_deck[card]}")
        st.write("---")
