document.querySelector("form").addEventListener("submit", function (e) {
    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;
  
    if (!name || !email) {
      e.preventDefault();
      alert("Please fill in all fields!");
    }
  });
  