import React from "react";
import axios from "axios";
import Productss from "../components/products";
import PForm from "../components/productForm";

class ProductList extends React.Component {
  state = {
    products: []
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/rest/prod/").then(res => {
      this.setState({
        products: res.data
      });
    });
  }

  render() {
    return (
      <>
        <Productss data={this.state.products} />
        <br />
        <h2>Crear un producto</h2>
        <PForm requestType="post" productID={null} buttonText="Crear" />
      </>
    );
  }
}

export default ProductList;
