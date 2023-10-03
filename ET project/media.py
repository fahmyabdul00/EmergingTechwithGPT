from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to get TV program recommendations for each genre
def get_tv_recommendations(genre):
    # Replace this code with your actual logic to fetch TV program recommendations for the genre
    # Example: You might have a database or API to fetch TV program data
    tv_recommendations = {
        "news": [("Citizen Nipashe", "19:00", "Monday - Friday"), ("Inooro News", "19:30", "Monday - Friday")],
        "music": [("Muziki Mzuqa", "15:00", "Saturday"), ("Mugithi Sunday", "14:00", "Sunday")],
        "entertainment": [("The Trend", "22:00", "Friday"), ("Inooro Ithe Wa Maria", "20:00", "Saturday")],
        "sports": [("Friday Night Football", "20:00", "Friday"), ("Monday Night Football", "20:00", "Monday")],
        "talk shows": [("Jeff Koinange Live", "20:00", "Wednesday"), ("Inooro Riika Na Ta", "21:00", "Saturday")]
        # Add more genres and program recommendations as needed
    }
    return tv_recommendations.get(genre.lower(), [])


# Function to get radio program recommendations for each genre
def get_radio_recommendations(genre):
    # Replace this code with your actual logic to fetch radio program recommendations for the genre
    # Example: You might have a database or API to fetch radio program data
    radio_recommendations = {
        "news": [("Royal News Bulletin", "07:00", "Monday - Friday"), ("Mugambo wa Mugikuyu", "19:00", "Monday - Friday")],
        "music": [("Lunchtime Reggae", "13:00", "Monday - Friday"), ("Benga Sunday", "14:00", "Sunday")],
        "entertainment": [("Brekko", "06:00", "Monday - Friday"), ("Rurumuka", "15:00", "Saturday")],
        "sports": [("Sports Roundup", "18:00", "Monday - Friday"), ("Bunge La Mwananchi", "21:00", "Wednesday")],
        "talk shows": [("Jambo Kenya", "07:00", "Monday - Friday"), ("Tuko Pamoja", "22:00", "Saturday")]
        # Add more genres and program recommendations as needed
    }
    return radio_recommendations.get(genre.lower(), [])


# Example route to handle AJAX request and return recommendations
@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    # Get the selected genres from the AJAX request
    selected_genres = request.json['selectedGenres']

    # Prepare the recommendations based on the selected genres
    recommendations = {}
    for genre in selected_genres:
        tv_recommendations = get_tv_recommendations(genre)
        radio_recommendations = get_radio_recommendations(genre)
        recommendations[genre] = tv_recommendations + radio_recommendations

    # Return the recommendations as a JSON response
    return jsonify(recommendations)

@app.route('/media.html')
def index():
    return render_template('media.html')

if __name__ == '__main__':
    app.run(debug=True)


# Welcome message
print("Welcome to the Royal Media Services!")
print("This system can assist viewers in recommending suitable media content based on their preferred genres.")
print("Please answer the following question to the best of your ability.")


# Function to recommend TV programs for each genre
def recommend_tv_programs(genre):
    tv_programs = {
        "news": [("Citizen Nipashe", "19:00", "Monday - Friday"), ("Inooro News", "19:30", "Monday - Friday")],
        "music": [("Muziki Mzuqa", "15:00", "Saturday"), ("Mugithi Sunday", "14:00", "Sunday")],
        "entertainment": [("The Trend", "22:00", "Friday"), ("Inooro Ithe Wa Maria", "20:00", "Saturday")],
        "sports": [("Friday Night Football", "20:00", "Friday"), ("Monday Night Football", "20:00", "Monday")],
        "talk shows": [("Jeff Koinange Live", "20:00", "Wednesday"), ("Inooro Riika Na Ta", "21:00", "Saturday")]
    }
    return tv_programs.get(genre.lower(), [])


# Function to recommend radio programs for each genre
def recommend_radio_programs(genre):
    radio_programs = {
        "news": [("Royal News Bulletin", "07:00", "Monday - Friday"),
                 ("Mugambo wa Mugikuyu", "19:00", "Monday - Friday")],
        "music": [("Lunchtime Reggae", "13:00", "Monday - Friday"), ("Benga Sunday", "14:00", "Sunday")],
        "entertainment": [("Brekko", "06:00", "Monday - Friday"), ("Rurumuka", "15:00", "Saturday")],
        "sports": [("Sports Roundup", "18:00", "Monday - Friday"), ("Bunge La Mwananchi", "21:00", "Wednesday")],
        "talk shows": [("Jambo Kenya", "07:00", "Monday - Friday"), ("Tuko Pamoja", "22:00", "Saturday")]
    }
    return radio_programs.get(genre.lower(), [])


# Function to fetch trending videos from Viusasa (Example: Using an API)
def fetch_viusasa_trending_videos():
    # Replace this code with your API call or data fetching mechanism for Viusasa
    trending_videos = [
        ("Comedy Skit 1", "10:00", "Today"),
        ("Music Video Mix", "15:00", "Today"),
        ("Drama Series Premiere", "19:00", "Today"),
    ]
    return trending_videos.get(genre.lower(), [])


# Genre list for the user to choose from
genre_list = ["news", "music", "entertainment", "sports", "talk shows", "Viusasa"]

# Dictionary of related genres
related_genres = {
    "news": ["talk shows", "news", "sports"],
    "music": ["entertainment", "talk shows"],
    "entertainment": ["music", "talk shows"],
    "sports": ["entertainment", "talk shows"],
    "talk shows": ["news", "music", "entertainment", "sports"],
    "viusasa": ["music", "entertainment"],
}

# Print list of genres
print("Available genres to choose from:")
for index, genre in enumerate(genre_list, start=1):
    print(f"{index}. {genre.capitalize()}")

# Prompt the user to select their preferred media genres
while True:
    genre_selection_str = input("Enter the genre numbers separated by commas (e.g., 1,3): ")

    # Validate genre selections
    selected_genres = genre_selection_str.strip().split(",")
    try:
        selected_genres = [genre_list[int(genre_index) - 1] for genre_index in selected_genres]
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid genre numbers.")
        continue

    if not selected_genres:
        print("Preferred genres cannot be empty. Please try again.")
    else:
        break

# Genre names and descriptions
genre_descriptions = {
    "news": "Stay up-to-date with the latest news and current affairs.",
    "music": "Listen to a wide range of music genres and artists.",
    "entertainment": "Enjoy entertaining shows, dramas, and reality TV.",
    "sports": "Catch up on sports events, matches, and highlights.",
    "talk shows": "Engage in interesting discussions and interviews on various topics.",
    "viusasa": "Explore trending videos and content on the Viusasa platform."

}

# Recommend media content based on user's preferences
# Example media recommendations based on genre
for genre in selected_genres:
    genre_lower = genre.lower()
    if genre_lower in genre_descriptions:
        print(f"\nFor the genre '{genre.capitalize()}': {genre_descriptions[genre_lower]}")
        # Recommend TV programs for the genre
        tv_programs = recommend_tv_programs(genre_lower)
        if tv_programs:
            print("\nTV Programs:")
            for program, time, day in tv_programs:
                print(f" - {program} at {time} on {day}")
        # Recommend radio programs for the genre
        radio_programs = recommend_radio_programs(genre_lower)
        if radio_programs:
            print("\nRadio Programs:")
            for program, time, day in radio_programs:
                print(f" - {program} at {time} on {day}")
    else:
        if genre_lower == "viusasa":
            trending_viusasa_videos = fetch_viusasa_trending_videos()
            if trending_viusasa_videos:
                print("\nTrending Viusasa Videos:")
                for video_title, time, date in trending_viusasa_videos:
                    print(f" - {video_title} at {time} on {date}")
            else:
                print("No trending videos available on Viusasa.")
else:
    print(f"\nGenre '{genre}' not recognized. Please try again with valid genres.")

# Conclusion message
print("Please remember that these are just recommendations. Feel free to explore and enjoy the content on Royal Media "
      "Services. If you have any questions or need further assistance, feel free to ask.")
