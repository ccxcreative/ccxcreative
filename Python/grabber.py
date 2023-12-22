<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect post data from the form
    $name = sanitize_input($_POST['name']);
    $email = sanitize_input($_POST['email']);
    $phone = sanitize_input($_POST['phone']);
    $message = sanitize_input($_POST['message']);

    // Process or store the form data as needed
    // For example, insert it into a database, send an email, etc.

    // Redirect to a thank you page or display a success message
    echo "Thank you for your message. We will contact you shortly.";
}

function sanitize_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>