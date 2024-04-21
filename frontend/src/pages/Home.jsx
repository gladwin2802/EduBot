import { useAuthContext } from "../hooks/useAuthContext";
import React, { useState } from 'react';
import axiosInstance from './axiosInstance'; // Import the Axios instance

const Home = () => {
    const { user } = useAuthContext();
    const [context, setContext] = useState('');
    const [question, setQuestion] = useState('');
    const [result, setResult] = useState('');

    const handleSummarize = async () => {
        try {
            const response = await axiosInstance.post('/api', {
                context: context,
                question: 'summarize',
            });
            setResult(response.data.summary);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const handleQuestionAnswering = async () => {
        try {
            const response = await axiosInstance.post('/api', {
                context: context,
                question: question,
            });
            setResult(response.data.answer);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div className="home">
            <h2>Welcome !!!</h2>
            <h2><span>{user.email}</span></h2>
            <h1>Question Answering System</h1>
            <textarea
                placeholder="Enter context..."
                value={context}
                onChange={(e) => setContext(e.target.value)}
                rows={10}
            />
            <br />
            <input
                type="text"
                placeholder="Enter question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />
            <br />
            <button onClick={handleSummarize}>Summarize</button>
            <button onClick={handleQuestionAnswering}>Answer</button>
            <br />
            <h2>Result:</h2>
            <p>{result}</p>
        </div>
    );
};

export default Home;
