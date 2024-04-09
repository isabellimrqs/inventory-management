import react, { useContext, useEffect } from 'react'
import { Table } from 'react-bootstrap';
import {ProductContext} from '../ProductContext'

const ProductsTable = () => {
    const [products, setProducts] = useContext(ProductContext)


    useEffect(()=>{
        fetch("http://127.0.0.1:8000/product")
        .then(response => {
            return response.json();
        }).then(results => {
            console.log(results)
            setProducts({"data" : [...results.data]})
        })
    })

    return (
        <div>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>Product Name</th>
                        <th>Quantity In Stock</th>
                        <th>Quantity Sold</th>
                        <th>Unit Price</th>
                        <th>Revenue</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>

                    
                        
                </tbody>
            </Table>
        </div>
    );

}

export default ProductsTable;