# Analytics.Ai

Analytics.Ai is a Flask-based application designed to provide REST APIs for analyzing social media posts. The project integrates LangFlow for Retrieval-Augmented Generation (RAG), enabling insightful analysis and responses about social media applications. Astra DB is used for data storage, along with its vector store capabilities for seamless integration with LangFlow.

---

## Tech Stack  
- **Flask**: For building REST APIs  
- **LangFlow**: For RAG implementation to retrieve insights  
- **Astra DB**: For storing social media post data and leveraging vector store capabilities  

---

## Features  
1. **REST APIs**: Provides endpoints for accessing and analyzing social media data.  
2. **RAG Integration**: Uses LangFlow to generate insights based on stored social media posts.  
3. **Astra DB Integration**:  
   - Stores social media posts in a scalable, cloud-native database.  
   - Utilizes vector storage for enhanced data retrieval and processing.  

---

## Installation  

### Prerequisites  
- Python 3.8 or higher  
- Astra DB account and credentials  
- Required Python libraries (listed in `requirements.txt`)  

### Steps  
1. **Clone the repository**  
   ```bash  
   https://github.com/social-media-analysis-org/sma-backend.git
   cd sma-backend
   
2. **Set up a virtual environment**  
   ```bash  
   python3 -m venv venv
   source venv/bin/activate

3. **Install dependencies**  
   ```bash  
   pip install -r requirements.txt 

4. **Run the application**  
   ```bash  
   python main.py

5. **Access the application**
   - Open your browser and navigate to http://127.0.0.1:5000/

