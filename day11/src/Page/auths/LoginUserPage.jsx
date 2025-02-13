
function LoginUserPage() {
    let email = localStorage.getItem('email');
    let role = localStorage.getItem('role');
    let username = localStorage.getItem('username');

  return (
    <div>
        <h1>Login User Page</h1>
        <h1>Email: {email}</h1>
        <h1>Role: {role}</h1>
        <h1>Username: {username}</h1>

    </div>
  )
}

export default LoginUserPage