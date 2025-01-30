html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Billy's zoo of planets</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrious/4.0.2/qrious.min.js"></script>
</head>
<body>

    <h2>Billy's zoo of planets</h2>
    <div id="plot"></div>
    <p id="output">Click on a planet to see details</p>
    <canvas id="qr-code"></canvas>  <!-- QR Code Canvas -->

    <script>
        // Load JSON data
        fetch("data.json")
            .then(response => response.json())
            .then(data => {
                var xValues = data.map(d => d.x);
                var yValues = data.map(d => d.y);
                var labels = data.map(d => d.planet);
                var urls = data.map(d => d.url);

                // Create the plot
                var trace = {
                    x: xValues,
                    y: yValues,
                    mode: 'markers',
                    type: 'scatter',
                    text: labels,
                    hoverinfo: 'text'
                };

                var layout = {
                    title: "Click on a Data Point",
                    dragmode: false  // Disable zoom & panning
                };
                var config = {
                    displayModeBar: false  // Hide the mode bar
                };

                Plotly.newPlot('plot', [trace], layout, config);

                document.getElementById('plot').on('plotly_click', function(eventData) {
                    var pointIndex = eventData.points[0].pointIndex;
                    var x = xValues[pointIndex];
                    var y = yValues[pointIndex];
                    var label = planetValues[pointIndex];
                    var url = urls[pointIndex];

                    document.getElementById('output').innerText = `Clicked on: \n${label} at x=${x}, y=${y} \nURL: ${url}`;

                    // Generate QR Code
                    var qr = new QRious({
                        element: document.getElementById('qr-code'),
                        value: url,
                        size: 150
                    });
                });
            })
            .catch(error => console.error("Error loading JSON:", error));
    </script>

</body>
</html>
"""

with open("plot.html", "w") as file:
    file.write(html_content)

print("plot.html has been generated! Open it in a browser.")
