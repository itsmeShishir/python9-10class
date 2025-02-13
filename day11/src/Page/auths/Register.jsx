import { useState } from "react"
import axios from "axios";
import { useNavigate } from "react-router-dom";
function Register() {
    let [email, setEmail] = useState('');
    let [password, setPassword] = useState('');
    let [username, setUsername] = useState('');
    let [phone, setPhone] = useState('');
    let navigate = useNavigate();

    let handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/api/register/', {
            email: email,
            password: password,
            username: username,
            phone_number : phone
        })
        .then(res => {
            console.log(res.data);
            navigate('/login');
           
        }).catch(err => {
            console.log(err);
        })
    }

  return (
    <>
        <div className="w-full max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow-sm sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700">
            <form className="space-y-6"  onSubmit={handleSubmit}>
                <h5 className="text-xl font-medium text-gray-900 dark:text-white">Sign in to our platform</h5>
                 <div>
                    <label htmlFor="username" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your username</label>
                    <input
                    value={username}
                    onChange={e=> setUsername(e.target.value)}
                    type="username" name="username" id="username" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="name@company.com" required />
                </div>
                <div>
                    <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                    <input
                     value={email}
                    onChange={e=> setEmail(e.target.value)}
                     type="email" name="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="name@company.com" required />
                </div>
                <div>
                    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
                    <input
                    value={password}
                    onChange={e=> setPassword(e.target.value)}
                    type="password" name="password" id="password" placeholder="••••••••" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required />
                </div>
                <div>
                    <label htmlFor="PhoneNumber" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Phone Number</label>
                    <input
                    value={phone}
                    onChange={e=> setPhone(e.target.value)}
                    type="number" name="PhoneNumber" id="PhoneNumber" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="+977" required />
                </div>
                
                <button type="submit" className="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Register to your account</button>
                <div className="text-sm font-medium text-gray-500 dark:text-gray-300">
                    Not registered? <a href="#" className="text-blue-700 hover:underline dark:text-blue-500">Create account</a>
                </div>
            </form>
        </div>
    </>
  )
}

export default Register