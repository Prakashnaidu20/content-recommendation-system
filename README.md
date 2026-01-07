# 🎬 Content Recommendation System

## 📌 Project Overview
This project implements an **AI-based Content Recommendation System** that suggests
relevant multimedia content based on **user context** such as **age, mood, and time of day**.

The system is designed using a **rule-based and score-driven recommendation approach**
to demonstrate the core principles behind modern recommendation systems used in
platforms like YouTube, Netflix, and Spotify.


## 🧠 Project Track
**Artificial Intelligence – Recommendation Systems**


## 🎯 Problem Statement
Digital platforms host a massive amount of content, making it difficult for users
to discover content that matches their interests and context.

The objective of this project is to:
- Reduce information overload
- Improve content discovery
- Recommend personalized content using AI-inspired logic


## 🌍 Real-World Relevance
Recommendation systems are widely used in:
- YouTube video suggestions
- Netflix movie recommendations
- Spotify music playlists
- Online education platforms

This project demonstrates a simplified and explainable version of such systems,
suitable for learning, experimentation, and academic evaluation.


## 📊 Dataset Description
- **Dataset Type:** Synthetic (manually curated)
- **Source:** Publicly available YouTube content
- **Categories Included:**
  - Education
  - Technology
  - Startups
  - Movies
  - Music
  - Comedy
  - Action

### 🔑 Features Used
- Content category
- User mood
- Time of day
- Age range
- Popularity rating


## ⚙️ System Design

### AI Technique Used
- Rule-Based + Score-Driven Recommendation System

### Recommendation Pipeline
1. User inputs (age, mood, time)
2. Contextual filtering
3. Relevance score computation
4. Content ranking
5. Top-N recommendations

### Design Justification
- Explainable and transparent AI
- No dependency on large user datasets
- Ideal for academic and prototype systems


## 🧪 Evaluation & Analysis

### Metrics Used
- Heuristic relevance score
- Contextual alignment
- Qualitative evaluation

### Observations
- Energetic users receive action, startup, and technology content
- Relaxed users receive music and comedy content
- Time-based context improves recommendation quality

### Limitations
- No collaborative filtering
- Synthetic dataset
- Manual weight tuning


## ⚖️ Ethical Considerations & Responsible AI
- Potential bias due to age and mood filtering
- Limited dataset diversity
- Designed strictly for educational and experimental use


## 🚀 Future Enhancements
- Collaborative filtering
- Machine learning models (KNN, Matrix Factorization)
- LLM-based semantic recommendations
- Real-time user feedback learning
- Database-backed system


## ▶️ How to Run the Project

### Run Notebook
1. Open `Content_Recommendation_System.ipynb`
2. Select **Kernel → Restart & Run All**
3. View outputs in the final cells

### Optional Streamlit Deployment
```bash
streamlit run app.py
