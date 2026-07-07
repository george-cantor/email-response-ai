#   AI Email Response Assistant (RAG)

An end-to-end Retrieval-Augmented Generation (RAG) system that automatically generates professional email responses using semantic search and Large Language Models.

Built using Sentence Transformers, Gemini API, and a custom evaluation framework.

---

##  Project Overview

Customer support teams often receive repetitive emails regarding password resets, billing issues, refunds, subscription plans, and product inquiries.

This project automates the response generation process by:

1. Retrieving similar historical emails using semantic search.
2. Generating context-aware professional responses using Gemini.
3. Evaluating response quality using multiple scoring mechanisms.
4. Logging results for performance analysis.

---

##  System Architecture

```text
User Email
    │
    ▼
Semantic Retriever
(Sentence Transformers)
    │
    ▼
Top-K Similar Emails
    │
    ▼
Context Builder
    │
    ▼
Gemini Generator
    │
    ▼
Generated Reply
    │
    ▼
Evaluation Engine
 ├── Semantic Similarity
 ├── Retrieval Confidence
 └── LLM Judge Score
    │
    ▼
Performance Logging
```

---

##  Features

- Retrieval-Augmented Generation (RAG)
- Semantic Search using Sentence Transformers
- Context-Aware Email Generation
- Gemini API Integration
- Automated Evaluation Framework
- Retrieval Confidence Scoring
- Semantic Similarity Analysis
- LLM-Based Response Judging
- CSV-Based Result Logging
- Modular Project Structure

---

##  Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Data Handling | Pandas |
| Embeddings | Sentence Transformers |
| Similarity Search | Cosine Similarity |
| LLM | Google Gemini |
| Evaluation | Custom Scoring Framework |
| Environment | Python Dotenv |

---

##  Project Structure

```text
email-response-ai/
│
├── data/
│   └── raw/
│       └── email_dataset_v2.csv
│
├── outputs/
│   └── results.csv
│
├── src/
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── generation/
│   │   └── generator.py
│   │
│   ├── evaluation/
│   │   ├── final_evaluator.py
│   │   ├── logger.py
│   │   └── system_score.py
│   │
│   └── config.py
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

##  Dataset

The system uses a categorized email dataset containing customer support conversations.

### Categories

- Password Reset
- Login Issues
- Billing Issues
- Subscription Plans
- Refund Requests
- Order Tracking
- Shipping Delays
- Demo Requests
- Meeting Scheduling
- Feature Requests

### Dataset Size

- 100+ Email–Reply Pairs
- 10 Business Categories

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/george-cantor/email-response-ai.git

cd email-response-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Environment Setup

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶ Running the Project

```bash
python main.py
```

Example:

```text
Enter Email:

I forgot my password and cannot access my account.
```

Generated Response:

```text
Please use the password reset option available on the login page.
If the issue persists, kindly contact our support team for further assistance.
```

---

##  Evaluation Framework

Generated responses are evaluated using three independent metrics.

### 1. Semantic Similarity

Measures similarity between:

- Generated Reply
- Ground Truth Reply

using Sentence Transformer embeddings and cosine similarity.

---

### 2. Retrieval Confidence

Measures confidence of the semantic retriever using similarity scores from the nearest historical examples.

---

### 3. LLM Judge

Gemini evaluates:

- Relevance
- Helpfulness
- Professionalism

and returns a score between 0–100.

---

### Final Score

```text
Final Score =
0.30 × Semantic Similarity
+ 0.50 × LLM Judge Score
+ 0.20 × Retrieval Confidence
```

---

##  Sample Output

```text
GENERATED REPLY

Please use the password reset option available on the login page.
If the issue persists, contact our support team.

EVALUATION

semantic_similarity: 92.14
llm_judge_score: 94
retrieval_confidence: 89.32
final_score: 92.12
```

---

##  Future Improvements

- Larger Training Dataset
- Streamlit Web Interface
- Multi-Turn Email Conversations
- Vector Database Integration (FAISS)
- Fine-Tuned Domain-Specific Models
- Human Feedback Evaluation Pipeline

---

##  Learning Outcomes

This project demonstrates practical experience with:

- Retrieval-Augmented Generation (RAG)
- Natural Language Processing
- Semantic Search
- Embedding Models
- Large Language Model Integration
- Evaluation of Generative AI Systems
- Production-Style Python Project Structure

---

##  Author

**Garg Parashar**
BSDS Student, Indian Statistical Institute Bangalore

Interested in:

- Data Science
- Machine Learning
- NLP
- Generative AI
- Applied Analytics

---

##  If you found this project interesting

Consider starring the repository and sharing feedback.
