var request_p = new XMLHttpRequest();
var request_g = new XMLHttpRequest();
var messages = null;

	
request_g.onreadystatechange = function ()
	{
		if (request_g.readyState == XMLHttpRequest.DONE)
		{
			if (request_g.status >= 200 && request_g.status < 400)
			{
				console.log("SUCCESSFUL GET");
				console.log(request_g.responseText);
				messages = JSON.parse(request_g.responseText);
				
				var recipe = document.getElementById('list');

				for (var i = 0; i < messages.length; i++)
				{

					var newListItem = document.createElement('li');
					//newListItem.innerHTML = "";
					newListItem.innerHTML = messages[i];
					recipe.appendChild(newListItem);
				}
				return

			}

			else 
			{
				console.log("ERROR");
			}
		}

	};

request_p.onreadystatechange = function ()
	{
		if (request_p.readyState == XMLHttpRequest.DONE)
		{
			if (request_p.status >= 200 && request_p.status < 400)
			{
				console.log("SUCCESSFUL POST");
				console.log(request_p.responseText);
				request_g.open('GET', "http://localhost:8080/recipes");
				request_g.send();
				return

			}
			else 
			{
				console.log("ERROR");
			}
		}

	};


var ingButton = document.getElementById("ingredient_button");
ingButton.onclick = function()
{
	console.log("button was clicked");
	var recipeInput = document.getElementById("ingredients");
	var recipe = recipeInput.value;
	var data = "ingredients=" + encodeURIComponent(recipe);
	request_p.open('POST', 'http://localhost:8080/recipes');
	request_p.send(data);
	

};

