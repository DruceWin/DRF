import React, {useEffect, useState} from 'react';
import './App.css';

const List = (props) => {
  const { prod } = props;
  if (!prod || prod.length === 0) return <p>No products, sorry</p>;
  return (
    <ul>
      <h2 className='list-head'>Available Products</h2>
      {prod.map((pr) => {
        return (
          <li key={pr.id} className='list'>
            <span className='prod-text'>{pr.title}. </span>
            <span className='prod-description'> Описание: {pr.description}.</span>
            <span className='prod-price'> Цена: {pr.price} руб.</span>
            {/*<span className='repo-category'> Категория: {pr.category_set}.</span>*/}
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
  const [Product, setProduct] = useState(
    'Нажми кнопку для получения продуктов')
  const [Category, setCategory] = useState(
      'Нажми кнопку для получения категорий')
  function get_products(){
    fetch('http://127.0.0.1:8000/api/product')
        .then((res) => res.json())
        .then(products=>{
          console.log(products)
            setProduct(products)
        })
  }
  function get_categories(){
    fetch('http://127.0.0.1:8000/api/categories')
        .then((res) => res.json())
        .then(categories=>{
          console.log(categories)
            setCategory(categories)
        })
  }
  useEffect(() => {
    setAppState({ loading: true });
    const apiUrl = `http://127.0.0.1:8000/api/product`;
    fetch(apiUrl)
      .then((res) => res.json())
      .then((prod) => {
        setAppState({ loading: false, prod: prod });
      });
  }, [setAppState]);
  return (
    <div className='App'>
      <div className='container'>
        <h1>My API</h1>
      </div>
        <input type="button" value={'получить продукты'} onClick={get_products}/>
        <input type="button" value={'получить категории'} onClick={get_categories}/>
      <div className="wrapper">
          {/*<div className="products">*/}
          {/*    {Product.map((pr) => <p>({pr.title}</p>)}*/}
          {/*</div>*/}
          <div className="categories">

          </div>
      </div>
      <div className='repo-container'>
        <ListLoading isLoading={appState.loading} prod={appState.prod} />
      </div>
    </div>
  );
}

export default App;
