import React from 'react';
import { Form, Input, Button, Select, InputNumber } from 'antd';
import axios from 'axios';

const { Option } = Select;
const layout = {
  labelCol: {
    span: 11,
  }
};
const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

class PForm extends React.Component {
  formRef = React.createRef();

  onGenderChange = value => {
    this.formRef.current.setFieldsValue({
      note: `Hi, ${value === 'male' ? 'man' : 'lady'}!`,
    });
  };

  onFinish = values => {
    console.log(values);
  };

  onReset = () => {
    this.formRef.current.resetFields();
  };

  onFill = () => {
    this.formRef.current.setFieldsValue({
      note: 'Hello world!',
      gender: 'male',
    });
  };

    state = {
        providers: []
    }

    componentDidMount(){
        axios.get('http://127.0.0.1:8000/rest/prov/').then(res => {
            this.setState({
                providers: res.data
            });
        })
    }

    bringProviders = () =>{

    }

    handleFormSubmit = (event, requestType, productID) => {
        //event.preventDefault();
        const name = event.target.elements.title.value;
        const pasillo = event.target.elements.pasillo.value;
        
        switch(requestType){
            case 'post':
                return axios.post('http://127.0.0.1:8000/rest/prod/', {
                    product_name:name,
                    hall: pasillo
                }).then(res => console.log(res)).catch(error => console.err(error));
            
            case 'put':
                return axios.put(`http://127.0.0.1:8000/rest/prod/${productID}/`, {
                    product_name:name,
                    hall: pasillo
                }).then(res => console.log(res)).catch(error => console.err(error));
        }

    }


  render() {
    return (
      <Form {...layout} ref={this.formRef} name="control-ref" onFinish={this.onFinish} onSubmit={(event) => this.handleFormSubmit(
          event, this.props.requestType, this.props.productID
      )}>
        <Form.Item
          name="Nombre"
          
          label="Nombre"
        >
          <Input name="name" placeholder="Nombre del producto" />
        </Form.Item>

        <Form.Item 
            name="Pasillo" 
            label="Pasillo" 
            rules={[
                { 
                type: 'number', min: 0, max: 99 
                }
            ]}
        >
        <InputNumber name="pasillo" placeholder="Nro del pasillo"/>
        </Form.Item>

        {/* <Form.Item
          name="Proveedor"
          label="Proveedor"
          rules={[
            {
              required: true,
            },
          ]}
        >
          <Select
            placeholder="Selecciona un proveedor"
            onChange={this.onGenderChange}
            allowClear
          >
            
            
            <Option value="male">male</Option>
            <Option value="female">female</Option>
            <Option value="other">other</Option>
          </Select>
        </Form.Item>
        <Form.Item
          noStyle
          shouldUpdate={(prevValues, currentValues) => prevValues.gender !== currentValues.gender}
        >
          {({ getFieldValue }) =>
            getFieldValue('gender') === 'other' ? (
              <Form.Item
                name="customizeGender"
                label="Customize Gender"
                rules={[
                  {
                    required: true,
                  },
                ]}
              >
                <Input />
              </Form.Item>
            ) : null
          }
        </Form.Item> */}
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
