import React from 'react';
import axios from 'axios';
import Productss from '../components/products';

class ProductList extends React.Component{

    state = {
        products: []
    }

    componentDidMount(){
        axios.get('http://127.0.0.1:8000/rest/prod/').then(res => {
            this.setState({
                products: res.data
            });
        })
    }


    render(){
        return (

            <Productss data ={this.state.products}/>

        )
    }
}

export default ProductList;