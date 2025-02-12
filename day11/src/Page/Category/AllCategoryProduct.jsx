import { useState, useEffect } from "react";
import axios from "axios";

function AllCategoryProduct() {
    let [datas, setData] = useState({});
    useEffect(()=>{
        let fetchs = async () => {
            let response = await axios.get("http://127.0.0.1:8000/api/categoryProduct/1/")

            setData(response.data)

        }
        fetchs();
    },[])


  return (
    <div>
        <h1 className="mt-[20px] mx-auto md:w-[70vw] items-start text-4xl ">Category : {datas.name}</h1>
        <h1 className="mt-[20px] mx-auto md:w-[70vw] items-start text-xl ">Description : {datas.description}</h1>
        <div className="grid mt-[20px] mx-auto md:w-[70vw] grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3 items-start">
            {/* {datas.product_set.map((item, index) => {
            return (
                <li key={index}>
                <h3>{item.name}</h3>
                <p>{item.price}</p>
                <img src={item.image} alt="" />
                <p>{item.description}</p>
                </li>
            )
        })} */}
            
        </div>
    </div>
  )
}

export default AllCategoryProduct