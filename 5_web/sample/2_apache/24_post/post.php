<?php
	$data = array(
		"name" => $_POST["name"],
		"age" => $_POST["age"]
	);
	file_put_contents("person.json", json_encode($data));
?>