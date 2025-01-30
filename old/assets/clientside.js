window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        updateAnnotationsAndQR: function(clickData, data) {
            let updatedFig1 = JSON.parse(JSON.stringify(dash_clientside.config.scatter_plot1));
            let updatedFig2 = JSON.parse(JSON.stringify(dash_clientside.config.scatter_plot2));
            
            if (!clickData) {
                return [updatedFig1, updatedFig2, ""];
            }

            let point = clickData.points[0];
            let x = point.x;
            let index = data.x.indexOf(x);
            let annotationText = data.description[index].replace(/\n/g, "<br>");
            let qrLink = data.qr_links[index];

            // Add annotation to scatter plot 1
            updatedFig1.layout.annotations = [
                {
                    x: x,
                    y: point.y,
                    xref: "x",
                    yref: "y",
                    text: annotationText,
                    showarrow: true,
                    arrowhead: 2,
                    ax: 40,
                    ay: -50,
                    bgcolor: "lightyellow",
                    font: { size: 14 },
                    bordercolor: "black",
                    borderwidth: 1
                }
            ];

            // Highlight the selected point in scatter plot 2
            updatedFig2.data[0].marker.size = data.x.map(val => val === x ? 15 : 7);
            updatedFig2.data[0].marker.color = data.x.map(val => val === x ? "red" : "blue");

            // Display QR Code
            let qrDiv = `
                <div style="text-align: center;">
                    <p style="font-size: 16px; font-weight: bold;">
                        Scan QR Code for More Info on ${data.label[index]}
                    </p>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=100x100&data=${encodeURIComponent(qrLink)}" 
                        style="width: 100px; height: 100px;">
                </div>
            `;

            return [updatedFig1, updatedFig2, qrDiv];
        }
    }
});
