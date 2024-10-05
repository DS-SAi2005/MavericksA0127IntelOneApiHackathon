function toggleMenu() {
    const navList = document.getElementById("nav-list");
    navList.classList.toggle("active");
}

document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    
    if (username === "admin" && password === "password") {
        alert("Login successful!");
    } else {
        alert("Invalid credentials. Please try again.");
    }
});
