from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load question answering and summarization models
qa_model_name = 'deepset/roberta-base-squad2'
qa_pipeline = pipeline('question-answering', model=qa_model_name, tokenizer=qa_model_name)

summarization_model = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=summarization_model)

@app.route('/api', methods=['POST'])
def process_request():
    req_data = request.json
    
    context = req_data.get('context', '')
    question = req_data.get('question', '')
    
    print(context, question)

    if not context:
        return jsonify({'error': 'Context is required'}), 400

    if not question:
        return jsonify({'error': 'Question is required'}), 400

    if 'summarize' in question.lower():
        # Summarization task
        summary = summarizer(context, max_length=200, min_length=100, do_sample=False)
        return jsonify({'summary': summary[0]['summary_text']})

    # Question answering task
    answer = qa_pipeline(question, context)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
