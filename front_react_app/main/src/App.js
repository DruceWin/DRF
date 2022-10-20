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
  const [product, setProduct] = useState(
      [{title:'najmi po prodyctam'}])
  const [category, setCategory] = useState(
      [{name:'najmi po kategoriyam'}])
  const [product_text, setProductText] = useState('a')
  const [product_title, setProductTitle] = useState({"title":''})
  function get_products(){
    fetch('http://127.0.0.1:8000/api/product/')
        .then((res) => res.json())
        .then(products=>{
            setProduct(products)
            console.log(products)
            console.log(product)
        })
  }
  function get_categories(){
    fetch('http://127.0.0.1:8000/api/categories/')
        .then((res) => res.json())
        .then(categories=>{
            setCategory(categories)
        })
  }

  function set_input_value_for_product_text(p){
      setProductText(p.target.value)
  }

  function get_product_for_text(){
      fetch(`http://127.0.0.1:8000/api/product/${product_text}`)
        .then((res) => res.json())
        .then(product=>{
            if (!product.title){
                setProductTitle({title: "net takogo producta"})
            }
            else {setProductTitle(product)}
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
      <div className="wrapper" style={{display:"flex"}}>
          <div className="products" style={{margin:"15px"}}>
              {product.map((item, i) => <p key={i}>{item.title}</p>)}
          </div>
          <div className="categories" style={{margin:"15px"}}>
              {category.map((item, i) => <p key={i}>{item.name}</p>)}
          </div>
      </div>
      <div>
          <form action="">
              <input type="text" placeholder="Введи название продукта" onChange={set_input_value_for_product_text}/>
              <input type="button" value="OK" onClick={get_product_for_text}/>
          </form>
      </div>
      <div style={{display:"flex", justifyContent:"center", alignContent:"center"}}>
          <div>
              <p>{product_title.title}</p>
              <p>{product_title.description}</p>
              <p>{product_title.price}</p>
          </div>
      </div>
      <div className='repo-container'>
        <ListLoading isLoading={appState.loading} prod={appState.prod} />
      </div>
    </div>
  );
}

export default App;
