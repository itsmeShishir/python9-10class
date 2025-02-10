import {useState, useEffect} from "react";
import axios from "axios";

function AllProducts() {
  let [data, setData] = useState([]);

  useEffect(() => {
    let fetchs = async () => {
      let response = await axios.get("http://127.0.0.1:8000/api/allProduct/");
      setData(response.data.results);
    }
    fetchs();
  }, []);
  return (
    <div>
      <h1>Product List</h1>
      {/* show all the data from the api in this */}
      <ul>
        {data.map((item, index) => {
          return (
            <li key={index}>
              <h3>{item.name}</h3>
              <p>{item.price}</p>
              <img src={item.image} alt="" />
              <p>{item.description}</p>
            </li>
          )
        })}
        </ul>
    </div>
  )
}

export default AllProducts;