import { Routes, Route } from 'react-router-dom'
import HomePage from './Page/Home/HomePage'
import AllProducts from './Page/Product/AllProducts'
import Navbar from './Component/Navbar'
import Footer from './Component/Footer'
import AllCategoryProduct from './Page/Category/AllCategoryProduct'
import SingleProduct from './Page/Product/SingleProduct'
import Login from './Page/auths/Login'
import PrivateRoute from './role/PrivateRoute'
import LoginUserPage from './Page/auths/LoginUserPage'
import AdminPage from './Page/Admin/AdminPage'
import Register from './Page/auths/Register'
import CartPage from './Page/Cart/CartPage'

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
      <Route path="/register" element={<Register />} />
      <Route path="/cart" element={<CartPage />} />
      <Route path="*" element={<h1>404 Not Found</h1>} />
       <Route path="/user" element={<PrivateRoute allowedRoles={["1"]} />}>
        <Route index element={<LoginUserPage />} />
        <Route path="details" element={<LoginUserPage />} />
      </Route>
      <Route path="/admin" element={<PrivateRoute allowedRoles={["2"]} />}>
        <Route index element={<AdminPage />} />
        <Route path="dashboard" element={<AdminPage />} />
      </Route>
    </Routes>
    <Footer />
   </>
  )
}

export default App