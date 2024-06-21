# // Create an array to store user accounts
let userAccounts = [];

// Function to create a new user account
function createUserAccount(username, password) {
    // Check if the username and password are not empty
    if (username!== "" && password!== "") {
        // Create a new user account object
        let newUserAccount = {
            username: username,
            password: password,
            isLoggedIn: false
        };

        // Add the new user account to the array
        userAccounts.push(newUserAccount);

        // Log a success message
        console.log("User account created successfully.");
    } else {
        // Log an error message
        console.log("Username and password cannot be empty.");
    }
}

// Function to log in a user
function loginUser(username, password) {
    // Loop through the user accounts
    for (let i = 0; i < userAccounts.length; i++) {
        // Check if the username and password match an existing account
        if (userAccounts[i].username === username && userAccounts[i].password === password) {
            // Set the isLoggedIn property to true
            userAccounts[i].isLoggedIn = true;

            // Log a success message
            console.log("User logged in successfully.");

            // Break the loop
            break;
        }
    }
}

// Create a new user account
createUserAccount("user1", "password1");

// Log in the user
loginUser("user1", "password1");
