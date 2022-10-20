import React, {useEffect, useState} from 'react';
import './App.css';


function App() {
    const [product, setProduct] = useState(
        [{title: 'najmi po prodyctam'}])
    const [category, setCategory] = useState(
        [{name: 'najmi po kategoriyam'}])
    const [product_sort, setProductSort] = useState(
        [{title: ''}])

    useEffect(() => {
        fetch('http://localhost:8000/api/categories/')
            .then(response => response.json())
            .then(data => {
                setCategory(data)
            })
    }, [])
    console.log(category)
    useEffect(() => {
        fetch('http://localhost:8000/api/product/')
            .then(response => response.json())
            .then(data => {
                setProduct(data)
            })
    }, [])

    function sort_products(e) {
        console.log(e.target.id)
        let data_sorted = []
        for(let i of product){
            if(i.category.name===e.target.id){
                data_sorted.push(i)
            }
        }
        setProductSort(data_sorted)
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
                        {category.map(item => <li style={{margin: '20px', color: 'yellow', cursor: 'pointer'}}
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
                    background: 'grey',
                    padding: '20px'
                }}>
                    {product.map(item => <div style={{
                        height: '150px',
                        width: "150px",
                        border: '1px solid red',
                        background: 'goldenrod',
                        margin: '20px'
                    }}>
                        <p>{item.title}</p><p>{item.price}</p>
                    </div>)}
                </main>
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
                        {category.map(item => <li style={{
                            margin: '20px',
                            color: 'yellow',
                            cursor: 'pointer'
                        }}
                                                  key={item.name}
                                                  onClick={sort_products}
                                                  id={item.name}>
                            {item.name}
                        </li>)}
                        <li>All</li>
                    </ul>
                </nav>
                <h3>Продукты</h3>
                <main style={{
                    display: 'flex',
                    width: '80%',
                    justifyContent: 'flex-start',
                    background: 'grey',
                    padding: '20px'
                }}>
                    {product_sort.map(item => <div style={{
                        height: '150px',
                        width: "150px",
                        border: '1px solid red',
                        background: 'goldenrod',
                        margin: '20px'
                    }}>
                        <p>{item.title}</p>
                        <p>{item.price}</p>
                    </div>)}
                </main>
            </div>
        );
    }
}
export default App;
