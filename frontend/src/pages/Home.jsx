import '../css/Home.css'
import addBtn from '../assets/add-30.png';
import msgIcon from '../assets/message.svg';
import sendBtn from '../assets/send.svg';
import userIcon from '../assets/user-icon.png'
import edubot from '../assets/edu-bot.png'
import React, { useState, useContext, useEffect } from 'react';
import { Context } from '../context/context.jsx';

function Home() {
    const { sent, setRecentInput, recentPrompt, showResult, loading, resultData, setInput, input } = useContext(Context);
    const [newChat, setNewChat] = useState(true);
    const [initialContent, setInitialContent] = useState('');
    const [query, setQuery] = useState('');
    const [prompt, setPrompt] = useState('');

    useEffect(() => {
        if (input != "" && query != "") {
            console.log("Input: " + input);
            sent();
            setNewChat(false);
            setPrompt(query);
            setQuery("")
        }
    }, [input]);

    const handleSendButtonClick = () => {
        const updatedInput = initialContent + "\n" + query;
        setInput(updatedInput)
    };

    return (
        <div className="Home">
            {/* side-bar */}
            <div className='sideBar'>
                <div className='upperSide'>
                    <button className="midBtn" onClick={() => { setNewChat(true) }}><img src={addBtn} alt="" className="addBtn" />New Chat</button>
                    <div className="upperSideBottom">
                        <button className="query" onClick={() => { setQuery("Summarise the content..."); }}><img src={msgIcon} alt='' />Summarise the content...</button>
                        <button className='query' onClick={() => { setQuery("What are the key points in this content ?"); }}><img src={msgIcon} alt='' />What are the key points in the content ?</button>
                    </div>
                </div>
            </div>
            {/* main */}
            <div className='main'>
                {((showResult) && (!newChat)) ? (<div className="chats">
                    <div className="chat bot1">
                        <img className='chatImg' src={userIcon} alt='' width={"50px"} height={"50px"} />
                        <p className='txt'>{prompt}</p>
                    </div>
                    <div className="chat bot">
                        <img className='chatImg' src={edubot} alt='' width={"50px"} height={"50px"} />
                        {loading ? <div className='loader'>
                            <hr />
                            <hr />
                            <hr />
                        </div> : <p>{resultData}</p>
                        }
                    </div>
                </div>) : (
                    <div className='home'>
                        <div className='centerImg'><img src={edubot} alt="Logo" className='logo' width={"150px"} height={"150px"} /></div>
                        <div className='Start-text'>
                            <h1>Hello,</h1>
                            <h2>How can I help you ?</h2>
                        </div>
                    </div>

                )}
                {/* Input for initial content */}
                <div className="chatFooter">
                    <div className="inp">
                        <input type="text" onChange={(e) => setInitialContent(e.target.value)} value={initialContent} placeholder="Enter the content here..." />
                    </div>
                    <div className="inp">
                        <input type="text" onChange={(e) => setQuery(e.target.value)} value={query} placeholder="Enter the query..."/>
                        <button onClick={handleSendButtonClick} className='send'><img src={sendBtn} alt='send' /></button>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default Home;