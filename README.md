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

## Dataset Construction

The dataset used in this project was manually curated and expanded into 100+ email–reply pairs covering common customer support scenarios.

The dataset includes realistic examples across 10 categories:

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

The dataset is synthetic rather than collected from real customer interactions. This avoids privacy concerns while still allowing realistic experimentation with retrieval-based response generation.

The goal was not to perfectly replicate a production support environment, but to create a representative dataset for evaluating email response generation systems.

---

## Design Decisions and Trade-offs

### Why Retrieval-Augmented Generation (RAG)?

With a relatively small dataset (100+ examples), fine-tuning a language model would likely overfit and require significantly more infrastructure.

Instead, I chose a Retrieval-Augmented Generation (RAG) approach:

1. Retrieve the most relevant historical emails.
2. Use retrieved examples as context.
3. Generate a response grounded in those examples.

This approach is lightweight, transparent, and performs well on small datasets.

### Why Sentence Transformers?

Sentence Transformers provide high-quality semantic embeddings that allow retrieval based on meaning rather than keyword matching.

This improves robustness when users phrase similar requests differently.

### Why Gemini?

Gemini was selected as the generation model because it provides strong instruction-following capabilities and produces professional customer-support style responses with minimal prompt engineering.

### Limitations

- Small dataset compared to production systems.
- Synthetic data may not cover every real-world scenario.
- Evaluation still relies partially on LLM judgment.
- Retrieval quality depends on dataset coverage.

---

## Why This Evaluation Approach?

Evaluating generated email responses is challenging because multiple responses can be correct for the same email.

For example, two replies may have different wording while providing equally useful support.

Because of this, exact text matching is too strict and does not reflect real-world quality.

To address this, the system combines three complementary metrics.

### Semantic Similarity (30%)

Measures how closely the generated reply matches the meaning of a known good response using sentence embeddings and cosine similarity.

### LLM Judge Score (50%)

A large language model evaluates:

- Relevance
- Helpfulness
- Professionalism

This better approximates how a human reviewer would assess response quality.

### Retrieval Confidence (20%)

Measures how strongly the incoming email matches examples found in the retrieval database.

Higher retrieval confidence suggests stronger grounding in historical examples.

### Why Combine Multiple Metrics?

Each metric captures a different aspect of quality:

| Metric | Measures |
|----------|----------|
| Semantic Similarity | Meaning Preservation |
| LLM Judge | Human-Like Quality |
| Retrieval Confidence | Grounding Strength |

Combining them produces a more reliable estimate than relying on any single metric.

---

## Use of AI Tools

AI tools were used during development for:

- Brainstorming synthetic dataset examples
- Reviewing code structure
- Debugging implementation issues
- Improving documentation

All final design decisions, implementation, retrieval pipeline, evaluation framework, and integration were completed and verified manually.

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

##  Running the Project

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

## Author

**Garg Parashar**

BSDS Student, Indian Statistical Institute Bangalore

Areas of Interest:

- Data Science
- Machine Learning
- Natural Language Processing
- Generative AI
- Applied Analytics

---

##  If you found this project interesting

Consider starring the repository and sharing feedback.
