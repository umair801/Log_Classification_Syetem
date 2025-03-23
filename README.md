# Log Classification with a Hybrid Classification Framework  

This project implements a **hybrid log classification system**, combining multiple approaches to effectively classify log data with varying levels of complexity. The framework ensures flexibility and robustness when handling **structured, semi-structured, and unstructured log patterns**.  

## 🔹 Classification Approaches  

1. **Regular Expressions (Regex)**  
   - Best for handling **simplified and predictable** log patterns.  
   - Useful when logs follow a **consistent structure** that can be captured using predefined rules.  

2. **Sentence Transformer + Logistic Regression**  
   - Suitable for **complex log patterns** with sufficient labeled training data.  
   - Utilizes **Sentence Transformer embeddings** and applies **Logistic Regression** for classification.  

3. **Large Language Models (LLM)**  
   - Designed for **highly complex or poorly labeled** log data.  
   - Serves as a **fallback** when sufficient training data is unavailable, leveraging the generalization power of LLMs.  

---  

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/umair801/Log_Classification_Syetem.git
cd Log_Classification_Syetem
```

### 2️⃣ Install Dependencies  
Ensure you have Python 3.8+ installed. Then, install the required dependencies:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Server  
Start the API service to process log classification requests:  
```bash
uvicorn main:app --reload
```

---  

## 📌 Usage  

Upload a **CSV file** containing logs to the FastAPI endpoint for classification. The file must include the following columns:  
- `source`  
- `log_message`  

After processing, the system returns a **CSV file** with an additional column:  
- `target_label` → The classified log category.  

---  

## 📬 API Endpoint  

- **URL**: `http://localhost:8000/classify`  
- **Method**: `POST`  
- **Payload**: CSV file with `source` and `log_message` columns.  
- **Response**: CSV file with an added `target_label` column.  
