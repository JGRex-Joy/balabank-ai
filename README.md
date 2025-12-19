# 🏦 Balabank AI API

**Balabank AI API** is an intelligent question-answering system built with FastAPI that provides personalized responses based on financial literature. The API uses RAG (Retrieval-Augmented Generation) architecture with Google's Gemini models to deliver context-aware answers tailored for different audiences.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [How It Works](#-how-it-works)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 🤖 **Role-based responses**: Tailored answers for children and parents
- 🔍 **Semantic search**: FAISS-powered vector similarity search
- 🧠 **LLM integration**: Powered by Google Gemini 2.5 Flash
- 📚 **RAG architecture**: Retrieval-Augmented Generation for accurate, context-aware responses
- 🚀 **Fast and efficient**: Built with FastAPI for high performance
- 📊 **Embeddings**: Custom vector embeddings using Gemini Embedding model

---

## 🛠 Tech Stack

- **Framework**: FastAPI
- **LLM**: Google Gemini 2.5 Flash
- **Embeddings**: Google Gemini Embedding (768 dimensions)
- **Vector Search**: FAISS
- **Language**: Python 3.x
- **Data Processing**: NumPy, JSON

---

## 📁 Project Structure

```
balabank-ai/
├── app/
│   ├── routers/
│   │   ├── ask.py          # Ask endpoints (children/parent)
│   │   └── health.py       # Health check endpoint
│   ├── services/
│   │   ├── llm.py          # LLM integration
│   │   ├── search.py       # Vector search logic
│   │   └── server_embedder.py  # Embedding service
│   └── main.py             # FastAPI application
├── data/
│   ├── chunks.json         # Text chunks from financial books
│   └── index.faiss         # FAISS vector index
└── README.md
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Google AI Studio API key

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/balabank-ai-api.git
cd balabank-ai-api
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install fastapi uvicorn google-generativeai faiss-cpu numpy pydantic
```

4. **Prepare data files**

Ensure you have the following files in the `data/` directory:
- `chunks.json` - JSON array of text chunks with metadata
- `index.faiss` - Pre-built FAISS index

---

## ⚙️ Configuration

### API Keys

Update the Google API key in the following files:

**`app/services/llm.py`**
```python
client = genai.Client(api_key="YOUR_GOOGLE_API_KEY_HERE")
```

**`app/services/server_embedder.py`**
```python
client = genai.Client(api_key="YOUR_GOOGLE_API_KEY_HERE")
```

> **Note**: For production, use environment variables instead of hardcoding API keys.

### Environment Variables (Recommended)

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

Then update the code:
```python
import os
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
```

---

## 🎯 Usage

### Running the API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📡 API Endpoints

### 1. Health Check

```http
GET /health/
```

**Response:**
```json
{
  "status": "ok"
}
```

---

### 2. Ask for Children

```http
POST /ask/children
```

**Request Body:**
```json
{
  "prompt": "What is saving money?"
}
```

**Response:**
```json
{
  "llm_answer": "Saving money is like putting coins in a piggy bank! It means you keep some of your money safe instead of spending it all right away..."
}
```

---

### 3. Ask for Parents

```http
POST /ask/parent
```

**Request Body:**
```json
{
  "prompt": "What investment strategies are recommended?"
}
```

**Response:**
```json
{
  "llm_answer": "Based on the financial literature, recommended investment strategies include diversification, long-term planning, and risk assessment..."
}
```

---

## 🔄 How It Works

### RAG Pipeline

1. **Query Reception**: User sends a question via API
2. **Embedding Generation**: Query is converted to a 768-dimensional vector
3. **Semantic Search**: FAISS finds top-K most similar text chunks
4. **Context Building**: Retrieved chunks are combined into context
5. **LLM Generation**: Gemini generates a role-appropriate answer
6. **Response Delivery**: Answer is returned to the user

### Architecture Diagram

```
User Query → Embedder → FAISS Search → Context Retrieval
                                              ↓
                                         LLM (Gemini)
                                              ↓
                                    Role-based Answer → User
```

---

## 💡 Examples

### Using cURL

**Children endpoint:**
```bash
curl -X POST "http://localhost:8000/ask/children" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Why should I save money?"}'
```

**Parent endpoint:**
```bash
curl -X POST "http://localhost:8000/ask/parent" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "How to teach children about financial literacy?"}'
```

### Using Python

```python
import requests

url = "http://localhost:8000/ask/children"
data = {"prompt": "What is a bank?"}

response = requests.post(url, json=data)
print(response.json()["llm_answer"])
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 TODO

- [ ] Add authentication and authorization
- [ ] Implement rate limiting
- [ ] Add logging and monitoring
- [ ] Create unit and integration tests
- [ ] Add Docker support
- [ ] Implement caching for frequent queries
- [ ] Add more role types (teens, educators, etc.)
- [ ] Multi-language support

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Amir Omurkulov**

JGRex-Joy - Junior AI Engineer

Built with ❤️ as a legal-tech & LLM/AI engineering project.

---

## 🙏 Acknowledgments

- Google Gemini AI for powerful LLM capabilities
- FAISS for efficient vector search
- FastAPI for the excellent web framework

---

