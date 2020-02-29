import React from 'react';
import axios from 'axios';
import { Card } from 'antd';
import PForm from '../components/productForm';


class ProductDetail extends React.Component{

    state = {
        product: {}
    }

    componentDidMount(){
        const productID = this.props.match.params.productID;
        axios.get(`http://127.0.0.1:8000/rest/prod/${productID}`).then(res => {
            this.setState({
                product: res.data
            });
        })
    }


    render(){
        return (
            <>
                <h2>Producto:</h2>
                <Card title={this.state.product.product_name + " (" + this.state.product.id + ")"}>
                    <p>ID del proveedor: {this.state.product.provider}</p>
                    <p>ID de la categoria: {this.state.product.category}</p>
                    <p>Pasillo: {this.state.product.hall}</p>
                </Card>
                <br/>
                <h2>Modificar Producto:</h2>
                <PForm requestType="put" productID={this.props.match.params.productID} buttonText="Modificar"/>
            </>

        )
    }
}

export default ProductDetail;