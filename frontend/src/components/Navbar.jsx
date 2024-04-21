import { Link } from "react-router-dom"
import { useLogout } from "../hooks/useLogOut"
import { useAuthContext } from "../hooks/useAuthContext"
import edubot from '../assets/edu-bot.png'

const Navbar = () => {

    const { logout } = useLogout()
    const { user } = useAuthContext()
    const handleClick = () => {
        logout()
    }

    return (
        <header>
            <div className="container">
                <Link to="/">
                    <div className="title-logo-container">
                        <img src={edubot} alt="" width={"50px"} height={"50px"} />
                        <h1>Edu Bot</h1>
                    </div>
                </Link>
                <nav>
                    {user && (<div>
                        <span>{user.email}</span>
                        <button onClick={handleClick}>Log out</button>
                    </div>)}
                    {!user && (<div>
                        <Link to="/login">Login</Link>
                        <Link to="/signup">SignUp</Link>
                    </div>)}
                </nav>
            </div>
        </header>
    )
}

export default Navbar