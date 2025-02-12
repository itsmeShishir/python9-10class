import {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import AllProducts from '../Product/AllProducts';

function HomePage() {
    const [categories, setCategories] = useState([]);
    useEffect(() => {
        let fetchData = async () => {
            let response = await fetch('http://127.0.0.1:8000/api/allCategory/');
            let data = await response.json();
            setCategories(data.results);
        }
        fetchData();
    }, []);
  return (
    <>
        <h1 className="mt-[20px] mx-auto md:w-[70vw] items-start text-4xl ">All Categories</h1>
        <div className="grid mt-[20px] mx-auto md:w-[70vw] grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3 items-start">
          {
           categories.map((category) => {
            return (
                <div key={category.id}>
                        <Link to="#" className="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
                        <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{category.name}</h5>
                        <p className="font-normal text-gray-700 dark:text-gray-400">{category.description}</p>
                        </Link>
                </div>
            )
           })
          }

        </div>
        <h1 className="mt-[20px] mx-auto md:w-[70vw] items-start text-4xl ">Featured Product</h1>
        <AllProducts />

        <h1 className="mt-[20px] mx-auto md:w-[70vw] items-start text-4xl ">All Products</h1>
          <AllProducts />



    </>
  )
}

export default HomePage