am4core.ready(function() {
                    
// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end

// Create map instance
var chart = am4core.create("chartdiv", am4maps.MapChart);

var title = chart.titles.create();
title.text = "[bold font-size: 20]Worldwide Earthquake Visualization";
title.textAlign = "middle";

$.getJSON("/static/json/earthquake_data_small.json", function(json) {

    var mapData = json;
    console.log(mapData);

    // Set map definition
    chart.geodata = am4geodata_worldLow;

    // Set projection
    chart.projection = new am4maps.projections.Miller();

    // Create map polygon series
    var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
    polygonSeries.exclude = ["AQ"];
    polygonSeries.useGeodata = true;
    polygonSeries.nonScalingStroke = true;
    polygonSeries.strokeWidth = 0.5;
    polygonSeries.calculateVisualCenter = true;

    var imageSeries = chart.series.push(new am4maps.MapImageSeries());
    imageSeries.data = mapData;
    imageSeries.dataFields.value = "Mag";

    var imageTemplate = imageSeries.mapImages.template;
    imageTemplate.nonScaling = true

    var circle = imageTemplate.createChild(am4core.Circle);
    circle.fillOpacity = 0.7;
    circle.propertyFields.fill = am4core.color("red");
    circle.tooltipText = "{Location Name}: [bold]{value}[/]";


    imageSeries.heatRules.push({
    "target": circle,
    "property": "radius",
    "min": 4,
    "max": 30,
    "dataField": "value"
    })

    imageTemplate.adapter.add("latitude", function(Latitude, target) {
    return parseFloat(target.dataItem.dataContext.Latitude);
    })

    imageTemplate.adapter.add("longitude", function(Longitude, target) {
    return parseFloat(target.dataItem.dataContext.Longitude);
    })
});



}); // end am4core.ready()