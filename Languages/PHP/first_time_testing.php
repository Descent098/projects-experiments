<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>
    <?php echo '<h1>Hello World</h1>'; 
    
    // Associative arrarys == Dictionaries in python
    $user = array("Name"=>"Kieran", "Country"=>"Canada", "Age"=>21);

    // Essentially a python for loop
    foreach($user as $attribute => $attribute_value){

    printf(" %s : %s <br><br>",$attribute, $attribute_value);
    }

    // Echos the Date Month and Year
    printf(" %s <br>", date("l F jS Y"));

    // Built in constants are auto-imported 
    echo pi();
    
    // Grab all headers
    $headers = headers_list();

    foreach($headers as $header){
      echo "<br>", $header, "<br>";
    }

    

    ?> 
  </body>
</html>