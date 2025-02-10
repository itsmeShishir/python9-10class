import { Routes, Route } from 'react-router-dom'
import HomePage from './Page/Home/HomePage'
import AllProducts from './Page/Product/AllProducts'
import Navbar from './Component/Navbar'
function App() {
  return (
   <>
    <Navbar />
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/products" element={<AllProducts />} />
    </Routes>
   </>
  )
}

export default App