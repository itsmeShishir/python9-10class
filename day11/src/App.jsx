import { Routes, Route } from 'react-router-dom'
import HomePage from './Page/Home/HomePage'
import AllProducts from './Page/Product/AllProducts'
import Navbar from './Component/Navbar'
import Footer from './Component/Footer'
import AllCategoryProduct from './Page/Category/AllCategoryProduct'
import SingleProduct from './Page/Product/SingleProduct'
import Login from './Page/auths/Login'
function App() {
  return (
   <>
    <Navbar />
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/products" element={<AllProducts />} />
      <Route path="/categoryproduct/:id" element= {<AllCategoryProduct />} />
      <Route path="/singleproduct/:id" element={<SingleProduct />} />
      <Route path="/login" element={<Login />} />
      <Route path="*" element={<h1>404 Not Found</h1>} />
    </Routes>
    <Footer />
   </>
  )
}

export default App