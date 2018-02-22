var dataset = [8, 48, 14, 31, 23];

var svg = d3.select("body").append("svg").attr({
    width: 500,
    height: 500
});

svg.selectAll("rect").data(dataset).enter().append("rect").attr({ x: 0, y: 0, width: 100, height: 20, fill: "orange" });

