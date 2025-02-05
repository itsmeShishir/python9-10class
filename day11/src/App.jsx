import React, {useState, useEffect} from "react";
import axios from "axios";

function App() {
  let [data, setData] = useState([]);

  useEffect(() => {
    let fetchs = async () => {
      let response = await axios.get("http://127.0.0.1:8000/api/allProduct/");
      setData(response.data);
    }
    fetchs();
  }, []);
  return (
    <div>
      <h1>Product List</h1>
      {data.forEach((item) => {
        return (
          <div key={item.id}>
            <h2>{item.name}</h2>
            <p>{item.price}</p>
          </div>
        )
      })};
    </div>
  )
}

export default App;