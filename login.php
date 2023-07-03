<?php
$servername = "localhost"; // ganti dengan servername MySQL Anda
$username = "root"; // ganti dengan username MySQL Anda
$password = ''; // ganti dengan password MySQL Anda
$dbname = "login"; // ganti dengan nama database MySQL Anda

// Membuat koneksi ke database
$conn = new mysqli($servername, $username, $password, $dbname);

// Memeriksa koneksi
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}


// Mengambil data yang dikirimkan dari form login
$username = $_POST['username'];
$password = $_POST['password'];

// Mengecek kecocokan username dan password dalam database
$sql = "SELECT * FROM user WHERE username = '$username' AND password = '$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    header("Location: index.html");
} 
else {

    header("Location: pages-login.html");
  }

$conn->close();
?>
