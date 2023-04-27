const form = document.getElementById("form");
const prediction = document.getElementById("prediction");

form.addEventListener("submit", (event) => {
  event.preventDefault(); // prevent the default form submission

  // send a POST request to the server with the form data
  const formData = new FormData();
  formData.append("country", document.getElementById("country").value);
  formData.append("year", parseInt(document.getElementById("year").value));
  formData.append("status", document.getElementById("status").value);
  formData.append("adult_mortality", parseFloat(document.getElementById("adult_mortality").value));
  formData.append("infant_deaths", parseInt(document.getElementById("infant_deaths").value));
  formData.append("alcohol", parseFloat(document.getElementById("alcohol").value));
  formData.append("percentage_expenditure", parseFloat(document.getElementById("percentage_expenditure").value));
  formData.append("hepatitis_b", parseFloat(document.getElementById("hepatitis_b").value));
  formData.append("measles", parseInt(document.getElementById("measles").value));
  formData.append("bmi", parseFloat(document.getElementById("bmi").value));
  formData.append("under_five_deaths", parseInt(document.getElementById("under_five_deaths").value));
  formData.append("polio", parseFloat(document.getElementById("polio").value));
  formData.append("total_expenditure", parseFloat(document.getElementById("total_expenditure").value));
  formData.append("diphtheria", parseFloat(document.getElementById("diphtheria").value));
  formData.append("hiv_aids", parseFloat(document.getElementById("hiv_aids").value));
  formData.append("gdp", parseFloat(document.getElementById("gdp").value));
  formData.append("population", parseInt(document.getElementById("population").value));
  formData.append("thinness_1_19_years", parseFloat(document.getElementById("thinness_1_19_years").value));
  formData.append("thinness_5_9_years", parseFloat(document.getElementById("thinness_5_9_years").value));
  formData.append("income_composition", parseFloat(document.getElementById("income_composition").value));
  formData.append("schooling", parseFloat(document.getElementById("schooling").value));

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "http://127.0.0.1:5000/predict", true);
  xhr.send(formData);

  xhr.onload = () => {
    if (xhr.status === 200) {
      // parse the response JSON data
      const response = JSON.parse(xhr.responseText);
      console.log(xhr.responseText)

      // set the predicted value in the HTML element
      prediction.innerHTML = `<h3>Predicted Life Expectancy: ${response.prediction.toFixed(2)}</h3>`;
    } else {
      console.error("Error:", xhr.statusText);
    }
  };
});
