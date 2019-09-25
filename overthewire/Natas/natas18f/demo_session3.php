<!-- Another way to show all the session variable values for a user session is to run the following code: -->
<?php
session_start();
?>
<!DOCTYPE html>
<html>
<body>

<?php
print_r($_SESSION);
?>

</body>
</html> 