import React, { useState } from 'react';
import './App.css';


function App() {
    const [auth, setAuth]=useState(false)
    const [login, setLogin]=useState("")
    const [password, setPassword]=useState("")

    function get_login(){
        let data = {
            "username":login,
            "password":password
        }
        console.log(data)
        fetch('http://127.0.0.1:8000/api/token/', {
            method:'POST',
            headers:{
                "Content-Type": "application/json",
            },
            body:JSON.stringify(data)
        })
            .then(response=>response.json())
            .then(tot_samui_token=>{console.log(tot_samui_token)
            setAuth(tot_samui_token.access)
            })

    }

    if(auth){
        return (
        <div>
            <h1>Hello in your account</h1>
        </div>
        )
    }

    return (
      <div className="App">
        <form action="">
            <input type="text" placeholder={"enter your login"} onChange={(e)=>setLogin(e.target.value)}/><br/>
            <input type="password" placeholder={"enter your password"} onChange={(e)=>setPassword(e.target.value)}/><br/>
            <input type="button" onClick={get_login} value={"login"}/>
        </form>
      </div>
    );
}

export default App;

