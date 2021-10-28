var menu = "Magnitude";

function draw_circles(menu) {
    am4core.ready(function () {

        // Themes begin
        am4core.useTheme(am4themes_animated);
        // Themes end

        // Create map instance
        var chart = am4core.create("chartdiv", am4maps.MapChart);

        var title = chart.titles.create();
        var title_text = "[bold font-size: 20]Worldwide Earthquake Visualization";
        title.text = title_text.concat(' - ', menu);

        title.textAlign = "middle";

//var mapData = [{'id': 0, 'name': 'PAKISTAN: BALOCHISTAN PROVINCE', 'value': 5.9, 'latitude':30.22, 'longitude': 68.014}];

        /*
var mapData = [
  { "id":"AF", "name":"Afghanistan", "value":32358260, "color": chart.colors.getIndex(0) },
  { "id":"AL", "name":"Albania", "value":3215988, "color":chart.colors.getIndex(1) },
  { "id":"DZ", "name":"Algeria", "value":35980193, "color":chart.colors.getIndex(2) },
  { "id":"AO", "name":"Angola", "value":19618432, "color":chart.colors.getIndex(2) },
  { "id":"AR", "name":"Argentina", "value":40764561, "color":chart.colors.getIndex(3) }
];

*/

        $.getJSON("/static/json/earthquake_data_small.json", function (json) {

            var mapData = json;

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
            if (menu === "Magnitude") {
                imageSeries.dataFields.value = "Mag";
            } else if (menu === "Death") {
                imageSeries.dataFields.value = "Deaths";
            } else if (menu === "Damage") {
                imageSeries.dataFields.value = "Damage ($Mil)";
            }


            var imageTemplate = imageSeries.mapImages.template;
            imageTemplate.nonScaling = true

            var circle = imageTemplate.createChild(am4core.Circle);
            circle.fillOpacity = 0.7;

            if (menu === "Magnitude") {
                circle.fillOpacity = 0.8;
                circle.fill = 'yellow';
            } else if (menu === "Death") {
                circle.fill = 'red';
            } else if (menu === "Damage") {
                circle.fill = 'blue';
            }


            //circle.propertyFields.fill = am4core.color("blue");
            circle.tooltipText = "{Location Name}: [bold]{value}[/]";


            imageSeries.heatRules.push({
                "target": circle,
                "property": "radius",
                "min": 4,
                "max": 30,
                "dataField": "value"
            })

            imageTemplate.adapter.add("latitude", function (Latitude, target) {
                return parseFloat(target.dataItem.dataContext.Latitude);
            })

            imageTemplate.adapter.add("longitude", function (Longitude, target) {
                return parseFloat(target.dataItem.dataContext.Longitude);
            })
        });


    }); // end am4core.ready()

}

draw_circles(menu);