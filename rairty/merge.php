<?php
$folder = "./json_files";
$files = scandir($folder);
$newfile = "";
foreach($files as $file){
	if(is_file($folder ."/$file")){
		if($newfile != "") $newfile .= ",\r\n";
		$thisfile = fopen($folder ."/$file", "r");
		while($line = fgets($thisfile)){
			$newfile .= "  " .$line;
		}
		fclose($thisfile);
	}
}
$newfile = "[\r\n" .$newfile ."\r\n]";
file_put_contents("merged.json", $newfile);
echo "New JSON file saved as $folder/merged.json";
?>