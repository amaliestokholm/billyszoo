html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Plotly Chart with QR Codes</title>
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
                // Extract x, y, and URLs
                var xValues = data.map(d => d.x);
                var yValues = data.map(d => d.y);
                var urls = data.map(d => d.url);

                // Create the plot
                var trace = {
                    x: xValues,
                    y: yValues,
                    mode: 'markers',
                    type: 'scatter'
                };

                var layout = {
                    title: "Click a Data Point"
                };

                Plotly.newPlot('plot', [trace], layout);

                // Event listener for clicking on data points
                document.getElementById('plot').on('plotly_click', function(eventData) {
                    var pointIndex = eventData.points[0].pointIndex; // Get index of clicked point
                    var x = xValues[pointIndex];
                    var y = yValues[pointIndex];
                    var url = urls[pointIndex]; // Get associated URL

                    document.getElementById('output').innerText = `Clicked on: x=${x}, y=${y} \nURL: ${url}`;

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
