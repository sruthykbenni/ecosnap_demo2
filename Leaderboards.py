def display_leaderboard(filter_option):
    """
    Display the leaderboard based on the selected filter option.
    
    Parameters:
    - filter_option (str): The selected filter for the leaderboard.
    """
    # Convert user data to DataFrame for easier manipulation
    df = pd.DataFrame(user_data)

    # Filter based on the selected option
    if filter_option == "Global":
        filtered_df = df
    elif filter_option == "Regional":
        region = st.selectbox("Select your region", df['region'].unique())
        filtered_df = df[df['region'] == region]
    elif filter_option == "Friends":
        filtered_df = df  # Replace with actual friends filter logic
    elif filter_option == "Corporate Teams":
        filtered_df = df  # Replace with actual corporate team logic

    # Sort by total CO₂ saved
    filtered_df = filtered_df.sort_values(by="total_co2_saved", ascending=False).reset_index(drop=True)

    # Add Rank column starting from 1
    filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))

    # Display the leaderboard
    st.write("### Leaderboard")
    st.dataframe(filtered_df[['Rank', 'username', 'total_co2_saved', 'streak_count']])

    # Highlight gamified metrics
    top_streak_holder = filtered_df.loc[filtered_df['streak_count'].idxmax()]
    st.write(f"🏆 **Top Streak Holder:** {top_streak_holder['username']} with a streak of {top_streak_holder['streak_count']} days!")

    greenest_user = filtered_df.loc[filtered_df['total_co2_saved'].idxmax()]
    st.write(f"🌱 **Greenest User of the Month:** {greenest_user['username']} with {greenest_user['total_co2_saved']} kg CO₂ saved!")
