# 🎵 Know Your Music: Music Analysis & Recommendation Hub

**Know Your Music** is a data-driven Django web application designed to help users explore a massive dataset of tracks and receive personalized recommendations. By integrating **Pandas** for data handling and **Matplotlib** for dynamic visualization, the app transforms static music data into an interactive discovery experience.

---

## 🚀 Key Features

* **Dynamic Data Ingestion:** Automatically populates the application database by parsing local Excel datasets (`.xlsx`) using the Pandas library.
* **Customized Recommendations:** A multi-layered filtering system that allows users to find tracks based on:
    * **Genre:** Dozens of options ranging from *Modern Bollywood* and *Qawwali* to *Alt Z* and *Trap Latino*.
    * **Era:** Precise filtering by release year (2010–2023).
    * **Duration:** Mood-based selection for short, medium, or long tracks.
* **Popularity Visualization:** Generates real-time bar charts using Matplotlib to compare the "Popularity Score" of recommended tracks, rendered directly in the browser via Base64 encoding.
* **Insightful Metadata:** Provides detailed track info, including acousticness, danceability, energy, and liveness.

---

## 🛠️ Technical Stack

* **Backend Framework:** Python & Django
* **Data Processing:** Pandas & Openpyxl
* **Data Visualization:** Matplotlib (Server-side rendering)
* **Database:** Django ORM (SQLite/PostgreSQL)
* **Frontend:** HTML5, CSS3, JavaScript

---

## 📂 Project Structure

```text
Project_song_analysis/
│
├── music_analysis/            # Configuration Folder
│   ├── settings.py            # App settings
│   └── urls.py                # Global routing
│
├── music_app/                 # Main Application Folder
│   ├── models.py              # Music track schema (19+ attributes)
│   ├── views.py               # Recommendation logic & chart generation
│   ├── forms.py               # User input handling
│   ├── templates/             # HTML User Interfaces
│   │   ├── home.html          # Landing page
│   │   ├── newpage.html       # Selection form
│   │   └── recommendations.html # Results & Visualization
│   └── static/                # CSS & Frontend scripts
│
└── manage.py                  # Project management script
```

---

## ⚙️ Logic Overview

### **Data Lifecycle**
1.  **Loading:** The `load_data()` function reads the `data_analytics_project.xlsx` file and maps every column (e.g., *speechiness*, *valence*, *tempo*) to the Django `Song` model.
2.  **Filtering:** When a user submits the `RecommendationForm`, the app uses Django's `icontains` query expressions to perform case-insensitive genre matches across the database. 
3.  **Analytics:** The `create_popularity_chart()` function takes the popularity scores of the final 10 selected tracks, creates a bar chart, and streams it to the frontend as a PNG without requiring local file storage.

---

## 📊 Input Options

The recommendation engine is optimized for a wide variety of musical tastes, including:
* **Genres:** Filmi, Indian Indie, Reggaeton, Classic Rock, Afrobeats, and more.
* **Duration:** * **Short:** < 3 minutes
    * **Medium:** 3–5 minutes
    * **Long:** > 5 minutes

---
