# Movie Recommender System

This project is a Movie Recommender System that suggests similar movies based on a user’s selection. Using content-based filtering techniques, it recommends movies by analyzing metadata and calculating similarity scores between films.

## 📂 Dataset

Source: TMDB Movie Dataset on Kaggle

Description: Contains movie metadata including titles, genres, overviews, cast, crew, and more.

## 🧠 Implementation Details

Vectorization:

Used Count Vectorizer to convert movie metadata (tags) into a numerical vector representation.

## Similarity Calculation:

Calculated Cosine Similarity (from sklearn.metrics) between movie vectors to measure how closely related two movies are.

## Recommendation Engine:

For any selected movie, the system retrieves the top N similar movies using the similarity matrix.

## UI Interface:

Built an interactive Streamlit interface for users to input a movie name and get recommendations instantly.

## 🛠️ Tech Stack

Language: Python

##Libraries:

scikit-learn for vectorization & similarity calculation

pandas, numpy for data handling

streamlit for UI

matplotlib, seaborn (optional) for visualization

## 📊 Features

Content-Based Filtering: Uses movie metadata to recommend similar movies.

Interactive UI: Easy-to-use Streamlit app for real-time recommendations.

Customizable Recommendations: Adjust the number of movies recommended as per your preference.

## 🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

## 📂 Project Structure
```
movie-recommender-system/
│
├── data/                   # Dataset (if included)
├── app.py                  # Streamlit UI application
├── model/                  # Saved similarity matrix (if saved)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── notebooks/              # Jupyter notebooks for exploration & preprocessing

```
## 📈 Results

Recommends movies based on similarity score using Count Vectorizer + Cosine Similarity.

Efficient recommendation engine with real-time results via Streamlit.

## 📚 References

TMDB Dataset on Kaggle

Scikit-learn Documentation

Streamlit Documentation

## 🤝 Contributing

Contributions are welcome! Fork the repository and create a pull request to add new features or improve existing ones.
