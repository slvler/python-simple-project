<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>Hello, world!</title>


	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css">

	<style>
		@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@500&display=swap');

body{
	background-color: #E7E9F5;
	font-family: 'Heebo', sans-serif;
}
.card{
	width: 500px;
	border: none;
	border-radius: 20px;
}
.form-control{
	border-radius: 7px;
	border: 1.5px solid #E3E6ED;
}
input.form-control:focus{
	box-shadow: none;
	border: 1.5px solid #E3E6ED;
	background-color: #F7F8FD;
	letter-spacing: 1px;
}
.btn-primary{
	background-color: #5878FF!important;
	border-radius: 7px;
}
.btn-primary:focus{
	box-shadow: none;
}
.text{
	font-size: 13px;
	color: #9CA1A4;
}
.price{
	background: #F5F8FD;
	border-top-right-radius: 10px;
	border-bottom-right-radius: 10px;
	width: 97px;
}
.flex-row{
	border: 1px solid #F2F2F4;
	border-radius: 10px; 
	margin: 0 1px 0;
}
.flex-column p{
	font-size: 14px;
}
span.mb-2{
	font-size: 12px;
	color: #8896BD;
}
h5 span{
	color: #869099;
}
@media screen and (max-width: 450px){
	.card{
		display: flex;
		justify-content: center;
		text-align: center;
	}
	.price{
		border: none;
		margin: 0 auto;
	}
}
	</style>
  </head>
  <body>
  <div class="container d-flex justify-content-center">
	<div class="card mt-5 p-4">
		<div class="input-group mb-3">
			<input type="text" class="form-control" id="search">
			<div class="input-group-append"><button class="btn btn-primary"><i class="fas fa-search"></i></button></div>
		</div>
		<span class="text mb-4">88 branding projects</span>
		<div class="d-flex flex-row justify-content-between mb-3">
			<div class="d-flex flex-column p-3"><p class="mb-1">Logo and marketing material design for Bakery</p> <small class="text-muted">8 days remaining</small>
			</div>
			<div class="price pt-3 pl-3">
				<span class="mb-2">Fixed</span>
				<h5><span>&dollar;</span>1,500</h5>
			</div>
		</div>
		<div class="d-flex flex-row justify-content-between mx-1">
			<div class="d-flex flex-column p-3"><p class="mb-1">Need to create brand guidelines for my brand</p> <small class="text-muted">12 days remaining</small>
			</div>
			<div class="price pt-3 pl-3">
				<span class="mb-2">Hourly</span>
				<h5><span>&dollar;</span>40</h5>
			</div>
		</div>
	</div>	
</div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
	<script src="https://code.jquery.com/jquery-3.6.1.js" integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->

	<script>
		$("#search").on("keyup", function(e) {
    
			let value = e.currentTarget.value;
			$.ajax({
				type: "POST",
				data: {value: value},
				url: "search.php",
				success: function(response){

					console.log(response);
				
				}
  			});

		
		});
	</script>
    <!--
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
    -->
  </body>
</html>