# RawalAps_Platform
Trips Management System TMS


## Recent modifications

Here you will find a list of the latest changes made to the project.

- Fixed the home page for improved login and registration clarity.
- Edited page titled "driver":
  1- Centered the button and title.
  2- Designed a responsive table and centered the items.


# Try this code in add_trip.html page
```
{% extends 'base.html' %}
{% block content %}
{% if user.is_authenticated %}

<div class="col">
  <h3>Add Trip</h3>
  <br/>

  <script>
    // Function to calculate the Percent of Total
    function calculatePercent() {
      var total = parseFloat(document.getElementById('total').value);
      var percent = parseFloat(document.getElementById('percent').value);
      var perTotal = (total * percent) / 100;

      // Display the result in the "Percent of Total" field
      document.getElementById('per_total').value = perTotal;
    }
  </script>

  <form method="POST" action="{% url 'add_trip' %}">
    {% csrf_token %}

    <div class="table-responsive ">
      <table class="table table-sm  table-striped-columns">
        <thead>
        </thead>
        <tbody>
          <!-- ... (Previous rows) ... -->
          <tr>
            <th scope="row">Total</th>
            <td><input type="number" name="total" id="total" oninput="calculatePercent()"></td>
            <th scope="row">Percent</th>
            <td><input type="number" name="percent" id="percent" oninput="calculatePercent()"></td>
            <th scope="row">Percent of Total</th>
            <td><input type="text" name="per_total" id="per_total" readonly></td>
          </tr>
          <!-- ... (Next rows) ... -->
        </tbody>
      </table>
    </div>

    <br/>
    <button type="submit" class="btn btn-secondary" style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">Add Trip</button>
    <a href="{% url 'home' %}" class="btn btn-secondary" style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">Back</a>
  </form>

</div>
{% endif %}
{% endblock %}
  ```
