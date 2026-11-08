import streamlit as st
import requests

st.set_page_config(
    page_title="TravelPlanner AI",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ TravelPlanner AI")
st.write("Plan your perfect trip using AI + n8n + Gemini")

# n8n production webhook
N8N_WEBHOOK_URL = "http://localhost:5678/webhook/travel-planner"


# =========================
# USER INPUT
# =========================

destination = st.text_input(
    "📍 Destination",
    placeholder="Example: Coorg"
)

days = st.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=30,
    value=3
)

budget = st.number_input(
    "💰 Budget (₹)",
    min_value=1000,
    max_value=1000000,
    value=15000
)

travel_mode = st.selectbox(
    "🚗 Travel Mode",
    [
        "Bike",
        "Car",
        "Bus",
        "Train",
        "Flight"
    ]
)

travelers = st.number_input(
    "👨‍👩‍👧‍👦 Number of Travelers",
    min_value=1,
    max_value=20,
    value=2
)

interests = st.multiselect(
    "🎯 Your Interests",
    [
        "Nature",
        "Adventure",
        "Beaches",
        "Historical Places",
        "Food",
        "Shopping",
        "Temples",
        "Photography",
        "Nightlife"
    ]
)


# =========================
# PLAN TRIP
# =========================

if st.button("✈️ Plan My Trip"):

    if not destination:

        st.warning("⚠️ Please enter a destination.")

    else:

        data = {
            "destination": destination,
            "days": days,
            "budget": budget,
            "travel_mode": travel_mode,
            "travelers": travelers,
            "interests": interests
        }

        try:

            with st.spinner(
                "🤖 Gemini is planning your trip..."
            ):

                response = requests.post(
                    N8N_WEBHOOK_URL,
                    json=data,
                    timeout=60
                )


            # =========================
            # SUCCESS
            # =========================

            if response.status_code == 200:

                st.success(
                    "✅ Trip plan generated!"
                )

                st.subheader(
                    "🗺️ Your AI Travel Plan"
                )

                try:

                    # Convert n8n JSON response
                    result = response.json()

                    # Extract Gemini response
                    advice = result[
                        "content"
                    ][
                        "parts"
                    ][0][
                        "text"
                    ]

                    # Display only AI answer
                    st.markdown(advice)

                except Exception as e:

                    st.error(
                        "⚠️ Could not read the AI response."
                    )

                    st.code(
                        response.text
                    )


            # =========================
            # n8n ERROR
            # =========================

            else:

                st.error(
                    f"❌ n8n Error: "
                    f"{response.status_code}"
                )

                st.code(
                    response.text
                )


        # =========================
        # CONNECTION ERROR
        # =========================

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to n8n. "
                "Make sure n8n is running."
            )


        # =========================
        # TIMEOUT
        # =========================

        except requests.exceptions.Timeout:

            st.error(
                "⏳ Request timed out. "
                "Gemini/n8n took too long to respond."
            )


        # =========================
        # OTHER ERROR
        # =========================

        except Exception as e:

            st.error(
                f"❌ Error: {e}"
            )