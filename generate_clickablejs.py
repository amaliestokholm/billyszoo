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
        fetch("data.json")
            .then(response => response.json())
            .then(data => {
                var xValues = data.map(d => d.x);
                var yValues = data.map(d => d.y);
                var labels = data.map(d => d.label);
                var urls = data.map(d => d.url);
                var descriptions = data.map(d => d.description || "No description available.");

                var markerSizes = new Array(xValues.length).fill(10);
                var markerColors = new Array(xValues.length).fill("blue");

                var trace = {
                    x: xValues,
                    y: yValues,
                    mode: 'markers',
                    type: 'scatter',
                    text: labels,
                    hoverinfo: 'text',
                    marker: {
                        size: markerSizes,
                        color: markerColors
                    }
                };

                var layout = {
                    title: {
                        text: "Click on a planet",
                        font: { family: "Arial, sans-serif", size: 18, color: "#333" }
                    },
                    xaxis: {
                        title: {
                            text: "log (orbital separation) [log(AU)]",
                            font: { family: "Courier New, monospace", size: 16, color: "darkblue" }
                        },
                        type: "log",
                        range: [0.1, 4]
                    },
                    yaxis: {
                        title: {
                            text: "log (Planet mass) [log(Earth mass)]",
                            font: { family: "Verdana, sans-serif", size: 16, color: "darkred" }
                        },
                        type: "log",
                        range: [0.1, 2]
                    },
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
                    var label = labels[pointIndex];
                    var description = descriptions[pointIndex];
                    var url = urls[pointIndex];

                    document.getElementById('output').innerHTML =
                        `Clicked on: <strong>${label}</strong><br>` +
                        `Description: ${description}<br>` +
                        `Coordinates: (x=${x}, y=${y})<br>` +
                        `URL: <a href="${url}" target="_blank" rel="noopener noreferrer">See ADS entry here</a>`;

                    markerSizes.fill(10);
                    markerColors.fill("blue");

                    // Change appearance of the clicked point
                    markerSizes[pointIndex] = 20;
                    markerColors[pointIndex] = "orange";

                    Plotly.restyle('plot', {
                        'marker.size': [markerSizes],
                        'marker.color': [markerColors]
                    });

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
