import React, {Component, useEffect, useState} from 'react';
import './App.css';

const List = (props) => {
  const { prod } = props;
  if (!prod || prod.length === 0) return <p>No repos, sorry</p>;
  return (
    <ul>
      <h2 className='list-head'>Available Products</h2>
      {prod.map((pr) => {
        return (
          <li key={pr.id} className='list'>
            <span className='repo-text'>{pr.title} </span>
            <span className='repo-description'>{pr.description}</span>
          </li>
        );
      })}
    </ul>
  );
};

function withListLoading(Component) {
  return function WihLoadingComponent({ isLoading, ...props }) {
    if (!isLoading) return <Component {...props} />;
    return (
      <p style={{ textAlign: 'center', fontSize: '30px' }}>
        Hold on, fetching data may take some time :)
      </p>
    );
  };
}

function App() {
  const ListLoading = withListLoading(List);
  const [appState, setAppState] = useState({
    loading: false,
    repos: null,
  });

  useEffect(() => {
    setAppState({ loading: true });
    const apiUrl = `http://127.0.0.1:8000/api/product/?format=json`;
    fetch(apiUrl)
      .then((res) => res.json())
      .then((prod) => {
        setAppState({ loading: false, prod: prod });
      });
  }, [setAppState]);
  return (
    <div className='App'>
      <div className='container'>
        <h1>My Repositories</h1>
      </div>
      <div className='repo-container'>
        <ListLoading isLoading={appState.loading} prod={appState.prod} />
      </div>
    </div>
  );
}

export default App;
