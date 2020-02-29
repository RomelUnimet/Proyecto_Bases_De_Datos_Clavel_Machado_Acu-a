import React from "react";
import { Form, Input, Button, Select, InputNumber } from "antd";
import axios from "axios";

const { Option } = Select;

const layout = {
  labelCol: {
    span: 11
  }
};

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16
  }
};

class PForm extends React.Component {
  formRef = React.createRef();

  onFinish = values => {
    console.log(values);
  };

  onReset = () => {
    this.formRef.current.resetFields();
  };

  state = {
    providers: [],
    category: []
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/rest/prov/").then(res => {
      this.setState({
        providers: res.data
      });
      console.log(this.state.providers);
    });

    axios.get("http://127.0.0.1:8000/rest/category/").then(ras => {
      this.setState({
        category: ras.data
      });
      console.log(this.state.category);
    });
  }

  handleFormSubmit = (event, requestType, productID) => {
    //event.preventDefault();
    const name = event.target.elements.name.value;
    const pasillo = event.target.elements.pasillo.value;
    const category = event.target.elements.category.value;
    const provider = event.target.elements.provider.value;

    switch (requestType) {
      case "post":
        return axios
          .post("http://127.0.0.1:8000/rest/prod/", {
            product_name: name,
            hall: pasillo,
            category: category,
            provider: provider
          })
          .then(res => console.log(res))
          .catch(error => console.err(error));

      case "put":
        return axios
          .put(`http://127.0.0.1:8000/rest/prod/${productID}/`, {
            product_name: name,
            hall: pasillo
          })
          .then(res => console.log(res))
          .catch(error => console.err(error));
    }
  };

  render() {
    return (
      <Form
        {...layout}
        ref={this.formRef}
        name="control-ref"
        onFinish={this.onFinish}
        onSubmit={event =>
          this.handleFormSubmit(
            event,
            this.props.requestType,
            this.props.productID
          )
        }
      >
        <Form.Item
          name="Nombre"
          rules={[
            {
              required: true
            }
          ]}
          label="Nombre"
        >
          <Input name="name" placeholder="Nombre del producto" />
        </Form.Item>

        <Form.Item
          name="Pasillo"
          label="Pasillo"
          rules={[
            {
              type: "number",
              min: 0,
              max: 99,
              required: true
            }
          ]}
        >
          <InputNumber name="pasillo" placeholder="Nro del pasillo" />
        </Form.Item>

        <Form.Item
          name="Proveedor"
          label="Proveedor"
          rules={[
            {
              required: true
            }
          ]}
        >
          <Select placeholder="Selecciona un proveedor" allowClear>
            {this.state.providers.map(provs => (
              <Option value={provs.name} key={provs.name}>
                {provs.name}
              </Option>
            ))}
          </Select>
        </Form.Item>

        <Form.Item
          name="Categoria"
          label="Categoria"
          rules={[
            {
              required: true
            }
          ]}
        >
          <Select placeholder="Selecciona una categoria" allowClear>
            {this.state.category.map(cats => (
              <Option value={cats.name} key={cats.name}>
                {cats.name}
              </Option>
            ))}
          </Select>
        </Form.Item>

        <Form.Item
          noStyle
          shouldUpdate={(prevValues, currentValues) =>
            prevValues.gender !== currentValues.gender
          }
        >
          {({ getFieldValue }) =>
            getFieldValue("gender") === "other" ? (
              <Form.Item
                name="customizeGender"
                label="Customize Gender"
                rules={[
                  {
                    required: true
                  }
                ]}
              >
                <Input />
              </Form.Item>
            ) : null
          }
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            {this.props.buttonText}
          </Button>
        </Form.Item>
      </Form>
    );
  }
}

export default PForm;
