function getRecommendations() {
    const selectedGenres = getSelectedGenres(); // Function to get selected genres from the form
    if (selectedGenres.length === 0) {
        alert("Please select at least one genre.");
        return;
    }

    // Send a POST request to the /get_recommendations endpoint
    fetch("/get_recommendations", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ selectedGenres: [genre] })
    })
    .then(response => response.json())
    .then(recommendation => {
        // Handle the response data and display recommendations
        displayRecommendations(re);
    })
    .catch(error => {
        console.error("Error fetching recommendations:", error);
    });
}

function getSelectedGenres() {
    // Your code to retrieve the selected genres from the user goes here
    // For example, you can use checkboxes to allow the user to select genres
    // and then get the selected genres from the checkboxes
    // Here, we'll use some dummy genres for testing
    return ['Viusasa', 'Entertainment', 'Music', 'News', 'Sports', 'Talk shows'];
}
function displayRecommendations(recommendations) {
    // Get the recommendationsSection element from the DOM
    const recommendationsSection = document.getElementById("recommendationsSection");
    recommendationsSection.innerHTML = ""; // Clear previous content (if any)

    // Loop through each genre and its recommendations
    for (const genre in recommendations) {
        const genreRecommendations = recommendations[genre];
        const genreTitle = document.createElement("h2");
        genreTitle.textContent = `${genre} Recommendations:`;
        recommendationsSection.appendChild(genreTitle);

        const recommendationList = document.createElement("ul");
        for (const recommendation of genreRecommendations) {
            const listItem = document.createElement("li");
            listItem.textContent = recommendation;
            recommendationList.appendChild(listItem);
        }
        recommendationsSection.appendChild(recommendationList);
    }
}

// script.js

// Event listener for the "Get Recommendations" button
document.getElementById("getRecommendationsButton").addEventListener("click", getRecommendations);

