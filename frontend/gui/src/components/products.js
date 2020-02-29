import React from 'react';
import { List, message, Avatar, Spin } from 'antd';
import reqwest from 'reqwest';
import InfiniteScroll from 'react-infinite-scroller';

const fakeDataUrl = 'https://randomuser.me/api/?results=5&inc=name,gender,email,nat&noinfo';

const Productss = (props) => {
    return (
        <div className="demo-infinite-container">
          <InfiniteScroll
            initialLoad={false}
            pageStart={0}
            useWindow={false}
          >
            <List
              dataSource={props.data}
              renderItem={item => (
                <List.Item key={item.id}>
                  <List.Item.Meta
                    title={<a href={`/${item.id}`}>{item.product_name}</a>}
                  />
                </List.Item>
              )}
            >
            </List>
          </InfiniteScroll>
        </div>
    );
}



export default Productss;