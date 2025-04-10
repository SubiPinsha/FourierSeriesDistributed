document
  .getElementById("fourier-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let functionInput = document.getElementById("function").value;
    let T = parseFloat(document.getElementById("T").value);
    let n_terms = parseInt(document.getElementById("n_terms").value);

    fetch("http://10.16.65.217:5000/compute_fourier", {
      // IP of Main Server
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ function: functionInput, T: T, n_terms: n_terms }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("results").innerText = JSON.stringify(
          data,
          null,
          2
        );
        document.getElementById(
          "graphImage"
        ).src = `data:image/png;base64,${data.graph_image}`;
      })
      .catch((error) => console.error("Error:", error));
  });
