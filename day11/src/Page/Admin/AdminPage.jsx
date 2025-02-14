import { useState } from "react";

function AdminPage() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState(null);

  // for product
  const[names, setNames] = useState('');
  const[prices, setPrices] = useState('');
  const[descriptions, setDescriptions] = useState('');
  const[images, setImages] = useState(null);
  const[category, setCategory] = useState('');
  const [user, setUser] = useState('');
  // for category

  const submitHandler = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("name", name);
    formData.append("description", description);
    if (image) {
      formData.append("image", image);
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/createCategory/", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: formData,
      });

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  // for Product
   const submitHandlers = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("name", names);
    formData.append("description", descriptions);
    formData.append("price", prices);
    formData.append("category", category);
    formData.append("user", "1");
    
    if (image) {
      formData.append("image", images);
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/createProduct/", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: formData,
      });

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  return (
    <div>
      <h1>Category Add</h1>
      <form onSubmit={submitHandler}>
        <div>
          <label htmlFor="name">Name</label>
          <input 
            type="text" 
            id="name" 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
          />
        </div>
        <div>
          <label htmlFor="description">Description</label>
          <input 
            type="text" 
            id="description" 
            value={description} 
            onChange={(e) => setDescription(e.target.value)} 
          />
        </div>
        <div>
          <label htmlFor="image">Image</label>
          <input 
            type="file" 
            id="image" 
            onChange={(e) => setImage(e.target.files[0])} 
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      <h1 className="text-5xl bg-red-500 ">For Product</h1>
        {/* for product */}
      <form onSubmit={submitHandlers}>
        <div>
          <label htmlFor="name">Name</label>
          <input 
            type="text" 
            id="name" 
            value={names} 
            onChange={(e) => setNames(e.target.value)} 
          />
        </div>
        <div>
          <label htmlFor="description">Description</label>
          <input 
            type="text" 
            id="description" 
            value={descriptions} 
            onChange={(e) => setDescriptions(e.target.value)} 
          />
        </div>
        <div>
          <label htmlFor="image">Image</label>
          <input 
            type="file" 
            id="image" 
            onChange={(e) => setImages(e.target.files[0])} 
          />
        </div>
         <div>
          <label htmlFor="image">Price</label>
          <input 
            type="text" 
            id="image"
            value={prices}  
            onChange={(e) => setPrices(e.target.value)} 
          />
        </div>
        
        <div>
          <label htmlFor="image">Category</label>
          <input 
            type="text" 
            id="image"
            value={category}  
            onChange={(e) => setCategory(e.target.value)} 
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default AdminPage;
