# Movie Recommender System

This project is a simple and fun movie recommender app built with Streamlit. If you ever find yourself stuck picking your next film, just open this app, pick a movie you like, and get five solid recommendations—complete with posters.

---

## What does it do?
- Lets you choose any movie from a big list (thousands of titles!)
- Instantly gives you five similar movies you might enjoy
- Shows the posters for each recommended movie
- All in a clean, easy-to-use web interface

---

## How to Run It

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Install the requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app**
   ```bash
   streamlit run app.py
   ```
   The app will open in your browser. Just pick a movie and hit "Recommend".

4. **(Optional) Add your TMDB API token**
   - For better poster quality, you can add your TMDB API Bearer token in `.streamlit/secrets.toml` like this:
     ```
     [general]
     TMDB_TOKEN = "your_tmdb_bearer_token"
     ```
   - If you skip this, the app still works, but some posters might not load.

---

## How it Works (in plain English)
- The app loads a list of movies and a pre-computed similarity matrix.
- When you pick a movie, it finds the five most similar ones (based on content, not ratings).
- For each recommendation, it fetches the poster from TMDB.
- Everything is shown in a friendly web interface using Streamlit.

---

## Project Structure

```
movie-recommender-system/
├── app.py                # Main app code
├── movies_dict.pkl       # Movie metadata
├── similarity.pkl        # Similarity matrix (auto-downloads if missing)
├── requirements.txt      # List of dependencies
├── Dataset/              # Source data (zipped CSVs)
│   ├── tmdb_5000_movies.csv.zip
│   └── tmdb_5000_credits.csv.zip
└── README.md
```

---

## Credits & Data
- Movie data from the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Posters and extra info via [The Movie Database (TMDB) API](https://www.themoviedb.org/documentation/api)

---

## License
This project is for learning and demo purposes. Please respect the terms of use for all data sources and APIs.

---

If you have any questions or ideas for improvement, feel free to open an issue or reach out!