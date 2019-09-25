<!-- To remove all global session variables and destroy the session, use session_unset() and session_destroy(): -->
<?php
session_start();
?>
<!DOCTYPE html>
<html>
<body>

<?php
// remove all session variables
session_unset();

// destroy the session
session_destroy();
print_r($_SESSION);
?>

</body>
</html> 