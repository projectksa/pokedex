const searchInput = document.querySelector("#poke-search");
const registerInput = document.querySelector("input");




searchInput.addEventListener('input', (e) =>  {
  const pokeNames = document.querySelectorAll(".card-title");
  const search = searchInput.value.toLowerCase();
  const pokeCard = document.querySelectorAll("#poke-card");
 


  pokeNames.forEach(pokeName => {
    pokeName.parentElement.parentElement.parentElement.style.display = 'block';
    if(!pokeName.innerHTML.toLowerCase().includes(search)){
      pokeName.parentElement.parentElement.parentElement.style.display = 'none';
    
    }
    
  });
})


