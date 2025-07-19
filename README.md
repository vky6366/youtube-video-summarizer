# YT-Insight

YT-Insight is a Streamlit web application designed to automatically extract, split, and analyze YouTube video transcripts using language models. It enables users to ask questions about any YouTube video and receive insightful, context-aware answers generated from the transcript content.

## Features

- **YouTube Transcript Extraction:** Paste any YouTube video URL, and the app retrieves its transcript.
- **Text Chunking:** Transcripts are split into manageable chunks for efficient processing.
- **Intelligent Q&A:** Leverages advanced language models (OpenAI GPT-4o-mini) to answer user queries based strictly on video content.
- **Beginner-Friendly Summaries:** Responses are formatted in bullet points and tailored for clarity.
- **Error Handling:** Gracefully manages missing captions and invalid URLs.

## How It Works

1. **Paste YouTube URL:** Enter a YouTube video link in the input box.
2. **Ask a Question:** Type your question (e.g., "Summarize this video").
3. **Get Answers:** The app extracts the transcript, processes it, and generates context-specific answers.

## Example Usage

```python
# app.py (Core usage)
from head.store import vector_store

yt_url = "https://www.youtube.com/watch?v=..."
question = "What is the main topic of this video?"

vs = vector_store(yt_url)
result = vs.my_invoke(question)
print(result)
```

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/vky6366/YT-Insight.git
    cd YT-Insight
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

    - Required packages include:
      - `streamlit`
      - `langchain`
      - `youtube-transcript-api`
      - `openai`
      - `python-dotenv`
    - (See your `requirements.txt` for full details.)

3. **Set up OpenAI API credentials:**
   - Create a `.env` file and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_key_here
     ```

## Running the App

```bash
streamlit run app.py
```

## Repository Structure

```
YT-Insight/
├── app.py                # Streamlit web application
├── head/
│   ├── store.py          # Main logic: transcript extraction, chunking, Q&A
│   └── utility/
│       ├── yt_transcription.py  # Transcript retrieval and splitting
│       └── yt_url_parser.py     # Robust YouTube URL parsing
├── requirements.txt
└── README.md
```

## How it works under the hood

- **URL Parsing:** Handles a variety of YouTube URL formats (regular, embed, short).
- **Transcript Retrieval:** Uses `youtube-transcript-api` to fetch English captions.
- **Chunking:** Splits transcript for efficient semantic search and context management.
- **Semantic Q&A:** Uses FAISS vector store for similarity search, and OpenAI models for natural language responses.

## Troubleshooting

- **No captions available:** Some videos may not have transcripts or captions.
- **Invalid URL:** Only valid YouTube video URLs are supported.

## License

MIT License

## Author

[vky6366](https://github.com/vky6366)

---

*This project leverages Streamlit, LangChain, YouTube Transcript API, FAISS, and OpenAI for seamless YouTube video insight extraction and question answering.*