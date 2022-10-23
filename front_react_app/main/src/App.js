import React, {useEffect, useState} from 'react';
import './App.css';


function App() {
    const [product, setProduct] = useState(
        [{title: 'najmi po prodyctam'}])
    const [category, setCategory] = useState(
        [{name: 'najmi po kategoriyam'}])
    const [product_sort, setProductSort] = useState(
        [{title: ''}])
    const [product_detail, setProductDetail] = useState(
        [{title: ''}])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/categories/')
            .then(response => response.json())
            .then(data => {
                setCategory(data)
            })
    }, [])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/product/')
            .then(response => response.json())
            .then(data => {
                setProduct(data)
            })
    }, [])

    function sort_products(e) {
        let data_sorted = []
        for(let i of product){
            if(i.category.name===e.target.id){
                data_sorted.push(i)
            }
        }
        setProductSort(data_sorted)
    }

        function detail_products(e) {
        let data_detail = []
        for (let i of product){
            if(i.title===e.target.id){
                data_detail.push(i)
            }
        }
        setProductDetail(data_detail)
    }

    function sort_all(){
        setProductSort([{title: ''}])
    }

    if (product_sort[0].title === '') {
        return (
            <div className='App'>
                <h1>My API</h1>
                <nav>
                    <ul style={{
                        display: 'flex',
                        width: '80%',
                        justifyContent: 'flex-start',
                        background: 'blue'
                    }}>
                        {category.map(item =>
                            <li style={{
                                margin: '20px',
                                color: 'yellow',
                                cursor: 'pointer'
                            }}
                                                  key={item.name}
                                                  onClick={sort_products}
                                                  id={item.name}>
                            {item.name}
                        </li>)}
                    </ul>
                </nav>
                <h3>Продукты</h3>
                <main style={{
                    display: 'flex',
                    width: '80%',
                    justifyContent: 'flex-start',
                    flexWrap: 'wrap',
                    background: 'grey',
                    padding: '20px'
                }}>
                    {product.map(item =>
                        <div style={{
                            height: '150px',
                            width: "150px",
                            border: '1px solid red',
                            background: 'goldenrod',
                            margin: '20px',
                            cursor: 'pointer'
                    }}
                             key={item.title}
                             onClick={detail_products}
                             id={item.title}>
                            <p id={item.title}>{item.title}</p>
                            <p id={item.title}>{item.price}</p>
                    </div>)}
                </main>
                <div style={{
                        height: '150px',
                        width: "150px",
                        border: '1px solid black',
                        background: 'yellowgreen',
                        margin: '20px'
                    }}>
                    <p>{product_detail[0].title}</p>
                    <p>{product_detail[0].price}</p>
                    <p>{product_detail[0].description}</p>
                </div>
            </div>
        );
    }
    else {
        return (
            <div className='App'>
                <h1>My API</h1>
                <nav>
                    <ul style={{
                        display: 'flex',
                        width: '80%',
                        justifyContent: 'flex-start',
                        background: 'blue'
                    }}>
                        {category.map(item =>
                            <li style={{
                            margin: '20px',
                            color: 'yellow',
                            cursor: 'pointer'
                        }}
                                key={item.name}
                                onClick={sort_products}
                                id={item.name}>
                            {item.name}
                        </li>)}
                        <li style={{
                            margin: '20px',
                            color: 'yellow',
                            cursor: 'pointer'
                        }}
                            key='all'
                            onClick={sort_all}>All</li>
                    </ul>
                </nav>
                <h3>Продукты</h3>
                <main style={{
                    display: 'flex',
                    width: '80%',
                    justifyContent: 'flex-start',
                    flexWrap: 'wrap',
                    background: 'grey',
                    padding: '20px'
                }}>
                    {product_sort.map(item =>
                        <div style={{
                            height: '150px',
                            width: "150px",
                            border: '1px solid red',
                            background: 'goldenrod',
                            margin: '20px',
                            cursor: 'pointer'
                    }}
                             key={item.title}
                             onClick={detail_products}
                             id={item.title}>
                        <p id={item.title}>{item.title}</p>
                        <p id={item.title}>{item.price}</p>
                    </div>)}
                </main>
                <div style={{
                        height: '150px',
                        width: "150px",
                        border: '1px solid black',
                        background: 'yellowgreen',
                        margin: '20px'
                    }}>
                    <p>{product_detail[0].title}</p>
                    <p>{product_detail[0].price}</p>
                    <p>{product_detail[0].description}</p>
                </div>
            </div>
        );
    }
}
export default App;
