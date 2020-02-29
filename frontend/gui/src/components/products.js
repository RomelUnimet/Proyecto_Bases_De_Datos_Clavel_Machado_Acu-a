import React from 'react';
import { List } from 'antd';
import InfiniteScroll from 'react-infinite-scroller';

const Productss = (props) => {
    return (
        <div className="demo-infinite-container">
          <InfiniteScroll
            initialLoad={false}
            pageStart={0}
            useWindow={false}
          >
            <h2>Productos:</h2>
            <List
              dataSource={props.data}
              renderItem={item => (
                <List.Item key={item.id}>
                  <List.Item.Meta
                    title={<a href={`prod/${item.id}`}>{item.product_name}</a>}
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