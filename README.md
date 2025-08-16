# 🎬 Film Recommendation System(Work in progress)

## 📌 Overview
The **Film Recommendation System** is a project designed to suggest movies to users based on their preferences.  
It uses different recommendation strategies to provide personalized results and enhance the movie discovery experience.

This project is suitable for learning **Machine Learning**, **Web Development**, and **MLOps** integration.

---

## 🚀 Features
- **Content-Based Filtering**: Recommends movies similar to the one selected by the user.
- **Roulette Recommendation**: A fun option that randomly suggests a movie from the dataset.
- **Web Interface**: Simple and interactive frontend for users to explore movie recommendations.

---

## 🛠️ Tech Stack
- **Python**: Backend logic and recommendation algorithms.
- **Pandas / Numpy**: Data processing and similarity computation.
- **Scikit-learn**: Machine learning utilities.
- **Flask**: Web framework for serving recommendations.
- **HTML / CSS / JavaScript**: Frontend interface.

---

## 📂 Project Structure
```
Film-recommendation-system/
│── app.py                # Flask application entry point
│── recommendation.py      # Core recommendation logic
│── static/                # CSS, JS, and images
│── templates/             # HTML frontend pages
│── data/                  # Movie dataset(s)
│── README.md              # Project documentation
│── requirements.txt       # Python dependencies
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/MedAzBc/Film-recommendation-system.git
cd Film-recommendation-system
```

2. **Create and activate a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Flask app**
```bash
python app.py
```

5. **Open in browser**
```
http://127.0.0.1:5000/
```

---

## 🎮 How to Use
1. Select a movie from the list or input a movie title.
2. Choose between **Content-Based** or **Roulette Recommendation**.
3. View suggested movies instantly in the browser.

---

## 📊 Example Dataset
The system uses a dataset containing movies with features such as:
- Title  
- Genres  
- Description/Overview  
- Ratings  


