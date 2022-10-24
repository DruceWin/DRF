import React, {useEffect, useState} from 'react';
import './App.css';


function App() {
    const [shops, setShops] = useState(
        [])
    const [shop, setShop] = useState([])
    const [products, setProducts] = useState(
        [])
    const [categories, setCategories] = useState(
        [])
    const [products_sort, setProductsSort] = useState(
        [{title: ''}])
    const [product_detail, setProductDetail] = useState(
        [{title: ''}])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/shops/')
            .then(response => response.json())
            .then(data => {
                setShops(data)
            })
    }, [])

    function sort_products(e) {
        let data_sorted = []
        for(let i of products){
            if(i.category.name===e.target.id){
                data_sorted.push(i)
            }
        }
        setProductsSort(data_sorted)
    }

    function detail_products(e) {
        let data_detail = []
        for (let i of products){
            if(i.title===e.target.id){
                data_detail.push(i)
            }
        }
        setProductDetail(data_detail)
    }

    function shop_detail(e) {
        fetch(`http://127.0.0.1:8000/api/shops/${e.target.id}`)
            .then(response => response.json())
            .then(data => {
                setShop(data.name)
                setProducts(data.products)
                var set_data = new Set()
                for (let i of data.products){
                    set_data.add(i.category.name)}
                var array_data = Array.from(set_data)
                setCategories(array_data)
            })
    }
    function sort_all(){
        setProductsSort([{title: ''}])
    }

    function clear_product_detail(){
        setProductDetail([{title: ''}])
    }
    console.log(shop)
    // eslint-disable-next-line
    if (shop == false) {
        return (
            <div className="container">
                <nav className="nav_bar">
                    <div className="nav_bar-logo">
                        Магазины:
                    </div>
                    {shops.map(item =>
                        <p key={item.name}
                            onClick={shop_detail}
                            id={item.id}>
                            {item.name}
                        </p>)}
                </nav>
            </div>
        )
    }

    else if (product_detail[0].title !== '') {
        return (
            <div className="container">
                <nav className="nav_bar">
                    <div className="nav_bar-logo">
                        Магазины:
                    </div>
                    {shops.map(item =>
                        <p key={item.name}
                            onClick={shop_detail}
                            id={item.id}>
                            {item.name}
                        </p>)}
                </nav>
                <h3>Продукты магазина {shop}</h3>
                <div className="container__main">
                    <div className="container__menu">
                        <h3>Категории:</h3>
                        {categories.map(item =>
                            <p key={item}
                               onClick={sort_products}
                               id={item}>
                                {item}
                            </p>)}
                    </div>
                    <main className="main_detail">
                        <div>
                            <p>Название: {product_detail[0].title}</p>
                            <p>Цена: {product_detail[0].price}</p>
                            <p>Описание: {product_detail[0].description}</p>
                        </div>
                        <button onClick={clear_product_detail}>Назад</button>
                    </main>
                </div>
            </div>
        );
    }

    else if (products_sort[0].title === '') {
        return (
            <div className="container">
                <nav className="nav_bar">
                    <div className="nav_bar-logo">
                        Магазины:
                    </div>
                    {shops.map(item =>
                        <p key={item.name}
                            onClick={shop_detail}
                            id={item.id}>
                            {item.name}
                        </p>)}
                </nav>
                <h3>Продукты магазина {shop}</h3>
                <div className="container__main">
                    <div className="container__menu">
                        <h3>Категории:</h3>
                        {categories.map(item =>
                            <p key={item}
                               onClick={sort_products}
                               id={item}>
                                {item}
                            </p>)}
                    </div>
                    <main className="main">
                        {products.map(item =>
                            <div key={item.title}
                                 onClick={detail_products}
                                 id={item.title}>
                                <p id={item.title}>{item.title}</p>
                                <p id={item.title}>{item.price}</p>
                        </div>)}
                    </main>
                </div>
            </div>
        );
    }

    else {
        return (
            <div className="container">
                <nav className="nav_bar">
                    <div className="nav_bar-logo">
                        Магазины:
                    </div>
                    {shops.map(item =>
                        <p key={item.name}
                            onClick={shop_detail}
                            id={item.id}>
                            {item.name}
                        </p>)}
                </nav>
                <h3>Продукты магазина {shop}</h3>
                <div className="container__main">
                    <div className="container__menu">
                        <h3>Категории:</h3>
                        <p key='all'
                            onClick={sort_all}>Все</p>
                        {categories.map(item =>
                            <p key={item}
                               onClick={sort_products}
                               id={item}>
                                {item}
                            </p>)}
                    </div>
                    <main className="main">
                        {products_sort.map(item =>
                            <div key={item.title}
                                 onClick={detail_products}
                                 id={item.title}>
                                <p id={item.title}>{item.title}</p>
                                <p id={item.title}>{item.price}</p>
                        </div>)}
                    </main>
                </div>
            </div>
        );
    }
}
export default App;
