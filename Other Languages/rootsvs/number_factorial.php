<?php
function factorial($n) {
    if ($n <= 1) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}

// Define the number for which you want to calculate the factorial
$number = 5; // You can change this to any positive integer

// Calculate the factorial
$result = factorial($number);

// Display the result
echo "The factorial of $number is: $result";
?>
